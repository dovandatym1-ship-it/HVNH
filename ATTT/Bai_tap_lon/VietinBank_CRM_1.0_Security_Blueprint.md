<!-- Slide number: 1 -->
Kiến trúc Bảo mật
Toàn diện CRM 1.0
Bản thiết kế hệ thống
phòng thú cho hệ sinh thái
Cloud-Native Microservices
Đối tượng: Hệ thống Quản lý Quan
hệ Khách hàng (CRM 1.0)
Cơ quan: Ngân hàng TMCP Công
Thương Việt Nam (VietinBank)
риди вле 1008 620
Tổng Bảo vệ API
Hệ thống Giảm sát Liên tục
Lớp Mã hoa Dỡ liệu
MA then tảa vi đên
0NO0NIS81E.0N0
Mà tÔ GtoBlt 01
ala &.ae Do if tin
Al NotebookLM

<!-- Slide number: 2 -->
Nghịch lý Chuyển đổi số: Mở rộng quy mô tỷ lệ thuận với Bề mặt tấn công
Hệ thống CRM 1.0
• Nên tảng: Cloud-Native
Microservices trên
Red Hat OpenShift (OCP)
Red Hat
• Quy mô nhân sự: 11.000+
cán bộ, giao dịch viên, RM
DATABASE
Bề mặt tấn công mở rộng
API GATENAY
• Kiến trúc: Chuyển đổi từ
Monolithic sang phần tán
BANAFS Z
fo-
INTEGRATED PLATFORM
EKPANSION MODULES
BASE SYSTEM
MICROSERVICE A
DATABASE
LEBAY SPSTEM
ERTERNAL
INTERFACE
→ Điểm yếu nội bộ: Lưu lượng
East-West không được kiểm
soát
• Phân mánh: Dữ liệu rải rác
trên PostgreSQL, Oracle, Redis
SCALE NTS
• Giao tiếp: Hàng chục điểm nối
API và Message Queue
MICROSERVICE B
DATABASE
Mục tiêu Chiến lược: Thiết lập kiến trúc bảo mật Assume Breach
(Giả định thất bại) trên mọi ranh giới tin cậy.
(3022 18523 70
SCALE NTS
PR8JECT:
HBAKUKSATKN
SHEET NO:
A_100
9 NotebookLM

<!-- Slide number: 3 -->
+
SCALE NTS
Tam giác CIA Triad được ánh xạ vào thực tiễn Dữ liệu CRM 1.0
Tính Bí mật
(Confidentiality)
Tài sản
CCCD, điểm tín dụng CIC,
số dư tài khoản
Mối đe dọa
Nghe lén, đánh cắp danh
tính, Phishing
Giải pháp
Mã hóa AES-256, kiểm
soát ngữ cảnh (ABAC)
Tính Toàn vẹn
(Integrity)
Tài sản
Luồng dữ liệu CDC
đồng bộ real-time
Mối đe dọa
SQL Injection, lạm dụng
quyền nội bộ
Giải pháp
Chữ ký số, Nhật ký kiểm
toán bất biến (WORM)
Tính Sẵn dùng
(Availability)
Tài sản
Uptime hệ thống trong giờ
giao dịch (8:00-17:00)
Mối đe dọa
DDoS, lỗi dây chuyền từ
Core Banking
Giải pháp
Circuit Breaker, Rate
Limiting, WAF
Mục tiêu Chiến lược: Thiết lập kiến trúc bảo mật Assume Breach
(Giả định thất bại) trên mọi ranh giới tin cậy.
+
SCALE NTS
PROJECT:
CASNATIN
SHEST NO:
1_100
n NotebookLM

<!-- Slide number: 4 -->
+
Phòng vệ có chiêu sâu (Defense in Depth) trên 7 Vùng Hạ tâng
→ 1. Vùng Người dùng: 11.000+ CBNV
> 2. Vùng Máy trạm: EDR, BitLocker
> 3. Vùng LAN: 802.1X, VLAN
4. Vung LAN-to-WAN: WAF, DDOS Scrubber
> 5. Vùng WAN: TLS 1.3, VPN
+ 6. Vùng Truy cập từ xa: ZTNA, MFA
>> 7. Vùng Hệ thống/Ứng dụng: OCP,
Microservices, CSDL
Ranh giới tin cậy (Trust Boundary):
Ranh giới tin cậy (Trust Boundary):
Mọi thông tin di chuyển qua các vùng
phải đối mặt với các trạm kiểm soát
Zero Trust độc lập.
SCALE NTS
Mục tiêu Chiến lược: Thiết lập kiến trúc bảo mật Assume Breach
(Giả định thất bại) trên mọi ranh giới tin cậy.
SCALE NTS
FROJECT:
SHEST NO:
1_100
9 NotebookLM

<!-- Slide number: 5 -->
Quy trình Nhận diện Rủi ro theo chuẩn NIST SP 800-30
Giai đoạn Chẩn đoán
Giai đoạn Đánh giá
Giai đoạn Kề đơn
3
6
Mô tả
hệ thống
Nhận diện
đe dọa
Nhận diện
lỗ hồng
Phân tích
kiểm soát
Đánh giá
xác suất
Phần tích
tác động
Xác định
mức độ rúi ro
Đề xuất
biện pháp
Lập tài liệu
ISMS
SEALE NTS
Công thức: Rủi ro = Xác suất xảy ra đe dọa (Likelihood)
x Mức độ tổn hại (Impact)
SCALE NTS
JoN Ust vor
FROJECT:
NTAN
CANNENATY
3NSST NO:
1_100
n NotebookLM

<!-- Slide number: 6 -->
+
SCALE NTS
Giải phẫu Kiến trúc Phân tán CRM 1.0
API Gateway
NextJS v.14
(Front-end)
(Single Entry Point)
Apache Kafka
(Bất đông bộ)
Tăng Phần mềm
& Middleware
Red Hat OpenShift
(OCP)
Các Container
Microservices độc lập
Tầng Tính toán
(Compute)
Giao tiếp đồng bộ
(Tight Coupling)
Tâng Phân cứng
& Dữ liệu
PostgreSQL
& Oracle (SAN)
S3 WORM
(Bất biến)
Redis
(In-memory)
Legacy Core Banking
sey Ust voro
SCALE NTS
FROJECT:
VESITAL
3NSST NO:
1_102
9 NotebookLM

<!-- Slide number: 7 -->
[R10] Phishing:
Lừa đào thông tin đăng nhập
của nhân viên qua email
Internet /
Ngoại vi
+
Lập bản đồ Rủi ro (Phần 1): Vùng Người dùng và Ranh giới mạng
[R05] Tấn công DDoS:
Làm ngập lụt kênh iPay/eFast
API (Điểm: 15/25)
[RO2] Tấn công SQL/API
Injection:
Xuyên thủng API Gateway
(Điểm: 20/25)
[R09] Shoulder Surfing:
Nhìn trộm màn hình máy
trạm tại chi nhánh
+
Mạng Nội bộ
[R06] Rò ri Token JWT:
Đánh cấp phiên qua token
không hết hạn
SSETBR A-10A
[R01] Lạm dụng quyền nội bộ:
Cán bộ truy xuất trái phép dữ
liệu CIC
(Điểm: 20/25)
SCALE NTS
eY UTLI vory
SCALE NTS
FRUVECT:
VORML
TEUNN CENATION
OWST NO-
9 NotebookLM

<!-- Slide number: 8 -->
Lập bản đồ Rủi ro (Phần 2): Bề mặt tấn công Microservices
[R04] Di chuyển ngang
(East-West): Giao tiếp
giữa các Pod không xác
thực (Điểm: 15/25)
2000
OpenShift
[R07] Không nhất quán dữ liệu:
Giao dịch thất bại giữa chừng
trên nhiều CSDL phân tán
(Điểm: 12/25)
1 8
[R08] Tấn công Chuồi cung
ung (Supply Chain):
Lô hông tiêm nhiêm từ
Docker images trong CI/CD
(Điểm: 12/25)
Lập bản đồ Rùi ro
(Phăn 2); Bè mặt tần công Microservices
Project: Franno Couctin, Nev ffaies
Date: 12/27/23
Al NotebookLM

<!-- Slide number: 9 -->
Hiệu ứng Domino: Mối đe dọa từ Hệ thống Legacy [R03]
Trạng thái 1: Bình thường
1000*
Trạng thái 2: Nghẽn cổ chai
1000'
Trạng thái 3: Cascading Failure
2000*
Connection limits
CRM
40
Core
Banking
76
100
180
CRM
CRM
Core
Banking
Gọi API đồng bộ.
Thời gian phản hồi < 200ms.
Latency c 3 connection limits
Core Banking quá tái.
Các microservice CRM bị treo,
chờ phản hồi.
1000'
Cạn kiệt Thread Pool.
Toàn bộ CRM đóng băng,
gây sụp đố hệ thổng
(Điểm: 16/25).
Nguyên nhân cốt lỗi: Khuyết thiếu cơ chế ngắt mạch tự động trong giao tiếp phân tán.
SCALE NTS
SCALE XTS
UOYUTLOTVOY
TRUVECT:
vei ML
TEUNN CENATION
OMST NO-
9 NotebookLM

<!-- Slide number: 10 -->
Xác suất (1-5)
Ma trận Rủi ro Tổng hợp: Đánh giá và Ưu tiên
12
R08: Supply Chain
R10: Phishing
9
R09: Shoulder
Surfing
20
R01: Lạm dụng
nội bộ (20)
12
R06: JWT Abuse
R07: Dữ liệu không
nhất quán
12
R04: Di chuyển
ngang (15)
20
R02: SQL/API
Injection (20)
16
R03: Cascading
Failures (16)
15
R05: Tấn công
DDOS (15)
498
Tác động (1-5)
Project: Franno Couctin, New ffaies
Date: 12/27/23
Al NotebookLM

<!-- Slide number: 11 -->
SCALE NTS
Thiết kế Phòng vệ: Mô hình Mạng 3-Tier Nghiêm ngặt
15000
PROJECT
DATE
Tier 1: Vùng DMZ
(Demilitarized Zone)
Chức nang: Lọc lưu lượng Internet
(iPay, eFast). Không có kết nối trực tiếp
vào mạng nội bộ.
WAF
DDoS Scrubber
Load Balancer
Tier 2: Vùng Application
(Internal Network)
Chức năng: Chạy API Gateway và
OCP Worker Nodes.
<op>
reode
code>
NetworkPolicy (Default-Deny)
Runtime Security
Tier 3: Vùng Database
(Isolated Zone)
Chức năng: Lưu trữ CSDL lỗi phân tán.
PORT
3083
PostgreSQL
Oracle
Whitelist IP/Port
SCALE NTS
PROJECT
DATE
AAKG
A-106
Al NotebookLM

<!-- Slide number: 12 -->
Zero Trust Nội bộ: mTLS và Istio Service Mesh
Mô hình Cũ (Lỗ hổng R04)
Mô hình Mới (Giải pháp mTLS STRICT)
Envoy
Proxy
Sidecar
Envoy
Proxy
Sidecar
Container Node
Container Node
Container Node
Container Node
Giao tiếp Plain-text. Nếu một container bị xâm nhập, kẻ tẫn
công tự do di chuyển ngang (Lateral Movement).
- Xác thực 2 chiều: Client và Server xác minh chứng chỉ số
- Trong suốt: Envoy tự động mã hóa/giải mã.
- Authorization Policy: Giới hạn nghiêm ngặt quyền gọi API.
Project: Franno Couctin, New ffaies
Date: 12/27/23
A) NotebookLM

<!-- Slide number: 13 -->
Chiến lược Mã hóa Đa tầng & Bảo vệ Quyền riêng tư
Data at Rest
(Lưu trữ)
Data in Transit
(Truyền tải)
Data in Use
(Giao diện)
VONG HOA AÂN NOI YSH VIỆT NAM
DEo te1.101s - 10050 0140
CCCD VIỆT NAM
30-000-
bata conroccol
0380****1234
************
S1:01 61109
- Tầng Đĩa: Khóa AES-256-XTS.
- Tầng CSDL: Transparent Data
Encryption (TDE) cho
PostgreSQL/Oracle.
- Tầng Ứng dụng: Mã hóa cột riêng
biệt cho CCCD/Mã PIN với HSM.
- Giao thức: Bắt buộc TLS 1.3
toàn hệ thống.
- Mạng nội bộ: Mã hóa kênh
Kafka Broker.
- Ưng dụng: Certificate Pinning
chống Man-in-the-Middle.
- Che mờ động (Data Masking) trên
giao diện (VD: 0380****1234).
- Ghi Audit Log bất biến ngay khi
nhấn "Hiển thị".
- Xử lý rui ro R09: Shoulder Surfing.
Project: Frannc Couctin, New ffaies
Date: 12/27/23
A) NotebookLM

