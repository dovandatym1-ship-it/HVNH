# 📚 HƯỚNG DẪN XỬ LÝ DỮ LIỆU KHUYẾT THIẾU (MISSING VALUES IMPUTATION)

**Tác giả:** Đỗ Văn Đạt  
**Chuyên ngành:** Phân tích dữ liệu trong kinh doanh (Business Analytics)  
**Mục đích:** Tài liệu tham khảo chuẩn cho các bài tập EDA, Tiền xử lý dữ liệu và Xây dựng mô hình học máy (Machine Learning).

---

## 1. TẠI SAO PHẢI XỬ LÝ DỮ LIỆU KHUYẾT (MISSING VALUES)?

* **Xóa dòng (`dropna`):** Làm mất kích thước mẫu ($N$), lãng phí thông tin quý giá ở các cột khác trong cùng một dòng.
* **Điền khuyết (Imputation):** Duy trì kích thước mẫu, giúp mô hình học máy (như hồi quy Logistic, cây quyết định, SVM,...) có thể nhận diện và xử lý toàn bộ tập dữ liệu mà không bị lỗi.

---

## 2. BẢN CHẤT: PHÂN BIỆT MEAN (TRUNG BÌNH) VÀ MEDIAN (TRUNG VỊ)

### Ví dụ trực quan:
Xét mức thu nhập của nhóm 5 người:
$$\text{Thu nhập (triệu VNĐ): } [10, 12, 11, 15, 1.000]$$

| Chỉ số | Công thức | Giá trị tính toán | Nhận xét thực tế |
| :--- | :---: | :---: | :--- |
| **Mean (Trung bình)** | $\bar{x} = \frac{\sum x_i}{n}$ | **209.6 triệu** | ❌ **Bị kéo lệch cực mạnh** bởi giá trị ngoại lai $1.000$ triệu. Con số này không đại diện cho bất kỳ ai trong 4 người có thu nhập bình thường. |
| **Median (Trung vị)** | Giá trị chính giữa | **12 triệu** |  **Chính xác & đại diện:** Không hề bị tác động bởi người có thu nhập 1 tỷ kia. |

---

## 3. SƠ ĐỒ QUYẾT ĐỊNH (DECISION TREE) CHỌN PHƯƠNG PHÁP ĐIỀN KHUYẾT

```
                                  KIỂU DỮ LIỆU CỦA BIẾN
                                            │
                     ┌──────────────────────┴──────────────────────┐
                     ▼                                             ▼
           BIẾN ĐỊNH TÍNH (Categorical)                  BIẾN ĐỊNH LƯỢNG (Numerical)
           (Chữ / Phân loại / Giới tính)                 (Số / Tuổi / Thu nhập / Điểm)
                     │                                             │
                     ▼                                 Kiểm tra Phân phối & Outlier
          DÙNG MODE (Yếu vị)                                       │
     (Giá trị có tần số cao nhất)                 ┌────────────────┴────────────────┐
                     │                            ▼                                 ▼
                     │                 Phân phối Chuẩn / Đối xứng          Phân phối Lệch (Skewed)
                     │                    (Không có Outlier)              (Hoặc có nhiều Outliers)
                     │                            │                                 │
                     │                            ▼                                 ▼
                     │                 DÙNG MEAN (Trung bình)            DÙNG MEDIAN (Trung vị)
                     │                            │                                 │
                     └────────────────────────────┼─────────────────────────────────┘
                                                  ▼
                                (Thực hiện df[col].fillna(...))
```

---

## 4. BẢNG SO SÁNH CHI TIẾT CÁC PHƯƠNG PHÁP

| Tiêu chí | Điền bằng **MEAN (Trung bình)** | Điền bằng **MEDIAN (Trung vị)** | Điền bằng **MODE (Yếu vị)** |
| :--- | :--- | :--- | :--- |
| **Loại biến áp dụng** | Biến định lượng (Số). | Biến định lượng (Số). | Biến định tính (Chữ / Phân loại). |
| **Phân phối dữ liệu** | Phân phối chuẩn (Normal), hình chuông đối xứng. | Phân phối lệch (Left/Right Skewed). | Mọi phân phối. |
| **Hệ số lệch (Skewness)** | $-0.5 \le \text{Skew} \le 0.5$ | $\text{Skew} < -0.5$ hoặc $\text{Skew} > 0.5$ | Không áp dụng. |
| **Xử lý Outlier** | Rất nhạy cảm với ngoại lai (Không nên dùng nếu có Outlier). | **Kháng ngoại lai cực tốt (Robust).** | Bỏ qua ngoại lai. |
| **Ví dụ điển hình** | Tuổi (`Customer_Age`), Chiều cao, Nhiệt độ. | Thu nhập (`Income`), Giá nhà, Dư nợ thẻ tín dụng. | Giới tính (`Gender`), Nghề nghiệp, Trình độ học vấn. |

---

## 5. MÃ NGUỒN PYTHON MẪU (CODE TEMPLATE)

### Cách 1: Sử dụng Pandas (Cơ bản & Trực quan)

```python
import pandas as pd
import numpy as np

# 1. Điền biến định tính bằng MODE
qual_cols = df.select_dtypes(include=['object']).columns
for col in qual_cols:
    mode_val = df[col].mode()[0]
    df[col] = df[col].fillna(mode_val)

# 2. Điền biến định lượng dựa theo độ lệch (Skewness)
quant_cols = df.select_dtypes(include=[np.number]).columns
for col in quant_cols:
    skew_val = df[col].skew()
    if abs(skew_val) <= 0.5:
        # Đối xứng -> Điền Mean
        fill_val = df[col].mean()
    else:
        # Lệch / Outlier -> Điền Median
        fill_val = df[col].median()
    df[col] = df[col].fillna(fill_val)
```

---

### Cách 2: Sử dụng Scikit-learn `SimpleImputer` (Chuẩn Machine Learning Pipeline)

```python
from sklearn.impute import SimpleImputer

# Imputer cho biến số (Strategy: 'mean' hoặc 'median')
num_imputer = SimpleImputer(strategy='median')
df[quant_cols] = num_imputer.fit_transform(df[quant_cols])

# Imputer cho biến phân loại (Strategy: 'most_frequent')
cat_imputer = SimpleImputer(strategy='most_frequent')
df[qual_cols] = cat_imputer.fit_transform(df[qual_cols])
```

---

## 6. LƯU Ý KHI LÀM BÀI BÁO CÁO / NGHIÊN CỨU

1. **Phương sai bị giảm:** Điền giá trị hằng số (Mean/Median) làm giảm độ biến thiên tự nhiên của dữ liệu.
2. **Kỹ thuật Cờ cảnh báo (Missing Indicator):** Nếu một biến bị khuyết > 5% - 10%, nên tạo thêm 1 cột phụ `col_is_missing` (nhận giá trị $1$ nếu khuyết, $0$ nếu có sẵn) để mô hình học máy nhận biết được hành vi thiếu dữ liệu của khách hàng.
