<!-- Slide number: 1 -->

![image.png](GoogleShape84p13.jpg)

BẢO MẬT HỆ THỐNG CRM 1.0 VIETINBANK
Nghiên cứu áp dụng tự động hoá đánh giá an ninh IaC và Container Image bằng Trivy / Terrascan
Nhóm thực hiện: Đỗ Văn Đạt, Trần Ngọc Dũng, Tạ Ngọc Tuệ, Nguyễn Linh Chi, Trương An Ninh
Giảng viên: TS. Vũ Duy Hiến
Hà Nội - 2026

### Notes:

<!-- Slide number: 2 -->

![image.png](GoogleShape96p14.jpg)

![image.png](GoogleShape97p14.jpg)

VietinBank Confidential
Page 02
PHẦN 1: OVERVIEW KIẾN TRÚC
PHẦN 2: TÍCH HỢP & DEMO
Kiến trúc tổng thể 6 lớp (Technical Layers)
Phân tích Stack Công nghệ: Frontend, API, Data
Luồng tích hợp Legacy & Cloud-native
Thách thức bảo mật chuỗi cung ứng
Trivy: Quét SCA, Secrets & Image
Terrascan: Kiểm soát chính sách IaC
Pipeline Hard-Gate & GitOps Flow
Demo: Scenario Phát hiện & Chặn lỗ hổng

![image.png](GoogleShape111p14.jpg)

![image.png](GoogleShape112p14.jpg)

![image.png](GoogleShape113p14.jpg)

![image.png](GoogleShape114p14.jpg)

![image.png](GoogleShape115p14.jpg)

![image.png](GoogleShape116p14.jpg)

![image.png](GoogleShape117p14.jpg)
CHƯƠNG TRÌNH THUYẾT TRÌNH

### Notes:

<!-- Slide number: 3 -->

![image.png](GoogleShape124p15.jpg)

![image.png](GoogleShape125p15.jpg)

PHẦN 1: OVERVIEW KIẾN TRÚC HỆ THỐNG

Phân tích kỹ thuật đa lớp CRM 1.0 VietinBank

### Notes:

<!-- Slide number: 4 -->

![image.png](GoogleShape134p16.jpg)

![image.png](GoogleShape135p16.jpg)

![image.png](GoogleShape136p16.jpg)

![image.png](GoogleShape137p16.jpg)

Mô hình phân lớp tách biệt (Decoupled Layers) đảm bảo khả năng mở rộng và hiệu năng cao cho CRM.
Architecture Overview
Page 04
KIẾN TRÚC TỔNG THỂ CRM 1.0 (TECHNICAL OVERVIEW)

![5b1e7112-5aed-45df-8153-9e39f3b18bc0](GoogleShape144p16.jpg)

### Notes:

<!-- Slide number: 5 -->

![image.png](GoogleShape149p17.jpg)

![image.png](GoogleShape150p17.jpg)

![image.png](GoogleShape152p17.jpg)
HTTPS / TLS 1.2+
Toàn bộ luồng dữ liệu từ Kênh truy cập được mã hóa đầu cuối và kiểm soát phiên (Session) chặt chẽ.
Web Frontend: Xây dựng trên nền tảng NextJS, hỗ trợ Server-side Rendering (SSR) giúp tối ưu trải nghiệm và bảo mật phía Client.
Mobile Access: Cán bộ QHKH truy cập qua Mobile App chuyên dụng, tích hợp SDK bảo mật.
MDM Control: Thiết bị đầu cuối được quản lý bởi Mobile Device Management (MDM) để kiểm soát cấu hình và ngăn chặn Malware.
LỚP KÊNH GIAO DỊCH (ACCESS LAYER)

### Notes:

<!-- Slide number: 6 -->

![image.png](GoogleShape164p18.jpg)

![image.png](GoogleShape165p18.jpg)

![image.png](GoogleShape167p18.jpg)
Thành phần cốt lõi:
IAM / ADFS: Quản lý định danh tập trung, hỗ trợ Single Sign-On (SSO) cho cán bộ nhân viên.
RBAC / ABAC: Kiểm soát truy cập dựa trên vai trò và thuộc tính (Chi nhánh, Phòng ban).
OAuth 2.0 / JWT: Sử dụng Token-based authentication để bảo mật giao tiếp giữa Frontend và API.

![image.png](GoogleShape172p18.jpg)

![image.png](GoogleShape173p18.jpg)

![image.png](GoogleShape174p18.jpg)
LỚP XÁC THỰC & BẢO MẬT ĐỊNH DANH