<!-- Slide number: 14 -->
Quản lý Định danh: SSO, JWT và Kiểm soát Ngữ cảnh
- OIDC/OAuth2 qua Keycloak/Entra ID.
→ - Tuổi thọ Access Token (JWT): Chỉ 30 phút.
- Xử lý R06/R10.
Lớp 1: Xác thực (SSO + MFA)
Lớp 2: Bộ lọc thô
(RBAC tại API Gateway)
Lớp 3: Bộ lọc mịn
(ABAC tại Logic & CSDL)
- Kiểm tra Vai trò (Role).
- VD: Giao dịch viên không được gọi API
tín dụng.
- Đánh giá ngữ cảnh: Giờ làm việc + IP nội bộ
+ Danh mục khách hàng.
- Row-Level Security (RLS): Chặn truy cập
trái phép ngay tại cấp CSDL.
- Chống rủi ro R01 (Lạm dụng nội bộ).
Project: Frannc Couctin, New ffaies
Date: 12/27/23
A NotebookLM

<!-- Slide number: 15 -->
Sức bền Phân tán: Circuit Breaker & Saga Pattern
Ngắt mạch tự động - Circuit Breaker (Xử lý R03)
Nhất quán dữ liệu - Saga Pattern (Xử lý RO7)
Lỗi > 50%
CLOSED
(Bình thường),
Microservice 1
Microservice 2
Microservice 3
OPEN
(Ngắt mạch)
Kafka
Events
Kafka
Events
HALF-OPEN
(Thử nghiệm)
Timeout
• Tránh cạn kiệt thread pool. Chuyển sang
Degraded Mode thay vì sụp đổ hoàn toàn.
Compensating Transaction (Hoàn tác)
, • Tự động kích hoạt luồng 'Undo' để giữ nguyên
trạng thái nếu một bước giao dịch thất bại.
Project: Frannc Couctin, New ffaies
Date: 12/27/23
Al NotebookLM

