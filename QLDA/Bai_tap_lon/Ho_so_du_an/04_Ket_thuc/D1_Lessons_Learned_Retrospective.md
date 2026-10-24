# BÀI HỌC KINH NGHIỆM (LESSONS LEARNED) & BIÊN BẢN TỔNG KẾT RETROSPECTIVE
## Dự án: Xây dựng Hệ thống Quản trị Nhân sự Nội bộ (ABC-HRM)
### Mã tài liệu: BTL-QLDA-D1 | Giai đoạn: Kết thúc Dự án (Project Closing)
### Tiêu chuẩn áp dụng: PMI PMBOK Guide / Organizational Learning Standard | Học phần: QLDA CNTT Nâng cao (HVNH)

---

## 1. KHUNG TIẾP CẬN BẢN CHẤT: LÀM GÌ? TẠI SAO LÀM? LÀM THẾ NÀO?

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                   MÔ HÌNH BẢO TOÀN VÀ ĐÓNG GÓI TRI THỨC TỔ CHỨC DỰ ÁN                            │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 1. TẠI SAO LÀM? (WHY)                                                                           │
│    • Một dự án kết thúc không chỉ dừng lại ở việc bàn giao phần mềm, mà tài sản quý giá nhất     │
│      còn lại là Tri thức Tổ chức (Organizational Process Assets - OPAs).                         │
│    • Nếu không tổ chức họp tổng kết và văn bản hóa bài học kinh nghiệm, các sai lầm kỹ thuật và │
│      vấn đề ước tính sẽ tiếp tục bị lặp lại ở các dự án tiếp theo của doanh nghiệp.              │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 2. LÀM GÌ? (WHAT)                                                                                │
│    • Tổ chức phiên họp Tổng kết Dự án (Project Retrospective Meeting) có đầy đủ 5 thành viên     │
│      nhóm dự án và đại diện các bên liên quan trọng yếu (HR Head, IT Lead).                     │
│    • Phân loại và đóng gói toàn diện 2 khối tri thức:                                            │
│      - Khối Tri thức Hữu hình (Explicit Knowledge): 04 quy chuẩn kỹ thuật và quy trình chuẩn.   │
│      - Khối Tri thức Vô hình (Tacit Knowledge): 03 bài học sâu sắc về tâm lý và giao tiếp.       │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 3. LÀM THẾ NÀO? (HOW)                                                                           │
│    • Áp dụng phương pháp điều phối phi phán xét (No-Blame Culture): Tập trung vào vấn đề và     │
│      quy trình thay vì chỉ trích cá nhân.                                                       │
│    • Chuyển hóa từng bài học thành Hành động Tiêu chuẩn (Actionable Standard Operating          │
│      Procedure - SOP) lưu trữ vào kho tri thức nội bộ của công ty.                              │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. BIÊN BẢN PHIÊN HỌP TỔNG KẾT DỰ ÁN (RETROSPECTIVE MEETING)

* **Thời gian tổ chức:** 09h00 – 11h30 ngày 02/05/2026 (sau khi hoàn thành đợt Go-Live).
* **Địa điểm:** Phòng họp tầng 5 Công ty Cổ phần ABC kết hợp trực tuyến qua Microsoft Teams.
* **Thành phần tham dự:**
  - Chủ trì: [Họ và tên Học viên 1] — Quản lý Dự án (PM).
  - Thư ký: [Họ và tên Học viên 2] — Chuyên viên Phân tích Nghiệp vụ (BA).
  - Khối Kỹ thuật: [Họ và tên Học viên 3] (Senior Dev), Dev 1, Dev 2, QA Engineer.
  - Đại diện Đơn vị Thụ hưởng: Bà Trần Thị B (Trưởng phòng Quản trị Nhân sự).
  - Đại diện Hạ tầng: Ông Phạm Quốc D (Trưởng phòng CNTT).
* **Nguyên tắc làm việc:** Cam kết cởi mở, minh bạch, nhìn thẳng vào sự thật, học hỏi từ sai sót để kiến tạo chuẩn mực tốt hơn cho các dự án tương lai.

---

## 3. ĐÓNG GÓI TRI THỨC HỮU HÌNH (EXPLICIT KNOWLEDGE PACKAGING)

Tri thức hữu hình là các kiến thức, quy trình, số liệu định lượng có thể văn bản hóa, lập trình hóa thành tài liệu chuẩn cho tổ chức:

