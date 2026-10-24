# BÁO CÁO TÌNH TRẠNG ĐÈN GIAO THÔNG (TRAFFIC LIGHT STATUS REPORT) & SỔ THEO DÕI VẤN ĐỀ (ISSUE LOG)
## Dự án: Xây dựng Hệ thống Quản trị Nhân sự Nội bộ (ABC-HRM)
### Mã tài liệu: BTL-QLDA-C3 | Giai đoạn: Thực hiện & Giám sát (Execution & M&C)
### Tiêu chuẩn áp dụng: PMI PMBOK Guide / Project Communications Governance | Học phần: QLDA CNTT Nâng cao (HVNH)

---

## 1. KHUNG TIẾP CẬN BẢN CHẤT: LÀM GÌ? TẠI SAO LÀM? LÀM THẾ NÀO?

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                   MÔ HÌNH BÁO CÁO TRUYỀN THÔNG VÀ THEO DÕI VẤN ĐỀ DỰ ÁN                          │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 1. TẠI SAO LÀM? (WHY)                                                                           │
│    • Ban Giám đốc và các bên liên quan cấp cao không có thời gian đọc các tài liệu kỹ thuật      │
│      dài hàng chục trang. Họ cần một công cụ trực quan, cô đọng để nắm bắt ngay "sức khỏe"      │
│      của dự án trong vòng 60 giây.                                                               │
│    • Hệ thống Đèn Giao Thông (Traffic Light: Xanh - Vàng - Đỏ) giúp chuẩn hóa truyền thông,     │
│      loại bỏ yếu tố thiên kiến chủ quan và kích hoạt kịp thời các quyết định hỗ trợ từ lãnh đạo. │
│    • Song song đó, Sổ theo dõi Vấn đề (Issue Log) ghi chép minh bạch các rủi ro đã trở thành   │
│      hiện thực, xác định người chịu trách nhiệm và thời hạn xử lý dứt điểm.                     │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 2. LÀM GÌ? (WHAT)                                                                                │
│    • Xây dựng 02 Báo cáo Tình trạng Dự án định kỳ (Status Reports) tại 2 mốc 15/10 và 20/10.    │
│    • Đánh giá tình trạng 4 lĩnh vực trọng yếu: Phạm vi, Thời gian, Chi phí, Chất lượng/Kỹ thuật.│
│    • Lập Sổ theo dõi Vấn đề (Issue Log) ghi nhận chi tiết 03 vấn đề kỹ thuật và vận hành thực tế.│
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 3. LÀM THẾ NÀO? (HOW)                                                                           │
│    • Áp dụng quy tắc ngưỡng định lượng: Xanh (Đạt $\ge 98\%$), Vàng (Sai lệch $5\% - 10\%$),    │
│      Đỏ (Sai lệch $> 10\%$, đe dọa đường găng và ngân sách).                                     │
│    • Ghi chép chi tiết nguyên nhân, giải pháp, người phụ trách và ngày đóng cho từng Issue.     │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. QUY CHUẨN ĐỊNH LƯỢNG HỆ THỐNG ĐÈN GIAO THÔNG (TRAFFIC LIGHT THRESHOLDS)

| Trạng thái | Ký hiệu | Tiêu chuẩn Đánh giá Phạm vi (Scope) | Tiêu chuẩn Tiến độ (Schedule - $SPI$) | Tiêu chuẩn Chi phí (Cost - $CPI$) | Mức độ Hành động Yêu cầu |
|:---:|:---:|---|---|---|---|
| **XANH (Green)** | 🟢 | Hoàn toàn nằm trong Baseline; không có tranh chấp phạm vi. | $SPI \ge 0,98$ (Sai lệch tiến độ $< 2\%$). | $CPI \ge 0,98$ (Chi phí trong hạn mức an toàn). | Tiếp tục vận hành bình thường theo kế hoạch. |
| **VÀNG (Amber)** | 🟡 | Xuất hiện yêu cầu thay đổi mới đang chờ thẩm định CCB. | $0,90 \le SPI < 0,98$ (Chậm từ $2\% - 10\%$). | $0,90 \le CPI < 0,98$ (Vượt chi nhẹ trong hạn mức). | Cần hành động điều chỉnh và giám sát hàng tuần. |
| **ĐỎ (Red)** | 🔴 | Phạm vi bị vỡ nghiêm trọng (Uncontrolled Scope Creep). | $SPI < 0,90$ (Chậm $> 10\%$, đe dọa đường găng). | $CPI < 0,90$ (Vượt chi nghiêm trọng, nguy cơ vỡ BAC). | Báo cáo khẩn cấp Sponsor, triệu tập CCB can thiệp. |

---

## 3. BÁO CÁO TÌNH TRẠNG DỰ ÁN TẠI HAI THỜI ĐIỂM (EXECUTIVE STATUS REPORTS)

### 3.1. Báo cáo Tình trạng số 01 — Thời điểm 15/10 (Tuần 14/24)

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                           BÁO CÁO TÌNH TRẠNG DỰ ÁN ĐỊNH KỲ (MỐC 15/10)                           │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ • Dự án: Quản trị Nhân sự ABC-HRM               • Người lập báo cáo: Quản lý Dự án (PM)          │
│ • Kỳ báo cáo: Tuần 14 (Hoàn thành 55% thực tế)  • Người nhận: Tổng Giám đốc (Sponsor) & HR Head  │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 1. TỔNG QUAN TÌNH TRẠNG SỨC KHỎE DỰ ÁN (TRAFFIC LIGHT SUMMARY):                                  │
│                                                                                                  │
│    [ PHẠM VI (SCOPE) ]     [ TIẾN ĐỘ (SCHEDULE) ]    [ CHI PHÍ (COST) ]    [ CHẤT LƯỢNG / KỸ THUẬT]
│         🟢 XANH                  🟡 VÀNG                  🟡 VÀNG                  🟡 VÀNG        │
│                                                                                                  │
│    • Phạm vi (Scope - 🟢 Xanh): Các phân hệ phát triển đúng theo tài liệu SRS; yêu cầu CR-001    │
│      đang được rà soát nội bộ, không có lạm phát phạm vi ngoài tầm kiểm soát.                    │
│    • Tiến độ (Schedule - 🟡 Vàng): Chỉ số SPI = 0,948 (< 0,98). Dự án đang bị chậm khoảng 5,2%   │
│      (tương đương chậm 1 tuần công) do sự cố tích hợp SDK máy chấm công vân tay ZKTeco.          │
│    • Chi phí (Cost - 🟡 Vàng): Chỉ số CPI = 0,962 (< 0,98). Phương sai chi phí CV = -17,9 tr.    │
│      Đang bị bội chi cục bộ do phát sinh thêm ngày công nghiên cứu sửa lỗi kết nối máy chấm công. │
│    • Chất lượng (Technical - 🟡 Vàng): Gặp trở ngại kỹ thuật về mất gói tin Socket máy chấm công.│
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 2. KẾT QUẢ ĐÃ ĐẠT ĐƯỢC TRONG KỲ:                                                                 │
│    • Hoàn thành lập trình 100% Backend & Frontend Phân hệ Quản lý Hồ sơ Nhân sự (WBS 1.4.1).     │
│    • Hoàn thành giao diện nộp đơn xin nghỉ phép và quy trình duyệt trực tuyến (WBS 1.4.2).       │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 3. CÁC HÀNH ĐỘNG KHẮC PHỤC TRỌNG TÂM TRONG KỲ TIẾP THEO:                                        │
│    1. Kích hoạt 15 triệu VNĐ từ Quỹ Dự phòng để thuê chuyên gia ZKTeco hỗ trợ kỹ thuật dứt điểm.│
│    2. Áp dụng kỹ thuật Fast-tracking (lập trình song song giao diện Tuyển dụng và KPI).          │
│    3. Đẩy mạnh kiểm thử cặp (Pair-testing) để kéo chỉ số SPI và CPI trở lại ngưỡng Xanh.         │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

### 3.2. Báo cáo Tình trạng số 02 — Thời điểm 20/10 (Tuần 18/24)

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                           BÁO CÁO TÌNH TRẠNG DỰ ÁN ĐỊNH KỲ (MỐC 20/10)                           │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ • Dự án: Quản trị Nhân sự ABC-HRM               • Người lập báo cáo: Quản lý Dự án (PM)          │
│ • Kỳ báo cáo: Tuần 18 (Hoàn thành 74% thực tế)  • Người nhận: Tổng Giám đốc (Sponsor) & HR Head  │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 1. TỔNG QUAN TÌNH TRẠNG SỨC KHỎE DỰ ÁN (TRAFFIC LIGHT SUMMARY):                                  │
│                                                                                                  │
│    [ PHẠM VI (SCOPE) ]     [ TIẾN ĐỘ (SCHEDULE) ]    [ CHI PHÍ (COST) ]    [ CHẤT LƯỢNG / KỸ THUẬT]
│         🟢 XANH                  🟢 XANH                  🟢 XANH                  🟢 XANH        │
│                                                                                                  │
│    • Phạm vi (Scope - 🟢 Xanh): Rất ổn định. Yêu cầu CR-001 đã lập trình xong; yêu cầu CR-002 đã │
│      được Hội đồng CCB bác bỏ dứt khoát đưa sang Phase 2, bảo vệ toàn vẹn phạm vi dự án.        │
│    • Tiến độ (Schedule - 🟢 Xanh): Chỉ số SPI = 0,987 (tiệm cận 1,0). Tốc độ hoàn thành công     │
│      việc thực tế đã bắt kịp tiến độ kế hoạch; nguy cơ trễ hạn go-live đã hoàn toàn bị triệt tiêu.│
│    • Chi phí (Cost - 🟢 Xanh): Chỉ số CPI = 0,994 (gần như đạt mức hoàn hảo 1,0). Mức vượt chi   │
│      thu hẹp từ -17,9 tr xuống chỉ còn -3,72 tr. Dự báo EAC = 826,96 triệu VNĐ < Ngân sách BAC.   │
│    • Chất lượng (Technical - 🟢 Xanh): Đã khắc phục 100% sự cố kết nối máy chấm công; module     │
│      Tính lương đã hoàn thành Unit Test với tỷ lệ bao phủ mã nguồn đạt 87,5%.                    │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 2. KẾT QUẢ ĐÃ ĐẠT ĐƯỢC TRONG KỲ:                                                                 │
│    • Hoàn thành toàn diện 6/6 phân hệ chức năng phần mềm cốt lõi (WBS 1.4.1 đến 1.4.6).          │
│    • Đóng gói thành công tính năng cảnh báo hợp đồng hết hạn trước 30 ngày (CR-001).             │
│    • Làm sạch thành công dữ liệu từ 15 file Excel cũ, chuẩn bị sẵn sàng cho khâu nạp CSDL.       │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 3. KẾ HOẠCH TRỌNG TÂM GIAI ĐOẠN TIẾP THEO:                                                      │
│    1. Triển khai đợt Kiểm thử Nghiệm thu Người dùng (UAT) với phòng HR từ ngày 25/10 đến 05/11. │
│    2. Tổ chức 02 buổi đào tạo người dùng và chuẩn bị hạ tầng Cloud Production cho ngày Go-Live.  │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 4. SỔ THEO DÕI VẤN ĐỀ PHÁT SINH THỰC TẾ (ISSUE LOG)

