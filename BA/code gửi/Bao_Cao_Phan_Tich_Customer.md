# 📋 BÁO CÁO PHÂN TÍCH DỮ LIỆU KHÁCH HÀNG (CUSTOMER ANALYSIS REPORT)

**Học phần:** Phân tích dữ liệu trong kinh doanh (Business Analytics)  
**Tập dữ liệu:** `customer.csv` (10,108 quan sát x 16 biến)  
**Tác giả:** Đỗ Văn Đạt  
**Môi trường thực thi:** Python 3 (Pandas, NumPy, Matplotlib, Seaborn, SciPy)  
**File mã nguồn:** [`customer_DatDV_160826.ipynb`](customer_DatDV_160826.ipynb)  

---

## 1. TỔNG QUAN VỀ TẬP DỮ LIỆU & KIỂU BIẾN (CÂU 1)

Bộ dữ liệu chứa thông tin nhân khẩu học và giao dịch tín dụng của khách hàng ngân hàng.

* **Số lượng quan sát (dòng):** **10,108** khách hàng.
* **Số lượng biến (cột):** **16** biến.
* **Dữ liệu khuyết (Missing value):** $0$ (tập dữ liệu hoàn chỉnh, không có giá trị Null).

### Bảng phân loại chi tiết các biến:

| STT | Tên biến | Kiểu dữ liệu Python | Thang đo / Phân loại Thống kê | Diễn giải ý nghĩa |
| :---: | :--- | :---: | :--- | :--- |
| 1 | `Client_Num` | `int64` | Định lượng rời rạc (Mã định danh) | Mã số định danh duy nhất của khách hàng |
| 2 | `Customer_Age` | `int64` | Định lượng liên tục/tỷ lệ | Độ tuổi của khách hàng (21 - 73 tuổi) |
| 3 | `Gender` | `object/str` | Định tính danh nghĩa (Nominal) | Giới tính khách hàng (`F`: Nữ, `M`: Nam) |
| 4 | `Dependent_Count` | `int64` | Định lượng rời rạc | Số lượng người phụ thuộc tài chính (0 - 5 người) |
| 5 | `Education_Level` | `object/str` | Định tính thứ bậc (Ordinal) | Trình độ học vấn (Uneducated, High School, Graduate,...) |
| 6 | `Marital_Status` | `object/str` | Định tính danh nghĩa (Nominal) | Tình trạng hôn nhân (Married, Single, Divorced,...) |
| 7 | `state_cd` | `object/str` | Định tính danh nghĩa (Nominal) | Mã bang / Thành phố cư trú (28 bang) |
| 8 | `Zipcode` | `int64` | Định tính danh nghĩa (Mã vùng) | Mã bưu chính khu vực |
| 9 | `Car_Owner` | `object/str` | Định tính nhị phân (Binary) | Sở hữu ô tô (`yes` / `no`) |
| 10 | `House_Owner` | `object/str` | Định tính nhị phân (Binary) | Sở hữu nhà ở (`yes` / `no`) |
| 11 | `Personal_loan` | `object/str` | Định tính nhị phân (Binary) | Có khoản vay cá nhân (`yes` / `no`) |
| 12 | `contact` | `object/str` | Định tính danh nghĩa (Nominal) | Kênh liên hệ (cellular, telephone, unknown) |
| 13 | `Customer_Job` | `object/str` | Định tính danh nghĩa (Nominal) | Nghề nghiệp khách hàng |
| 14 | `Income` | `int64` | Định lượng liên tục/tỷ lệ | Thu nhập hàng năm của khách hàng (USD) |
| 15 | `Cust_Satisfaction_Score` | `int64` | Định tính thứ bậc (Thang Likert) | Điểm đánh giá độ hài lòng (1 - 5) |
| 16 | `Total_Trans_Ct` | `int64` | Định lượng rời rạc | Tổng số lượng giao dịch thẻ đã thực hiện |

---

## 2. BẢNG TỔNG QUAN MÔ TẢ TOÀN BỘ DỮ LIỆU (CÂU 2)

### A. Thống kê mô tả biến định lượng (Quantitative Statistics)

$$ \text{Mean} = \frac{1}{n}\sum_{i=1}^n x_i, \quad s = \sqrt{\frac{1}{n-1}\sum_{i=1}^n (x_i - \bar{x})^2} $$

| Tên biến | Số lượng | Trung bình (Mean) | Độ lệch chuẩn (Std) | Min | Tứ phân vị Q1 (25%) | Trung vị Q2 (50%) | Tứ phân vị Q3 (75%) | Max |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Customer_Age** | 10,108 | 46.27 | 8.09 | 21 | 41.00 | 46.00 | 52.00 | 73 |
| **Dependent_Count** | 10,108 | 2.35 | 1.30 | 0 | 1.00 | 2.00 | 3.00 | 5 |
| **Income** | 10,108 | 56,976.10 | 38,103.54 | 0 | 29,985.75 | 44,792.00 | 76,392.75 | 239,791 |
| **Cust_Satisfaction_Score** | 10,108 | 3.19 | 1.26 | 1 | 2.00 | 3.00 | 4.00 | 5 |
| **Total_Trans_Ct** | 10,108 | 64.81 | 23.45 | 10 | 45.00 | 67.00 | 81.00 | 139 |

### B. Thống kê mô tả biến định tính (Qualitative / Categorical Statistics)

| Tên biến | Số lượng | Số nhóm (Unique) | Giá trị phổ biến nhất (Top) | Tần số cao nhất (Freq) | Tỷ trọng nhóm phổ biến (%) |
| :--- | :---: | :---: | :--- | :---: | :---: |
| **Gender** | 10,108 | 2 | `F` (Nữ) | 5,880 | 58.17% |
| **Education_Level** | 10,108 | 6 | `Graduate` (Tốt nghiệp ĐH) | 4,134 | 40.90% |
| **Marital_Status** | 10,108 | 3 | `Married` (Đã kết hôn) | 5,128 | 50.73% |
| **state_cd** | 10,108 | 28 | `CA` (California) | 2,468 | 24.42% |
| **Car_Owner** | 10,108 | 2 | `no` (Không sở hữu ô tô) | 6,044 | 59.79% |
| **House_Owner** | 10,108 | 2 | `no` (Không sở hữu nhà) | 5,390 | 53.32% |
| **Personal_loan** | 10,108 | 2 | `no` (Không vay cá nhân) | 8,822 | 87.28% |
| **contact** | 10,108 | 3 | `cellular` (Điện thoại di động) | 7,457 | 73.77% |
| **Customer_Job** | 10,108 | 6 | `Selfemployeed` (Tự kinh doanh) | 2,575 | 25.47% |

---

## 3. THỐNG KÊ MÔ TẢ ĐẦY ĐỦ CHO BIẾN ĐỘ TUỔI (`Customer_Age`) (CÂU 3)

| STT | Chỉ tiêu thống kê | Ký hiệu / Công thức | Giá trị tính toán | Ý nghĩa thống kê & Nghiệp vụ |
| :---: | :--- | :---: | :---: | :--- |
| 1 | **Trung bình (Mean)** | $\bar{x} = \frac{\sum x}{n}$ | **46.2744 tuổi** | Độ tuổi bình quân của toàn bộ khách hàng. |
| 2 | **Trung vị (Median / Q2)** | $Me = x_{(50\%)}$ | **46.0000 tuổi** | Điểm phân vị chính giữa, 50% khách hàng $\le 46$ tuổi và 50% khách hàng $\ge 46$ tuổi. |
| 3 | **Yếu vị / Mốt (Mode)** | $Mo$ | **44 tuổi** | Độ tuổi có mật độ khách hàng đông đảo nhất. |
| 4 | **Phương sai mẫu (Variance)** | $s^2 = \frac{\sum (x - \bar{x})^2}{n-1}$ | **65.4137** | Mức độ phân tán bình phương của độ tuổi quanh số trung bình. |
| 5 | **Độ lệch chuẩn mẫu (Std)** | $s = \sqrt{s^2}$ | **8.0879 tuổi** | Độ phân tán trung bình của độ tuổi là $\approx 8.09$ tuổi. |
| 6 | **Tứ phân vị thứ nhất (Q1)** | $Q_1 = x_{(25\%)}$ | **41.0000 tuổi** | Có 25% khách hàng trẻ hơn hoặc bằng 41 tuổi. |
| 7 | **Tứ phân vị thứ hai (Q2)** | $Q_2 = Me$ | **46.0000 tuổi** | Trùng khớp với giá trị trung vị. |
| 8 | **Tứ phân vị thứ ba (Q3)** | $Q_3 = x_{(75\%)}$ | **52.0000 tuổi** | Có 75% khách hàng dưới 52 tuổi (hoặc 25% lớn hơn 52 tuổi). |
| 9 | **Khoảng tứ phân vị (IQR / TQR)** | $IQR = Q_3 - Q_1$ | **11.0000 tuổi** | 50% khách hàng ở vùng lõi trung tâm dao động trong độ tuổi từ 41 đến 52. |
| 10 | **Hệ số biến thiên (CV %)** | $CV = \frac{s}{\bar{x}} \times 100\%$ | **17.4781%** | $CV < 20\%$, chứng tỏ mức độ biến thiên thấp, dữ liệu có tính đồng nhất cao. |

---

## 4. PHÂN BỐ KHÁCH HÀNG THEO THÀNH PHỐ / BANG (`state_cd`) (CÂU 4)

Khách hàng phân bố rải rác trên **28 bang/thành phố**, tuy nhiên có sự tập trung rất cao tại các trung tâm kinh tế:

* **Thành phố/Bang đông khách hàng nhất:** **CA (California)** với **2,468** khách hàng (**24.42%**).
* **Thành phố/Bang ít khách hàng nhất:** **OR (Oregon)** với **5** khách hàng (**0.05%**).
* **Top 4 bang lớn:** CA, TX, NY, FL đóng góp tới **87.48%** tổng số khách hàng toàn hệ thống.

### Bảng phân bố Top 10 bang lớn nhất:
| Bang (state_cd) | Tên đầy đủ | Số lượng khách hàng | Tỷ trọng (%) | Tỷ trọng tích lũy (%) |
| :---: | :--- | :---: | :---: | :---: |
| **CA** | California | 2,468 | 24.42% | 24.42% |
| **TX** | Texas | 2,394 | 23.68% | 48.10% |
| **NY** | New York | 2,270 | 22.46% | 70.56% |
| **FL** | Florida | 1,711 | 16.93% | 87.48% |
| **NJ** | New Jersey | 716 | 7.08% | 94.57% |
| **MI** | Michigan | 63 | 0.62% | 95.19% |
| **IL** | Illinois | 58 | 0.57% | 95.77% |
| **NV** | Nevada | 56 | 0.55% | 96.32% |
| **IA** | Iowa | 47 | 0.46% | 96.78% |
| **AK** | Alaska | 31 | 0.31% | 97.09% |

---

## 5. PHÂN CHIA NHÓM TUỔI & TỶ TRỌNG (CÂU 5)

Phân chia theo các nhóm tuổi theo yêu cầu nghiệp vụ:

| Nhóm tuổi | Khoảng độ tuổi | Số lượng khách hàng | Tỷ trọng (%) | Đánh giá |
| :---: | :---: | :---: | :---: | :--- |
| **18 - 24** | $18 \le \text{Tuổi} \le 24$ | 15 | 0.15% | Nhóm khách hàng sinh viên/mới đi làm (tỷ lệ rất nhỏ). |
| **25 - 34** | $25 \le \text{Tuổi} \le 34$ | 739 | 7.31% | Nhóm người trẻ bắt đầu tích lũy tài chính. |
| **35 - 44** | $35 \le \text{Tuổi} \le 44$ | 3,434 | 33.97% | Nhóm khách hàng gia đình, tài chính ổn định. |
| **45 - 54** | $45 \le \text{Tuổi} \le 54$ | **4,311** | **42.65%** | **Nhóm chiếm tỷ trọng LỚN NHẤT (Khách hàng mục tiêu cốt lõi).** |
| **55 - 64** | $55 \le \text{Tuổi} \le 64$ | 1,498 | 14.82% | Nhóm trung niên, chuẩn bị nghỉ hưu. |
| **65+** | $\text{Tuổi} \ge 65$ | 111 | 1.10% | Nhóm khách hàng cao tuổi đã nghỉ hưu. |
| **Tổng cộng** | | **10,108** | **100.00%** | |

