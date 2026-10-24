"""Shared scoring and demo policy. It does not authorize or block transactions."""
import math
import time
from numbers import Real
import pandas as pd
from train_model import FEATURES

BOUNDS={'amount':(20_000,500_000_000),'hour':(0,23),'channel':(0,3),
        'new_device':(0,1),'location_anomaly':(0,1),'failed_attempts':(0,3),
        'tx_frequency_10m':(1,20),'new_beneficiary':(0,1)}


def validate(transaction):
    if not isinstance(transaction,dict) or set(transaction)!=set(FEATURES):
        raise ValueError('Giao dịch phải có đúng 8 trường đặc trưng.')
    normalized={}
    for key,(lo,hi) in BOUNDS.items():
        value=transaction[key]
        if isinstance(value,bool) or not isinstance(value,Real) or not math.isfinite(float(value)) or not lo<=value<=hi:
            raise ValueError(f'{key}: yêu cầu số hữu hạn trong [{lo}, {hi}].')
        if key!='amount' and float(value)!=int(value):
            raise ValueError(f'{key}: phải là số nguyên.')
        normalized[key]=float(value) if key=='amount' else int(value)
    return pd.DataFrame([normalized],columns=FEATURES)


def action(score, threshold, high_threshold):
    if not 0<=score<=1 or not 0<=threshold<=high_threshold<=1:
        raise ValueError('Điểm hoặc ngưỡng chính sách demo không hợp lệ.')
    if score>=high_threshold: return 'Đề xuất chuyển chuyên viên xem xét'
    if score>=threshold: return 'Đề xuất xác thực bổ sung'
    return 'Rủi ro thấp; giữ nguyên các kiểm soát thông thường'


def score_transaction(model, report, transaction):
    frame=validate(transaction); started=time.perf_counter_ns()
    score=float(model.predict_proba(frame)[0,1])
    latency=(time.perf_counter_ns()-started)/1e6
    threshold=float(report['metrics']['xgboost_by_seed']['42']['threshold'])
    high=float(report['demo_policy']['high_threshold'])
    return {'score':score,'latency_ms':latency,'action':action(score,threshold,high),
            'model_seed':42,'run_id':report['run_id']}
