

Thành viên 1: Ninh \- Giới thiệu dự án (Slide 1 \- 3\)  
Slide 1: Title  
"Dạ em chào thầy TS. Vũ Duy Hiến và toàn thể các bạn. Em là Trương An Ninh, đại diện cho Nhóm 5\. Hôm nay, nhóm chúng em xin trình bày đề tài: 'Nghiên cứu áp dụng tự động hoá đánh giá an ninh IaC và Container Image bằng Trivy và Terrascan'. Đối tượng nghiên cứu thực tiễn được chúng em lựa chọn triển khai là hệ thống CRM 1.0 của Ngân hàng VietinBank."

Slide 2: Agenda  
"Nội dung báo cáo của chúng em được chia làm 2 phần chính. Phần 1 là Technical Overview, tập trung bóc tách kiến trúc 6 lớp của hệ thống CRM từ khía cạnh công nghệ và hạ tầng. Phần 2 là nội dung cốt lõi: Thiết kế luồng CI/CD, phân tích cơ chế hoạt động của Trivy, Terrascan và thực hiện Demo luồng Hard-Gate trên môi trường thực tế."

Slide 3: Phần 1 \- Overview Kiến trúc  
"Để có cơ sở triển khai giải pháp DevSecOps, trước tiên chúng ta cần nắm rõ vòng đời dữ liệu và cấu trúc nền tảng của hệ thống CRM. Sau đây, em xin nhường lời cho bạn Linh Chi để trình bày chi tiết về kiến trúc ứng dụng và luồng tích hợp hệ thống."

Thành viên 2: Chi \- Tổng quan kiến trúc (Slide 4 \- 11\)  
Slide 4: Kiến trúc tổng thể CRM 1.0  
"Cảm ơn Ninh. Thưa thầy và các bạn, trên màn hình là mô hình kiến trúc phân lớp (Decoupled Layers) của hệ thống CRM 1.0. Kiến trúc này được thiết kế theo hướng phân tách các miền lỗi (Fault Domains), giúp hệ thống có khả năng mở rộng ngang (Horizontal Scaling) và hạn chế downtime. Chúng em chia hệ thống thành 6 lớp kỹ thuật, bắt đầu từ Access Layer đến Infrastructure Layer."

Slide 5: Lớp kênh giao dịch (Access Layer)  
"Tại lớp Access Layer, Frontend được xây dựng bằng NextJS với cơ chế Server-side Rendering (SSR), giúp ẩn đi logic xử lý khỏi trình duyệt của client. Về mặt mạng, toàn bộ Inbound Traffic đều bị ép buộc (force) sử dụng giao thức HTTPS với chuẩn TLS 1.2 trở lên. Đối với thiết bị di động của cán bộ, chúng em tích hợp giải pháp MDM (Mobile Device Management) nhằm cô lập phân vùng dữ liệu công việc và chặn thực thi mã độc tại End-point."

Slide 6: Lớp xác thực & bảo mật định danh (Identity Layer)  
"Luồng Request tiếp tục đi qua API Gateway và trạm kiểm soát định danh IAM. Tại đây, hệ thống tích hợp với ADFS của ngân hàng để xử lý Single Sign-On (SSO). Cơ chế xác thực hoàn toàn phi trạng thái (Stateless) dựa trên chuẩn OAuth 2.0. Sau khi xác thực, hệ thống trả về một JWT (JSON Web Token) chứa các Claims về RBAC/ABAC của User. JWT này sẽ được Verify tại API Gateway trước khi định tuyến xuống Backend."

Slide 7: Lớp dịch vụ CRM (Microservices Layer)  
"Dữ liệu sau khi qua API Gateway sẽ đi vào lớp Microservices. Các service được đóng gói thành Docker Container và điều phối bởi Red Hat OpenShift. Để tối ưu giao tiếp nội bộ (Inter-service Communication), chúng em áp dụng 2 cơ chế: REST API (gọi đồng bộ cho các tác vụ cần response ngay) và Kafka Event Streaming (gọi bất đồng bộ cho các tác vụ như gửi Notification hay Audit Log) nhằm tránh nghẽn luồng xử lý chính."

Slide 8: Lớp tích hợp ngân hàng (Integration Layer)  
"Tại lớp Integration, CRM đóng vai trò là Hub trung tâm. Để giao tiếp với Core Banking hay LOS (hệ thống Legacy), chúng em cấu hình các giao thức chuyển đổi tại Enterprise Service Bus (ESB), ví dụ như chuyển đổi từ SOAP XML sang REST JSON, kết hợp với Message Broker để đảm bảo tính toàn vẹn của gói tin khi hệ thống tải cao."