### Notes:

<!-- Slide number: 7 -->

![image.png](GoogleShape181p19.jpg)

![image.png](GoogleShape182p19.jpg)

![image.png](GoogleShape183p19.jpg)

![image.png](GoogleShape184p19.jpg)

Hệ thống được thiết kế theo kiến trúc Microservices, đóng gói dưới dạng Docker Containers chạy trên nền tảng Red Hat OpenShift.
Shared Services
Auth Service, Notification, File Storage, PDF Generator. Phục vụ các module nghiệp vụ chung.
Business Services
Customer Management, Campaign, Lead/Opportunity, Product Catalog. Xử lý logic nghiệp vụ đặc thù.
Inter-service Comm
Giao tiếp qua REST API (Đồng bộ) và Kafka Event Streaming (Bất đồng bộ).
LỚP DỊCH VỤ CRM (MICROSERVICES LAYER)

### Notes:

<!-- Slide number: 8 -->

![image.png](GoogleShape199p20.jpg)

![image.png](GoogleShape200p20.jpg)

CRM 1.0 đóng vai trò trung tâm, kết nối dữ liệu từ các hệ thống Legacy của VietinBank:

| Hệ thống | Phương thức |
| --- | --- |
| Core Banking | ESB / API Gateway |
| Internet/Mobile Banking | Open API / Kafka |
| Contact Center | SIP / Internal API |
| Loan Origin System (LOS) | SOAP / REST |

![image.png](GoogleShape204p20.jpg)

LỚP TÍCH HỢP NGÂN HÀNG (INTEGRATION)

### Notes:

<!-- Slide number: 9 -->

![image.png](GoogleShape219p21.jpg)

![image.png](GoogleShape220p21.jpg)

![image.png](GoogleShape221p21.jpg)

![image.png](GoogleShape222p21.jpg)

![image.png](GoogleShape223p21.jpg)

![image.png](GoogleShape225p21.jpg)

![image.png](GoogleShape226p21.jpg)
Relational DB
Sử dụng Oracle DB cho các dữ liệu giao dịch trọng yếu và PostgreSQL cho các Microservices mới.

![image.png](GoogleShape229p21.jpg)
In-memory Cache
Redis Cluster được sử dụng để cache thông tin phiên, danh mục sản phẩm nhằm giảm tải cho DB Core.

![image.png](GoogleShape232p21.jpg)
Object Storage
Lưu trữ tài liệu khách hàng, hợp đồng điện tử và các tệp tin đính kèm (ECM/CDM).
LỚP DỮ LIỆU (DATA PERSISTENCE)

### Notes:

<!-- Slide number: 10 -->

![image.png](GoogleShape241p22.jpg)

![image.png](GoogleShape242p22.jpg)

![image.png](GoogleShape244p22.jpg)
Container Orchestration: Sử dụng Red Hat OpenShift để quản lý vòng đời container.
High Availability: Triển khai Multi-AZ, cân bằng tải tại lớp Ingress và Service.
Automation: Toàn bộ hạ tầng được định nghĩa dưới dạng mã (Terraform / K8s Manifests).
HẠ TẦNG CLOUD-NATIVE (INFRASTRUCTURE)

### Notes:

<!-- Slide number: 11 -->

![image.png](GoogleShape254p23.jpg)

![image.png](GoogleShape255p23.jpg)

![image.png](GoogleShape256p23.jpg)

Vấn đề hiện tại
Đề xuất DevSecOps
•
Kiểm tra bảo mật thủ công, tốn thời gian.
•
Lỗ hổng CVE trong thư viện nguồn mở khó kiểm soát.
•
Cấu hình sai Kubernetes (Misconfiguration) tiềm ẩn rủi ro leo thang quyền.
•
Rò rỉ Secrets (API Keys) trong mã nguồn.
•
Tích hợp quét an ninh tự động vào Pipeline CI/CD.
•
Áp dụng Trivy để quét Image & SCA.
•
Áp dụng Terrascan để kiểm tra chính sách IaC.
•
Thiết lập Hard Gate chặn deploy nếu không an toàn.
THÁCH THỨC BẢO MẬT & ĐỀ XUẤT CẢI THIỆN

### Notes:

<!-- Slide number: 12 -->

![image.png](GoogleShape282p24.jpg)

![image.png](GoogleShape283p24.jpg)

PHẦN 2: CHUYÊN SÂU TÍCH HỢP TRIVY & TERRASCAN

Tự động hóa đánh giá an ninh hạ tầng và chuỗi cung ứng

