# BÀI TẬP LỚN CUỐI KỲ

## NGHIÊN CỨU, ĐÁNH GIÁ RỦI RO VÀ ĐỀ XUẤT KIẾN TRÚC BẢO MẬT TOÀN DIỆN CHO HỆ THỐNG QUẢN LÝ QUAN HỆ KHÁCH HÀNG (CRM 1.0) TẠI NGÂN HÀNG TMCP CÔNG THƯƠNG VIỆT NAM (VIETINBANK)

**Môn học:** An toàn thông tin trong Hệ thống thông tin quản lý  
**Học viên:** [Họ và tên]  
**Lớp:** Cao học Hệ thống thông tin quản lý  
**Năm học:** 2025 – 2026  

---

## LỜI MỞ ĐẦU

### 1. Tính cấp thiết của đề tài

Trong bối cảnh chuyển đổi số diễn ra với tốc độ chưa từng có, hệ thống tài chính – ngân hàng Việt Nam đang đứng trước những thách thức bảo mật thông tin vừa cấp bách, vừa phức tạp hơn bất kỳ thời điểm nào trong lịch sử. Theo báo cáo của Cục An toàn thông tin – Bộ Thông tin và Truyền thông, trong giai đoạn 2022–2024, lĩnh vực tài chính – ngân hàng liên tục nằm trong nhóm các ngành bị tấn công mạng nhiều nhất, với số lượng sự cố được ghi nhận tăng trưởng bình quân trên 35% mỗi năm. Các hình thức tấn công ngày càng tinh vi, từ các chiến dịch APT (Advanced Persistent Threat) nhắm vào hệ thống lõi, cho đến các kỹ thuật khai thác API, đánh cắp phiên đăng nhập và lạm dụng quyền hạn nội bộ.

**Ngân hàng TMCP Công Thương Việt Nam (VietinBank)**, với mạng lưới hơn 150 chi nhánh, hơn 1.000 phòng giao dịch và đội ngũ hơn 25.000 nhân viên, đang vận hành một trong những hệ sinh thái công nghệ thông tin quy mô nhất trong khối ngân hàng thương mại trong nước. Trong chiến lược hiện đại hóa hạ tầng công nghệ giai đoạn 2022–2025, VietinBank đã triển khai **Hệ thống Quản lý Quan hệ Khách hàng phiên bản 1.0 (CRM 1.0)** theo kiến trúc **Cloud-Native Microservices** trên nền tảng **Red Hat OpenShift Container Platform (OCP)**. Đây là một cuộc cách mạng về mặt kiến trúc phần mềm, chuyển đổi hoàn toàn từ mô hình nguyên khối (Monolithic Architecture) sang mô hình dịch vụ vi phân tán, nhằm đạt được khả năng mở rộng linh hoạt, tốc độ triển khai cao và hiệu quả vận hành vượt trội.

Tuy nhiên, mọi sự chuyển đổi kiến trúc đều mang theo những **rủi ro bảo mật đặc thù và mới nổi**. Hệ thống CRM 1.0 của VietinBank lưu trữ và xử lý thông tin của hàng chục triệu khách hàng cá nhân và doanh nghiệp, bao gồm dữ liệu định danh (CCCD, hộ chiếu), thông tin tài chính (số dư, lịch sử giao dịch), hồ sơ tín dụng CIC (Credit Information Centre) và hàng loạt dữ liệu nhạy cảm khác. Sự rò rỉ, sai lệch hay gián đoạn trong việc truy cập các dữ liệu này không chỉ gây thiệt hại tài chính trực tiếp mà còn ảnh hưởng nghiêm trọng đến uy tín thương hiệu và niềm tin của khách hàng – vốn là tài sản cốt lõi của bất kỳ tổ chức tín dụng nào.

Kiến trúc Microservices, dù mang lại nhiều lợi thế về kỹ thuật, đồng thời cũng mở ra một **bề mặt tấn công (Attack Surface) rộng hơn và phức tạp hơn**: hàng chục đầu điểm API cần được bảo vệ; dữ liệu phân tán trên nhiều loại cơ sở dữ liệu (PostgreSQL, Oracle, Redis) đòi hỏi chiến lược bảo mật nhất quán; giao tiếp dịch vụ nội bộ qua Message Queue (Apache Kafka) có thể trở thành điểm yếu nếu không được mã hóa và xác thực nghiêm ngặt; và sự phụ thuộc vào hệ thống di sản (Legacy Core Banking) tạo ra những điểm nghẽn cổ chai không dễ xử lý.

Trước thực tiễn đó, **việc nghiên cứu một cách hệ thống các rủi ro bảo mật và đề xuất một kiến trúc bảo mật toàn diện, phù hợp với đặc thù kiến trúc của hệ thống CRM 1.0 tại VietinBank là nhiệm vụ vừa có giá trị học thuật, vừa có ý nghĩa ứng dụng thực tiễn cao**. Đây chính là lý do cốt lõi thôi thúc tác giả lựa chọn và theo đuổi đề tài này.

### 2. Mục tiêu nghiên cứu

Bài tập lớn này hướng tới ba mục tiêu nghiên cứu chính, có mối quan hệ logic và kế thừa lẫn nhau:

**Mục tiêu 1:** Hệ thống hóa các kiến thức lý thuyết nền tảng về An toàn thông tin doanh nghiệp, bao gồm mô hình CIA Triad, nguyên tắc Phòng vệ chiều sâu (Defense in Depth), phương pháp đánh giá rủi ro 9 bước và các công nghệ bảo mật lõi, làm cơ sở lý luận vững chắc cho toàn bộ bài viết.

**Mục tiêu 2:** Phân tích hiện trạng kiến trúc kỹ thuật của hệ thống CRM 1.0 tại VietinBank theo góc nhìn đa chiều (hạ tầng phần cứng, phần mềm, dữ liệu), sau đó nhận diện và đánh giá định tính các rủi ro bảo mật tiềm ẩn tương ứng với từng vùng hạ tầng CNTT của hệ thống.