Slide 9: Lớp dữ liệu (Data Persistence)  
"Đối với Persistence Layer, hệ thống áp dụng nguyên lý Polyglot Persistence. Core CRM Data yêu cầu tính ACID nghiêm ngặt sẽ nằm tại Oracle DB. Các Microservices độc lập sử dụng PostgreSQL. Đồng thời, chúng em thiết lập Redis Cluster làm In-memory Cache để lưu trữ Session State và Danh mục sản phẩm nhằm tối ưu độ trễ truy vấn."

Slide 10: Hạ tầng Cloud-native (Infrastructure)  
"Toàn bộ khối kiến trúc trên được triển khai tự động thông qua IaC (Infrastructure as Code). Cụm OpenShift được cấu hình Multi-AZ (Multi-Availability Zones) để đảm bảo High Availability, kết hợp với các Ingress Controller để cân bằng tải L7."

Slide 11: Thách thức bảo mật & Đề xuất  
"Tuy nhiên, thưa thầy và các bạn, việc chuyển dịch sang Cloud-native và tự động hóa CI/CD lại mở ra bề mặt tấn công mới. Các Container Image có thể kế thừa (inherit) lỗ hổng CVE từ Base Image. Các file K8s Manifest có thể bị khai báo sai quyền (Privileged Escalation). Để giải quyết triệt để, chúng em đề xuất nhúng Trivy và Terrascan trực tiếp vào luồng CI/CD. Chi tiết kỹ thuật cấu hình, xin mời bạn Tuệ trình bày."

Thành viên 3: Tuệ \- Chi tiết cấu hình Trivy & Terrascan (Slide 12 \- 17\)  
Slide 12: Phần 2 \- Tích hợp Trivy & Terrascan  
"Cảm ơn Chi. Thưa thầy và các bạn, tiếp nối vấn đề mà Chi vừa nêu, em xin phép trình bày thiết kế kỹ thuật của luồng CI/CD và cách chúng em cấu hình các công cụ Security Scanner để chặn đứng mã độc ngay từ khâu Build."

Slide 13:  
Về kiến trúc tổng thế giải pháp bảo mật, chúng em đã thiết kế thành một kiến trúc tổng thể 5 lớp như trên Hình 3.1. Mã nguồn từ lớp Phát triển đi qua lớp CI/CD để quét bảo mật và chặn lỗi bằng Hard Gate. Sau khi qua cổng, Image được ký số và lưu trữ tại Registry. Cuối cùng, lớp Triển khai dùng ArgoCD để đồng bộ an toàn xuống OpenShift, đồng thời mọi hoạt động được lưu vết WORM tại lớp Giám sát.

Slide 14: Triết lý Shift-Left Security  
"Tư tưởng chủ đạo ở đây là 'Shift-Left Security'. Thay vì để SOC team dùng tool Nessus quét hệ thống sau khi đã Deploy lên Production (rất tốn thời gian và rủi ro cao), chúng em dịch chuyển quy trình Security về sát với khâu Commit Code của Developer. Lỗi ở đâu, Fail pipeline ở đó."

Slide 15: Luồng Pipeline GitLab CI/CD tích hợp  
"Chúng em thiết kế một Pipeline 9 bước trên GitLab. Tại giai đoạn Build Image xong, artifact chưa được phép đẩy (push) lên Registry. Nó bị giữ lại nội bộ tại Runner để đi qua 2 Security Gate: Trivy và Terrascan. Phải Pass cả 2 Gate này thì mới tới các bước tiếp theo."

Slide 16: Trivy (Quét SCA, Secrets & Image)  
Trivy là một công cụ quét bảo mật mã nguồn mở quét các lỗ hổng trong container và các tài nguyên khác được tạo và duy trì bởi AquaSecurity. Nó có một cơ sở dữ liệu nội bộ gọi là trivy-db chứa thông tin về các lỗ hổng khác nhau.

Trivy không chỉ quét lỗ hổng mà còn đưa ra các đề xuất để giải quyết vấn đề và liên kết đến dữ liệu lỗ hổng để biết thêm thông tin. Trivy có thể truy cập một loạt thông tin lỗ hổng từ các cơ sở dữ liệu lỗ hổng khác nhau và sử dụng dữ liệu lỗ hổng từ các cơ sở dữ liệu đó để phát hiện các vấn đề bảo mật. Một số cơ sở dữ liệu lỗ hổng bao gồm National Vulnerability Database (NVD), Red Hat Security Data và Alpine SecDB.

Khi quét, Trivy so sánh các gói phần mềm và thư viện trong thư mục hoặc hình ảnh container với thông tin trong cơ sở dữ liệu lỗ hổng và nếu tìm thấy sự trùng khớp, điều đó có nghĩa là gói hoặc thư viện trong hình ảnh container có lỗ hổng. Sau đó, Trivy báo cáo các lỗ hổng này cùng với các chi tiết khác như mức độ nghiêm trọng, phiên bản bị ảnh hưởng và các đề xuất sửa chữa.