| Lĩnh vực | Vấn đề Thực tế Phát sinh trong Dự án | Bài học Rút ra (Lesson Learned) | Hành động Tiêu chuẩn cho Dự án Sau (How to apply?) |
|---|---|---|---|
| **Ước tính Lịch trình & Chi phí** | Phân hệ Tính lương bị thiếu $20\%$ công sức ước tính ban đầu do xem nhẹ sự phức tạp của luật thuế TNCN và các trường hợp người phụ thuộc sinh giữa năm. | Không thể áp dụng định mức ước tính thông thường cho các phân hệ liên quan mật thiết đến pháp lý tài chính. | **Quy tắc đệm 25%:** Mọi gói công việc liên quan đến tài chính, thuế, ngân hàng phải tự động cộng thêm hệ số dự phòng kỹ thuật tối thiểu **$25\%$ thời lượng và chi phí**. |
| **Tích hợp Phần cứng Bên ngoài** | Mất 10 ngày công và 15 triệu chi phí thuê ngoài để xử lý sự cố rớt kết nối Socket máy quét vân tay ZKTeco do thiếu tài liệu Keep-Alive. | Phụ thuộc vào SDK của bên thứ ba mà không kiểm chứng sớm là rủi ro công nghệ nghiêm trọng nhất. | **Quy chuẩn Sprint 0:** Bắt buộc phải thực hiện thử nghiệm kết nối kỹ thuật (**PoC tích hợp phần cứng**) ngay trong 02 tuần đầu tiên của dự án trước khi phê duyệt Baseline lịch trình. |
| **Đảm bảo Chất lượng Mã nguồn** | Hoạt động Code Review bắt được 15 lỗi sai lệch công thức làm tròn số học trong phân hệ tiền lương trước khi bước vào đợt UAT. | Kiểm thử tự động (Unit Test) và đánh giá chéo mã nguồn là rào chắn hiệu quả nhất để loại bỏ lỗi logic nhạy cảm. | **Quy tắc 2-Reviewer:** Mã nguồn thuộc phân hệ Tính lương bắt buộc phải qua xét duyệt (PR) của ít nhất **02 kỹ sư cao cấp**; tỷ lệ bao phủ mã nguồn (Unit Test Coverage) đạt tối thiểu **$\ge 85\%$**. |
| **Chuyển đổi Dữ liệu Lịch sử** | Dữ liệu nhân sự trong 15 file Excel cũ bị trùng lặp 12 số CCCD và không chuẩn hóa mã phòng ban, gây chậm trễ khâu nạp DB. | Dữ liệu thủ công tích lũy nhiều năm của khách hàng luôn chứa đựng sai sót vượt quá dự kiến ban đầu. | **Quy chuẩn Làm sạch Sớm:** Thành lập tổ công tác làm sạch dữ liệu (Data Cleansing) ngay từ **Giai đoạn Phân tích Yêu cầu (Tháng 1)**; không để dồn việc làm sạch dữ liệu vào giai đoạn Triển khai. |

---

## 4. ĐÓNG GÓI TRI THỨC VÔ HÌNH (TACIT KNOWLEDGE PACKAGING)

Tri thức vô hình là những trải nghiệm, trực giác, kỹ năng mềm và sự thấu cảm tâm lý sâu sắc thu hoạch được qua quá trình cọ xát thực tế:

### 4.1. Nghệ thuật Hóa giải Tâm lý E ngại Thay đổi của Bên Liên quan (Stakeholder Empathy)
* **Thực tế trải nghiệm:** Trong 4 tuần đầu tiên, Trưởng phòng HR (Bà Trần Thị B) tỏ ra rất dè dặt, liên tục bảo vệ thói quen dùng Excel cũ vì lo ngại phần mềm mới phức tạp, dễ mất mát dữ liệu lương nhạy cảm.
* **Chiêm nghiệm sâu sắc (Tacit Insight):** Con người không chống lại sự thay đổi; họ chỉ chống lại cảm giác **bị mất kiểm soát**. Nếu chỉ thuyết phục bằng lý thuyết hoặc văn bản hành chính, sự e dè sẽ biến thành sự chống đối ngầm.
* **Nghệ thuật ứng xử đã áp dụng thành công:**
  - Nhóm BA và UI/UX đã chủ động dựng bản Mockup tương tác trên Figma ngay từ Tuần 3, mời trực tiếp Trưởng phòng HR thao tác thử các nút bấm duyệt đơn và xuất phiếu lương thử nghiệm.
  - Khi tận mắt nhìn thấy giao diện đẹp mắt, bảng lương được tính tự động chỉ trong 3 giây và dữ liệu cũ được bảo toàn nguyên vẹn, bà B đã chuyển biến tâm lý hoàn toàn: Từ trạng thái e ngại trở thành **Đại sứ Cổ vũ Nhiệt thành nhất (Change Champion)** của dự án, hỗ trợ nhóm đôn đốc nhân viên nộp đơn online.
  - **Bài học vô hình:** *"Trăm nghe không bằng một thấy. Cho người dùng trải nghiệm sản phẩm trực quan từ sớm là chìa khóa vàng để xóa bỏ mọi rào cản tâm lý".*