**Mục tiêu 3:** Trên cơ sở các rủi ro đã được nhận diện, đề xuất một kiến trúc bảo mật đa lớp cụ thể, bao gồm các giải pháp kỹ thuật (mã hóa, kiểm soát truy cập, bảo mật API, xử lý lỗi phân tán) và các chính sách quản trị (ISMS theo ISO/IEC 27001, DevSecOps, tuân thủ pháp luật Việt Nam) nhằm bảo vệ toàn diện hệ thống CRM 1.0.

### 3. Đối tượng và Phạm vi nghiên cứu

**Đối tượng nghiên cứu:** Kiến trúc bảo mật thông tin và các giải pháp kỹ thuật, quản trị đảm bảo an toàn thông tin cho hệ thống thông tin doanh nghiệp trong lĩnh vực ngân hàng.

**Phạm vi nghiên cứu:** Bài viết tập trung vào **Hệ thống CRM 1.0 (giai đoạn MVP1)** của VietinBank, bao gồm toàn bộ stack công nghệ từ lớp Front-end (NextJS v.14), lớp trung gian (API Gateway, Apache Kafka), lớp ứng dụng vi dịch vụ (chạy trên Red Hat OpenShift), đến lớp dữ liệu (PostgreSQL, Oracle, Redis, lưu trữ S3). Phạm vi bảo mật được xem xét trải dài từ điểm truy cập của người dùng cuối (hơn 11.000 cán bộ, giao dịch viên) đến hạ tầng lưu trữ dữ liệu tập trung, bao gồm cả điểm tích hợp với Core Banking và các kênh số đối ngoại (iPay, eFast). Đề tài không đi sâu vào chi tiết triển khai phần cứng vật lý (data center) hay kiến trúc hạ tầng mạng WAN của VietinBank, mà tập trung vào tầng bảo mật ứng dụng và dữ liệu.

### 4. Phương pháp nghiên cứu

Bài viết sử dụng phương pháp **nghiên cứu định tính kết hợp phân tích hệ thống**, cụ thể:

- **Phương pháp phân tích tài liệu:** Tổng hợp và hệ thống hóa kiến thức từ giáo trình môn học An toàn thông tin, các tiêu chuẩn quốc tế (ISO/IEC 27001, NIST SP 800-30) và tài liệu kỹ thuật của hệ thống CRM 1.0 VietinBank.
- **Phương pháp tiếp cận theo mô hình:** Vận dụng mô hình **Phòng vệ chiều sâu (Defense in Depth)** làm khung phân tích và thiết kế kiến trúc bảo mật; vận dụng **phương pháp đánh giá rủi ro kết hợp (Combined Approach)** để nhận diện và lượng giá rủi ro trên từng vùng hạ tầng.
- **Phương pháp đối chiếu thực tiễn:** Đối chiếu kiến trúc thực tế của CRM 1.0 với các best-practice bảo mật trong ngành công nghiệp phần mềm tài chính, từ đó xây dựng các đề xuất có tính khả thi và phù hợp với đặc thù môi trường vận hành.

---

## CHƯƠNG 1: CƠ SỞ LÝ THUYẾT VỀ AN TOÀN THÔNG TIN TRONG HỆ THỐNG DOANH NGHIỆP

### 1.1. Tổng quan về An toàn thông tin

#### 1.1.1. Khái niệm An toàn thông tin

**An toàn thông tin (Information Security – ATTT)** là một lĩnh vực khoa học và thực hành rộng lớn, tập trung vào việc bảo vệ thông tin và hệ thống thông tin khỏi sự truy cập trái phép, sử dụng sai mục đích, tiết lộ ngoài ý muốn, gián đoạn hoạt động, sửa đổi bất hợp pháp hoặc phá hủy. Theo định nghĩa của Viện Tiêu chuẩn và Công nghệ Quốc gia Hoa Kỳ (NIST), ATTT là "việc bảo vệ thông tin và hệ thống thông tin khỏi truy cập, sử dụng, tiết lộ, gián đoạn, sửa đổi, hoặc phá hủy trái phép nhằm đảm bảo tính bí mật, toàn vẹn và sẵn dùng."

Trong môi trường ngân hàng hiện đại, ATTT không còn là vấn đề thuần túy kỹ thuật mà đã trở thành một **yếu tố chiến lược kinh doanh**. Một sự cố bảo mật không chỉ gây thiệt hại tài chính trực tiếp (chi phí khắc phục, bồi thường) mà còn kéo theo hệ lụy pháp lý (vi phạm luật bảo vệ dữ liệu cá nhân), thiệt hại thương hiệu và mất niềm tin từ khách hàng – những thiệt hại vô hình nhưng có thể còn nghiêm trọng hơn về dài hạn.

Hệ thống thông tin dựa trên máy tính, về bản chất, bao gồm năm thành phần cốt lõi có mối quan hệ tương tác chặt chẽ: **(1) Phần cứng (Hardware)** – bao gồm máy chủ, thiết bị lưu trữ, thiết bị mạng; **(2) Phần mềm (Software)** – hệ điều hành, ứng dụng, middleware; **(3) Dữ liệu (Data)** – tài nguyên cần bảo vệ quan trọng nhất; **(4) Con người (People)** – người dùng, quản trị viên, nhà phát triển; và **(5) Quy trình (Procedures)** – chính sách vận hành và kiểm soát. Bất kỳ điểm yếu nào trong một trong năm thành phần trên đều có thể trở thành cánh cửa để kẻ tấn công khai thác, do đó, một chiến lược ATTT toàn diện phải xem xét và bảo vệ đồng thời cả năm lớp này.

#### 1.1.2. Tam giác CIA Triad – Nền tảng lý thuyết của An toàn thông tin

Mô hình **CIA Triad** (Confidentiality – Integrity – Availability) là nền tảng lý thuyết căn bản và bất biến của khoa học An toàn thông tin. Ba thuộc tính này không chỉ là khái niệm lý thuyết trừu tượng mà còn là **tiêu chí đo lường thực tiễn** để đánh giá mức độ bảo mật của bất kỳ hệ thống thông tin nào. Mỗi quyết định kiến trúc bảo mật, mỗi chính sách kiểm soát hay mỗi giải pháp kỹ thuật đều có thể và cần được lý giải dựa trên một hoặc nhiều thuộc tính trong bộ ba này.

**Bảng 1.1: Phân tích CIA Triad và áp dụng vào hệ thống CRM 1.0 – VietinBank**

