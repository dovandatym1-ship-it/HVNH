# Bài tập Thảo luận Tại lớp (20 phút): Đổi mới Sáng tạo trong Tập đoàn Bán lẻ Truyền thống
**Học phần:** Công nghệ Mới nổi và Đổi mới (CNM / MIS01)  
**Học viện Ngân hàng (Banking Academy of Vietnam - HVNH)**  
**Giảng viên:** TS. Đinh Trọng Hiếu  
**Slide tham chiếu:** Slide 41 - `1.2_Sang_tao_va_Doi_moi.md`

---

## 🎯 ĐỀ BÀI & BỐI CẢNH THẢO LUẬN

> **Thông điệp cốt lõi:**  
> *"Đổi mới sáng tạo không phải là một sự kiện ngẫu nhiên, mà là một năng lực tổ chức phải được thiết kế và bảo vệ."*

* **Thời gian thảo luận nhóm:** 20 phút.
* **Nhiệm vụ:**
  1. Chọn 1 công nghệ mới nổi hiện nay (*AI tạo sinh, Blockchain, AR/VR*).
  2. Phân tích **2 rào cản lớn nhất** mà một tập đoàn bán lẻ truyền thống tại Việt Nam (ví dụ: chuỗi siêu thị/bách hóa, điện máy, bán lẻ thời trang) sẽ gặp phải khi triển khai công nghệ này.
  3. Đề xuất **hệ thống giải pháp** chiến lược dựa trên các khung lý thuyết đã học (*Ambidextrous Organization, Skunkworks, Psychological Safety, Fail Fast, Learning Milestones*).

---

## 🚀 LỰA CHỌN CÔNG NGHỆ: TRÍ TUỆ NHÂN TẠO TẠO SINH (GENERATIVE AI)

### 1. Bối cảnh Doanh nghiệp Giả định
* **Chủ thể:** Một Tập đoàn Bán lẻ Truyền thống quy mô lớn tại Việt Nam (mô hình tương tự Saigon Co.op, WinCommerce, Bách Hóa Xanh, hoặc Central Retail Vietnam).
* **Quy mô:** 500 – 2.000 điểm bán vật lý, hàng chục nghìn nhân sự vận hành (quản lý ngành hàng, thu ngân, kho vận, tiếp thị).
* **Mục tiêu ứng dụng GenAI:**
  - Cá nhân hóa trải nghiệm khách hàng: Trợ lý ảo tư vấn mua sắm thông minh (Virtual Shopping Assistant) trên ứng dụng di động.
  - Tự động hóa tiếp thị: Tạo nội dung quảng cáo, hình ảnh, banner khuyến mãi cá nhân hóa theo từng cụm khách hàng trong vài giây thay vì vài tuần.
  - Tối ưu chuỗi cung ứng: Phân tích báo cáo tồn kho, dự báo sức mua theo thời tiết/lễ hội và tự động tạo đơn hàng đề xuất cho nhà cung ứng.

---

## 🧱 PHÂN TÍCH 2 RÀO CẢN LỚN NHẤT

### ⚠️ Rào cản 1: "Bẫy Hiệu quả Ngắn hạn" & Phân mảnh Dữ liệu Cấu trúc (Structural & Metric Trap)
* **Bản chất lý thuyết:** 
  - Doanh nghiệp truyền thống mắc kẹt trong **Tư duy Khai thác (Exploit)**: Áp lực chỉ tiêu doanh số hàng tháng, biên lợi nhuận mỏng (thường chỉ 2-4% trong ngành bán lẻ) và thước đo tài chính truyền thống (ROI, NPV ngắn hạn). Ban lãnh đạo thường đòi hỏi dự án công nghệ phải chứng minh sinh lời ngay trong 1-2 quý.
  - **Dữ liệu bị cô lập (Data Silos):** Hệ thống ERP (SAP/Oracle), phần mềm quản lý kho (WMS) và máy tính tiền POS tại hàng nghìn điểm bán được xây dựng chắp vá qua nhiều thập kỷ, thiếu chuẩn hóa dữ liệu lớn. GenAI không thể vận hành hiệu quả nếu thiếu dữ liệu sạch và được kết nối thời gian thực.
* **Hậu quả:** Các đề xuất AI bị xếp vào "nghĩa địa ý tưởng" (Ideas Graveyard) vì không vượt qua được bài toán thẩm định NPV ngắn hạn; hoặc nếu mua các giải pháp GenAI đóng gói sẵn (Off-the-shelf) về cắm vào hạ tầng dữ liệu phân mảnh thì mô hình sinh ra kết quả ảo giác (Hallucination), gây lãng phí hàng triệu USD.

