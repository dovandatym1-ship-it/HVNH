# BT cuối kỳ — Tác động của AI đến Việc làm năm 2030

**Học phần:** Phân tích Kinh doanh — Học viện Ngân hàng
**Sinh viên thực hiện:** Đỗ Văn Đạt

Bộ deliverable này mô phỏng cấu trúc bài tập giữa kỳ `BT_Giua_Ky_BankChurners` (cùng thư mục
`HVNH/BA`), áp dụng cho dữ liệu `AI_ViecLam2030_Raw.csv` (đã có sẵn trong `BA/BT cuôi kỳ/`, dưới
tên gốc `BaiTap_TienXuLyDuLieu_DeBai.csv`). File `ncr_ride_bookings.csv` trong cùng thư mục cha
KHÔNG được dùng làm dữ liệu cho đề tài này — chỉ có notebook Kaggle *Predicting Uber Ride
Cancellations* (gắn với bộ dữ liệu đó) được tham khảo về **phong cách trình bày quy trình**
(đọc dữ liệu → hiển thị dòng đầu → tiền xử lý → EDA → mô hình hoá).

## Phát hiện chính
`Job_Title` (nghề nghiệp) giải thích **85,7%** phương sai của `Automation_Probability_2030`
(eta²), trong khi mọi đặc điểm cá nhân (kỹ năng, kinh nghiệm, học vấn, lương) gần như không có
giá trị dự báo. Đưa `Job_Title` vào mô hình nâng F1-macro từ mức ngẫu nhiên (~0,22–0,34) lên
**0,9947** và R² hồi quy lên **0,862**. Xem chi tiết đầy đủ trong báo cáo.

## Danh mục file

| File | Mô tả |
|---|---|
| `AI_ViecLam2030_Raw.csv` | Dữ liệu gốc (3.000 dòng x 18 cột) |
| `AI_ViecLam2030_Cleaned.csv` | Dữ liệu sau tiền xử lý + feature engineering (25 cột) |
| `AI_ViecLam2030_Clustered.csv` | Dữ liệu đã gắn nhãn cụm K-Means (Cluster 0-3) |
| `run_ai_jobs_pipeline.py` | Script pipeline tổng hợp: tiền xử lý → EDA → phân cụm → phân loại → hồi quy → xuất `figures/` + `pipeline_summary.json` |
| `pipeline_summary.json` | Toàn bộ số liệu/kết quả định lượng (dùng để dựng báo cáo & slide tự động) |
| `pipeline_run.log` | Log console của lần chạy pipeline cuối cùng |
| `figures/` | 17 biểu đồ PNG (EDA, phân cụm, mô hình hoá) |
| `AI_ViecLam2030_EDA_TienXuLy.ipynb` | Notebook 1/2 — khám phá dữ liệu thô, tiền xử lý, EDA (đã chạy, không lỗi) |
| `AI_ViecLam2030_Data_Processing_and_Mining_DoVanDat.ipynb` | Notebook 2/2 — phân cụm, phân loại, hồi quy (đã chạy, không lỗi) |
| `build_notebooks.py` | Script dựng 2 notebook trên bằng `nbformat` |
| `Bao_Cao_Cuoi_Ky_TacDongAI_ViecLam2030.docx` | Báo cáo Word chuẩn `hvnh-assignment` (bìa khung viền, mục lục, 8 bảng, 17 hình, TLTK) |
| `Bao_Cao_Cuoi_Ky_TacDongAI_ViecLam2030.md` | Bản mirror Markdown của báo cáo trên |
| `build_docx_report.py` | Script dựng báo cáo Word bằng thư viện `word_docx_recipes.py` (skill academic-docx-writer) |
| `Slide_Thuyet_Trinh_TacDongAI_ViecLam2030.pptx` | Slide thuyết trình 18 slide, kiến trúc EasySlides (16:9, Action Titles, Speaker Notes) |
| `Slide_Thuyet_Trinh_TacDongAI_ViecLam2030.html` | Bản slide xem trực tiếp trên trình duyệt (mở file này, dùng phím ◀ ▶ hoặc nút điều hướng) |
| `Slide_Thuyet_Trinh_TacDongAI_ViecLam2030.md` | Bản mirror Markdown của slide |
| `build_pptx_slides.py` | Script dựng slide bằng thư viện `presentation_pptx_recipes.py` (skill academic-slide-writer) |
| `Kich_Ban_Thuyet_Trinh_va_Cau_Hoi_Phan_Bien.md` | Lời thoại thuyết trình đầy đủ theo từng slide + 10 câu hỏi phản biện dự kiến kèm gợi ý trả lời |

## Cách tái tạo toàn bộ kết quả từ đầu
```bash
python3 run_ai_jobs_pipeline.py      # 1. Tiền xử lý + EDA + phân cụm + mô hình hoá -> figures/, *.csv, pipeline_summary.json
python3 build_notebooks.py           # 2. Dựng 2 notebook (sau đó chạy jupyter nbconvert --execute để có output)
python3 build_docx_report.py         # 3. Dựng báo cáo Word
python3 build_pptx_slides.py         # 4. Dựng slide PowerPoint
```

## Giới hạn cần lưu ý khi đọc kết quả
Đây là bộ dữ liệu **mô phỏng (synthetic)** — `Automation_Probability_2030` được gán gắn với
`Job_Title` theo quy tắc, không phải khảo sát thực địa. Hiệu suất mô hình gần như tuyệt đối phản
ánh cơ chế sinh dữ liệu có kiểm soát, **không nên** diễn giải như bằng chứng cho khả năng dự báo
tương tự trong thị trường lao động thực tế. Xem mục 3.5 của báo cáo để biết chi tiết.