| Thuộc tính | Định nghĩa kỹ thuật | Mối đe dọa điển hình | Áp dụng cụ thể tại CRM 1.0 VietinBank |
|---|---|---|---|
| **Tính Bí mật (Confidentiality)** | Đảm bảo thông tin chỉ được tiếp cận bởi những chủ thể được phép; ngăn chặn mọi hình thức tiết lộ trái phép | Nghe lén đường truyền (Eavesdropping), đánh cắp thông tin xác thực (Credential Theft), tấn công Man-in-the-Middle, rò rỉ dữ liệu qua API không được bảo vệ | Hơn 11.000 cán bộ có thể truy cập dữ liệu khách hàng; thông tin CCCD, CIC, số dư tài khoản cần được mã hóa và kiểm soát hiển thị theo vai trò |
| **Tính Toàn vẹn (Integrity)** | Đảm bảo thông tin và quy trình xử lý không bị sửa đổi trái phép, dữ liệu luôn chính xác và đáng tin cậy theo thời gian | Tấn công SQL Injection làm sai lệch dữ liệu, gian lận nội bộ thay đổi hồ sơ khách hàng, lỗi đồng bộ trong giao dịch phân tán | Giao dịch CDC đồng bộ dữ liệu real-time từ Core Banking sang CRM phải đảm bảo không bị can thiệp; hồ sơ tín dụng CIC phải có chữ ký số xác nhận tính gốc |
| **Tính Sẵn dùng (Availability)** | Đảm bảo hệ thống và dữ liệu luôn sẵn sàng phục vụ cho các chủ thể được phép, vào đúng thời điểm cần thiết | Tấn công từ chối dịch vụ DDoS, sự cố kỹ thuật (cascading failures), lỗi phần cứng không có phương án dự phòng | Hệ thống CRM phải đảm bảo uptime cao trong giờ giao dịch ngân hàng (8:00–17:00); nghẽn cổ chai do hệ thống Legacy Core Banking treo có thể làm toàn bộ CRM ngừng hoạt động |

**Tính Bí mật (Confidentiality)** là thuộc tính đề cập đến quyền kiểm soát thông tin – ai được phép biết điều gì. Trong ngữ cảnh ngân hàng, đây là thuộc tính nhạy cảm nhất vì dữ liệu khách hàng thuộc loại **Dữ liệu Cá nhân Nhạy cảm (Sensitive Personal Data)** được bảo vệ bởi pháp luật. Tính bí mật không chỉ bị đe dọa từ bên ngoài (tin tặc) mà còn từ bên trong (insider threats): một giao dịch viên có thể truy xuất thông tin tài chính của khách hàng không thuộc phạm vi phục vụ của mình, hoặc một nhân viên rời việc nhưng tài khoản truy cập chưa bị thu hồi. Kỹ thuật bảo vệ tính bí mật bao gồm mã hóa dữ liệu, kiểm soát truy cập theo vai trò (RBAC), che mờ dữ liệu (Data Masking) và phân vùng mạng (Network Segmentation).

**Tính Toàn vẹn (Integrity)** đề cập đến sự chính xác, nhất quán và đáng tin cậy của dữ liệu trong suốt vòng đời của nó. Một hệ thống có thể bí mật hoàn hảo nhưng vẫn bị xem là không an toàn nếu dữ liệu có thể bị sửa đổi mà không để lại dấu vết. Trong kiến trúc Microservices của CRM 1.0, tính toàn vẹn đối mặt với thách thức đặc thù là **tính nhất quán phân tán (Distributed Consistency)**: khi một giao dịch kinh doanh trải dài trên nhiều microservices và nhiều cơ sở dữ liệu, làm thế nào để đảm bảo hoặc tất cả các phần thay đổi cùng được áp dụng thành công, hoặc tất cả cùng bị hủy – không xảy ra trạng thái dở dang, không nhất quán? Công nghệ bảo vệ toàn vẹn bao gồm hàm băm mật mã (SHA-256), chữ ký số (Digital Signature), giao thức giao dịch phân tán (2PC, Saga Pattern) và nhật ký kiểm toán chống giả mạo (WORM Audit Log).

**Tính Sẵn dùng (Availability)** đảm bảo hệ thống luôn phục vụ được khi người dùng hợp pháp cần. Đây là thuộc tính thường bị đánh giá thấp trong các thiết kế bảo mật truyền thống, nhưng lại cực kỳ quan trọng trong môi trường ngân hàng vì gián đoạn dịch vụ dù chỉ vài phút cũng có thể gây thiệt hại hàng trăm triệu đồng và ảnh hưởng trực tiếp đến hàng nghìn giao dịch tài chính. Tính sẵn dùng bị đe dọa không chỉ bởi các cuộc tấn công chủ động (DDoS) mà còn bởi các lỗi kỹ thuật (cascading failures trong kiến trúc Microservices) và thiên tai. Các biện pháp bảo vệ bao gồm thiết kế dự phòng (Redundancy), cân bằng tải (Load Balancing), Circuit Breaker Pattern và kế hoạch khôi phục sau thảm họa (Disaster Recovery Plan).

Ba thuộc tính CIA không tồn tại độc lập mà có **mối quan hệ đánh đổi (Trade-off) tinh tế**: tăng cường tính bí mật (ví dụ, thêm nhiều lớp xác thực) có thể làm giảm tính sẵn dùng (người dùng mất nhiều thời gian đăng nhập hơn); tăng cường tính sẵn dùng (ví dụ, nhân bản dữ liệu ra nhiều node) có thể làm tăng nguy cơ rò rỉ bí mật (nhiều điểm lưu trữ hơn = nhiều điểm có thể bị tấn công). Năng lực của một kiến trúc sư bảo mật chính là ở khả năng **tìm kiếm điểm cân bằng tối ưu** giữa ba thuộc tính này, phù hợp với yêu cầu nghiệp vụ và mức độ chấp nhận rủi ro của tổ chức.

---

### 1.2. Mô hình tổng quát đảm bảo An toàn thông tin

#### 1.2.1. Nguyên tắc Phòng vệ nhiều lớp có chiều sâu (Defense in Depth)