---

### ⚠️ Rào cản 2: Nỗi sợ Bị Thay thế & Sự Thiếu hụt "An toàn Tâm lý" (Psychological Safety Deficit)
* **Bản chất lý thuyết:** 
  - **Tâm lý ác cảm tổn thất (Loss Aversion) & Thiên vị hiện trạng (Status Quo Bias):** Hàng nghìn nhân viên từ khối tiếp thị, chăm sóc khách hàng (CSKH), thu mua (Procurement) đến quản lý cửa hàng cảm thấy vị thế và công việc của họ bị đe dọa trực tiếp bởi AI.
  - **Thiếu hụt An toàn tâm lý (Edmondson, 1999):** Nhân viên sợ rằng nếu họ thử nghiệm dùng AI mà xảy ra sai sót (ví dụ: Chatbot trả lời nhầm giá khuyến mãi cho khách hàng, hoặc câu từ không chuẩn thuần phong mỹ tục), họ sẽ bị khiển trách hoặc phạt trừ lương.
* **Hậu quả:** Xuất hiện sự **kháng cự thụ động (Passive Resistance)**. Đội ngũ bán hàng không tích cực hướng dẫn khách dùng app, nhân viên marketing tiếp tục làm thủ công theo thói quen cũ, dữ liệu phản hồi từ thực địa không được cập nhật cho mô hình học tập, dẫn đến dự án "chết yểu" từ tầng văn hóa cơ sở.

---

## 💡 HỆ THỐNG GIẢI PHÁP ĐỔI MỚI TOÀN DIỆN

Để hiện thực hóa thông điệp *"Đổi mới sáng tạo phải được thiết kế và bảo vệ"*, doanh nghiệp bán lẻ cần triển khai đồng bộ 4 giải pháp tương ứng với các trụ cột:

```
                            CHIẾN LƯỢC ĐỔI MỚI GENAI
                                       |
    +------------------+---------------+------------------+------------------+
    |                  |                                  |                  |
[THIẾT KẾ CẤU TRÚC]  [THIẾT KẾ CÔNG CỤ]             [BẢO VỆ VĂN HÓA]  [BẢO VỆ CON NGƯỜI]
Ambidextrous Org    Learning Milestones            Psychological     Augmented AI Workforce
& Skunkworks Unit   thay cho NPV ngắn hạn          Safety & Sandbox  (Trợ lý, không thay thế)
```

### 1. Thiết kế Cấu trúc: Mô hình Tổ chức Hai tay (Ambidextrous Organization) & Đơn vị Skunkworks
* **Cơ chế:** Tách biệt rõ ràng 2 nhánh vận hành:
  - **Tay trái (Exploit - Khai thác):** Khối bán lẻ truyền thống (siêu thị, cửa hàng) tiếp tục vận hành chuẩn chỉ theo quy trình nghiêm ngặt, tối ưu hóa chi phí và kiểm soát dòng tiền hiện tại.
  - **Tay phải (Explore - Khám phá):** Thành lập **"Retail GenAI Lab" (Đơn vị Skunkworks độc lập)** trực thuộc Tổng Giám đốc. Đơn vị này được giải phóng hoàn toàn khỏi các thủ tục phê duyệt hành chính cồng kềnh, được cấp ngân sách nghiên cứu độc lập và tự do tuyển dụng nhân tài dữ liệu/AI.
* **Tác dụng:** Bảo vệ sáng kiến GenAI non trẻ không bị "bóp nghẹt" bởi các quy chuẩn vận hành khắt khe của bộ máy bán lẻ truyền thống.

### 2. Thiết kế Công cụ Quản trị: Đánh giá theo Cột mốc Học hỏi (Learning Milestones)
* **Cơ chế:** Không áp KPI doanh thu hay tỷ suất hoàn vốn ROI trong 6 - 12 tháng đầu. Thay vào đó, áp dụng khung đo lường tiến độ thử nghiệm:
  - *Cột mốc 1 (3 tháng):* Làm sạch và liên thông dữ liệu hành vi của 500.000 khách hàng thân thiết.
  - *Cột mốc 2 (6 tháng):* Mức độ chính xác của phản hồi Chatbot CSKH đạt > 85%; thời gian tạo ấn phẩm marketing giảm từ 5 ngày xuống 30 phút.
  - *Cột mốc 3 (9 tháng):* Tỷ lệ chuyển đổi mua hàng (Conversion Rate) qua trợ lý tư vấn cá nhân hóa tăng 15% tại 10 cửa hàng thử nghiệm.
* **Tác dụng:** Tránh rơi vào bẫy từ chối dự án vì thiếu NPV ngắn hạn, tạo không gian đủ dài để mô hình AI học và thích nghi với hành vi tiêu dùng nội địa.

### 3. Bảo vệ Văn hóa: Xây dựng An toàn Tâm lý (Psychological Safety) & Văn hóa Thất bại Nhanh (Fail Fast)
* **Cơ chế:**
  - Lãnh đạo cấp cao tuyên bố chính sách: *"Thử nghiệm sai không bị phạt, không thử nghiệm mới là lỗi"*.
  - Thiết lập **Môi trường Hộp cát Nội bộ (Internal Sandbox)**: Triển khai thử nghiệm quy mô nhỏ với chi phí thấp (Low-cost Experiments). Ví dụ: Chỉ thử nghiệm GenAI tạo kịch bản bán lẻ cho 1 nhóm hàng mỹ phẩm trước; nếu sai sót thì thiệt hại kinh tế chỉ dưới vài triệu đồng.
  - Tổ chức ngày hội *"Tôn vinh Thất bại mang lại Bài học lớn"* (Failure Awards) để khích lệ tinh thần dám dấn thân của nhân viên.
* **Tác dụng:** Xóa bỏ rào cản sợ hãi, kích hoạt tư duy phân kỳ (Divergent Thinking) từ chính những nhân viên tuyến đầu am hiểu khách hàng nhất.

### 4. Bảo vệ Con người: Định vị AI Tăng cường (Augmented Workforce)
* **Cơ chế:**
  - Truyền thông nội bộ nhất quán: GenAI là **"Copilot" (Trợ lý đắc lực)** giúp nhân viên giảm bớt 70% các công việc bàn giấy, đối soát lặp lại nhàm chán để họ tập trung vào tư vấn cảm xúc, thấu hiểu khách hàng – việc mà AI không thể làm được.
  - Cam kết không cắt giảm nhân sự vì lý do ứng dụng AI; thay vào đó, mở các chương trình đào tạo lại (Reskilling & Upskilling) kỹ năng sử dụng Prompt Engineering cho nhân viên toàn hệ thống.
* **Tác dụng:** Biến lực lượng lao động từ "đối tượng kháng cự" trở thành "đồng minh đồng kiến tạo" trong làn sóng đổi mới.

---

## 🎤 DÀN Ý BẢO VỆ BÀI THẢO LUẬN TẠI LỚP (PITCH TRONG 3 PHÚT)

| Thời lượng | Nội dung phát biểu của nhóm | Khung lý thuyết tương ứng |
| :---: | :--- | :--- |
| **0:00 - 0:30** | **Mở đầu & Tuyên ngôn:** *"Đổi mới sáng tạo không phải là một sự kiện ngẫu nhiên, mà là một năng lực tổ chức phải được thiết kế và bảo vệ."* Nhóm chọn công nghệ **Generative AI** ứng dụng vào **Tập đoàn Bán lẻ Truyền thống tại Việt Nam**. | Thông điệp cốt lõi |
| **0:30 - 1:30** | **2 Rào cản lớn nhất:**<br>1. **Rào cản Cấu trúc:** Bẫy đòi hỏi ROI ngắn hạn và tình trạng dữ liệu phân mảnh (Silos) giữa hàng nghìn cửa hàng POS/ERP.<br>2. **Rào cản Văn hóa:** Thiếu an toàn tâm lý (Psychological Safety), nhân viên sợ mất việc nên kháng cự ngầm. | Structural Inertia & Status Quo Bias |
| **1:30 - 2:30** | **Hệ thống Giải pháp 4 bước:**<br>• *Thiết kế:* Lập đơn vị **Skunkworks AI Lab** độc lập (Mô hình Ambidextrous) + Đo lường bằng **Learning Milestones**.<br>• *Bảo vệ:* Xây dựng **An toàn tâm lý**, cho phép **Fail Fast** trong Sandbox nhỏ + Cam kết **Augmented Workforce** (AI là trợ lý, không thay thế con người). | Ambidextrous, Skunkworks, Psychological Safety, Learning Milestones |
| **2:30 - 3:00** | **Kết luận:** GenAI chỉ là công cụ công nghệ; việc doanh nghiệp có gặt hái được quả ngọt hay không hoàn toàn phụ thuộc vào việc Ban Lãnh đạo có dũng cảm **thiết kế cấu trúc mới** và **bảo vệ văn hóa an toàn** cho nhân viên hay không. | Schumpeter & Leadership |
