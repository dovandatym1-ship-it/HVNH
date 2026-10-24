"""Reproducible academic PoC; all records and labels are synthetic, not MB data."""
from __future__ import annotations
import hashlib
import json
import platform
import time
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd
import sklearn
import xgboost as xgb
from sklearn.metrics import (average_precision_score, confusion_matrix, f1_score,
                             fbeta_score, precision_recall_curve, precision_score,
                             recall_score, roc_auc_score)
from sklearn.model_selection import train_test_split

FEATURES = ['amount', 'hour', 'channel', 'new_device', 'location_anomaly',
            'failed_attempts', 'tx_frequency_10m', 'new_beneficiary']
BASE = Path(__file__).resolve().parent
SCHEMA_VERSION = '1.1'
SEEDS = (42, 52, 62)


def generate_synthetic_bank_data(n_samples: int = 25_000, random_state: int = 42) -> pd.DataFrame:
    """Generate synthetic transactions; the 1.8% label rate is a design choice."""
    if not isinstance(n_samples, int) or n_samples < 100:
        raise ValueError('n_samples phải là số nguyên >= 100.')
    rng = np.random.default_rng(random_state)
    amount = np.clip(rng.lognormal(mean=13.5, sigma=1.5, size=n_samples), 20_000, 500_000_000)
    hour_weights = np.array([.01,.005,.005,.005,.01,.02,.04,.06,.08,.08,.07,.06,
                             .05,.06,.08,.08,.07,.06,.06,.05,.03,.02,.015,.01])
    hour = rng.choice(np.arange(24), size=n_samples, p=hour_weights/hour_weights.sum())
    channel = rng.choice([0,1,2,3], size=n_samples, p=[.70,.15,.10,.05])
    new_device = rng.choice([0,1], size=n_samples, p=[.92,.08])
    location_anomaly = rng.choice([0,1], size=n_samples, p=[.95,.05])
    failed_attempts = rng.choice([0,1,2,3], size=n_samples, p=[.88,.08,.03,.01])
    tx_frequency_10m = np.clip(rng.geometric(p=.4, size=n_samples),1,20)
    new_beneficiary = rng.choice([0,1], size=n_samples, p=[.15,.85])
    latent = ((amount > 30_000_000).astype(int)*2.0 +
              (amount > 100_000_000).astype(int)*3.0 +
              ((hour >= 1)&(hour <= 4)).astype(int)*2.5 + new_device*3.5 +
              location_anomaly*4.0 + (failed_attempts >= 2).astype(int)*3.0 +
              (tx_frequency_10m >= 5).astype(int)*2.5 + (new_beneficiary == 0).astype(int)*2.0)
    latent += rng.normal(0,1.2,size=n_samples)
    label_cut = np.percentile(latent,98.2)
    is_fraud = (latent >= label_cut).astype(int)
    return pd.DataFrame({
        'amount':amount, 'hour':hour, 'channel':channel, 'new_device':new_device,
        'location_anomaly':location_anomaly, 'failed_attempts':failed_attempts,
        'tx_frequency_10m':tx_frequency_10m, 'new_beneficiary':new_beneficiary,
        'is_fraud':is_fraud
    })


def rule_score(X: pd.DataFrame) -> np.ndarray:
    """Transparent rule baseline on three features, distinct from label formula."""
    return ((X.new_device == 1).astype(float) +
            (X.location_anomaly == 1).astype(float) +
            (X.amount > 30_000_000).astype(float)).to_numpy()/3.0


def choose_f2_threshold(y_true, scores):
    """Maximize validation F2; ties choose the smaller validation alert rate."""
    y = np.asarray(y_true, dtype=int)
    s = np.asarray(scores, dtype=float)
    thresholds = np.unique(s)
    thresholds = np.append(thresholds, np.nextafter(thresholds.max(), np.inf))
    candidates = []
    for threshold in thresholds:
        pred = s >= threshold
        candidates.append((float(fbeta_score(y,pred,beta=2,zero_division=0)),
                           float(pred.mean()), float(threshold)))
    best_f2 = max(r[0] for r in candidates)
    tied = [r for r in candidates if np.isclose(r[0],best_f2,rtol=0,atol=1e-12)]
    return min(tied,key=lambda r:(r[1],-r[2]))