**Phòng vệ nhiều lớp có chiều sâu (Defense in Depth – DiD)** là một trong những nguyên tắc kiến trúc quan trọng nhất trong lĩnh vực An toàn thông tin, được vay mượn từ học thuyết quân sự cổ điển: không bao giờ dựa vào một hàng rào phòng thủ duy nhất, mà phải xây dựng nhiều lớp phòng thủ chồng chéo, sao cho ngay cả khi kẻ tấn công vượt qua được một lớp, chúng vẫn phải đối mặt với các lớp tiếp theo trước khi chạm được vào tài sản cần bảo vệ.

Theo mô hình này, hệ thống phòng thủ được tổ chức thành **ba lớp chính** có tính chất bổ trợ lẫn nhau:

- **Lớp An ninh Cơ quan/Tổ chức (Organizational Security):** Đây là lớp phòng vệ phi kỹ thuật nhưng không kém phần quan trọng, bao gồm chính sách bảo mật (Security Policy), quy trình quản lý nhân sự (đào tạo, sàng lọc nhân viên), các biện pháp kiểm soát vật lý (kiểm soát vào ra khu vực máy chủ) và văn hóa an toàn thông tin. Lớp này nhắm vào yếu tố **Con người (People)** và **Quy trình (Procedures)** – vốn là nguồn gốc của hơn 70% các sự cố bảo mật theo thống kê từ IBM Security Reports.

- **Lớp An ninh Mạng (Network Security):** Bảo vệ hạ tầng mạng và luồng thông tin di chuyển giữa các thành phần hệ thống. Các công cụ tiêu biểu bao gồm Tường lửa (Firewall), Hệ thống phát hiện và ngăn chặn xâm nhập (IDS/IPS), Tường lửa ứng dụng web (WAF), phân vùng mạng DMZ và mã hóa đường truyền (TLS/SSL). Đây là lớp chịu trách nhiệm **lọc và kiểm soát luồng lưu lượng mạng** theo chính sách cho phép/từ chối.

- **Lớp An ninh Hệ thống & Ứng dụng (System/Application Security):** Bảo vệ trực tiếp tại tầng hệ điều hành, ứng dụng và cơ sở dữ liệu. Bao gồm kiểm soát truy cập (Access Control), quản lý bản vá (Patch Management), mã hóa dữ liệu lưu trữ (Encryption at Rest), kiểm toán và ghi nhật ký (Audit Logging). Đây là lớp cuối cùng trực tiếp bảo vệ **tài sản thông tin (Data)**.

Trong thực tế, nguyên tắc DiD không chỉ dừng lại ở ba lớp mà còn được cụ thể hóa thành **bảy vùng hạ tầng CNTT** như trình bày ở phần tiếp theo. Sức mạnh của DiD nằm ở tư duy **"giả định thất bại" (Assume Breach)**: thiết kế hệ thống với giả định rằng một vài lớp phòng vệ sẽ bị vượt qua, do đó mỗi lớp phải hoạt động độc lập và không phụ thuộc vào sự hoàn hảo của lớp khác.

#### 1.2.2. Bảy vùng hạ tầng CNTT và các mối đe dọa tương ứng

Mô hình bảy vùng hạ tầng CNTT (Seven Domains of IT Infrastructure) là một framework phân tích rủi ro cấu trúc, giúp kiến trúc sư bảo mật có cái nhìn toàn diện về mọi điểm có thể bị tấn công trong một tổ chức. Mỗi vùng có đặc điểm riêng biệt về các mối đe dọa tiềm ẩn và các biện pháp kiểm soát tương ứng.

**Bảng 1.2: Bảy vùng hạ tầng CNTT – Đặc điểm và mối đe dọa điển hình**

| STT | Vùng hạ tầng | Mô tả | Mối đe dọa chính | Biện pháp kiểm soát |
|---|---|---|---|---|
| 1 | **Vùng Người dùng (User Domain)** | Con người tương tác với hệ thống thông tin | Lạm dụng quyền hạn, rò rỉ thông tin xác thực, Social Engineering, Phishing | Đào tạo nhận thức, Chính sách mật khẩu mạnh, MFA (Xác thực đa yếu tố) |
| 2 | **Vùng Máy trạm (Workstation Domain)** | Máy tính cá nhân, laptop của người dùng cuối | Phần mềm độc hại (Malware), Keylogger, truy cập vật lý trái phép | Antivirus, Endpoint Detection & Response (EDR), Mã hóa ổ đĩa (BitLocker) |
| 3 | **Vùng LAN (LAN Domain)** | Mạng nội bộ của tổ chức | ARP Spoofing, Man-in-the-Middle nội bộ, Lateral Movement sau khi đã xâm nhập | 802.1X Network Access Control, VLAN phân vùng, IDS/IPS nội bộ |
| 4 | **Vùng LAN-to-WAN (LAN-to-WAN Domain)** | Điểm kết nối giữa mạng nội bộ và Internet | DDoS, SQL Injection qua API, tấn công ứng dụng web, khai thác lỗ hổng tường lửa | Stateful Firewall, WAF, IPS, DMZ, Rate Limiting |
| 5 | **Vùng WAN (WAN Domain)** | Hạ tầng Internet công cộng | Nghe lén đường truyền, BGP Hijacking, DNS Poisoning | SSL/TLS mã hóa đường truyền, DNSSEC, VPN |
| 6 | **Vùng Truy cập từ xa (Remote Access Domain)** | Nhân viên/đối tác truy cập từ bên ngoài mạng tổ chức | Brute Force đăng nhập từ xa, đánh cắp VPN credentials | Zero Trust Network Access (ZTNA), MFA, Just-in-Time Access |
| 7 | **Vùng Hệ thống/Ứng dụng (System/Application Domain)** | Máy chủ, cơ sở dữ liệu, ứng dụng | Khai thác lỗ hổng ứng dụng, SQL Injection, Privilege Escalation, Ransomware | Patch Management, RBAC, Mã hóa CSDL, Audit Logging, Backup |