<!-- Slide number: 16 -->
Ma trận Tổng hợp: Từ Rủi ro đến Giải pháp
RỦI RO (DIAGNOSTIC)
R01: Lạm dụng nội bộ
RO2: API Injection
RO3: Cascading Failures
R04: Lateral Movement
R06: Token Abuse
RO7: Data Inconsistency
GIẢI PHÁP (PRESCRIPTION)
ABAC + PostgreSQL RLS + Data Masking
(Hạ xuống mức Thấp)
Mô hình 3-Tier + WAF OWASP (Hạ xuống mức Thấp)
Circuit Breaker Pattern (Hạ xuống mức Trung Bình)
mTLS + Istio STRICT Mode (Hạ xuống mức Thấp)
JWT TTL 30 phút + Revocation (Hạ xuống mức Rất Thấp)
Saga Pattern + Kafka Transactions (Hạ xuống mức Thấp)
1 00% rủi ro nghiêm trọng đã được kiểm soát bằng các chốt chặn kỹ thuật.
Project: Frannc Couctin, New ffaies
Date: 12/27/23
Al NotebookLM

<!-- Slide number: 17 -->
Động cơ Quản trị ISMS: Chu trình PDCA (ISO/IEC 27001)
ACT (Cải tiến)
• Phân tích nguyên nhân gốc
rế (Root Cause Analysis).
• Cập nhật chính sách.
PLAN (Lập kế hoạch)
• Cập nhật Threat Model.
• Xây dựng Risk Treatment
Plan trước các đợt release.
CHECK (Kiểm tra)
• Internal Audit 6 tháng/lần.
• PenTest hàng năm.
• Giám sát MTTD/MTTR qua
SIEM.
DO (Thực hiện)
• Triển khai kiến trúc kỹ thuật.
• Đào tạo nhận thức 11.000+
nhân sự.
Project: Frannc Couctin, New ffaies
Date: 12/27/23
Al NotebookLM