### Notes:

<!-- Slide number: 13 -->
KIẾN TRÚC TỔNG THỂ GIẢI PHÁP BẢO MẬT

![image.png](GoogleShape294p25.jpg)

![image.png](GoogleShape295p25.jpg)
Lớp 1 - Phát triển: Mã nguồn & IaC được quản lý tập trung tại GitLab (Single Source of Truth).

Lớp 2 - CI/CD (Security Gate): Tự động Build & Scan với Trivy (SCA/Image) và Terrascan (IaC). Áp dụng Hard Gate chặn đứng luồng nếu phát hiện lỗi High/Critical. Ký số bằng Cosign.

Lớp 3 - GitOps & Lưu trữ: Image sạch đưa lên Private Registry, Cấu hình Manifest đưa lên GitOps Repo.

Lớp 4 - Triển khai (Runtime): ArgoCD đồng bộ xuống OpenShift. Admission Controller xác thực chữ ký số.

Lớp 5 - Giám sát: Lưu SBOM, Security Reports và WORM Audit Log.

![C:\Users\TueTN\AppData\Local\Microsoft\Windows\INetCache\Content.Word\Kiến trúc giải pháp.png](GoogleShape297p25.jpg)

### Notes:

<!-- Slide number: 14 -->

![image.png](GoogleShape303p26.jpg)

![image.png](GoogleShape304p26.jpg)

Thay vì kiểm tra bảo mật ở giai đoạn cuối, chúng ta đưa bảo mật vào ngay từ bước đầu của vòng đời phát triển (SDLC).

![image.png](GoogleShape307p26.jpg)
TRIẾT LÝ SHIFT-LEFT SECURITY

### Notes:

<!-- Slide number: 15 -->

![image.png](GoogleShape314p27.jpg)

![image.png](GoogleShape315p27.jpg)

![image.png](GoogleShape316p27.jpg)

![image.png](GoogleShape317p27.jpg)

![image.png](GoogleShape318p27.jpg)

![image.png](GoogleShape319p27.jpg)

![image.png](GoogleShape320p27.jpg)

Pipeline được cấu hình tự động (Automation) để thực hiện các bài kiểm tra an ninh mà không cần sự can thiệp của con người.

![image.png](GoogleShape323p27.jpg)

![image.png](GoogleShape324p27.jpg)

![image.png](GoogleShape325p27.jpg)

![image.png](GoogleShape326p27.jpg)
TRIVY
TERRASCAN
LUỒNG PIPELINE GITLAB CI/CD TÍCH HỢP

### Notes:

<!-- Slide number: 16 -->

![image.png](GoogleShape335p28.jpg)

![image.png](GoogleShape337p28.jpg)
Technical Command:
•
Secret Scanning: Phát hiện API Keys, Passwords hardcode trong code.
•
SCA (Software Composition Analysis): Quét lỗ hổng CVE trong các thư viện (Go, NodeJS, Python).
•
Image Scanning: Quét các lớp (Layers) của Docker Image để tìm OS vulnerabilities.
TRIVY: QUÉT SCA, SECRETS & IMAGE

### Notes:

<!-- Slide number: 17 -->

![image.png](GoogleShape351p29.jpg)

![image.png](GoogleShape353p29.jpg)
Technical Command:
•
Kiểm soát các rủi ro trong Kubernetes Manifests.
•
Sử dụng ngôn ngữ Rego (OPA) để định nghĩa các Policy bảo mật.
•
Đảm bảo Best Practices: No-Root, Resource Limits, AppArmor/Seccomp profiles.
TERRASCAN: PHÂN TÍCH IAC MISCONFIGURATION

### Notes:

<!-- Slide number: 18 -->

![image.png](GoogleShape367p30.jpg)

![image.png](GoogleShape368p30.jpg)

![image.png](GoogleShape369p30.jpg)

Logic Dừng Pipeline
Nếu kết quả quét trả về lỗ hổng mức CRITICAL hoặc HIGH, Pipeline sẽ tự động trả về Exit Code 1.
Điều này ngăn chặn việc build image và đẩy lên Container Registry (Harbor).
Exception (Waiver) Flow
Trong trường hợp lỗ hổng chưa có bản vá (Fix version) nhưng cần deploy gấp, bộ phận SecOps sẽ phê duyệt bản ghi .trivyignore có thời hạn.
CƠ CHẾ HARD GATE & FAILING LOGIC

### Notes:

<!-- Slide number: 19 -->