Điểm đặc biệt của mô hình bảy vùng là tư duy **phân tách ranh giới tin cậy (Trust Boundary)**: mỗi khi thông tin di chuyển từ vùng này sang vùng khác, cần có cơ chế xác thực và kiểm soát bổ sung, không được mặc nhiên tin tưởng rằng thông tin đến từ vùng nội bộ là an toàn. Đây chính là nền tảng của triết lý **Zero Trust Architecture** – "Không bao giờ tin tưởng mặc định, luôn luôn xác minh" – một hướng tiếp cận ngày càng được các tổ chức tài chính lớn trên thế giới áp dụng.

---

### 1.3. Phương pháp đánh giá rủi ro An toàn thông tin

#### 1.3.1. Khái niệm Rủi ro và Phương pháp tiếp cận

**Rủi ro an toàn thông tin (Information Security Risk)** được định nghĩa là khả năng xảy ra của một sự kiện đe dọa, kết hợp với mức độ tổn hại mà sự kiện đó gây ra. Về mặt toán học, công thức đơn giản hóa thường được sử dụng là:

> **Rủi ro = Xác suất xảy ra đe dọa × Mức độ tổn hại**

Trong thực tế, đánh giá rủi ro ATTT thường phức tạp hơn vì phải xem xét đồng thời ba yếu tố: **(1) Mối đe dọa (Threat)** – các tác nhân hay sự kiện có thể gây hại (tin tặc, nhân viên bất mãn, thiên tai); **(2) Lỗ hổng (Vulnerability)** – các điểm yếu trong hệ thống có thể bị khai thác; và **(3) Tác động (Impact)** – mức độ thiệt hại nếu đe dọa thành hiện thực qua lỗ hổng.

Có hai phương pháp đánh giá rủi ro chính: **Phương pháp định tính (Qualitative)** sử dụng thang đánh giá mô tả (Cao/Trung bình/Thấp) dựa trên phán đoán chuyên gia – ưu điểm là nhanh và linh hoạt; **Phương pháp định lượng (Quantitative)** gán giá trị số học cho từng yếu tố (ví dụ: ALE = ARO × SLE) – ưu điểm là chính xác nhưng đòi hỏi nhiều dữ liệu thống kê lịch sử. Trong thực tế, phương pháp **kết hợp (Combined Approach)** thường được áp dụng để tận dụng ưu điểm của cả hai.

#### 1.3.2. Quy trình đánh giá rủi ro 9 bước theo NIST SP 800-30

Quy trình đánh giá rủi ro ATTT chuẩn hóa theo NIST SP 800-30 (và tương thích với ISO/IEC 27005) bao gồm **9 bước** có tính tuần tự và logic chặt chẽ:

**Bảng 1.3: Quy trình đánh giá rủi ro ATTT 9 bước**

| Bước | Tên bước | Nội dung thực hiện | Đầu ra (Output) |
|---|---|---|---|
| **1** | **Mô tả hệ thống (System Characterization)** | Xác định phạm vi, ranh giới, các thành phần phần cứng/phần mềm/dữ liệu/nhân sự/quy trình của hệ thống cần đánh giá | Hồ sơ đặc tả hệ thống (System Profile) |
| **2** | **Nhận diện mối đe dọa (Threat Identification)** | Lập danh sách toàn diện các mối đe dọa tiềm ẩn, phân loại theo nguồn gốc (bên ngoài, bên trong, môi trường) | Danh sách đe dọa (Threat Catalog) |
| **3** | **Nhận diện lỗ hổng (Vulnerability Identification)** | Xác định các điểm yếu kỹ thuật và phi kỹ thuật trong hệ thống có thể bị mối đe dọa khai thác | Danh sách lỗ hổng (Vulnerability List) |
| **4** | **Phân tích biện pháp kiểm soát (Control Analysis)** | Đánh giá các biện pháp kiểm soát bảo mật hiện có (đã triển khai và đang lên kế hoạch) | Danh sách biện pháp kiểm soát |
| **5** | **Xác định khả năng xảy ra (Likelihood Determination)** | Đánh giá xác suất một mối đe dọa cụ thể thành công khai thác lỗ hổng (thang: Cao/TB/Thấp) | Điểm khả năng xảy ra |
| **6** | **Phân tích tác động (Impact Analysis)** | Đánh giá mức độ tổn hại đến tổ chức nếu đe dọa thành công (tài chính, danh tiếng, pháp lý) | Điểm mức độ tác động |
| **7** | **Xác định mức độ rủi ro (Risk Determination)** | Tổng hợp xác suất xảy ra và mức độ tác động để xếp hạng rủi ro trên ma trận | Ma trận rủi ro (Risk Matrix) |
| **8** | **Đề xuất biện pháp kiểm soát (Control Recommendations)** | Đề xuất các biện pháp kỹ thuật/quy trình để giảm thiểu rủi ro xuống mức chấp nhận được | Danh sách đề xuất biện pháp |
| **9** | **Lập tài liệu kết quả (Documentation)** | Ghi chép toàn bộ kết quả đánh giá thành báo cáo chuẩn cho lãnh đạo và nhóm kỹ thuật | Báo cáo đánh giá rủi ro chính thức |

Điểm mấu chốt của quy trình 9 bước là tính **vòng lặp liên tục**: đánh giá rủi ro không phải là hoạt động một lần mà phải được thực hiện định kỳ (ít nhất mỗi năm một lần) và đặc biệt sau mỗi thay đổi lớn về kiến trúc hệ thống hoặc khi có sự cố mới xảy ra trong ngành. Trong bối cảnh CRM 1.0 của VietinBank, mỗi lần triển khai một microservice mới hay thêm một điểm tích hợp với hệ thống bên ngoài đều nên kích hoạt một chu kỳ đánh giá rủi ro cập nhật.

#### 1.3.3. Ma trận Rủi ro – Công cụ trực quan hóa và ưu tiên hóa

Sau khi hoàn thành bước 5 và bước 6, kết quả được ánh xạ lên **Ma trận Rủi ro (Risk Matrix)** – một công cụ trực quan hóa 2 chiều kết hợp trục xác suất xảy ra (Likelihood) và trục mức độ tác động (Impact). Ma trận này giúp lãnh đạo tổ chức ra quyết định ưu tiên nguồn lực để xử lý các rủi ro theo nguyên tắc **Rủi ro cao nhất – Giải quyết trước tiên**.

