# KẾ HOẠCH LỊCH TRÌNH: MÔ HÌNH MẠNG PERT, ĐƯỜNG GĂNG (CPM) VÀ BIỂU ĐỒ GANTT
## Dự án: Xây dựng Hệ thống Quản trị Nhân sự Nội bộ (ABC-HRM)
### Mã tài liệu: BTL-QLDA-B5-B6 | Giai đoạn: Lập kế hoạch (Planning)
### Tiêu chuẩn áp dụng: PMI PMBOK Guide / Schedule Network Analysis | Học phần: QLDA CNTT Nâng cao (HVNH)

---

## 1. TỔNG QUAN VỀ QUẢN LÝ TIẾN ĐỘ VÀ PHƯƠNG PHÁP LUẬN

Để thiết lập **Đường cơ sở Lịch trình (Schedule Baseline)** có căn cứ khoa học vững chắc, nhóm nghiên cứu áp dụng phối hợp 3 kỹ thuật phân tích lịch trình chuẩn mực quốc tế:
1. **Phương pháp Lập sơ đồ Theo thứ tự Ưu tiên (Precedence Diagramming Method - PDM):** Xác định các mối quan hệ logic phụ thuộc trước - sau (Dependencies: Finish-to-Start [FS], Start-to-Start [SS], Finish-to-Finish [FF]) giữa các hoạt động.
2. **Kỹ thuật Ước tính Ba điểm PERT (Program Evaluation and Review Technique):** Lượng hóa yếu tố rủi ro và bất định của các công việc phát triển phần mềm thông qua 3 kịch bản: Lạc quan ($O$), Khả dĩ nhất ($M$), và Bi quan ($P$).
3. **Phương pháp Đường Găng (Critical Path Method - CPM):** Tính toán các mốc thời gian sớm nhất (Early Start - ES, Early Finish - EF) và muộn nhất (Late Start - LS, Late Finish - LF) thông qua hai lượt duyệt thuận (Forward Pass) và duyệt nghịch (Backward Pass) để xác định các hoạt động găng và tổng thời lượng dự án.

---

## 2. BẢNG ƯỚC TÍNH THỜI LƯỢNG BA ĐIỂM PERT (13 HOẠT ĐỘNG CHÍNH)

Công thức tính thời lượng kỳ vọng ($T_e$), phương sai ($\sigma^2$) và độ lệch chuẩn ($\sigma$) theo phân phối xác suất Beta:
$$T_e = \frac{O + 4M + P}{6} \quad ; \quad \sigma = \frac{P - O}{6} \quad ; \quad \sigma^2 = \left( \frac{P - O}{6} \right)^2$$

| Mã HĐ | Tên Hoạt động Dự án | Hoạt động Tiền nhiệm | Mối quan hệ Ràng buộc | $O$ *(Lạc quan)* | $M$ *(Khả dĩ)* | $P$ *(Bi quan)* | Thời lượng kỳ vọng $T_e$ (ngày) | Độ lệch chuẩn $\sigma$ | Phương sai $\sigma^2$ |
|:---:|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **A** | Khảo sát Hiện trạng & Đặc tả SRS | — | — | 8,0 | 12,0 | 20,0 | **12,67** | 2,00 | 4,00 |
| **B** | Thiết kế Kiến trúc Hệ thống & CSDL | A | FS | 5,0 | 8,0 | 14,0 | **8,50** | 1,50 | 2,25 |
| **C** | Thiết kế Giao diện Chi tiết UI/UX | A | FS | 5,0 | 7,0 | 12,0 | **7,50** | 1,17 | 1,36 |
| **D** | Lập trình Module Hồ sơ Nhân sự | B, C | FS | 8,0 | 10,0 | 15,0 | **10,50** | 1,17 | 1,36 |
| **E** | Lập trình Module Chấm công & SDK | B | FS | 10,0 | 14,0 | 22,0 | **14,67** | 2,00 | 4,00 |
| **F** | Lập trình Module Tính lương & Thuế | E | FS | 12,0 | 18,0 | 28,0 | **18,67** | 2,67 | 7,11 |
| **G** | Lập trình Module Tuyển dụng & Onboarding | D | SS | 6,0 | 8,0 | 12,0 | **8,33** | 1,00 | 1,00 |
| **H** | Lập trình Module Quản trị KPI | D | FS | 8,0 | 10,0 | 16,0 | **10,67** | 1,33 | 1,78 |
| **I** | Lập trình Module Dashboard & Báo cáo | F, H | FS | 6,0 | 8,0 | 14,0 | **8,67** | 1,33 | 1,78 |
| **J** | Kiểm thử Tích hợp & Kiểm thử Tải | D, F, G, I | FS | 8,0 | 12,0 | 18,0 | **12,33** | 1,67 | 2,78 |
| **K** | Kiểm thử Chấp nhận Người dùng (UAT) | J | FS | 5,0 | 7,0 | 10,0 | **7,17** | 0,83 | 0,69 |
| **L** | Cài đặt Production & Di chuyển Dữ liệu | K | FS | 3,0 | 5,0 | 10,0 | **5,50** | 1,17 | 1,36 |
| **M** | Đào tạo Người dùng & Go-Live | L | FS | 3,0 | 5,0 | 7,0 | **5,00** | 0,67 | 0,44 |

---

## 3. TÍNH TOÁN THỜI ĐIỂM SỚM/MUỘN VÀ XÁC ĐỊNH ĐỘ TRỄ (CPM FORWARD & BACKWARD PASS)

* **Quy tắc Duyệt Thuận (Forward Pass):** Tính $ES$ (Bắt đầu sớm) và $EF = ES + T_e$ (Kết thúc sớm). Với hoạt động có nhiều tiền nhiệm, $ES = \max(EF_{\text{tiền nhiệm}})$.
* **Quy tắc Duyệt Nghịch (Backward Pass):** Tính $LF$ (Kết thúc muộn) và $LS = LF - T_e$ (Bắt đầu muộn). Với hoạt động có nhiều kế nhiệm, $LF = \min(LS_{\text{kế nhiệm}})$.
* **Độ trễ tổng thể (Total Float - TF):** $TF = LS - ES = LF - EF$. Hoạt động có $TF = 0$ là **Hoạt động Găng (Critical Activity)**.
* **Độ trễ tự do (Free Float - FF):** $FF = \min(ES_{\text{kế nhiệm}}) - EF$.

### Bảng Kết Quả Tính Toán Đường Găng (CPM Parameters Table):

| Mã HĐ | Tên Hoạt động | $T_e$ *(ngày)* | Bắt đầu sớm ($ES$) | Kết thúc sớm ($EF$) | Bắt đầu muộn ($LS$) | Kết thúc muộn ($LF$) | Total Float ($TF$) | Free Float ($FF$) | Trạng thái Găng |
|:---:|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **A** | Khảo sát & Đặc tả SRS | 12,67 | **0,00** | **12,67** | **0,00** | **12,67** | **0,00** | 0,00 | **GĂNG (Critical)** |
| **B** | Thiết kế Kiến trúc & CSDL | 8,50 | **12,67** | **21,17** | **12,67** | **21,17** | **0,00** | 0,00 | **GĂNG (Critical)** |
| **C** | Thiết kế Giao diện UI/UX | 7,50 | 12,67 | 20,17 | 13,67 | 21,17 | 1,00 | 1,00 | Không găng (Float 1 ngày) |
| **D** | Lập trình Module Hồ sơ NS | 10,50 | 21,17 | 31,67 | 39,34 | 49,84 | 18,17 | 0,00 | Không găng (Float 18,17 ngày) |
| **E** | Lập trình Module Chấm công & SDK | 14,67 | **21,17** | **35,84** | **21,17** | **35,84** | **0,00** | 0,00 | **GĂNG (Critical)** |
| **F** | Lập trình Module Tính lương | 18,67 | **35,84** | **54,51** | **35,84** | **54,51** | **0,00** | 0,00 | **GĂNG (Critical)** |
| **G** | Lập trình Tuyển dụng & Onboarding | 8,33 | 25,00 | 33,33 | 41,51 | 49,84 | 16,51 | 16,51 | Không găng (Float 16,51 ngày) |
| **H** | Lập trình Module Quản trị KPI | 10,67 | 31,67 | 42,34 | 35,17 | 45,84 | 3,50 | 3,50 | Không găng (Float 3,50 ngày) |
| **I** | Lập trình Dashboard & Báo cáo | 8,67 | 54,51 | 63,18 | 54,51 | 63,18 | 8,66 | 0,00 | Không găng (Float 8,66 ngày) |
| **J** | Kiểm thử Tích hợp & Tải | 12,33 | **54,51** | **66,84** | **54,51** | **66,84** | **0,00** | 0,00 | **GĂNG (Critical)** |
| **K** | Kiểm thử Nghiệm thu UAT | 7,17 | **66,84** | **74,01** | **66,84** | **74,01** | **0,00** | 0,00 | **GĂNG (Critical)** |
| **L** | Cài đặt Production & Di chuyển DL | 5,50 | **74,01** | **79,51** | **74,01** | **79,51** | **0,00** | 0,00 | **GĂNG (Critical)** |
| **M** | Đào tạo & Go-Live | 5,00 | **79,51** | **84,51** | **79,51** | **84,51** | **0,00** | 0,00 | **GĂNG (Critical)** |