def evaluate(y_true, scores, threshold):
    y = np.asarray(y_true,dtype=int); s = np.asarray(scores,dtype=float)
    pred = (s >= threshold).astype(int)
    tn,fp,fn,tp = confusion_matrix(y,pred,labels=[0,1]).ravel()
    return {
        'roc_auc':float(roc_auc_score(y,s)),
        'average_precision':float(average_precision_score(y,s)),
        'precision':float(precision_score(y,pred,zero_division=0)),
        'recall':float(recall_score(y,pred,zero_division=0)),
        'f1':float(f1_score(y,pred,zero_division=0)),
        'f2':float(fbeta_score(y,pred,beta=2,zero_division=0)),
        'false_positive_rate':float(fp/(fp+tn)) if fp+tn else 0.0,
        'alert_rate':float(pred.mean()),
        'confusion_matrix':[[int(tn),int(fp)],[int(fn),int(tp)]]
    }


def _threshold_tradeoff(y_true, scores, model_name):
    y=np.asarray(y_true,dtype=int); s=np.asarray(scores,dtype=float)
    unique=np.unique(s)
    if len(unique)>1200:
        idx=np.unique(np.linspace(0,len(unique)-1,1200).round().astype(int))
        unique=unique[idx]
    values=[]
    for t in unique:
        m=evaluate(y,s,float(t))
        values.append({'model':model_name,'threshold':float(t),'precision':m['precision'],
            'recall':m['recall'],'f2':m['f2'],'false_positive_rate':m['false_positive_rate'],
            'alert_rate':m['alert_rate']})
    return values


def _measure_inference_latency(model, X_test, repetitions=250):
    row=X_test.iloc[[0]]
    for _ in range(30): model.predict_proba(row)
    times=[]
    for i in range(repetitions):
        sample=X_test.iloc[[i % len(X_test)]]
        start=time.perf_counter_ns(); model.predict_proba(sample); times.append((time.perf_counter_ns()-start)/1e6)
    return {'method':'single-row predict_proba; 30 warm-ups, 250 measured calls; local process only',
            'median_ms':float(np.median(times)),'p95_ms':float(np.percentile(times,95)),
            'n_warmup':30,'n_measured':repetitions}


