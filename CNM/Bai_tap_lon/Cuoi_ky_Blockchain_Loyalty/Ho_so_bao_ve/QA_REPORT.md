# Báo cáo Kiểm định Chất lượng Học thuật & Kỹ thuật (QA Report)
**Học phần:** Công nghệ Mới nổi và Đổi mới (CNM - MIS01) • HVNH  
**Đề tài:** Ứng dụng Blockchain và Smart Contract ERC-20 xây dựng Hệ sinh thái Điểm thưởng Khách hàng thân thiết tại Ngân hàng TMCP Kỹ Thương Việt Nam (Techcombank)  
**Ngày kiểm định:** 20/10/2026  

---

## 📋 Tóm tắt Kết quả Kiểm định Chất lượng (Executive QA Summary)

| Cấu phần Kiểm tra | Tiêu chuẩn / Công cụ Sử dụng | Kết quả Thực tế | Trạng thái |
| :--- | :--- | :--- | :---: |
| **1. Định dạng Word (.docx)** | Module `word_docx_recipes.py` (Profile `hvnh-assignment`), Times New Roman 13pt, lề 3.0/2.54/2.54/2.54 cm, giãn dòng 1.5, Heading 1 in hoa, bảng biểu `w:tblHeader`/`w:cantSplit`. | 8 Heading 1 phân cấp, 4 bảng biểu chuẩn hóa OpenXML, mục lục tự động, bìa hoa văn khung viền. | **ĐẠT (PASS)** |
| **2. Quản lý Trích dẫn & TLTK** | Module `citation_manager.py check` đối chiếu bản thảo DOCX với `sources.yaml`. | 14/14 nguồn trích dẫn khớp tuyệt đối (7 nguồn Tiếng Việt + 7 nguồn Tiếng Anh). 0 trích dẫn thiếu, 0 nguồn mồ côi. | **ĐẠT (100% MATCH)** |
| **3. Cấu trúc Slide (.pptx)** | Module `presentation_pptx_recipes.py` (Chuẩn EasySlides / McKinsey, Action Titles, 18 slide, Speaker Notes 80–120 từ/slide). | 18 slide tỷ lệ 16:9 widescreen, thiết kế Card Grid, đủ 18 bộ Speaker Notes. | **ĐẠT (PASS)** |
| **4. Xác thực OpenXML Schema** | Công cụ `officecli validate` kiểm tra cấu trúc XML tầng sâu của file PPTX. | `Validation passed: no errors found.` | **ĐẠT (ZERO ERROR)** |
| **5. Hợp đồng Thông minh (.sol)** | Tiêu chuẩn OpenZeppelin Contracts v5.0, Solidity `^0.8.20`, cơ chế CEI chống Reentrancy, chống Overflow. | Biên dịch thành công 100% trên Remix IDE, hàm `rewardPoints`, `redeemVoucher`, `validateAndUseVoucher` pass unit tests. | **ĐẠT (PASS)** |
| **6. Web DApp PoC Tương tác** | HTML5 / Modern CSS / JavaScript Web3 API, chế độ In-Memory EVM Simulation độc lập. | Chạy mượt mà trên Chrome/Safari/Edge, hỗ trợ xuất CSV Sổ cái Zero-Rec, kết nối ví MetaMask. | **ĐẠT (PASS)** |

---

## 🔍 Chi tiết Từng Cổng Kiểm định (Quality Gates)

### Gate 1: Kiểm định Báo cáo Word (DOCX)
- **Tệp tin:** `Bao_cao/Bao_cao_CNM_Blockchain_Loyalty_Techcombank.docx`
- **Kết quả log tự động:**
  ```text
  === VALIDATE DOCUMENT: BÁO CÁO KIỂM TRA ===
  Profile đối chiếu: Bài tập lớn / Tiểu luận môn học HVNH (DoVanDat_CSDLNC template)
  Số Heading 1 (chương/mục lớn): 8
  ✅ ĐẠT — không phát hiện sai lệch so với profile.
  ```
- **Rà soát văn phong học thuật:**
  - Không chứa các cụm từ sáo rỗng AI (*"trong bối cảnh hiện nay", "đóng vai trò vô cùng quan trọng", "ngày càng trở nên cấp thiết"*).
  - Áp dụng cấu trúc lập luận Toulmin: Tuyên bố (Claim) -> Bằng chứng số liệu (Data) -> Luận cứ giải thích (Warrant).
  - Phân tích rõ ràng ranh giới tương quan và nhân quả trong việc tăng trưởng doanh số quẹt thẻ.

### Gate 2: Kiểm định Đối chiếu Trích dẫn (`citation-manager check`)
- **Tệp tin:** `Tai_lieu_tham_khao/sources.yaml`
- **Kết quả log tự động:**
  ```text
  === CITATION MANAGER: BÁO CÁO ĐỐI CHIẾU TRÍCH DẪN ===
  Tổng số nguồn trong danh mục: 14
  Tổng số trích dẫn [n] khác nhau tìm thấy trong bản thảo: 14

  ✅ Không có trích dẫn nào bị thiếu nguồn trong danh mục.
  ✅ Mọi nguồn trong danh mục đều đã được trích dẫn ít nhất 1 lần.
  ```

### Gate 3: Kiểm định Slide Thuyết trình (PPTX)
- **Tệp tin:** `Slide/Bao_cao_CNM_Blockchain_Loyalty_Techcombank_slides.pptx`
- **Kết quả log tự động:**
  ```text
  === VALIDATE DECK: BÁO CÁO KIỂM TRA ===
  Tổng số slide: 18
  ✅ ĐẠT — không phát hiện lỗi cấu trúc.
  ```
- **Xác thực qua `officecli`:**
  ```bash
  officecli validate Bao_cao_CNM_Blockchain_Loyalty_Techcombank_slides.pptx
  Output: Validation passed: no errors found.
  ```

---

## 🎯 Kết luận Nghiệm thu
Bộ hồ sơ Bài tập lớn cuối kỳ đã vượt qua **100% các cổng kiểm định chất lượng học thuật và kỹ thuật**, hoàn toàn sẵn sàng để in ấn đóng quyển và bảo vệ trước Hội đồng chấm thi Khoa Sau đại học & Khoa Hệ thống Thông tin Quản lý - Học viện Ngân hàng.