---

## 4. XÁC LẬP ĐƯỜNG GĂNG (CRITICAL PATH) VÀ PHÂN TÍCH RỦI RO LỊCH TRÌNH

### 4.1. Chuỗi Hoạt Động Trên Đường Găng
Căn cứ vào bảng tính toán, chuỗi đường găng có tổng $TF = 0$ duy nhất của dự án là:
$$\mathbf{A \longrightarrow B \longrightarrow E \longrightarrow F \longrightarrow J \longrightarrow K \longrightarrow L \longrightarrow M}$$

$$\text{Tổng thời lượng đường găng } T_{\text{Critical}} = 12,67 + 8,50 + 14,67 + 18,67 + 12,33 + 7,17 + 5,50 + 5,00 = \mathbf{84,51 \text{ ngày công làm việc}}$$
Quy đổi theo tuần làm việc tiêu chuẩn 5 ngày/tuần (không tính Thứ Bảy, Chủ Nhật và ngày nghỉ lễ):
$$\text{Thời gian thực hiện dự án} \approx \frac{84,51}{5} \times 7 \approx 118 \text{ ngày lịch} \approx \mathbf{24 \text{ tuần làm việc (6 tháng)}}$$
*Thời gian này hoàn toàn ăn khớp tuyệt đối với mốc mục tiêu bắt đầu từ **01/11/2025** và Go-live vào **30/04/2026** đã cam kết trong Hiến chương Dự án.*

---

### 4.2. Luận Giải Khoa Học: Tại sao Phân hệ Chấm công (E) và Tính lương (F) Bắt buộc Nằm trên Đường Găng?

> [!IMPORTANT]
> **Giải thích Tính Chất Trọng Yếu của Đường Găng:**
> 1. **Quan hệ Ràng buộc Nghiệp vụ Cốt lõi (Business Dependency):** Trong quy trình quản trị nhân sự, tiền lương không thể được tính toán chính xác nếu không có dữ liệu đối soát công thực tế (ngày công chuẩn, giờ làm thêm OT, ngày nghỉ phép không lương). Mối quan hệ giữa Module Chấm công (E) và Module Tính lương (F) là mối quan hệ cứng **Finish-to-Start (FS)**. Phân hệ Tính lương chỉ có thể bắt đầu lập trình và kiểm thử logic nghiệp vụ khi các API và cấu trúc dữ liệu của Phân hệ Chấm công đã hoàn tất.
> 2. **Độ phức tạp Kỹ thuật Cao nhất:**
>    - Module Chấm công (E) đòi hỏi tích hợp phần cứng máy quét vân tay ZKTeco thông qua kết nối Socket/Webhook, tiềm ẩn rủi ro về độ ổn định kết nối mạng nội bộ.
>    - Module Tính lương (F) là động cơ tính toán phức tạp nhất, chứa đựng hàng chục quy tắc pháp lý về thuế TNCN lũy tiến 7 bậc và trần đóng bảo hiểm xã hội.
> 3. **Hậu quả của việc Chậm trễ:**
>    Bất kỳ sự chậm trễ nào dù chỉ **01 ngày** tại hoạt động E hoặc F đều sẽ trực tiếp đẩy lùi thời điểm bắt đầu của Kiểm thử Tích hợp (J), kiểm thử UAT (K) và ngày go-live toàn công ty (M), do độ trễ tổng thể của chúng bằng $0$ ($TF = 0$).

---

### 4.3. Xác suất Hoàn thành Dự án Theo Phương pháp Thống kê PERT
Nhóm nghiên cứu đánh giá độ biến động của đường găng thông qua tổng phương sai các hoạt động găng:
$$\sigma_{\text{Project}}^2 = \sum \sigma_{\text{Critical}}^2 = \sigma_A^2 + \sigma_B^2 + \sigma_E^2 + \sigma_F^2 + \sigma_J^2 + \sigma_K^2 + \sigma_L^2 + \sigma_M^2$$
$$\sigma_{\text{Project}}^2 = 4,00 + 2,25 + 4,00 + 7,11 + 2,78 + 0,69 + 1,36 + 0,44 = \mathbf{22,63}$$
$$\Rightarrow \sigma_{\text{Project}} = \sqrt{22,63} = \mathbf{4,76 \text{ ngày}}$$