def train_and_save(output_dir=BASE, n_samples=25_000):
    out=Path(output_dir); out.mkdir(parents=True,exist_ok=True)
    df=generate_synthetic_bank_data(n_samples=n_samples,random_state=42)
    X=df[FEATURES].reset_index(drop=True); y=df.is_fraud.reset_index(drop=True)
    X_dev,X_test,y_dev,y_test=train_test_split(X,y,test_size=.20,random_state=42,stratify=y)
    X_train,X_val,y_train,y_val=train_test_split(X_dev,y_dev,test_size=.25,random_state=42,stratify=y_dev)
    # Fixed data/splits across seeds; seed variation measures training stochasticity only.
    data_digest=hashlib.sha256(pd.concat([X,y.rename('is_fraud')],axis=1).to_csv(index=False).encode()).hexdigest()
    rule_val=rule_score(X_val); rule_pick=choose_f2_threshold(y_val,rule_val)
    rule_test=rule_score(X_test)
    baselines={
        'always_negative':evaluate(y_test,np.zeros(len(y_test)),.5),
        'simple_rule':evaluate(y_test,rule_test,rule_pick[2])
    }
    baselines['simple_rule']['validation_threshold']=rule_pick[2]
    results={}; models={}; predictions={
        'synthetic_row_id':[f'SYN-{i:05d}' for i in X_test.index],
        'synthetic_label':y_test.to_numpy(),
        'rule_score':rule_test,
        'rule_pred':(rule_test>=rule_pick[2]).astype(int),
        'always_negative_pred':np.zeros(len(y_test),dtype=int)
    }
    seed_rows=[]; tradeoff=[]; pr_rows=[]
    for seed in SEEDS:
        model=xgb.XGBClassifier(n_estimators=150,max_depth=5,learning_rate=.08,
            scale_pos_weight=float((y_train==0).sum()/y_train.sum()),subsample=.8,
            colsample_bytree=.8,eval_metric='aucpr',random_state=seed,n_jobs=2)
        model.fit(X_train,y_train)
        val_scores=model.predict_proba(X_val)[:,1]
        threshold_pick=choose_f2_threshold(y_val,val_scores)
        test_scores=model.predict_proba(X_test)[:,1]
        item=evaluate(y_test,test_scores,threshold_pick[2])
        item.update({'threshold':threshold_pick[2], 'validation_f2':threshold_pick[0],
                     'validation_alert_rate':threshold_pick[1]})
        results[str(seed)]=item; models[seed]=model
        predictions[f'model_score_seed_{seed}']=test_scores
        predictions[f'model_pred_seed_{seed}']=(test_scores>=threshold_pick[2]).astype(int)
        seed_rows.append({'seed':seed,'threshold':threshold_pick[2],**{k:v for k,v in item.items() if k!='confusion_matrix'}})
        if seed==42:
            tradeoff.extend(_threshold_tradeoff(y_test,test_scores,'XGBoost seed 42'))
            p,r,t=precision_recall_curve(y_test,test_scores)
            ap=float(average_precision_score(y_test,test_scores))
            pr_rows.extend([{'model':'XGBoost seed 42','recall':float(r[i]),'precision':float(p[i]),
                            'threshold':float(t[i]) if i<len(t) else None,'average_precision':ap}
                           for i in range(len(p))])
    tradeoff.extend(_threshold_tradeoff(y_test,rule_test,'Simple rules'))
    model_path=out/'fraud_model.json'; models[42].save_model(model_path)
    model_sha=hashlib.sha256(model_path.read_bytes()).hexdigest()
    summary={}
    for metric in ['roc_auc','average_precision','precision','recall','f1','f2','false_positive_rate','alert_rate']:
        values=np.array([results[str(s)][metric] for s in SEEDS],dtype=float)
        summary[metric]={'mean':float(values.mean()),'sample_sd':float(values.std(ddof=1))}
    report={
        'schema_version':SCHEMA_VERSION,'run_id':f"SYN25K-S42-SPLIT42-MODEL42_52_62-{data_digest[:12]}",
        'data_source':'synthetic_only_not_MB','data_sha256':data_digest,
        'label_generation':'synthetic latent risk score + Gaussian noise; top 1.8 percentile labeled positive',
        'n_samples':len(df),'positive_rate':float(y.mean()),
        'split':{'train':len(y_train),'validation':len(y_val),'test':len(y_test),
                 'ratios':'60/20/20 stratified','same_split_for_all_model_seeds':True},
        'selection_protocol':{'metric':'F2','beta':2,'selection_data':'validation only',
           'candidate_thresholds':'unique validation scores plus nextafter(max, +inf)',
           'tie_break':'lower validation alert rate, then higher threshold',
           'test_used_for_threshold_selection':False},
        'demo_policy':{'model_seed':42,'high_threshold':max(.75,float(results['42']['threshold'])),
            'high_threshold_status':'display-only policy assumption; fixed minimum 0.75, not tuned or approved by MB'},
        'model_sha256':model_sha,
        'feature_order':FEATURES,
        'metrics':{'always_negative':baselines['always_negative'],'simple_rule':baselines['simple_rule'],
                   'xgboost_by_seed':results,'xgboost_seed_summary':summary},
        'latency_seed_42':_measure_inference_latency(models[42],X_test),
        'environment':{'python':platform.python_version(),'platform':platform.platform(),
             'machine':platform.machine(),'cpu_count':__import__('os').cpu_count(),
             'numpy':np.__version__,'pandas':pd.__version__,'scikit_learn':sklearn.__version__,
             'xgboost':xgb.__version__},
        'created_at_utc':datetime.now(timezone.utc).isoformat()
    }
    metric_path=out/'metrics.json'; metric_path.write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    pd.DataFrame(predictions).to_csv(out/'test_predictions.csv',index=False)
    pd.DataFrame(seed_rows).to_csv(out/'seed_results.csv',index=False)
    pd.DataFrame(tradeoff).to_csv(out/'threshold_tradeoff.csv',index=False)
    pd.DataFrame(pr_rows).to_csv(out/'pr_curve_seed42.csv',index=False)
    booster=models[42].get_booster()
    importance=pd.DataFrame({'feature':FEATURES,'gain':booster.get_score(importance_type='gain').values()})
    gain=booster.get_score(importance_type='gain')
    importance=pd.DataFrame([{'feature':f,'gain':float(gain.get(f,0))} for f in FEATURES]).sort_values('gain',ascending=False)
    importance.to_csv(out/'feature_importance_seed42.csv',index=False)
    manifest={'schema_version':SCHEMA_VERSION,'run_id':report['run_id'],'model_file':model_path.name,
      'model_sha256':model_sha,'metrics_file':metric_path.name,
      'metrics_sha256':hashlib.sha256(metric_path.read_bytes()).hexdigest(),
      'feature_order':FEATURES,'seed':42}
    (out/'artifact_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(report,ensure_ascii=False,indent=2))
    return models[42],report

if __name__=='__main__':
    train_and_save()
