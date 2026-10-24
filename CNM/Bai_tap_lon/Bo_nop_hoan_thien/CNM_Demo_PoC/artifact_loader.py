"""Fail-closed loading for model + evaluation artifacts."""
import hashlib
import json
from pathlib import Path
import xgboost as xgb
from train_model import FEATURES, SCHEMA_VERSION


def verify_artifacts(directory):
    base=Path(directory)
    manifest=json.loads((base/'artifact_manifest.json').read_text(encoding='utf-8'))
    metrics_path=base/manifest['metrics_file']; model_path=base/manifest['model_file']
    metrics_sha=hashlib.sha256(metrics_path.read_bytes()).hexdigest()
    model_sha=hashlib.sha256(model_path.read_bytes()).hexdigest()
    if manifest.get('schema_version')!=SCHEMA_VERSION: raise ValueError('Sai schema_version trong manifest.')
    if manifest.get('feature_order')!=FEATURES: raise ValueError('Thứ tự feature trong manifest không khớp.')
    if metrics_sha!=manifest.get('metrics_sha256'): raise ValueError('metrics.json không cùng artifact manifest.')
    if model_sha!=manifest.get('model_sha256'): raise ValueError('Model không cùng artifact manifest.')
    metrics=json.loads(metrics_path.read_text(encoding='utf-8'))
    if metrics.get('model_sha256')!=model_sha or metrics.get('run_id')!=manifest.get('run_id'):
        raise ValueError('Run ID hoặc hash model/metrics không nhất quán.')
    model=xgb.XGBClassifier(); model.load_model(model_path)
    if model.get_booster().feature_names!=FEATURES: raise ValueError('Feature model không khớp contract.')
    return model,metrics,manifest