---

### 4.2. Nghệ thuật Trao quyền và Tạo Động lực Nội tại cho Kỹ sư Trẻ (Empowerment)
* **Thực tế trải nghiệm:** Kỹ sư phần mềm Dev 2 (thành viên trẻ nhất nhóm) ban đầu làm việc thụ động, chỉ viết code đúng theo từng dòng đặc tả mà không có sự sáng tạo.
* **Chiêm nghiệm sâu sắc (Tacit Insight):** Giám sát vi mô (Micromanagement) làm thui chột tinh thần trách nhiệm. Khi được tin tưởng và trao quyền làm chủ (Ownership), kỹ sư sẽ bộc phát năng lực vượt bậc.
* **Nghệ thuật ứng xử đã áp dụng thành công:**
  - Tại Sprint 3, PM quyết định giao toàn quyền cho Dev 2 tự thiết kế luồng trải nghiệm người dùng (UX) cho Phân hệ Tuyển dụng và Onboarding.
  - Nhận được sự tin tưởng, Dev 2 đã chủ động nghiên cứu thêm các thư viện hoạt ảnh (Micro-animations), thiết kế tính năng kéo-thả ứng viên (Drag-and-Drop Kanban) cực kỳ mượt mà, giúp phân hệ Tuyển dụng trở thành điểm sáng được Ban Giám đốc khen ngợi nhiều nhất trong buổi nghiệm thu.
  - **Bài học vô hình:** *"Lòng tin và sự tôn trọng tính tự chủ tạo ra sức bật năng suất gấp nhiều lần mệnh lệnh hành chính khô khan".*

---

### 4.3. Giá trị của Giao tiếp Trực tiếp Thay vì Báo cáo Hình thức (Real-time Transparency)
* **Thực tế trải nghiệm:** Giai đoạn Mốc 15/10 khi chỉ số EVM bị sụt giảm ($SPI = 0,948$), nếu PM chỉ gửi một bản báo cáo số liệu qua email, Ban Giám đốc có thể đã hoang mang và can thiệp thô bạo vào quy trình kỹ thuật.
* **Nghệ thuật ứng xử đã áp dụng thành công:**
  - PM chủ động xin một cuộc gặp trực tiếp 20 phút với Tổng Giám đốc (Sponsor). Thay vì giấu giếm khó khăn, PM giải thích thẳng thắn sự cố máy chấm công bằng hình vẽ luồng mạng đơn giản, đồng thời trình bày sẵn Kế hoạch hành động 3 điểm để khắc phục trong 4 tuần.
  - Sự thẳng thắn, tự tin và giải pháp rõ ràng đã thuyết phục Sponsor hoàn toàn, đồng ý giải ngân ngay 15 triệu từ Quỹ Dự phòng mà không có bất kỳ sự khiển trách nào.
  - **Bài học vô hình:** *"Minh bạch về rủi ro đi kèm giải pháp hành động cụ thể là nền tảng xây dựng niềm tin vững chắc nhất giữa PM và Nhà tài trợ".*

---

## 5. KẾT LUẬN VÀ LƯU TRỮ VÀO TÀI SẢN QUY TRÌNH TỔ CHỨC (OPAs)

Toàn bộ các tài liệu mã nguồn mẫu, kịch bản kiểm thử UAT, thuật toán tính thuế TNCN chuẩn hóa và bản tổng kết bài học kinh nghiệm này đã được đóng gói thành tệp lưu trữ số (**Zip Archive & Git Tag `v1.0-release`**) và đưa vào Thư viện Tri thức Nội bộ của Công ty Cổ phần ABC. 

Đây sẽ là cẩm nang hướng dẫn chuẩn mực cho **Giai đoạn 2 (Dự án Mở rộng Quản trị Đào tạo LMS)** và các dự án chuyển đổi số công nghệ thông tin tiếp theo của tổ chức.
