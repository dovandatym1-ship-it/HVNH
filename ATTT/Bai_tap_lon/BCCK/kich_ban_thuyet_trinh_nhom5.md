# KỊCH BẢN THUYẾT TRÌNH TÓM GỌN: BẢO MẬT HỆ THỐNG THÔNG TIN (NHÓM 5)

**Đề tài:** Nghiên cứu áp dụng tự động hoá đánh giá an ninh hạ tầng mã nguồn (IaC) và container image bằng Trivy/Terrascan trong quy trình GitOps cho hệ thống CRM tại Vietinbank.
**Tổng thời lượng:** ~15 phút (Mỗi thành viên trình bày khoảng 3 phút - Rất ngắn gọn, đi thẳng vào trọng tâm).

> [!TIP]
> Do thời gian mỗi người chỉ có 3 phút, hãy nói lướt qua các lý thuyết nền (ai cũng đã biết) và tập trung mạnh vào **Vấn đề cụ thể của CRM** và **Pipeline Giải pháp**. Tổng số slide nên giữ ở mức 10-12 slide.

---

## 👨‍💼 THÀNH VIÊN 1: ĐỖ VĂN ĐẠT - ĐẶT VẤN ĐỀ & MỤC TIÊU (Slide 1 - 3)
**⏱ Thời lượng:** ~3 phút
**🎯 Trọng tâm:** Tại sao cần giải pháp này?

### Slide 1: Trang bìa
*   **Tiêu đề:** Tự động hóa đánh giá an ninh IaC & Container trong GitOps cho CRM tại VietinBank.
*   **Nội dung:** Tên nhóm, GVHD (Nói lướt 10s: *"Kính chào thầy và các bạn, tôi là Đỗ Văn Đạt, đại diện nhóm 5 xin phép bắt đầu phần trình bày..."*).

### Slide 2: Bối cảnh VietinBank & Vấn đề ATTT
*   **Tiêu đề:** Chuyển đổi số CRM & Thách thức bảo mật
*   **Nội dung chính:**
    *   CRM VietinBank đang chuyển dịch lên kiến trúc Microservices & Cloud-native để tăng tốc độ phát triển.
    *   **Vấn đề:** Tốc độ deploy (CI/CD) quá nhanh, bảo mật truyền thống không theo kịp.
    *   Rủi ro mở rộng sang Container, IaC và chuỗi cung ứng phần mềm.
*   **Hình ảnh:** Sơ đồ DevOps bị nút thắt (bottleneck) ở khâu Security.

### Slide 3: Mục tiêu nghiên cứu
*   **Tiêu đề:** Mục tiêu & Hướng tiếp cận Shift-Left
*   **Nội dung chính:**
    *   Mục tiêu: Đưa bảo mật vào sớm nhất có thể trong quy trình code (Shift-Left).
    *   Phạm vi: Tự động hóa quét lỗ hổng Image (Trivy), lỗi cấu hình hạ tầng (Terrascan) qua GitOps.

---

## 👩‍💼 THÀNH VIÊN 2: TRẦN NGỌC DŨNG - KIẾN TRÚC HỆ THỐNG CRM (Slide 4 - 5)
**⏱ Thời lượng:** ~3 phút
**🎯 Trọng tâm:** Chỉ ra các điểm "yết hầu" trong kiến trúc.

### Slide 4: Kiến trúc Cloud-native của CRM
*   **Tiêu đề:** Tổng quan Kiến trúc CRM VietinBank
*   **Nội dung chính:**
    *   Phân rã thành hàng chục Microservices độc lập, chạy trên Kubernetes.
    *   Giao tiếp phức tạp qua API Gateway và Kafka.
*   **Hình ảnh:** Sơ đồ kiến trúc CRM 1.0 (Hình 2.1).

### Slide 5: Tài sản & Luồng dữ liệu nhạy cảm
*   **Tiêu đề:** Phân loại tài sản thông tin trọng yếu
*   **Nội dung chính:**
    *   Dữ liệu: PII (Thông tin khách hàng định danh), lịch sử giao dịch.
    *   Hạ tầng: Image, Manifest, Config (Nơi chứa nhiều rủi ro cấu hình sai).
    *   Secrets: API Keys để tích hợp với Core Banking.
*   **Hình ảnh:** Sơ đồ luồng dữ liệu (Data Flow) nhấn mạnh vùng chứa Dữ liệu nhạy cảm.

---

## 👨‍💻 THÀNH VIÊN 3: TẠ NGỌC TUỆ - ĐÁNH GIÁ RỦI RO (Slide 6 - 7)
**⏱ Thời lượng:** ~3 phút
**🎯 Trọng tâm:** Hacker tấn công vào đâu và ma trận rủi ro.

