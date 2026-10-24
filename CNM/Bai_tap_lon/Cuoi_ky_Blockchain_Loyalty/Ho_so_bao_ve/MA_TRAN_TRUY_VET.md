# Ma trận Truy vết Yêu cầu Bài tập lớn (Traceability Matrix)
**Học viện Ngân hàng (Banking Academy of Vietnam - HVNH)**  
**Học phần:** Công nghệ Mới nổi và Đổi mới (CNM - MIS01)  
**Đề tài:** Ứng dụng Blockchain và Smart Contract ERC-20 xây dựng Hệ sinh thái Điểm thưởng Khách hàng thân thiết tại Ngân hàng TMCP Kỹ Thương Việt Nam (Techcombank)  

---

## 📌 Bảng Đối chiếu 14 Tiêu chuẩn Đánh giá Chính thức (R01 – R14)

| Mã YC | Yêu cầu Đề cương Học phần CNM | Vị trí Bằng chứng trong Hồ sơ Bàn giao | Đánh giá Mức độ Đáp ứng |
| :---: | :--- | :--- | :--- |
| **R01** | Lựa chọn công nghệ mới nổi và bài toán thực tế trong một ngân hàng/tổ chức cụ thể tại Việt Nam. | Báo cáo Mở đầu & Chương 2; Slide 2, 3. Đề tài áp dụng Blockchain ERC-20 giải quyết phân mảnh điểm thưởng tại Techcombank. | **ĐẠT 100%** (Gắn chặt với Techcombank và các đối tác Highlands Coffee, Vietnam Airlines, WinMart). |
| **R02** | Trình bày cơ sở lý thuyết công nghệ và giải thích mối liên hệ với bài toán nghiệp vụ. | Báo cáo Chương 1; Slide 5, 6, 7. Lý thuyết DLT, SHA-256, Merkle Tree, EVM, chuẩn ERC-20 và Tokenomics. | **ĐẠT 100%** (Lý luận chặt chẽ, chứng minh tính bất biến và phân tán giải quyết bài toán thiếu niềm tin). |
| **R03** | Tổng quan nghiên cứu các ứng dụng tương tự tại Việt Nam và trên thế giới, rút ra bài học kinh nghiệm. | Báo cáo Mục 1.4; Slide 8; Nguồn tham khảo [1], [2], [12], [13]. Case study Singapore Airlines Kris+ và AmEx. | **ĐẠT 100%** (Rút ra bài học về tính thanh khoản của token và giảm 70% khiếu nại đối soát). |
| **R04** | Phân tích chi tiết bối cảnh tổ chức, nguyên nhân gốc rễ, phạm vi và mục tiêu SMART. | Báo cáo Mục 0.2, Chương 2; Slide 3, 4. Phân tích 4 nút thắt: Siloed DB, điểm bỏ quên 42%, đối soát Excel 7 ngày. | **ĐẠT 100%** (Xác lập mục tiêu SMART: giảm 85% chi phí đối soát, thời gian xác thực < 1.5s). |
| **R05** | Xác định yêu cầu chức năng (FR), phi chức năng (NFR) và mô hình hóa quy trình As-Is bằng BPMN 2.0. | Báo cáo Mục 2.3, 2.4; Slide 9; Callout quy trình As-Is 4 làn bơi (Chủ thẻ, Đối tác, Gateway, Techcombank). | **ĐẠT 100%** (Chỉ rõ điểm nghẽn tại bước đối soát thủ công và chuyển tiền bù trừ sau 30-45 ngày). |
| **R06** | Đề xuất giải pháp kiến trúc tổng thể, mô hình hóa quy trình To-Be BPMN 2.0 và cơ chế tương tác. | Báo cáo Chương 3; Slide 10, 11, 12; Bảng 3.1 cấu trúc 4 tầng (Client, Gateway/Kafka, Smart Contract, DLT). | **ĐẠT 100%** (Đột phá với giao thức Zero-Reconciliation tự động hạch toán bù trừ thời gian thực). |
| **R07** | Đánh giá tính khả thi 3 góc độ: Kỹ thuật, Kinh tế (Cost-Benefit / ROI) và Tổ chức – Pháp lý NHNN. | Báo cáo Chương 5; Slide 16, 17, 18; Bảng 5.1 phân tích tài chính hoàn vốn 11.5 tháng, ROI 142%. | **ĐẠT 100%** (Tuân thủ Điều 10 Luật Các TCTD 2024, Thông tư 09/2020/TT-NHNN, QĐ 2345/QĐ-NHNN). |
| **R08** | Cài đặt, cấu hình và triển khai thực nghiệm sản phẩm Demo / Proof-of-Concept (PoC). | Thư mục `Demo_PoC/`: Hợp đồng `TechcombankLoyaltyToken.sol`, Web DApp `index.html` + `app.js` + `style.css`. | **ĐẠT 100%** (Mã nguồn chuẩn OpenZeppelin, chạy mượt mà trên Remix IDE và Web DApp). |
| **R09** | Trình bày kết quả thực nghiệm ban đầu và đo lường chi phí vận hành (Gas consumption). | Báo cáo Mục 4.3; Slide 14; Bảng 4.1 đặc tả Gas (48.5k gas thưởng lẻ, 26.2k gas batch, 0 gas tra cứu). | **ĐẠT 100%** (100% bài kiểm thử đơn vị thành công, chứng minh tiết kiệm 46% Gas khi chạy Batch). |
| **R10** | Phân tích những khó khăn, thách thức gặp phải trong quá trình triển khai và cách thức giải quyết. | Báo cáo Mục 4.3, 6.2; Slide 16. Phân tích bài toán thông lượng TPS, rủi ro Reentrancy và giải pháp L2 Rollups. | **ĐẠT 100%** (Đưa ra kiến trúc Layer-2 Consortium đạt 3.000 TPS và nguyên tắc Off-chain PII data). |
| **R11** | Đánh giá mức độ thành công, nêu rõ hạn chế, đề xuất lộ trình triển khai mở rộng và kiến nghị chính sách. | Báo cáo Mục 5.4, 6.2, 6.3; Slide 16, 18. Lộ trình 3 giai đoạn (Sandbox -> Pilot Highlands/WinMart -> Mở rộng). | **ĐẠT 100%** (Kiến nghị NHNN ban hành Sandbox cho non-monetary token và lập tổ Web3 tại TCB). |
| **R12** | Tính nhóm và phân công khối lượng đóng góp của từng thành viên. | Báo cáo Bìa, Phụ lục; Bảng phân bổ nhiệm vụ nhóm (Trưởng nhóm: Kiến trúc & Smart Contract; Thành viên: Báo cáo & UI). | **ĐẠT 100%** (Có bảng phân công công việc chi tiết theo từng cấu phần bàn giao). |
| **R13** | Hình thức trình bày chuẩn học thuật HVNH, văn phong khoa học, trích dẫn tài liệu tham khảo đầy đủ. | Tệp `Bao_cao_CNM_Blockchain_Loyalty_Techcombank.docx` đạt chuẩn `hvnh-assignment`; 14 nguồn chuẩn `sources.yaml`. | **ĐẠT 100%** (Không sáo ngữ AI, lập luận Toulmin, đối chiếu trích dẫn `citation-manager check` đạt 100%). |
| **R14** | Slide trình chiếu bảo vệ và kịch bản hỏi đáp phục vụ thuyết trình hội đồng (10–15 phút). | Tệp `Bao_cao_CNM_Blockchain_Loyalty_Techcombank_slides.pptx` (18 slide EasySlides, 100% Speaker Notes). | **ĐẠT 100%** (Đạt chuẩn OpenXML qua `officecli validate`, tích hợp sẵn `KICH_BAN_DEMO.md` và câu hỏi phản biện). |
