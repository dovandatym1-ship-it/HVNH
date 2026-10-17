# QUẢN LÝ GIÁ TRỊ THU ĐƯỢC (EARNED VALUE MANAGEMENT - EVM) TẠI HAI THỜI ĐIỂM BÁO CÁO
## Dự án: Xây dựng Hệ thống Quản trị Nhân sự Nội bộ (ABC-HRM)
### Mã tài liệu: BTL-QLDA-C2 | Giai đoạn: Thực hiện & Giám sát (Execution & M&C)
### Tiêu chuẩn áp dụng: PMI PMBOK Guide / ANSI/EIA-748 EVMS Standard | Học phần: QLDA CNTT Nâng cao (HVNH)

---

## 1. KHUNG TIẾP CẬN BẢN CHẤT: LÀM GÌ? TẠI SAO LÀM? LÀM THẾ NÀO?

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                   MÔ HÌNH QUẢN LÝ GIÁ TRỊ THU ĐƯỢC (EVM) TRONG DỰ ÁN ABC-HRM                     │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 1. TẠI SAO LÀM? (WHY)                                                                           │
│    • Nếu chỉ so sánh giữa Chi phí Thực tế (AC) và Ngân sách Kế hoạch (PV), nhà quản lý không thể │
│      biết được số tiền đã chi ra đã tạo ra được bao nhiêu giá trị thực tế của công việc.        │
│    • Phương pháp Quản lý Giá trị Thu được (EVM) là công cụ khoa học tích hợp đồng thời 3 yếu tố:│
│      Phạm vi (Scope), Tiến độ (Schedule) và Chi phí (Cost) trên cùng một thước đo tiền tệ, giúp  │
│      phát hiện sớm sai lệch và dự báo chính xác kết cục của dự án trước khi quá muộn.           │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 2. LÀM GÌ? (WHAT)                                                                                │
│    • Thu thập Dữ liệu Hiệu suất Công việc (Work Performance Data) và phân tích các chỉ số EVM   │
│      tại đúng 02 thời điểm báo cáo quy định trong đề bài:                                       │
│      - Mốc Báo cáo 1 (Ngày 15/10 - Tuần 14/24): Giai đoạn phát hiện nguy cơ chậm trễ.           │
│      - Mốc Báo cáo 2 (Ngày 20/10 - Tuần 18/24): Giai đoạn đánh giá sự phục hồi sau can thiệp.   │
│    • Tính toán đầy đủ 10 chỉ số cốt lõi: PV, EV, AC, CV, SV, CPI, SPI, EAC, ETC, TCPI.          │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 3. LÀM THẾ NÀO? (HOW)                                                                           │
│    • Áp dụng hệ thống công thức toán học chuẩn quốc tế của Viện Quản lý Dự án (PMI).             │
│    • Thực hiện Phân tích Nguyên nhân Sâu xa (Root Cause Analysis) khi chỉ số bị suy giảm.        │
│    • Ban hành Kế hoạch Hành động Điều chỉnh (Corrective Action Plan) nén tiến độ (Fast-Tracking)│
│      và theo dõi sự phục hồi của các chỉ số hiệu suất tới mốc báo cáo tiếp theo.                │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. HỆ THỐNG CÔNG THỨC TOÁN HỌC CHUẨN CỦA PHƯƠNG PHÁP EVM

| Chỉ số EVM | Tên gọi Tiếng Việt | Công thức Tính toán | Ý nghĩa & Tiêu chuẩn Đánh giá |
|:---:|---|:---:|---|
| **BAC** | Ngân sách Khi Hoàn thành | Phê duyệt trong Baseline | Tổng ngân sách dự kiến của dự án (sau điều chỉnh CR-001 = **822.000.000 VNĐ**). |
| **PV** | Giá trị Kế hoạch (Planned Value) | $PV = \% \text{ Kế hoạch} \times BAC$ | Khối lượng giá trị công việc đáng lẽ phải hoàn thành theo kế hoạch. |
| **EV** | Giá trị Thu được (Earned Value) | $EV = \% \text{ Thực tế} \times BAC$ | Khối lượng giá trị công việc thực sự đã hoàn thành và được nghiệm thu. |
| **AC** | Chi phí Thực tế (Actual Cost) | Ghi nhận sổ kế toán thực tế | Tổng số tiền đã thực sự chi tiêu để hoàn thành khối lượng công việc EV. |
| **CV** | Phương sai Chi phí (Cost Variance) | $CV = EV - AC$ | $CV > 0$: Tiết kiệm ngân sách; $CV < 0$: Vượt chi ngân sách (Báo động). |
| **SV** | Phương sai Tiến độ (Schedule Variance) | $SV = EV - PV$ | $SV > 0$: Vượt tiến độ; $SV < 0$: Chậm tiến độ so với kế hoạch (Báo động). |
| **CPI** | Chỉ số Hiệu suất Chi phí | $CPI = \frac{EV}{AC}$ | $CPI > 1,0$: Tốt; $CPI < 1,0$: Lãng phí (1 đồng chi ra chỉ tạo $< 1$ đồng giá trị). |
| **SPI** | Chỉ số Hiệu suất Lịch trình | $SPI = \frac{EV}{PV}$ | $SPI > 1,0$: Nhanh hơn kế hoạch; $SPI < 1,0$: Chậm hơn kế hoạch. |
| **EAC** | Ước tính Chi phí Khi Hoàn thành | $EAC = \frac{BAC}{CPI}$ | Dự báo tổng chi phí cuối cùng nếu tiếp tục giữ nguyên hiệu suất chi phí hiện tại. |
| **ETC** | Ước tính Chi phí Để Hoàn tất | $ETC = EAC - AC$ | Dự toán số tiền còn phải chi thêm để hoàn thành nốt khối lượng công việc còn lại. |
| **TCPI** | Chỉ số Hiệu suất Cần đạt | $TCPI = \frac{BAC - EV}{BAC - AC}$ | Hiệu suất chi phí tối thiểu mà đội ngũ phải đạt được từ nay tới cuối dự án để không vỡ BAC. |

---

## 3. PHÂN TÍCH CHI TIẾT THỜI ĐIỂM BÁO CÁO 1 (NGÀY 15/10 — TUẦN 14/24)

### 3.1. Dữ liệu Hiệu suất Thu thập Thực tế (Performance Data)
* **Thời điểm báo cáo:** Ngày 15/10 (tương đương kết thúc Tuần 14 trong chu kỳ 24 tuần của dự án).
* **Tiến độ kế hoạch mục tiêu:** Đáng lẽ phải hoàn thành **$58,0\%$** khối lượng dự án.
* **Tiến độ hoàn thành thực tế:** Đội ngũ mới chỉ nghiệm thu được **$55,0\%$** khối lượng công việc.
* **Tổng chi phí giải ngân thực tế ghi nhận:** **$470.000.000$ VNĐ**.
* **Đường cơ sở ngân sách áp dụng:** $BAC = 822.000.000$ VNĐ (sau phê duyệt CR-001).

### 3.2. Bảng Tính toán Các Chỉ số EVM Mốc 15/10

| STT | Chỉ số Đo lường | Phép tính Toán học | Giá trị Tính toán | Đánh giá & Diễn giải Ý nghĩa |
|:---:|---|---|---:|---|
| 1 | **Planned Value (PV)** | $58,0\% \times 822.000.000$ | **476.760.000 VNĐ** | Mục tiêu công việc cần đạt theo kế hoạch. |
| 2 | **Earned Value (EV)** | $55,0\% \times 822.000.000$ | **452.100.000 VNĐ** | Giá trị công việc thực sự đã tạo ra được. |
| 3 | **Actual Cost (AC)** | Kế toán dự án xác nhận | **470.000.000 VNĐ** | Tổng số tiền đã thực tế chi ra. |
| 4 | **Cost Variance (CV)** | $EV - AC = 452.100.000 - 470.000.000$ | **−17.900.000 VNĐ** | ⚠️ **VƯỢT CHI 17,9 triệu VNĐ** (Chi phí vượt giá trị tạo ra). |
| 5 | **Schedule Variance (SV)**| $EV - PV = 452.100.000 - 476.760.000$ | **−24.660.000 VNĐ** | ⚠️ **CHẬM TIẾN ĐỘ 24,66 triệu VNĐ** (Tương đương trễ ~1 tuần công). |
| 6 | **Cost Performance Index (CPI)** | $CPI = \frac{452.100.000}{470.000.000}$ | **0,962** | ⚠️ **DƯỚI CHUẨN:** Mỗi 1 đồng bỏ ra chỉ thu lại được 0,962 đồng giá trị. |
| 7 | **Schedule Performance Index (SPI)**| $SPI = \frac{452.100.000}{476.760.000}$ | **0,948** | ⚠️ **CHẬM TIẾN ĐỘ:** Tốc độ thực tế chỉ đạt 94,8% so với tốc độ kế hoạch. |
| 8 | **Estimate at Completion (EAC)** | $EAC = \frac{822.000.000}{0,962}$ | **854.469.854 VNĐ** | ⚠️ **CẢNH BÁO:** Dự báo chi phí cuối cùng sẽ vượt ngân sách 32,5 triệu! |
| 9 | **Estimate to Complete (ETC)** | $EAC - AC = 854.469.854 - 470.000.000$ | **384.469.854 VNĐ** | Cần thêm khoảng 384,5 triệu để hoàn tất dự án. |
| 10| **To-Complete Performance Index (TCPI)**| $\frac{822.000.000 - 452.100.000}{822.000.000 - 470.000.000} = \frac{369.900.000}{352.000.000}$ | **1,051** | Đội ngũ bắt buộc phải tăng năng suất lên **105,1%** để giữ vững BAC. |

### 3.3. Phân tích Nguyên nhân Sâu xa (Root Cause Analysis)
Qua rà soát kỹ thuật nội bộ, PM xác định nguyên nhân chính dẫn tới sự sụt giảm hiệu suất:
1. **Rủi ro R3 trở thành hiện thực:** Phân hệ Chấm công (WBS 1.4.2) gặp sự cố mất kết nối Socket định kỳ với máy quét vân tay ZKTeco do tài liệu SDK cung cấp bởi bên thứ ba bị thiếu các đặc tả về cơ chế giữ kết nối (Keep-Alive Header).
2. Senior Dev và Dev 1 đã mất 05 ngày công ngoài kế hoạch để đảo ngược mã nguồn (Reverse-engineer) giao thức kết nối và viết lại module Adapter, phát sinh thêm chi phí nhân công và làm chậm tiến độ tích hợp.

### 3.4. Kế hoạch Hành động Điều chỉnh (Corrective Action Plan Mốc 15/10)
Để kéo các chỉ số $CPI$ và $SPI$ quay về ngưỡng an toàn $\approx 1,0$, Quản lý Dự án (PM) ban hành ngay 3 quyết định can thiệp khẩn cấp:
1. **Áp dụng Kỹ thuật Nén Tiến độ Bằng Cách Làm Song Song (Fast-Tracking):** Cho phép triển khai lập trình trước khung giao diện Frontend của phân hệ Tuyển dụng và KPI (vốn không nằm trên đường găng) trong khi Senior Dev hoàn tất kiểm thử phân hệ Chấm công.
2. **Tăng cường Nguồn lực Chuyên gia:** Kích hoạt 15 triệu VNĐ từ Quỹ Dự trữ Dự phòng (Contingency Reserve) để thuê chuyên gia kỹ thuật của ZKTeco hỗ trợ tối ưu hóa thư viện kết nối trong 02 ngày cuối tuần, dứt điểm hoàn toàn lỗi socket.
3. **Thực hiện Lập trình Cặp (Pair-Programming):** Senior Dev kết hợp chặt chẽ với Dev 1 để tăng tốc độ kiểm thử phân hệ Tính lương (WBS 1.4.3), cam kết bù lại tiến độ trong vòng 4 tuần tiếp theo.

---

## 4. PHÂN TÍCH CHI TIẾT THỜI ĐIỂM BÁO CÁO 2 (NGÀY 20/10 — TUẦN 18/24)

### 4.1. Dữ liệu Hiệu suất Thu thập Thực tế (Performance Data)
* **Thời điểm báo cáo:** Ngày 20/10 (tương đương kết thúc Tuần 18 trong chu kỳ 24 tuần của dự án).
* **Tiến độ kế hoạch mục tiêu:** Kế hoạch yêu cầu hoàn thành **$75,0\%$** khối lượng dự án.
* **Tiến độ hoàn thành thực tế:** Đội ngũ đã nỗ lực hoàn thành xuất sắc **$74,0\%$** khối lượng công việc.
* **Tổng chi phí giải ngân thực tế ghi nhận:** **$612.000.000$ VNĐ**.
* **Đường cơ sở ngân sách áp dụng:** $BAC = 822.000.000$ VNĐ.

### 4.2. Bảng Tính toán Các Chỉ số EVM Mốc 20/10

| STT | Chỉ số Đo lường | Phép tính Toán học | Giá trị Tính toán | Đánh giá & Diễn giải Ý nghĩa |
|:---:|---|---|---:|---|
| 1 | **Planned Value (PV)** | $75,0\% \times 822.000.000$ | **616.500.000 VNĐ** | Mục tiêu công việc kế hoạch Tuần 18. |
| 2 | **Earned Value (EV)** | $74,0\% \times 822.000.000$ | **608.280.000 VNĐ** | Khối lượng giá trị công việc thực sự hoàn thành. |
| 3 | **Actual Cost (AC)** | Kế toán dự án xác nhận | **612.000.000 VNĐ** | Chi phí thực tế đã giải ngân. |
| 4 | **Cost Variance (CV)** | $EV - AC = 608.280.000 - 612.000.000$ | **−3.720.000 VNĐ** | ✅ **PHỤC HỒI MẠNH:** Mức vượt chi giảm tới 79% (từ -17,9 tr còn -3,7 tr). |
| 5 | **Schedule Variance (SV)**| $EV - PV = 608.280.000 - 616.500.000$ | **−8.220.000 VNĐ** | ✅ **PHỤC HỒI TIẾN ĐỘ:** Khoảng cách trễ giảm 67% (từ -24,66 tr còn -8,22 tr). |
| 6 | **Cost Performance Index (CPI)** | $CPI = \frac{608.280.000}{612.000.000}$ | **0,994** | ✅ **TIỆM CẬN 1,0:** Hiệu suất sử dụng chi phí phục hồi gần như hoàn hảo. |
| 7 | **Schedule Performance Index (SPI)**| $SPI = \frac{608.280.000}{616.500.000}$ | **0,987** | ✅ **TIỆM CẬN 1,0:** Tiến độ thực tế đạt 98,7% so với kế hoạch (gần như bắt kịp). |
| 8 | **Estimate at Completion (EAC)** | $EAC = \frac{822.000.000}{0,994}$ | **826.961.770 VNĐ** | ✅ **AN TOÀN NGÂN SÁCH:** Dự báo chi phí hoàn thành nằm an toàn trong trần BAC! |
| 9 | **Estimate to Complete (ETC)** | $EAC - AC = 826.961.770 - 612.000.000$ | **214.961.770 VNĐ** | Chỉ cần thêm khoảng 215 triệu VNĐ để hoàn thành dự án. |
| 10| **To-Complete Performance Index (TCPI)**| $\frac{822.000.000 - 608.280.000}{822.000.000 - 612.000.000} = \frac{213.720.000}{210.000.000}$ | **1,018** | Áp lực hiệu suất giảm mạnh: Đội ngũ chỉ cần duy trì hiệu suất 101,8%. |

---

## 5. ĐỐI CHIẾU SO SÁNH HAI THỜI ĐIỂM VÀ DỰ BÁO KẾT CỤC DỰ ÁN

### 5.1. Bảng Tổng Hợp Đối Chiếu Xu Hướng Biến Động EVM

| Đại lượng EVM | Mốc 15/10 (Tuần 14) | Mốc 20/10 (Tuần 18) | Mức độ Biến động | Đánh giá Xu hướng Hiệu suất |
|---|:---:|:---:|:---:|---|
| **Kế hoạch hoàn thành** | 58,0% | 75,0% | +17,0% | Tiến trình dự án bước vào giai đoạn tăng tốc |
| **Thực tế hoàn thành** | 55,0% | 74,0% | +19,0% | Tốc độ hoàn thành thực tế vượt tốc độ kế hoạch |
| **Phương sai Chi phí ($CV$)** | −17,90 triệu VNĐ | −3,72 triệu VNĐ | **+14,18 triệu VNĐ** | ✅ Cắt giảm 79,2% tình trạng bội chi |
| **Phương sai Lịch trình ($SV$)** | −24,66 triệu VNĐ | −8,22 triệu VNĐ | **+16,44 triệu VNĐ** | ✅ Bù đắp được 66,7% độ trễ tiến độ |
| **Chỉ số Hiệu suất Chi phí ($CPI$)** | **0,962** | **0,994** | **+0,032** | ✅ Phục hồi tiệm cận mốc chuẩn 1,0 |
| **Chỉ số Hiệu suất Tiến độ ($SPI$)** | **0,948** | **0,987** | **+0,039** | ✅ Phục hồi ngoạn mục lên 98,7% kế hoạch |
| **Dự báo Chi phí Cuối ($EAC$)** | 854,47 triệu VNĐ | 826,96 triệu VNĐ | **−27,51 triệu VNĐ** | ✅ Giảm dự toán, bảo toàn ngân sách dự án |
| **Hệ số Hiệu suất Cần đạt ($TCPI$)** | 1,051 | 1,018 | **−0,033** | ✅ Áp lực hoàn thành giảm mạnh |

### 5.2. Biểu Đồ Xu Hướng Hiệu Suất CPI và SPI (Performance Trend Chart)

```
Chỉ số Hiệu suất (Index)
 1.05 ┼                                                         • TCPI = 1.018
 1.00 ┼─────────────────────────────────────────────────────────┼── Ngưỡng Chuẩn = 1.000
      │                                                   •'    │
 0.99 ┼                                              •' CPI=0.994 (Phục hồi 99.4%)
      │                                         •' SPI=0.987 (Phục hồi 98.7%)
 0.96 ┼───────• CPI = 0.962 (Mốc 15/10)
      │
 0.95 ┼──• SPI = 0.948 (Mốc 15/10)
      │
 0.90 ┼───────┴──────────────────────────────────────────┴──────► Thời gian
           Mốc 1: 15/10 (Tuần 14)                  Mốc 2: 20/10 (Tuần 18)
```

---

## 6. KẾT LUẬN VÀ DỰ BÁO KẾT QUẢ DỰ ÁN

1. **Hiệu quả của Hành động Can thiệp:** Việc theo dõi sát sao dữ liệu EVM tại mốc 15/10 đã giúp Ban Quản lý Dự án phát hiện ngay sự cố kỹ thuật về máy chấm công trước khi nó trở thành thảm họa làm vỡ tiến độ. Các quyết định can thiệp (thuê chuyên gia dứt điểm lỗi SDK, áp dụng Fast-Tracking) đã phát huy hiệu quả tối ưu, đưa cả $CPI$ (0,994) và $SPI$ (0,987) quay trở lại quỹ đạo kiểm soát tại mốc 20/10.
2. **Dự báo Kết cục Dự án:**
   - **Về Chi phí:** Với chỉ số $EAC \approx 826,96$ triệu VNĐ, dự án được dự báo sẽ hoàn thành với chi phí thực tế thấp hơn Ngân sách được duyệt ($BAC = 850$ triệu VNĐ), tiết kiệm cho doanh nghiệp khoảng **23,04 triệu VNĐ** (tương đương tiết kiệm 2,7% tổng mức đầu tư).
   - **Về Tiến độ:** Với $SPI = 0,987$ và khối lượng công việc còn lại chủ yếu là kiểm thử UAT và đào tạo, dự án tự tin sẽ hoàn thành toàn bộ công tác bàn giao và Go-Live thành công đúng vào ngày cam kết **30/04/2026**.