**Bảng 1.4: Mẫu Ma trận Rủi ro tổng quát (5×5)**

| | **Tác động rất thấp (1)** | **Tác động thấp (2)** | **Tác động TB (3)** | **Tác động cao (4)** | **Tác động rất cao (5)** |
|---|---|---|---|---|---|
| **Xác suất rất cao (5)** | Trung bình (5) | Cao (10) | **Rất cao (15)** | **Rất cao (20)** | **Rất cao (25)** |
| **Xác suất cao (4)** | Thấp (4) | Trung bình (8) | Cao (12) | **Rất cao (16)** | **Rất cao (20)** |
| **Xác suất TB (3)** | Thấp (3) | Trung bình (6) | Trung bình (9) | Cao (12) | **Rất cao (15)** |
| **Xác suất thấp (2)** | Rất thấp (2) | Thấp (4) | Trung bình (6) | Trung bình (8) | Cao (10) |
| **Xác suất rất thấp (1)** | Rất thấp (1) | Rất thấp (2) | Thấp (3) | Thấp (4) | Trung bình (5) |

*Chú thích: Ô màu đậm (≥ 15) là rủi ro cần xử lý ngay lập tức. Ô (8–14) là rủi ro cần lên kế hoạch xử lý. Ô (≤ 7) là rủi ro có thể chấp nhận được hoặc giám sát định kỳ.*

---

### 1.4. Các công nghệ bảo mật lõi

#### 1.4.1. Mật mã học trong Bảo mật thông tin

**Mật mã học (Cryptography)** là trụ cột kỹ thuật không thể thiếu trong kiến trúc bảo mật hiện đại, cung cấp nền tảng toán học cho ba dịch vụ bảo mật quan trọng nhất: **bảo mật thông tin (Confidentiality)** qua mã hóa, **xác minh tính toàn vẹn (Integrity)** qua hàm băm và **xác thực nguồn gốc (Authentication)** qua chữ ký số.

**a) Mã hóa đối xứng (Symmetric Encryption):**
Trong mã hóa đối xứng, **cùng một khóa (Secret Key)** được sử dụng cho cả quá trình mã hóa (Encryption) và giải mã (Decryption). Thuật toán tiêu chuẩn vàng hiện nay là **AES (Advanced Encryption Standard)** với độ dài khóa 256-bit (AES-256), được chính phủ Mỹ thông qua là chuẩn mã hóa quốc gia từ năm 2001 và được NIST xác nhận là an toàn trước các cuộc tấn công lượng tử trong tương lai gần. Chế độ vận hành **GCM (Galois/Counter Mode)** kết hợp mã hóa với xác thực tính toàn vẹn (Authenticated Encryption with Associated Data – AEAD), là lựa chọn tối ưu cho môi trường ngân hàng.

Ưu điểm của mã hóa đối xứng là **tốc độ xử lý cực nhanh** (phù hợp để mã hóa khối lượng dữ liệu lớn như cơ sở dữ liệu), nhưng nhược điểm là **vấn đề phân phối khóa an toàn (Key Distribution Problem)**: làm thế nào để trao đổi khóa bí mật giữa hai bên qua kênh truyền không an toàn? Đây chính là điểm mà mã hóa bất đối xứng giải quyết.

**b) Mã hóa bất đối xứng (Asymmetric Encryption):**
Mã hóa bất đối xứng sử dụng **cặp khóa (Key Pair)**: **Khóa công khai (Public Key)** để mã hóa dữ liệu hoặc xác minh chữ ký; và **Khóa bí mật (Private Key)** để giải mã dữ liệu hoặc tạo chữ ký số. Thuật toán phổ biến nhất là **RSA (Rivest-Shamir-Adleman)** với độ dài khóa tối thiểu 2048-bit (khuyến nghị 4096-bit cho môi trường ngân hàng). Thuật toán **ECDSA (Elliptic Curve Digital Signature Algorithm)** ngày càng được ưa chuộng vì cho phép đạt được mức độ bảo mật tương đương RSA-3072 với khóa chỉ 256-bit, tiết kiệm đáng kể tài nguyên tính toán.

Trong thực tế, mã hóa bất đối xứng thường được dùng để **trao đổi khóa đối xứng một cách an toàn** (ví dụ: trong bắt tay TLS), sau đó toàn bộ dữ liệu phiên được mã hóa bằng AES – kết hợp này tận dụng ưu điểm của cả hai: sự an toàn trong trao đổi khóa của bất đối xứng và tốc độ xử lý cao của đối xứng.

**c) Hàm băm mật mã (Cryptographic Hash Function):**
Hàm băm mật mã (ví dụ: SHA-256, SHA-3) là hàm một chiều biến dữ liệu đầu vào có độ dài tùy ý thành chuỗi băm (Hash/Digest) có độ dài cố định. Ba đặc tính cốt lõi đảm bảo tính hữu dụng của hàm băm là: **(1) Kháng tiền ảnh (Preimage Resistance)** – không thể tính ngược từ hash ra dữ liệu gốc; **(2) Kháng va chạm (Collision Resistance)** – cực kỳ khó tìm hai đầu vào khác nhau cho cùng một hash; và **(3) Hiệu ứng tuyết lở (Avalanche Effect)** – chỉ một thay đổi nhỏ trong dữ liệu gốc tạo ra hash hoàn toàn khác biệt. Hàm băm là nền tảng cho kiểm tra tính toàn vẹn dữ liệu, lưu trữ mật khẩu (kết hợp với Salt), chữ ký số và blockchain.

**d) Giao thức SSL/TLS:**
**SSL/TLS (Secure Sockets Layer / Transport Layer Security)** là giao thức mật mã cung cấp kênh truyền thông an toàn giữa hai điểm đầu cuối qua mạng không tin cậy (Internet). TLS 1.3 (phiên bản mới nhất, công bố năm 2018) là tiêu chuẩn bắt buộc trong môi trường tài chính, loại bỏ các thuật toán mã hóa yếu (RC4, DES, 3DES) và chỉ hỗ trợ **Perfect Forward Secrecy (PFS)** – đảm bảo rằng dù khóa phiên bị rò lộ trong tương lai, các phiên truyền thông đã hoàn thành trong quá khứ vẫn không bị giải mã được.