Ngoài ra, Trivy cập nhật cơ sở dữ liệu của nó mỗi 6 giờ. Khi bạn bắt đầu quét, trivy tự động cập nhật cơ sở dữ liệu để bạn không cần phải theo dõi các bản cập nhật cơ sở dữ liệu. Một tính năng quan trọng khác của Trivy là tạo SBOM. Nó cung cấp một danh sách chi tiết tất cả các thành phần được sử dụng trong phần mềm, bao gồm các thư viện mã nguồn mở và bên thứ ba.

"Về mặt kỹ thuật, Trivy thực thi qua CLI với 3 mode chính: 

- Thứ nhất, lệnh *trivy fs* quét cây thư mục mã nguồn để tìm các Hardcoded Secrets (như AWS Access Key, DB Password).  
-  Thứ hai, Trivy đọc và dùng các file package.json hoặc pom.xml để làm SCA (Software Composition Analysis) đối chiếu với các CVE Database toàn cầu.   
- Thứ ba, lệnh trivy image sẽ phân tích các layer của Docker Image để quét lỗ hổng ở cấp độ OS (như Alpine, Ubuntu)."

Slide 17: Terrascan (Phân tích IaC Misconfiguration)

"Tại trạm gác bảo mật thứ hai, chúng em sử dụng Terrasca \- đây là 1 công cụ phân tích tĩnh dành cho Infrastructure as Code (IaC) để kiểm tra các tệp cấu hình như là  Kubernetes Manifest, Helm Chart, Terraform  hoặc các file định nghĩa hạ tầng khác. Khác với việc quét mã nguồn ở bước trước, Terrascan tập trung vào việc phân tích tĩnh các cấu hình hạ tầng nhằm phát hiện sớm những sai lệch về cấu hình và các rủi ro bảo mật trước khi triển khai.

Công cụ Terrascan  sẽ so sánh các cấu hình này với tập các chính sách bảo mật đã được định nghĩa. Bộ máy đánh giá chính sách của Terrascan được xây dựng trên Open Policy Agent (OPA). OPA sử dụng ngôn ngữ Rego để mô tả các quy tắc kiểm tra, nhờ vậy cho phép xây dựng và có thể dễ dàng tùy chỉnh các policy phù hợp với yêu cầu bảo mật.

Trong giải pháp của nhóm, chúng em xây dựng các policy như: không cho phép sử dụng hostPath để tránh truy cập trực tiếp vào máy chủ, bắt buộc container phải chạy với runAsNonRoot=true nhằm hạn chế leo thang đặc quyền, và yêu cầu khai báo resources.limits để ngăn ngừa tình trạng cạn kiệt tài nguyên hoặc lỗi Out of Memory.

Nếu Terrascan phát hiện cấu hình không đáp ứng các chính sách bảo mật đã định nghĩa, Security Gate sẽ chặn pipeline và yêu cầu nhóm phát triển khắc phục trước khi tiếp tục triển khai. Nhờ đó, các rủi ro về cấu hình được loại bỏ ngay từ giai đoạn xây dựng hạ tầng, thay vì chỉ được phát hiện khi hệ thống đã đi vào vận hành."

Để tìm hiểu sâu hơn về cơ chế xử lý khi phát hiện lỗi và luồng triển khai an toàn phía sau, em xin nhường lời cho bạn Dũng tiếp tục trình bày."

Thành viên 4: Dũng \- Hard Gate, Ký số, GitOps & Demo (Slide 18 \- 23\)  
Slide 18: Cơ chế Hard Gate & Failing Logic  
"Cảm ơn Tuệ. Dạ em chào thầy và các bạn. Tiếp nối luồng CI/CD, em xin trình bày về cơ chế 'Hard Gate' – điểm mấu chốt để tự động hóa toàn bộ quy trình này. Chúng em cấu hình tham số \--exit-code 1 cho cả Trivy và Terrascan đối với các lỗ hổng có severity là HIGH hoặc CRITICAL. Khi bash script nhận Exit Code 1, tiến trình GitLab Job sẽ bị Killed. Toàn bộ Pipeline chuyển sang trạng thái FAILED. Nếu dev muốn bypass một CVE chưa có bản vá, họ phải tạo file .trivyignore và cần rule approval từ nhánh của SecOps."

Slide 19: Supply Chain Security (Ký số Cosign)  
"Chỉ khi Image sạch hoàn toàn (vượt qua Hard Gate), Pipeline mới chuyển sang bước Cosign. Công cụ này dùng cơ chế mật mã bất đối xứng để ký số điện tử (Sign) lên Image Hash (Digest), sau đó đính kèm chữ ký này thành một OCI Artifact lưu trên Registry. Admission Controller trên OpenShift sẽ reject bất kỳ Pod nào request pull image mà không có chữ ký hợp lệ."