![image.png](GoogleShape382p31.jpg)

![image.png](GoogleShape383p31.jpg)

Đảm bảo Image không bị thay đổi (Tampered) từ lúc Build đến lúc Run.
•
Chỉ Image đã vượt qua tất cả bài test mới được ký số.
•
Sử dụng khóa Private được bảo mật trong GitLab CI.
•
Xác minh chữ ký tại OpenShift Cluster trước khi triển khai.
SUPPLY CHAIN SECURITY: KÝ SỐ COSIGN

### Notes:

<!-- Slide number: 20 -->

![image.png](GoogleShape398p32.jpg)

![image.png](GoogleShape399p32.jpg)

![image.png](GoogleShape401p32.jpg)
•
Single Source of Truth: Mọi cấu hình hạ tầng đều nằm trên Git.
•
Drift Detection: Tự động phát hiện và khôi phục nếu có thay đổi trái phép trên Cluster.
•
Sync Policy: Chỉ đồng bộ các Image đã được xác thực qua Chữ ký số.
GITOPS WORKFLOW: ĐỒNG BỘ QUA ARGOCD

### Notes:

<!-- Slide number: 21 -->

![image.png](GoogleShape414p33.jpg)

![image.png](GoogleShape415p33.jpg)

![image.png](GoogleShape416p33.jpg)

![image.png](GoogleShape417p33.jpg)

Runner
GitLab Runner chạy trên Docker, tích hợp sẵn binary Trivy & Terrascan.
Target
OpenShift Cluster giả lập cho hệ thống CRM Backend.
Policies
Tập luật OPA cho Terrascan: Chặn privileged containers & root users.
CẤU HÌNH MÔI TRƯỜNG DEMO (SETUP)

### Notes:

<!-- Slide number: 22 -->

![image.png](GoogleShape431p34.jpg)

![image.png](GoogleShape432p34.jpg)

![image.png](GoogleShape433p34.jpg)

Kịch bản: Developer  khai báo sử dụng thư viện Java cũ (VD: log4j-core:2.14.1 hoặc Spring Boot phiên bản cũ) trong file pom.xml, hoặc sử dụng Base Image openjdk:8 chứa lỗi bảo mật.
Kết quả:

![image.png](GoogleShape437p34.jpg)
DEMO 1: PHÁT HIỆN & CHẶN LỖ HỔNG CVE

Trivy phân tích pom.xml và .jar, phát hiện lỗ hổng CRITICAL (VD: CVE-2021-44228 - Log4Shell).
Kích hoạt Hard Gate (Exit Code 1) -> Job FAILED.
Ngăn chặn rủi ro RCE (Remote Code Execution) trước khi đẩy lên Registry.

### Notes:

<!-- Slide number: 23 -->

![image.png](GoogleShape445p35.jpg)

![image.png](GoogleShape446p35.jpg)

![image.png](GoogleShape447p35.jpg)

Kịch bản: File deployment.yaml cho phép container chạy với quyền privileged: true.
Kết quả:

![image.png](GoogleShape451p35.jpg)
DEMO 2: SAI CẤU HÌNH K8S MANIFEST

### Notes:

<!-- Slide number: 24 -->

![image.png](GoogleShape458p36.jpg)

![image.png](GoogleShape459p36.jpg)

![image.png](GoogleShape460p36.jpg)

Mean Time to Remediation (MTTR) giảm đáng kể nhờ phát hiện sớm và tự động hóa.

Trước DevSecOps
MTTR: 7 Ngày

Sau DevSecOps
MTTR: 2 Giờ
HIỆU QUẢ KỸ THUẬT MANG LẠI

### Notes:

<!-- Slide number: 25 -->

![image.png](GoogleShape475p37.jpg)

![image.png](GoogleShape476p37.jpg)

![image.png](GoogleShape477p37.jpg)

Kết luận
Tích hợp Trivy & Terrascan vào GitOps không chỉ bảo mật hệ thống CRM mà còn xây dựng văn hóa Security-as-Code tại VietinBank.
Roadmap
•
Nghiên cứu Runtime Security (Falco).
•
Tích hợp AI để dự đoán và tự động vá lỗ hổng (Auto-remediation).
•
Mở rộng mô hình cho toàn bộ 500+ API của VietinBank.
KẾT LUẬN & LỘ TRÌNH KỸ THUẬT

### Notes:

<!-- Slide number: 26 -->

![image.png](GoogleShape494p38.jpg)

Q&A
Trân trọng cảm ơn sự lắng nghe của quý vị!

### Notes: