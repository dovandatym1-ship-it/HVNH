from pathlib import Path
import json
import shutil
import numpy as np
import pytest
import xgboost as xgb
from train_model import generate_synthetic_bank_data, FEATURES, choose_f2_threshold, rule_score
from risk_engine import action, validate, score_transaction
from artifact_loader import verify_artifacts

BASE=Path(__file__).resolve().parent

def test_generator_reproducible_and_schema():
    a=generate_synthetic_bank_data(25000,42)
    assert a.equals(generate_synthetic_bank_data(25000,42))
    assert a.is_fraud.sum()==450 and not a.isna().any().any()
    assert a.hour.between(0,23).all() and list(a.columns[:-1])==FEATURES

def test_threshold_tie_break_uses_lower_alert_rate():
    threshold=choose_f2_threshold([0,1,0,1],[.1,.2,.3,.4])
    assert 0<=threshold[2]<=1 and threshold[0]>0

@pytest.mark.parametrize('score,expected',[(0,'Rủi ro thấp'),(.69999,'Rủi ro thấp'),(.70,'Đề xuất xác thực'),(.74999,'Đề xuất xác thực'),(.75,'Đề xuất chuyển'),(1,'Đề xuất chuyển')])
def test_action_boundaries(score,expected):
    assert action(score,.70,.75).startswith(expected)

def test_equal_thresholds_produce_empty_middle_band_not_failure():
    assert action(1.0,1.0,1.0).startswith('Đề xuất chuyển')
    assert action(0.999,1.0,1.0).startswith('Rủi ro thấp')

@pytest.mark.parametrize('key,value',[('amount',float('nan')),('amount',float('inf')),('amount',19999),('hour',24),('hour',1.5),('channel',4),('new_device',2),('tx_frequency_10m',0)])
def test_invalid_input_rejected(key,value):
    tx=dict(amount=20000,hour=0,channel=0,new_device=0,location_anomaly=0,failed_attempts=0,tx_frequency_10m=1,new_beneficiary=1); tx[key]=value
    with pytest.raises(ValueError): validate(tx)

def test_missing_extra_and_boolean_fields_rejected():
    tx=dict(amount=20000,hour=0,channel=0,new_device=0,location_anomaly=0,failed_attempts=0,tx_frequency_10m=1,new_beneficiary=1)
    with pytest.raises(ValueError): validate({})
    with pytest.raises(ValueError): validate({**tx,'unexpected':0})
    with pytest.raises(ValueError): validate({**tx,'hour':True})

def test_manifest_hash_and_schema_fail_closed(tmp_path):
    for name in ['fraud_model.json','metrics.json','artifact_manifest.json']:
        shutil.copy2(BASE/name,tmp_path/name)
    model,metrics,manifest=verify_artifacts(tmp_path)
    assert metrics['run_id']==manifest['run_id']
    (tmp_path/'metrics.json').write_text('{}')
    with pytest.raises(ValueError,match='metrics.json'): verify_artifacts(tmp_path)

def test_shap_sum_raw_margin_matches_model_score():
    model,report,_=verify_artifacts(BASE)
    frame=generate_synthetic_bank_data(100)[FEATURES]
    contrib=model.get_booster().predict(xgb.DMatrix(frame),pred_contribs=True)
    scores=model.predict_proba(frame)[:,1]
    np.testing.assert_allclose(1/(1+np.exp(-contrib.sum(axis=1))),scores,rtol=1e-4,atol=1e-6)

def test_score_matches_manifest_and_decision():
    model,report,manifest=verify_artifacts(BASE)
    tx=dict(amount=1_500_000,hour=14,channel=0,new_device=0,location_anomaly=0,failed_attempts=0,tx_frequency_10m=1,new_beneficiary=1)
    result=score_transaction(model,report,tx)
    assert result['run_id']==manifest['run_id'] and result['latency_ms']>=0
    assert result['action'] in ['Rủi ro thấp; giữ nguyên các kiểm soát thông thường','Đề xuất xác thực bổ sung','Đề xuất chuyển chuyên viên xem xét']

def test_ui_happy_path_and_history():
    from streamlit.testing.v1 import AppTest
    app=AppTest.from_file(str(BASE/'app.py')).run(timeout=60)
    assert not app.exception
    submit=next(b for b in app.button if b.label=='Chấm điểm mô phỏng')
    submit.click().run(timeout=60)
    assert not app.exception and len(app.session_state['history'])==1
    assert app.session_state['history'][0]['run_id']==json.loads((BASE/'metrics.json').read_text())['run_id']