**Bảng 1.5: So sánh các thuật toán mật mã lõi**

| Thuật toán | Loại | Độ dài khóa khuyến nghị | Ứng dụng tại CRM 1.0 | Tốc độ |
|---|---|---|---|---|
| **AES-256-GCM** | Đối xứng | 256-bit | Mã hóa dữ liệu CSDL lưu trữ (Data at Rest), mã hóa hồ sơ hình ảnh trên S3 | Rất nhanh (~1GB/s trên phần cứng hiện đại) |
| **RSA-4096** | Bất đối xứng | 4096-bit | Trao đổi khóa TLS, ký số văn bản hồ sơ khách hàng | Chậm (chỉ dùng cho dữ liệu nhỏ) |
| **ECDSA-P256** | Bất đối xứng (đường cong elliptic) | 256-bit | Chứng chỉ TLS của API Gateway, ký token JWT | Nhanh, hiệu quả trên thiết bị di động |
| **SHA-256** | Hàm băm | N/A (output 256-bit) | Kiểm tra toàn vẹn hồ sơ, lưu mật khẩu (bcrypt + SHA), Audit Log | Cực nhanh |
| **TLS 1.3** | Giao thức | N/A | Toàn bộ giao tiếp giữa Browser ↔ API Gateway, API Gateway ↔ Microservices | Overhead tối thiểu |

#### 1.4.2. Kiểm soát truy cập – RBAC và ABAC

**Kiểm soát truy cập (Access Control)** là cơ chế xác định **ai được làm gì với tài nguyên nào** trong hệ thống thông tin. Đây là một trong những biện pháp bảo mật quan trọng nhất để đảm bảo nguyên tắc **"Quyền tối thiểu" (Principle of Least Privilege – PoLP)**: mỗi chủ thể (người dùng, tiến trình) chỉ được cấp đúng và đủ quyền cần thiết để thực hiện nhiệm vụ hợp pháp của mình, không hơn không kém.

Có ba mô hình kiểm soát truy cập chính trong học thuật:

**a) DAC – Kiểm soát tùy quyền (Discretionary Access Control):** Chủ sở hữu tài nguyên tự quyết định quyền truy cập của người khác (ví dụ: phân quyền file trong Windows). Mô hình này linh hoạt nhưng thiếu nhất quán và khó quản lý tập trung ở quy mô doanh nghiệp.

**b) MAC – Kiểm soát bắt buộc (Mandatory Access Control):** Hệ thống gán nhãn bảo mật cho cả tài nguyên (Data Labels: TOP SECRET, SECRET, CONFIDENTIAL, UNCLASSIFIED) và người dùng (Clearance Level), sau đó kiểm soát truy cập dựa trên so sánh hai nhãn này theo chính sách tập trung. MAC thường được dùng trong môi trường quân sự và chính phủ.

**c) RBAC – Kiểm soát dựa trên vai trò (Role-Based Access Control):** RBAC là mô hình phổ biến và phù hợp nhất cho môi trường doanh nghiệp. Thay vì gán quyền trực tiếp cho từng người dùng (gây bùng nổ về số lượng chính sách và khó bảo trì), RBAC gán quyền cho **Vai trò (Role)**, và người dùng được gán vào các vai trò phù hợp với chức danh công việc của họ.

Các thành phần cốt lõi của RBAC bao gồm:
- **Người dùng (User):** Danh tính cụ thể trong hệ thống (ví dụ: nguyenthia@vietinbank.vn)
- **Vai trò (Role):** Nhóm quyền hạn được định nghĩa theo chức năng nghiệp vụ (ví dụ: Relationship_Manager, Branch_Manager, System_Admin)
- **Quyền hạn (Permission):** Thao tác cụ thể được phép thực hiện trên tài nguyên cụ thể (ví dụ: customer_profile:read, credit_report:view)
- **Phiên làm việc (Session):** Ánh xạ tạm thời giữa người dùng và tập con các vai trò đang kích hoạt

**Bảng 1.6: Ma trận phân quyền RBAC mẫu cho hệ thống CRM Ngân hàng**

| Vai trò | Xem TT KH | Tạo Leads | Sửa hồ sơ | Xem CIC | Tải hồ sơ PDF | Phê duyệt hạn mức | Quản trị hệ thống |
|---|---|---|---|---|---|---|---|
| **Giao dịch viên (Teller)** | ✅ (chi nhánh mình) | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **Chuyên viên QHKH (RM)** | ✅ (KH phụ trách) | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ |
| **Trưởng phòng KH** | ✅ (toàn chi nhánh) | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| **Giám đốc Chi nhánh** | ✅ (toàn chi nhánh) | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ |
| **Kiểm soát viên (Auditor)** | ✅ (chỉ đọc) | ❌ | ❌ | ✅ | ✅ | ❌ | ❌ |
| **Quản trị hệ thống (SysAdmin)** | ❌ (không truy cập dữ liệu KH) | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |

*Chú thích: Nguyên tắc "Phân tách nhiệm vụ (Separation of Duties)" được thể hiện qua việc SysAdmin có quyền quản trị hệ thống NHƯNG không được truy cập dữ liệu khách hàng, ngăn chặn nguy cơ người có quyền cao nhất cũng là người có thể lạm dụng dữ liệu.*

**d) ABAC – Kiểm soát dựa trên thuộc tính (Attribute-Based Access Control):** ABAC mở rộng RBAC bằng cách bổ sung thêm **ngữ cảnh động (Dynamic Context)** vào quyết định kiểm soát truy cập. Thay vì chỉ dựa trên vai trò tĩnh, ABAC cho phép định nghĩa chính sách phức tạp hơn như: "Chuyên viên QHKH (RM) chỉ được xem thông tin CIC nếu đang trong giờ làm việc (8:00–17:00), đang đăng nhập từ IP nội bộ của ngân hàng, VÀ khách hàng đó đang được phân công cho họ." Đây là mô hình cho phép triển khai **kiểm soát truy cập theo ngữ cảnh (Context-Aware Access Control)** và sẽ được đề xuất áp dụng chi tiết trong Chương 3.

#### 1.4.3. Tường lửa (Firewall) và Hệ thống phát hiện/ngăn chặn xâm nhập (IDS/IPS)

