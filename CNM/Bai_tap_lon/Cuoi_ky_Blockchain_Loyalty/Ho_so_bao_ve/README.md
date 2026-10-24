# Gói Hồ sơ Bài tập lớn Cuối kỳ: Hệ sinh thái Blockchain Loyalty Techcombank
**Học viện Ngân hàng (Banking Academy of Vietnam - HVNH)**  
**Khoa Sau Đại học & Khoa Hệ thống Thông tin Quản lý**  
**Học phần:** Công nghệ Mới nổi và Đổi mới (CNM - MIS01)  
**Giảng viên giảng dạy:** TS. Đinh Trọng Hiếu (Đổi mới sáng tạo & Cloud) • TS. Đỗ Văn Thuật (Blockchain & Web3)  
**Học viên thực hiện:** Đỗ Văn Đạt (Trưởng nhóm) • Mã học viên: HV24MIS01018  

---

## 📁 Cấu trúc Thư mục Toàn diện Gói Nộp Bài

```
Cuoi_ky_Blockchain_Loyalty/
├── 📄 Bao_cao/
│   ├── Bao_cao_CNM_Blockchain_Loyalty_Techcombank.docx    # Báo cáo Word chuẩn học thuật HVNH (OpenXML)
│   ├── Bao_cao_CNM_Blockchain_Loyalty_Techcombank.md      # Bản thảo Markdown đầy đủ phục vụ đọc nhanh
│   └── build_report.py                                   # Mã nguồn Python tự động hóa sinh file DOCX
│
├── 📊 Slide/
│   ├── Bao_cao_CNM_Blockchain_Loyalty_Techcombank_slides.pptx # Slide 18 trang chuẩn EasySlides 16:9
│   └── build_slide_deck.py                               # Mã nguồn Python dựng slide & Speaker Notes
│
├── 💻 Demo_PoC/
│   ├── TechcombankLoyaltyToken.sol                       # Hợp đồng thông minh Solidity chuẩn ERC-20
│   ├── index.html                                        # Giao diện Web DApp tương tác đa nền tảng
│   ├── style.css                                         # Bảng phong cách thiết kế thương hiệu Techcombank
│   ├── app.js                                            # Logic Web3 & Mô phỏng EVM In-Memory
│   └── HUONG_DAN_CHAY_REMIX_VA_TESTNET.md                # Cẩm nang 2 phương án demo trước Hội đồng
│
├── 📚 Tai_lieu_tham_khao/
│   └── sources.yaml                                      # 14 nguồn học thuật quản lý bởi citation-manager
│
└── 🛡️ Ho_so_bao_ve/
    ├── MA_TRAN_TRUY_VET.md                               # Đối chiếu 14 tiêu chuẩn chính thức R01 - R14
    ├── KICH_BAN_DEMO.md                                  # Kịch bản thuyết trình và thao tác trực tiếp 3-5 phút
    ├── BO_CAU_HOI_PHAN_BIEN.md                           # 8 câu hỏi phản biện chuyên sâu kèm đáp án học thuật
    ├── QA_REPORT.md                                      # Báo cáo kiểm định chất lượng OpenXML & Citation
    └── README.md                                         # Tài liệu điều hướng tổng quan (Tệp tin này)
```

---

## 🎯 Điểm Nhấn Chiến Lược Của Bộ Hồ Sơ

1. **Chuẩn mực Học thuật Sau Đại học:**
   - Định dạng Word chuẩn HVNH (`hvnh-assignment`): lề 3.0/2.54/2.54/2.54 cm, giãn dòng 1.5, font Times New Roman 13pt, Word Native Headings, bảng biểu OpenXML `w:tblHeader`/`w:cantSplit`.
   - Văn phong chống sáo ngữ AI (Anti-AI Smell), lập luận logic Toulmin Model (Claim -> Data -> Warrant).
   - Danh mục trích dẫn đối chiếu tự động đạt độ khớp tuyệt đối 100% (14 nguồn Tiếng Việt và Tiếng Anh).

2. **Kiến trúc Slide Chuẩn Quốc Tế:**
   - 18 slide tỷ lệ 16:9 màn hình rộng chuẩn EasySlides & McKinsey Pyramid Principle.
   - 100% các slide đều có **Tiêu đề Hành động (Action Titles)** và **Speaker Notes** lời thoại thuyết minh (80–120 từ/slide).
   - Đạt chứng chỉ xác thực OpenXML không lỗi (`Validation passed: no errors found`).

3. **Sản phẩm Demo / PoC "Bulletproof" (Không bao giờ lỗi):**
   - Chạy 100% trên trình duyệt Web (chế độ In-Memory EVM Simulation) hoặc chạy trực tiếp trên Remix Ethereum IDE.
   - Thao tác 3 kịch bản mượt mà trong 2 phút: Ngân hàng thưởng điểm quẹt thẻ -> Khách hàng đổi voucher và đốt token -> Sổ cái Zero-Reconciliation tự động hạch toán đối soát.