Nếu Ban Giám đốc yêu cầu hoàn thành dự án trong thời hạn cam kết $T_d = 90$ ngày làm việc:
$$Z = \frac{T_d - T_e}{\sigma_{\text{Project}}} = \frac{90 - 84,51}{4,76} = \frac{5,49}{4,76} \approx \mathbf{+1,15}$$
Tra bảng phân phối chuẩn $N(0, 1)$: $P(Z \le 1,15) \approx \mathbf{87,49\%}$.
* **Kết luận:** Dự án có xác suất đạt tới **87,49%** sẽ hoàn thành đúng hoặc trước thời hạn cam kết mà không bị trễ hạn.

---

## 5. SƠ ĐỒ MẠNG LỊCH TRÌNH VÀ BIỂU ĐỒ GANTT (GANTT CHART)

### 5.1. Sơ đồ Mạng Lịch trình PDM (Network Diagram Flow)

```
        ┌────────────────────────────────────────────────────────┐
        │ [C] UI/UX Design (7.5d) [TF=1d]                        │
        └───────────────────────────┬────────────────────────────┘
                                    ▼
┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ [A] Khảo sát │     │ [B] Thiết kế │     │ [E] Dev Chấm │     │ [F] Dev Tính │     │ [J] Kiểm thử │
│ & SRS (12.7d)├────►│ K.Trúc (8.5d)├────►│ công (14.7d) ├────►│ lương (18.7d)├────►│ T.Hợp (12.3d)│
└──────────────┘     └──────┬───────┘     └──────────────┘     └──────────────┘     └──────┬───────┘
  [CRITICAL]           [CRITICAL]           [CRITICAL]           [CRITICAL]                │
                            │                                                              │
                            ▼                                                              │
        ┌────────────────────────────────────────────────────────┐                         │
        │ [D] Dev Hồ sơ (10.5d) [TF=18d] ──► [G] Dev T.Dụng (8.3)│                         │
        │                            └─────► [H] Dev KPI (10.7d) ├─────────────────────────┤
        └────────────────────────────────────────────────────────┘                         ▼
                                                                                    ┌──────────────┐
                                                                                    │ [K] Nghiệm   │
                                                                                    │ thu UAT(7.2d)│
                                                                                    └──────┬───────┘
                                                                                           ▼
                                                                                    ┌──────────────┐
                                                                                    │ [L] Di chuyển│
                                                                                    │ DL & Prod(5d)│
                                                                                    └──────┬───────┘
                                                                                           ▼
                                                                                    ┌──────────────┐
                                                                                    │ [M] Đào tạo  │
                                                                                    │ & Go-live(5d)│
                                                                                    └──────────────┘
                                                                                      [CRITICAL]
```

### 5.2. Biểu đồ Tiến độ Tổng thể (Gantt Chart 24 Tuần)

```
Hoạt động Dự án     T1 T2 T3 T4 T5 T6 T7 T8 T9 T10 T11 T12 T13 T14 T15 T16 T17 T18 T19 T20 T21 T22 T23 T24
────────────────────────────────────────────────────────────────────────────────────────────────────────
[A] Khảo sát & SRS  ███ ███
[B] Kiến trúc & DB          ███ ██
[C] UI/UX Mockup            ███ ░
[D] Dev Hồ sơ NS                   ███ ███ ░░░ ░░░
[E] Dev Chấm công                  ███ ███ ███
[F] Dev Tính lương                             ███ ███ ███ ███
[G] Dev Tuyển dụng                      ███ ██ ░░░ ░░░ ░░░ ░░░
[H] Dev KPI                                    ███ ███ ░░
[I] Dev Dashboard                                      ███ ███ ░░░
[J] Kiểm thử T.Hợp                                             ███ ███
[K] Nghiệm thu UAT                                                     ███ ██
[L] Di chuyển DL                                                              ███
[M] Đào tạo & Go-Live                                                             ███
────────────────────────────────────────────────────────────────────────────────────────────────────────
Ghi chú:  ███ = Hoạt động trên Đường Găng (Critical)    ░░░ = Thời gian dự trữ (Float)
```
