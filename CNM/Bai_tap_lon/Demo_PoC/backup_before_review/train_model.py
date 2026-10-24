import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, roc_auc_score, confusion_matrix
import xgboost as xgb
import joblib

def generate_synthetic_bank_data(n_samples=20000, random_state=42):
    """
    Sinh tập dữ liệu giao dịch ngân hàng giả lập mô phỏng đặc thù Việt Nam (MB Bank)
    Tỷ lệ gian lận thực tế khoảng 1.5% - 2.0%
    """
    np.random.seed(random_state)
    
    # 1. Số tiền giao dịch (VND) - phân phối Log-Normal
    # Đại đa số giao dịch từ 50,000 VND đến 10,000,000 VND
    amount = np.random.lognormal(mean=13.5, sigma=1.5, size=n_samples)
    amount = np.clip(amount, 20000, 500000000) # Từ 20 nghìn đến 500 triệu
    
    # 2. Khung giờ giao dịch (0 - 23h)
    hour = np.random.choice(range(24), size=n_samples, p=[
        0.01, 0.005, 0.005, 0.005, 0.01, 0.02, # 0h - 5h (ít)
        0.04, 0.06, 0.08, 0.08, 0.07, 0.06,    # 6h - 11h
        0.05, 0.06, 0.08, 0.08, 0.07, 0.06,    # 12h - 17h
        0.06, 0.05, 0.03, 0.02, 0.015, 0.01   # 18h - 23h
    ])
    
    # 3. Kênh giao dịch (0: App MBBank, 1: Internet Banking, 2: Thẻ/POS, 3: Ví điện tử)
    channel = np.random.choice([0, 1, 2, 3], size=n_samples, p=[0.70, 0.15, 0.10, 0.05])
    
    # 4. Thiết bị mới đăng nhập (0: Cũ quen thuộc, 1: Thiết bị lạ vừa đổi)
    new_device = np.random.choice([0, 1], size=n_samples, p=[0.92, 0.08])
    
    # 5. Vị trí địa lý bất thường / Nhảy cóc tốc độ cao (0: Bình thường, 1: Bất thường)
    location_anomaly = np.random.choice([0, 1], size=n_samples, p=[0.95, 0.05])
    
    # 6. Số lần nhập sai OTP/PIN trong 30 phút qua (0, 1, 2, 3)
    failed_attempts = np.random.choice([0, 1, 2, 3], size=n_samples, p=[0.88, 0.08, 0.03, 0.01])
    
    # 7. Tần suất giao dịch liên tiếp trong 10 phút gần nhất (1 đến 15 lần)
    tx_frequency_10m = np.random.geometric(p=0.4, size=n_samples)
    tx_frequency_10m = np.clip(tx_frequency_10m, 1, 20)
    
    # 8. Tuổi tài khoản nhận tiền (0: Tài khoản mới mở < 7 ngày / tài khoản rác, 1: Bình thường)
    new_beneficiary = np.random.choice([0, 1], size=n_samples, p=[0.15, 0.85])

    # Xây dựng nhãn gian lận thực tế dựa trên sự kết hợp rủi ro
    risk_score = (
        (amount > 30000000).astype(int) * 2.0 +
        (amount > 100000000).astype(int) * 3.0 +
        ((hour >= 1) & (hour <= 4)).astype(int) * 2.5 +
        new_device * 3.5 +
        location_anomaly * 4.0 +
        (failed_attempts >= 2).astype(int) * 3.0 +
        (tx_frequency_10m >= 5).astype(int) * 2.5 +
        (new_beneficiary == 0).astype(int) * 2.0
    )
    
    # Thêm nhiễu ngẫu nhiên
    risk_score += np.random.normal(0, 1.2, size=n_samples)
    
    # Ngưỡng gian lận (khoảng 1.8% mẫu bị coi là gian lận rõ rệt)
    threshold = np.percentile(risk_score, 98.2)
    is_fraud = (risk_score >= threshold).astype(int)
    
    df = pd.DataFrame({
        'amount': amount,
        'hour': hour,
        'channel': channel,
        'new_device': new_device,
        'location_anomaly': location_anomaly,
        'failed_attempts': failed_attempts,
        'tx_frequency_10m': tx_frequency_10m,
        'new_beneficiary': new_beneficiary,
        'is_fraud': is_fraud
    })
    
    return df

def train_and_save():
    print("⏳ Đang sinh dữ liệu giao dịch ngân hàng giả lập...")
    df = generate_synthetic_bank_data(n_samples=25000)
    
    X = df.drop('is_fraud', axis=1)
    y = df['is_fraud']
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    # Tỷ lệ mất cân bằng
    scale_pos_weight = (len(y_train) - sum(y_train)) / sum(y_train)
    
    print(f"🔹 Huấn luyện mô hình XGBoost với scale_pos_weight = {scale_pos_weight:.2f}...")
    model = xgb.XGBClassifier(
        n_estimators=150,
        max_depth=5,
        learning_rate=0.08,
        scale_pos_weight=scale_pos_weight,
        subsample=0.8,
        colsample_bytree=0.8,
        eval_metric='aucpr',
        random_state=42
    )
    model.fit(X_train, y_train)
    
    # Đánh giá
    y_pred_proba = model.predict_proba(X_test)[:, 1]
    y_pred = (y_pred_proba >= 0.5).astype(int)
    
    roc_auc = roc_auc_score(y_test, y_pred_proba)
    print("\n✅ KẾT QUẢ ĐÁNH GIÁ MÔ HÌNH:")
    print(f"ROC-AUC Score: {roc_auc:.4f}")
    print(classification_report(y_test, y_pred, target_names=['Bình thường', 'Gian lận']))
    
    # Lưu mô hình
    save_path = "/Users/dovandat/WORKSPACE/HVNH/CNM/Bai_tap_lon/Demo_PoC/fraud_model.pkl"
    joblib.dump(model, save_path)
    print(f"💾 Đã lưu mô hình thành công vào: {save_path}")

if __name__ == '__main__':
    train_and_save()