<!-- Slide number: 18 -->
Tích hợp DevSecOps: Bảo mật Tự động Shift-Left
Giai đoạn CODE
• Quét SAST real-time qua
SonarLint trên IDE.
' Giai đoạn PACKAGE
• Quét lỗ hổng Docker Image bằng
Trivy/Clair. Ký số bằng Cosign
(Chống R08).
@ Giai đoạn RUNTIME
• Giám sát bằng Falco trên
OpenShift để phát hiện hành vi
container bát thường.
Giai đoạn BUILD
• SonarQube quét toàn bộ
source code. Fail build
nếu có lỗi Critical.
Project: Frannc Couctin, New ffaies
Date: 12/27/23
Al NotebookLM

<!-- Slide number: 19 -->
Trust but Verif: Hệ thống Audit Log WORM & Quản trị Con người
Khía cạnh Kỹ thuật: Audit Log Bất biến
Khía cạnh Con người: Đạo đức & Văn hóa
POLICY
Arn
• Moi thao tác xem/sứa được lưu trực tiếp vào tù đĩa S3 WORM
• Bảo vệ bằng Hash Chain (SHA-256 kiểu blockchain).
• Lưu trữ tối thiểu 5 năm, quản trị viên IT không thể xóa sửa.
• Đào tạo Phishing Simulation định kỳ (yêu cầu >80% điểm).
• Bộ Quy tắc Ứng xử (Code of Conduct) với chế tài kỷ luật
nghiêm ngặt.
• Chính sách Clean Desk & Screen lock tự động.
Project: Frannc Couctin, New ffaies
Date: 12/27/23
Al NotebookLM

<!-- Slide number: 20 -->
Khung Tuân thủ Pháp luật Việt Nam cho Dữ liệu Ngân hàng
Luật ATTT Mạng
(86/2015) - Điều 17
Yêu cầu: Bảo vệ dữ liệu cá
nhân nhạy cảm.
Kiến trúc: Áp dụng mã hóa
AES-256, ABAC, và Data
AES-256
Masking.
Luật An ninh mạng
(24/2018) - Điều 26
Nghị định
13/2023/NĐ-CP
COMPLANCE
8
Yêu cầu: Lưu trữ dữ liệu
trong nước (Data
Localization).
Yêu cầu: Đánh giá DPIA,
thông báo vi phạm
trong 72h.
Kiến trúc: OpenShift Cluster
& S3 WORM vận hành 100%
tại Data Center nội địa.
Kiến trúc: Bổ nhiệm DPO, tích
hợp SIEM để phát hiện và
cảnh báo sư cố tức thời.
Project: Frannc Couctin, New fiaies
Date: 12/27/23
Al NotebookLM

<!-- Slide number: 21 -->
Kiến trúc Bảo mật Hợp nhất: Nền tảng cho Kỷ nguyên Open Banking
Chính sách ISMS, DevSecOps & Tuân thủ Pháp luật
Mạng 3-Tier: DMZ (WAF), Application, Database
Lõi Microservices: Xác thực
mTLS, Circuit Breaker
Tài sản: Mã hóa Đa tầng
& WORM Audit
Bảo mật trong CRM 1.0 là một hệ miễn dịch động
- tự nhận thức, tự phòng vệ, và sẵn sàng thích nghi
trước mọi thách thức của môi trường tài chính số.
Project: Frannc Couctin, New faies
Date: 12/27/23
A) NotebookLM