Sổ theo dõi Vấn đề ghi nhận các vấn đề (Issues) đã phát sinh trong quá trình triển khai, trạng thái giải quyết và người chịu trách nhiệm:

| Mã Issue | Ngày ghi nhận | Phân loại | Mô tả Chi tiết Vấn đề Phát sinh | Mức độ Nghiêm trọng | Người chịu TN Xử lý | Biện pháp Khắc phục Đã Thực hiện (Làm thế nào?) | Ngày Đóng | Trạng thái |
|:---:|:---:|:---:|---|:---:|:---:|---|:---:|:---:|
| **ISS-001** | 08/01/2026 | **Kỹ thuật** | Dịch vụ Adapter chấm công bị mất kết nối Socket định kỳ với máy ZKTeco sau mỗi 6 tiếng hoạt động, làm đứt đoạn luồng log chấm công. | **Cao (High)** | **Senior Dev** | • Thuê chuyên gia ZKTeco phối hợp phân tích gói tin mạng.<br/>• Bổ sung cơ chế Heartbeat gửi gói tin ping mỗi 30 giây để duy trì kết nối.<br/>• Cài đặt cơ chế tự động kết nối lại (Auto-reconnect) khi rớt mạng. | 18/01/2026 | ✅ **CLOSED** |
| **ISS-002** | 20/01/2026 | **Dữ liệu** | Quá trình chạy thử nghiệm script ETL phát hiện 12 bản ghi nhân viên trong file Excel cũ bị trùng số CCCD và không có mã số thuế cá nhân. | **Vừa (Medium)** | **BA & Dev 1** | • Trích xuất danh sách 12 nhân viên gửi trực tiếp cho Trưởng phòng HR.<br/>• HR liên hệ các nhân sự liên quan để thu thập bổ sung CCCD chuẩn.<br/>• Chuẩn hóa mã nhân viên thống nhất dạng `ABC-XXXX` trước khi nạp DB. | 23/01/2026 | ✅ **CLOSED** |
| **ISS-003** | 15/02/2026 | **Nghiệp vụ** | Động cơ tính lương tính sai mức giảm trừ gia cảnh cho 03 nhân sự có con sinh trong năm (chỉ được giảm trừ từ tháng sinh thực tế). | **Cao (High)** | **Senior Dev** | • Bổ sung trường dữ liệu `start_date` và `end_date` vào bảng người phụ thuộc `dependents`.<br/>• Viết lại thuật toán tính thuế TNCN tính giảm trừ theo số tháng thực tế trong năm.<br/>• Bổ sung thêm 5 Test Cases kiểm thử hồi quy (Regression Test). | 17/02/2026 | ✅ **CLOSED** |

---

## 5. KẾT LUẬN VỀ KIỂM SOÁT VÀ GIÁM SÁT DỰ ÁN

Sự kết hợp giữa **Báo cáo Tình trạng Đèn Giao Thông** và **Sổ Theo dõi Vấn đề (Issue Log)** đã chứng minh tính minh bạch và năng lực xử lý tình huống chuyên nghiệp của Ban Quản lý Dự án:
* Mọi trở ngại kỹ thuật (ISS-001, ISS-003) và sai lệch dữ liệu (ISS-002) đều được nhận diện sớm, phân công cụ thể và đóng dứt điểm trong vòng từ 2 đến 10 ngày.
* Việc chuyển trạng thái toàn diện từ **Vàng (Mốc 15/10)** sang **Xanh (Mốc 20/10)** khẳng định đường cơ sở hiệu suất (PMB) đã được kiểm soát vững chắc, đưa dự án bước vào giai đoạn kiểm thử UAT và bàn giao với sự tự tin cao nhất.