👉 **Kết luận:** Khách hàng chủ lực của ngân hàng tập trung trong độ tuổi **35 - 54 tuổi** (chiếm tới **76.62%** tổng khách hàng).

---

## 6. SO SÁNH THỐNG KÊ TUỔI GIỮA CÁC THÀNH PHỐ (CÂU 6)

### Tiêu chí xác định thành phố "già" nhất:
1. **Theo độ tuổi trung bình (Mean Age) cao nhất:** **NE (Nebraska)** đạt **51.38 tuổi** (tiếp theo là AK: 50.45, PA: 50.22, NM: 49.92).
2. **Theo trung vị tuổi (Median Age) cao nhất:** **NM (New Mexico)** đạt **52.50 tuổi** (tiếp theo là AK: 52.0, PA: 52.0).
3. **Theo khách hàng cao tuổi nhất (Max Age):** **IL (Illinois)** sở hữu khách hàng lớn tuổi nhất đạt **73 tuổi**.

---

## 7. MÃ HOÁ BIẾN & MA TRẬN TƯƠNG QUAN PEARSON (CÂU 7)

### Phương pháp mã hóa:
1. **Biến giới tính (`Gender`):** Mã hoá nhị phân (Binary Encoding): $\text{Female} = 0, \text{Male} = 1$.
2. **Biến thành phố/bang (`state_cd`):** Mã hoá biến giả (One-hot Dummy Encoding): Tạo 28 cột `State_CA`, `State_TX`,... nhận giá trị $\{0, 1\}$.

### Kết quả tương quan:
* $r(\text{Customer\_Age}, \text{Gender\_M}) = -0.029$: Tuổi tác không có sự phân hóa theo giới tính.
* $r(\text{Customer\_Age}, \text{Dependent\_Count}) = -0.120$: Tương quan âm nhẹ; khách hàng càng lớn tuổi thì số con cái/người phụ thuộc sống cùng càng giảm.
* Tương quan giữa `Customer_Age` và các biến giả bang (`State_*`) đều rất thấp ($|r| < 0.03$).

---

## 8. BIỂU ĐỒ TẦN SUẤT (HISTOGRAM) & ĐƯỜNG MẬT ĐỘ (KDE) (CÂU 8)

* **Hình dạng phân phối:** Phân phối đơn đỉnh (unimodal), hình chuông gần như đối xứng hoàn hảo (xấp xỉ phân phối chuẩn $N(\mu \approx 46.27, \sigma \approx 8.09)$).
* **Đường thẳng trung bình & trung vị:** Giá trị $\text{Mean} = 46.27$ và $\text{Median} = 46.00$ hầu như trùng khít tại trục tâm của đồ thị.

---

## 9. BIỂU ĐỒ HỘP (BOXPLOT) SO SÁNH TUỔI NAM VÀ NỮ (CÂU 9)

| Giới tính | Số lượng | Mean | Std | Min | Q1 | Median | Q3 | Max | IQR |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Nữ (F)** | 5,880 | 46.48 | 8.01 | 21 | 41.0 | 47.0 | 52.0 | 67 | 11.0 |
| **Nam (M)** | 4,228 | 45.99 | 8.19 | 21 | 40.0 | 46.0 | 52.0 | 73 | 12.0 |

* **Nhận xét Boxplot:**
  * Độ cao thân hộp (IQR) và đường gạch trung vị (Median) của Nam và Nữ gần như bằng nhau.
  * Nhóm Nam giới có điểm ngoại lai nhẹ (Outlier) phía trên ở tuổi 73.
  * Tỷ lệ khách hàng Nữ chiếm thế đa số trong tập dữ liệu (58.17% Nữ so với 41.83% Nam).

---

<!-- GOAL_COMPLETE -->