### Slide 6: Các rủi ro bảo mật chính
*   **Tiêu đề:** Nhận diện rủi ro tại các lớp
*   **Nội dung chính:**
    *   **Lớp Container:** Lỗ hổng (CVE) từ OS/Thư viện mã nguồn mở.
    *   **Lớp CI/CD & IaC:** Lộ lọt Credentials, cấu hình Terraform/Helm mở port trái phép (Misconfiguration).
*   **Hình ảnh:** Icon Hacker chĩa mũi tên vào Registry và Kubernetes cluster.

### Slide 7: Ma trận rủi ro tổng hợp
*   **Tiêu đề:** Rủi ro trọng yếu đối với hệ thống CRM
*   **Nội dung chính:**
    *   Rủi ro nghiêm trọng nhất: Chiếm quyền điều khiển qua lỗ hổng Container và rò rỉ dữ liệu do sai sót cấu hình (IaC).
    *   Hậu quả: Gián đoạn dịch vụ, vi phạm chuẩn bảo mật NHNN.
*   **Hình ảnh:** Ma trận Heatmap (Tập trung nhấn mạnh 1-2 ô màu Đỏ rủi ro cao nhất).

---

## 👩‍💼 THÀNH VIÊN 4: NGUYỄN LINH CHI - GIẢI PHÁP DEVSECOPS PIPELINE (Slide 8 - 10)
**⏱ Thời lượng:** ~3 phút
**🎯 Trọng tâm:** Giải thích luồng 9 bước tự động hoạt động như thế nào.

### Slide 8: Bộ công cụ tích hợp
*   **Tiêu đề:** Công cụ kiểm tra: Trivy, Terrascan & Cosign
*   **Nội dung chính:**
    *   **Trivy:** Quét lỗ hổng Image/Dependency tự động.
    *   **Terrascan:** Phân tích tĩnh mã IaC để tìm lỗi cấu hình.
    *   **Cosign:** Ký số xác thực Image an toàn.
*   **Hình ảnh:** Logo Trivy, Terrascan, Cosign.

### Slide 9: Luồng Pipeline 9 Bước (Quan trọng nhất)
*   **Tiêu đề:** Kiến trúc DevSecOps & Luồng thực thi
*   **Nội dung chính:**
    *   Chỉ trình bày thẳng vào luồng: Code -> CI Pipeline (Trivy quét Image + Terrascan quét IaC) -> Nếu Pass: Ký số (Cosign) -> Đẩy lên Git -> ArgoCD đồng bộ vào Kubernetes.
    *   Security Gate: Chặn ngay lệnh Build nếu Trivy phát hiện lỗi `CRITICAL`.
*   **Hình ảnh:** Sơ đồ luồng Pipeline 9 bước (Hình 3.2).

### Slide 10: Tự động hóa triển khai với GitOps
*   **Tiêu đề:** Vai trò của GitOps (ArgoCD)
*   **Nội dung chính:**
    *   Bảo vệ môi trường Production: ArgoCD chỉ kéo các Image đã được ký số (Cosign verify).
    *   Không ai được can thiệp thủ công vào Kubernetes cluster, mọi thay đổi qua Git.

---

## 👨‍🏫 THÀNH VIÊN 5: TRƯƠNG AN NINH - KẾT LUẬN & Q&A (Slide 11 - 12)
**⏱ Thời lượng:** ~3 phút
**🎯 Trọng tâm:** Khẳng định giá trị đề tài và chốt lại tự tin.

### Slide 11: Đánh giá hiệu quả giải pháp
*   **Tiêu đề:** Hiệu quả & Lợi ích đạt được
*   **Nội dung chính:**
    *   Phát hiện sớm rủi ro (Shift-Left) giúp giảm chi phí sửa lỗi.
    *   Tự động hóa hoàn toàn 100% thay vì kiểm tra thủ công.
    *   Đáp ứng tuân thủ ISO 27001 và yêu cầu NHNN.
*   **Hình ảnh:** Biểu đồ so sánh thời gian fix bug trước và sau khi có DevSecOps.

### Slide 12: Hạn chế & Q&A
*   **Tiêu đề:** Định hướng phát triển & Q&A
*   **Nội dung chính:**
    *   Hạn chế: Cảnh báo giả (False Positives) từ công cụ nguồn mở.
    *   Định hướng: Áp dụng AI phân tích log và OPA quản lý chính sách tập trung.
    *   **Chốt:** *"Phần trình bày của nhóm 5 xin được kết thúc tại đây. Kính mời thầy và các bạn đặt câu hỏi thảo luận!"*
*   **Hình ảnh:** Q&A/Thank you chuyên nghiệp.