Slide 20: GitOps Workflow (Đồng bộ qua ArgoCD)  
"Sau khi có Image sạch và đã ký số, ArgoCD đóng vai trò là một Controller liên tục watch (theo dõi) repo GitOps. Nó thực thi vòng lặp Reconciliation Loop, so sánh Desired State trên Git và Live State trên Cluster. Nếu có sự sai lệch (Drift), ArgoCD tự động Sync lại."

Slide 21: Cấu hình môi trường Demo  
"Để chứng minh các cơ chế lý thuyết vừa trình bày hoạt động ra sao trong thực tế, chúng em đã chuẩn bị một môi trường Lab để thực chứng giải pháp. Môi trường bao gồm một GitLab Runner chạy trên Docker Engine đã cài sẵn binary Trivy, Terrascan và Cosign. Target là một cụm OpenShift Mini. Tập luật OPA Rego đã được config để cấm quyền root. Chúng em sẽ chạy 2 kịch bản."

Slide 22: Demo 1 \- Phát hiện & Chặn lỗ hổng Thư viện Java (Trivy)  
"Kịch bản 1: Do dự án backend CRM được phát triển bằng ngôn ngữ Java, trong quá trình code, lập trình viên có thể vô tình khai báo một thư viện đã cũ trong file pom.xml (ví dụ như thư viện log4j-core bản 2.14), hoặc sử dụng Base Image openjdk:8 chứa nhiều lỗi bảo mật. Chúng em tiến hành trigger Pipeline...

Thưa thầy và các bạn có thể thấy trên màn hình console, Trivy không chỉ quét hệ điều hành mà còn đi sâu vào phân tích các file .jar và cấu hình Maven. Nó đã quét ra các lỗ hổng CRITICAL liên quan đến RCE (Remote Code Execution) – điển hình như lỗi Log4Shell khét tiếng. Ngay lập tức, Trivy return Exit Code 1, Job Build bị đánh Failed, và Image chứa thư viện độc hại này bị xóa khỏi Runner. Giải pháp đã tự động chặn đứng hoàn toàn việc phát hành một ứng dụng Java chứa lỗi ra môi trường thực tế."

Slide 23: Demo 2 \- Sai cấu hình K8s Manifest (Terrascan)  
"Kịch bản 2: Chúng em sửa lại Base Image an toàn, nâng cấp thư viện Java, nhưng trong file deployment.yaml, dev lại cố tình khai báo securityContext: privileged: true để lấy toàn quyền truy cập Node. Trigger lại Pipeline... Lần này Trivy Pass, nhưng ở Job Terrascan, engine OPA đã parse ra cấu hình vi phạm chuẩn Rego. Console báo lỗi: 'Privileged container is not allowed'. Hard Gate kích hoạt, Pipeline tiếp tục Failed. Cơ chế này đã chặn đứng hoàn toàn rủi ro sai cấu hình hạ tầng từ con người. Sau đây, xin mời bạn Đạt tổng kết lại bài báo cáo."

Thành viên 5: Đạt \- Tổng kết & Lộ trình (Slide 23 \- 26\)  
Slide 24: Hiệu quả kỹ thuật mang lại  
"Cảm ơn phần demo thực tế của Dũng. Thưa thầy và các bạn, qua phân tích kiến trúc và demo kỹ thuật, chúng ta thấy rõ hiệu quả định lượng lớn nhất là tối ưu chỉ số MTTR (Mean Time To Remediation). Việc bắt lỗi bằng Hard Gate tại Pipeline giúp Dev nhận được feedback chỉ trong vài phút, thay vì phải đợi hàng tuần để có report Audit từ team bảo mật."

Slide 25: Kết luận & Lộ trình (Roadmap)  
"Tóm lại, sự kết hợp giữa Trivy, Terrascan, Cosign và GitOps đã giải quyết trọn vẹn bài toán bảo mật chuỗi cung ứng (Supply Chain Security) và IaC cho hệ thống CRM. Về lộ trình tiếp theo, chúng em định hướng nghiên cứu sâu hơn ở tầng Runtime với Falco để bắt các System Calls bất thường, và xây dựng cơ chế Webhook để Auto-remediation (tự động vá lỗi)."

Slide 26: Q\&A  
"Bài báo cáo của Nhóm 5 xin phép được khép lại tại đây. Chúng em xin chân thành cảm ơn thầy và các bạn đã dành thời gian lắng nghe. Nhóm rất mong nhận được những câu hỏi chuyên môn và sự góp ý từ thầy để hoàn thiện đề tài ạ."