**Tường lửa (Firewall)** là thiết bị hoặc phần mềm kiểm soát luồng lưu lượng mạng dựa trên một tập hợp các quy tắc (Rules) được định nghĩa trước. Tường lửa hoạt động như một **trạm kiểm soát biên giới (Border Control)** giữa các vùng mạng với mức độ tin cậy khác nhau. Có ba thế hệ tường lửa chính:

- **Packet Filtering Firewall:** Kiểm tra từng gói tin riêng lẻ dựa trên địa chỉ IP nguồn/đích và số cổng (Port). Đây là thế hệ cơ bản nhất, nhanh nhưng không hiểu ngữ cảnh kết nối.
- **Stateful Inspection Firewall:** Theo dõi trạng thái của toàn bộ phiên kết nối (Connection State Table), cho phép các gói phản hồi hợp lệ đi qua mà không cần quy tắc rõ ràng. Đây là tiêu chuẩn tối thiểu cho môi trường doanh nghiệp.
- **Next-Generation Firewall (NGFW):** Kết hợp Stateful Inspection với khả năng kiểm tra ứng dụng tầng 7 (Deep Packet Inspection – DPI), phát hiện và ngăn chặn phần mềm độc hại, lọc URL và tích hợp Threat Intelligence.

**Tường lửa ứng dụng web (Web Application Firewall – WAF)** là một dạng đặc biệt của NGFW, chuyên bảo vệ các ứng dụng web khỏi các cuộc tấn công tầng ứng dụng như SQL Injection, Cross-Site Scripting (XSS), Cross-Site Request Forgery (CSRF) và các kỹ thuật tấn công API phổ biến. WAF là thành phần không thể thiếu trong kiến trúc DMZ của hệ thống ngân hàng trực tuyến.

**Hệ thống phát hiện xâm nhập (Intrusion Detection System – IDS)** giám sát lưu lượng mạng và/hoặc hoạt động của hệ thống để phát hiện các hành vi bất thường hoặc các mẫu tấn công đã biết (Signatures), sau đó **cảnh báo (Alert)** cho quản trị viên. IDS không tự động ngăn chặn tấn công mà chỉ ghi nhận và thông báo.

**Hệ thống ngăn chặn xâm nhập (Intrusion Prevention System – IPS)** là bước phát triển tiếp theo của IDS: ngoài khả năng phát hiện, IPS còn có thể **tự động ngăn chặn (Block)** các gói tin hoặc kết nối độc hại theo thời gian thực. IPS được phân loại theo vị trí triển khai: **NIPS (Network-based)** đặt tại các điểm then chốt của hạ tầng mạng, và **HIPS (Host-based)** cài đặt trực tiếp trên máy chủ/container để phát hiện các hành vi bất thường từ bên trong.

**Bảng 1.7: So sánh các công nghệ kiểm soát truy cập mạng**

| Công nghệ | Tầng OSI hoạt động | Khả năng | Hạn chế | Vị trí triển khai phù hợp |
|---|---|---|---|---|
| **Packet Filter Firewall** | Tầng 3–4 (Network/Transport) | Lọc theo IP/Port nhanh | Không hiểu ngữ cảnh kết nối | Router biên giới |
| **Stateful Firewall** | Tầng 3–4 + trạng thái kết nối | Theo dõi trạng thái phiên | Không phân tích nội dung | Ranh giới vùng mạng |
| **WAF** | Tầng 7 (Application) | Phát hiện SQLi, XSS, CSRF, API Attack | Chi phí xử lý cao hơn | Trước lớp API Gateway trong DMZ |
| **NGFW** | Tầng 3–7 | DPI, phát hiện malware, lọc URL | Chi phí cao | Điểm tập trung luồng lưu lượng |
| **NIDS/NIPS** | Tầng 3–7 (phân tích toàn diện) | Phát hiện mẫu tấn công, anomaly detection | False positive rate cần tinh chỉnh | Trong vùng nội bộ, tại các switch lõi |
| **HIDS/HIPS** | Tầng ứng dụng (trên host) | Phát hiện hành vi bất thường trên container | Tốn tài nguyên tính toán | Trực tiếp trên Worker Nodes OpenShift |

---

### Tóm tắt Chương 1

Chương 1 đã xây dựng một nền tảng lý thuyết vững chắc và toàn diện làm cơ sở cho toàn bộ nghiên cứu. Qua bốn phần chính, chúng ta đã:

**(1)** Làm rõ bản chất và tầm quan trọng của An toàn thông tin thông qua mô hình CIA Triad, đặc biệt làm nổi bật mối quan hệ đánh đổi tinh tế giữa ba thuộc tính và yêu cầu cân bằng trong thiết kế kiến trúc bảo mật.

**(2)** Hệ thống hóa mô hình Phòng vệ chiều sâu (Defense in Depth) với ba lớp bảo vệ chính và bảy vùng hạ tầng CNTT, cung cấp framework phân tích rủi ro có cấu trúc sẽ được áp dụng trực tiếp trong Chương 2.

**(3)** Trình bày quy trình đánh giá rủi ro 9 bước theo NIST SP 800-30 với Ma trận Rủi ro 5×5, trang bị công cụ phân tích định tính để nhận diện và ưu tiên hóa các rủi ro bảo mật của CRM 1.0.

**(4)** Giới thiệu các công nghệ bảo mật lõi – mật mã học (AES-256, RSA, SHA-256, TLS 1.3), kiểm soát truy cập (RBAC kết hợp ABAC), Firewall thế hệ mới và IDS/IPS – như những "hòn gạch xây dựng" (Building Blocks) cho kiến trúc bảo mật được đề xuất trong Chương 3.

Với nền tảng lý thuyết này, Chương 2 sẽ chuyển từ lý luận tổng quát sang phân tích cụ thể, ánh xạ các lý thuyết đã học vào thực tiễn kiến trúc của hệ thống CRM 1.0 tại VietinBank để nhận diện các rủi ro thực sự và đặc thù mà hệ thống đang đối mặt.

---

*[Tiếp theo: Chương 2 – Phân tích hiện trạng và đánh giá rủi ro hệ thống CRM 1.0 tại VietinBank]*
