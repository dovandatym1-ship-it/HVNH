# NỘI DUNG CHI TIẾT KỊCH BẢN THUYẾT TRÌNH (12 SLIDE)

---

## Slide 1
- **Tiêu đề:** Tự động hóa đánh giá an ninh IaC & Container trong GitOps cho CRM tại VietinBank
- **Layout:** Title Slide (Tiêu đề chính giữa, thông tin nhóm bên dưới).
- **Nội dung:**
  - Học phần: Bảo mật hệ thống thông tin.
  - Nhóm thực hiện: Nhóm 5.
  - Thành viên: Đỗ Văn Đạt, Trần Ngọc Dũng, Tạ Ngọc Tuệ, Nguyễn Linh Chi, Trương An Ninh.
  - Giảng viên hướng dẫn: TS. Vũ Duy Hiến.
- **Key Message:** Giới thiệu thông tin chung về đề tài và nhóm thuyết trình.
- **Speaker Notes:** "Kính chào thầy Vũ Duy Hiến và các bạn học viên. Tôi là Đỗ Văn Đạt, đại diện nhóm 5 xin phép bắt đầu phần trình bày về đề tài: Nghiên cứu áp dụng tự động hoá đánh giá an ninh hạ tầng mã nguồn và container image bằng Trivy, Terrascan trong quy trình GitOps cho hệ thống CRM tại Vietinbank."
- **Visual Suggestion:** Nền Abstract mờ ảo phong cách công nghệ ngân hàng hiện đại (Màu xanh dương đậm của VietinBank). Logo Học viện Ngân hàng & VietinBank.
- **Image Prompt (English):** A professional abstract background for a banking technology presentation, featuring subtle glowing blue and silver digital network lines, modern corporate aesthetic, clean and minimalist design, 8k resolution.
- **Design Notes:** Sử dụng font chữ hiện đại (Roboto, Inter), màu chủ đạo là Xanh dương đậm (Navy) và Xanh dương nhạt (Cyan).

---

## Slide 2
- **Tiêu đề:** Chuyển đổi số CRM & Thách thức bảo mật
- **Layout:** Two Columns (Cột trái: Text, Cột phải: Hình ảnh minh họa).
- **Nội dung:**
  - Hệ thống CRM VietinBank đang chuyển dịch sang kiến trúc Microservices & Cloud-native.
  - Áp dụng Agile và CI/CD giúp tăng tốc độ phát triển và phát hành phần mềm.
  - Rủi ro mở rộng sang lớp Container, IaC và chuỗi cung ứng phần mềm.
  - Kiểm thử bảo mật truyền thống trở thành "nút thắt cổ chai" (bottleneck), không theo kịp tốc độ CI/CD.
- **Key Message:** Việc chuyển đổi số nhanh chóng đòi hỏi phương pháp bảo mật mới, không thể dùng cách cũ.
- **Speaker Notes:** "Như chúng ta đã biết, VietinBank đang đẩy mạnh số hóa hệ thống CRM sang kiến trúc Cloud-native. Tuy nhiên, tốc độ CI/CD quá nhanh khiến các phương pháp kiểm thử an ninh truyền thống không thể theo kịp, tạo ra các nút thắt cổ chai. Rủi ro lúc này không chỉ ở code mà đã lan rộng sang container và cấu hình hạ tầng."
- **Visual Suggestion:** Hình ảnh minh họa "Nút thắt cổ chai" trong quy trình phát triển.
- **Image Prompt (English):** Conceptual 3D illustration of a software development pipeline bottleneck, a high-speed glowing digital data stream being slowed down by a heavy traditional padlock, modern tech aesthetic, deep blue and neon red colors.
- **Design Notes:** Các bullet point sử dụng icon dấu tích hoặc mũi tên để tạo sự mạch lạc.

---

## Slide 3
- **Tiêu đề:** Mục tiêu & Hướng tiếp cận Shift-Left
- **Layout:** Title & Content (Với các Box nổi bật).
- **Nội dung:**
  - **Mục tiêu:** Tự động hóa đánh giá an ninh cho Container Image và hạ tầng IaC trong quy trình GitOps.
  - **Hướng tiếp cận "Shift-Left":** Tích hợp bảo mật từ rất sớm trong vòng đời phát triển phần mềm (SDLC).
  - **Phạm vi áp dụng:** Sử dụng công cụ Trivy, Terrascan và Cosign.
- **Key Message:** Giải pháp giải quyết bài toán tốc độ bằng cách tự động hóa bảo mật ngay từ khâu viết code.
- **Speaker Notes:** "Để giải quyết thách thức đó, nhóm 5 đặt mục tiêu ứng dụng mô hình DevSecOps với hướng tiếp cận Shift-Left – tức là đẩy bảo mật về giai đoạn sớm nhất của quy trình viết code. Chúng tôi tập trung vào việc tự động hóa quét lỗ hổng bằng Trivy và Terrascan trực tiếp trong GitOps."
- **Visual Suggestion:** Timeline vòng đời phát triển phần mềm (SDLC) với một mũi tên chỉ mạnh về phía bên trái (khâu Code/Build) kèm biểu tượng cái khiên.
- **Image Prompt (English):** Conceptual 3D illustration of the "Shift-Left" security approach in software development, a glowing shield icon moving towards the left side of a digital timeline, futuristic tech aesthetic, blue and cyan lighting.
- **Design Notes:** Highlight chữ "Shift-Left" bằng màu nổi (Cam hoặc Đỏ) để gây ấn tượng.

---

## Slide 4
- **Tiêu đề:** Tổng quan Kiến trúc CRM VietinBank
- **Layout:** Diagram (Sơ đồ kiến trúc chiếm 70% không gian, Text chú thích 30%).
- **Nội dung:**
  - Kiến trúc phân lớp: Access, Frontend, Internal API, Microservices, Database & Cache.
  - Chạy trên nền tảng điều phối Container (Kubernetes/OpenShift).
  - Tích hợp phức tạp qua API Gateway và Kafka với Core Banking, ERP, Data Lake.
- **Key Message:** Kiến trúc Microservices phức tạp tạo ra hàng nghìn điểm kết nối cần bảo vệ.
- **Speaker Notes:** "Xin chào, tôi là Trần Ngọc Dũng. Đi sâu vào hệ thống, CRM VietinBank hiện tại có kiến trúc phân lớp rõ ràng, chạy trên Kubernetes. Như các bạn thấy trên sơ đồ, các Microservices giao tiếp qua API Gateway và Kafka. Sự phân rã này mang lại tính linh hoạt nhưng đồng thời tạo ra hàng ngàn điểm kết nối – chính là bề mặt tấn công rất lớn."
- **Visual Suggestion:** Sử dụng trực tiếp sơ đồ Hình 2.1 (Kiến trúc tổng thể và luồng xử lý của hệ thống CRM) trong báo cáo gốc.
- **Image Prompt (English):** N/A (Sử dụng sơ đồ kỹ thuật từ tài liệu gốc sẽ chính xác và học thuật hơn).
- **Design Notes:** Sơ đồ cần rõ nét. Các bullet point rút gọn tối đa chỉ dùng để bổ trợ cho sơ đồ.

---

## Slide 5
- **Tiêu đề:** Phân loại tài sản thông tin & Dữ liệu nhạy cảm
- **Layout:** Table / Bảng phân loại.
- **Nội dung:**
  - **Dữ liệu khách hàng (PII):** Hồ sơ định danh, lịch sử giao dịch (Yêu cầu bảo mật cao nhất).
  - **Mã nguồn & Pipeline:** Container Image, CI/CD Pipeline (Nơi dễ bị cài cắm mã độc).
  - **Hạ tầng & Secrets:** Kubernetes Manifest, cấu hình hệ thống, API Keys, JWT Tokens.
- **Key Message:** Dữ liệu PII của khách hàng xuất hiện ở hầu hết các luồng giao tiếp, do đó rủi ro rò rỉ là rất lớn.
- **Speaker Notes:** "Trong kiến trúc đó, tài sản thông tin giá trị nhất là Dữ liệu định danh khách hàng (PII). Tuy nhiên, chúng ta không thể bỏ qua các tài sản vô hình khác như Container Image, mã nguồn cấu hình IaC và các API Keys. Một khi các tài sản hạ tầng này bị lộ lọt, toàn bộ dữ liệu khách hàng bên trong cũng sẽ bị phơi bày."
- **Visual Suggestion:** Bảng 3 dòng hiển thị Icon, Nhóm tài sản, và Độ nhạy cảm.
- **Image Prompt (English):** N/A (Thiết kế Bảng/Table trực tiếp trên slide sẽ trực quan hơn).
- **Design Notes:** Dùng màu Đỏ nhạt cho dòng "Dữ liệu khách hàng" để biểu thị độ nhạy cảm cao nhất.

---

## Slide 6
- **Tiêu đề:** Nhận diện rủi ro tại các lớp
- **Layout:** Three Columns (3 cột ứng với 3 nhóm rủi ro).
- **Nội dung:**
  - **Lớp API & Access:** Đánh cắp phiên (Session Hijacking), thiếu xác thực (Broken Access Control).
  - **Lớp Container:** Base Image chứa lỗ hổng (CVE), thư viện mã nguồn mở lỗi thời.
  - **Chuỗi cung ứng (CI/CD & IaC):** Cấu hình IaC mở port trái phép, lộ mật khẩu (Hardcoded secrets) trong Git.
- **Key Message:** Rủi ro nghiêm trọng nhất đang nằm ở quá trình triển khai mã nguồn và container.
- **Speaker Notes:** "Tôi là Tạ Ngọc Tuệ. Dựa trên phân tích tài sản, nhóm đã nhận diện các rủi ro ở 3 khu vực chính. Ở lớp Access, rủi ro là đánh cắp phiên. Tuy nhiên, nguy hiểm nhất hiện nay nằm ở lớp Container và Chuỗi cung ứng phần mềm. Việc lập trình viên cấu hình sai tệp Kubernetes hoặc vô tình commit mật khẩu lên Git là những điểm yếu chí mạng."
- **Visual Suggestion:** 3 khối hộp nổi bật. Mỗi hộp có 1 icon cảnh báo.
- **Image Prompt (English):** Conceptual 3D illustration of cybersecurity threats targeting a cloud infrastructure, glowing red warning signs hovering over a futuristic digital server cluster, deep blue background, isometric view.
- **Design Notes:** Icon ổ khóa vỡ, con bọ (bug), và tệp tài liệu bị rò rỉ.

---

## Slide 7
- **Tiêu đề:** Ma trận rủi ro trọng yếu đối với CRM
- **Layout:** Matrix / Heatmap.
- **Nội dung:**
  - Đánh giá theo NIST SP 800-30 (Likelihood x Impact).
  - **Rủi ro Rất cao (Score 20):** Container Image chứa lỗ hổng CVE mức Critical/High.
  - **Rủi ro Rất cao (Score 20):** Container chạy quyền Root, cấu hình IaC sai lệch.
  - **Hệ quả:** Dẫn đến leo thang đặc quyền, rò rỉ dữ liệu, vi phạm pháp lý.
- **Key Message:** Ưu tiên số 1 là phải kiểm soát chặt chẽ Image và cấu hình IaC trước khi triển khai.
- **Speaker Notes:** "Đánh giá theo chuẩn NIST SP 800-30, chúng ta có một ma trận rủi ro tổng hợp. Trong đó, 2 rủi ro đỏ chót (điểm 20) cao nhất chính là: Sử dụng Image chứa lỗ hổng Critical và Cấu hình container chạy quyền Root. Hậu quả là hacker có thể leo thang đặc quyền chiếm toàn bộ hệ thống. Đây chính là mục tiêu mà giải pháp DevSecOps của chúng tôi nhắm tới."
- **Visual Suggestion:** Bảng Heatmap (Màu xanh - vàng - cam - đỏ) hoặc trích xuất Bảng 2.5 (cô đọng lại).
- **Image Prompt (English):** N/A (Vẽ Heatmap hoặc Table).
- **Design Notes:** Tập trung làm mờ các rủi ro thấp và highlight thật rực rỡ 2 dòng rủi ro có điểm 20 (R01, R02).

---

## Slide 8
- **Tiêu đề:** Công cụ kiểm tra: Trivy, Terrascan & Cosign
- **Layout:** Three Columns (Giới thiệu 3 công cụ).
- **Nội dung:**
  - **Trivy (Aqua Security):** Quét lỗ hổng tự động trong Container Image và thư viện phần mềm.
  - **Terrascan (Tenable):** Phân tích tĩnh (SAST) mã IaC (Kubernetes, Helm) để tìm lỗi cấu hình.
  - **Cosign (Sigstore):** Ký số Container Image sau khi quét sạch, chống chỉnh sửa (Tamper-proof).
- **Key Message:** Bộ 3 công cụ mã nguồn mở mạnh mẽ, dễ dàng tích hợp vào CI/CD.
- **Speaker Notes:** "Xin chào, tôi là Nguyễn Linh Chi. Để xử lý triệt để 2 rủi ro lớn nhất ở trên, chúng tôi đề xuất sử dụng bộ ba công cụ: Trivy chuyên quét lỗ hổng bên trong Container Image; Terrascan chuyên phân tích mã IaC để bắt lỗi cấu hình sai; và cuối cùng là Cosign dùng để ký số xác thực, đảm bảo Image không bị thay đổi lén lút."
- **Visual Suggestion:** Logo của 3 công cụ (Trivy, Terrascan, Cosign) đặt cân đối ở 3 cột.
- **Image Prompt (English):** N/A (Sử dụng Logo thực tế của các công cụ sẽ chuyên nghiệp hơn).
- **Design Notes:** Bố cục gọn gàng, nền sáng giúp logo các công cụ nổi bật.

---

## Slide 9
- **Tiêu đề:** Kiến trúc DevSecOps & Luồng thực thi
- **Layout:** Process / Flowchart.
- **Nội dung:**
  - Quy trình 9 bước tự động hoàn toàn.
  - Điểm nhấn 1 (CI): Trivy và Terrascan tạo **Security Gate** - chặn đứng lệnh build nếu có lỗi Critical.
  - Điểm nhấn 2: Chỉ khi vượt qua vòng quét, Image mới được Cosign ký số.
- **Key Message:** Bảo mật không phụ thuộc vào con người mà trở thành một "bức tường lửa" tự động trong luồng Code.
- **Speaker Notes:** "Đây là slide quan trọng nhất của bài trình bày: Luồng Pipeline 9 bước. Khi lập trình viên push code, hệ thống CI tự động gọi Trivy và Terrascan. Nếu phát hiện lỗi Critical, quá trình build bị đánh trượt ngay lập tức (Hard Gate). Chỉ khi hoàn toàn sạch lỗi, Image mới được Cosign ký số số hóa. Mọi thứ tự động 100%."
- **Visual Suggestion:** Sử dụng Hình 3.2 (Quy trình triển khai 9 bước) từ báo cáo.
- **Image Prompt (English):** N/A (Cắt hình 3.2 đưa vào là tốt nhất).
- **Design Notes:** Thêm các vòng tròn đỏ hoặc viền highlight vào bước gọi Trivy/Terrascan trên sơ đồ.

---

## Slide 10
- **Tiêu đề:** Vai trò của GitOps (ArgoCD)
- **Layout:** Diagram (Bên trái) + Text (Bên phải).
- **Nội dung:**
  - GitOps: Lấy Git làm nguồn chân lý duy nhất (Single Source of Truth).
  - ArgoCD: Công cụ triển khai tự động, đồng bộ từ Git vào cụm Kubernetes.
  - Admission Controller: Từ chối pull các Image chưa được ký số (Cosign verify).
- **Key Message:** Không ai được sửa trực tiếp trên Production, mọi thay đổi phải đi qua GitOps.
- **Speaker Notes:** "Sau khi Image được ký số, ArgoCD sẽ đảm nhận vai trò GitOps. Nghĩa là ArgoCD sẽ tự động kéo bản cập nhật vào Kubernetes. Hơn thế nữa, cụm Kubernetes được cấu hình Admission Controller để từ chối bất kỳ Image nào không có chữ ký của Cosign. Từ đây, không ai có thể can thiệp thủ công vào môi trường Production nữa."
- **Visual Suggestion:** Sơ đồ nhỏ minh họa kho Git -> ArgoCD -> Kubernetes Cluster.
- **Image Prompt (English):** Abstract 3D illustration representing GitOps, a glowing central Git repository icon syncing securely with a Kubernetes cluster of containers, glowing green checkmarks, modern cyber security aesthetic.
- **Design Notes:** Thiết kế mang tính đồng bộ và kết nối.

---

## Slide 11
- **Tiêu đề:** Hiệu quả & Lợi ích đạt được
- **Layout:** Bullet points với icon tích cực.
- **Nội dung:**
  - **Phòng ngừa sớm:** Phát hiện 80% rủi ro cấu hình/lỗ hổng trước khi lên môi trường Production.
  - **Tối ưu tốc độ:** Giảm thời gian kiểm tra bảo mật thủ công, duy trì tần suất phát hành nhanh (Agile).
  - **Bảo vệ hệ thống CRM:** Đảm bảo toàn vẹn dữ liệu khách hàng.
  - **Tuân thủ pháp lý:** Đáp ứng tiêu chuẩn ISO 27001 và yêu cầu bảo mật của NHNN.
- **Key Message:** DevSecOps là giải pháp hoàn hảo cân bằng giữa tốc độ kinh doanh và an toàn thông tin.
- **Speaker Notes:** "Chào thầy và các bạn, tôi là Trương An Ninh, tôi xin phép tổng kết lại lợi ích của giải pháp. Nhờ Shift-Left, chúng ta ngăn chặn được 80% rủi ro từ rất sớm, duy trì được tốc độ phát hành cực nhanh của Agile. Quan trọng nhất, CRM được bảo vệ toàn vẹn, hoàn toàn tuân thủ các quy định khắt khe của Ngân hàng Nhà nước."
- **Visual Suggestion:** Biểu đồ xu hướng (Trend line) cho thấy rủi ro giảm mạnh trong khi tốc độ release giữ nguyên hoặc tăng lên.
- **Image Prompt (English):** Conceptual business technology chart, a glowing digital line graph showing a sharp decrease in security risks while another line shows stable high-speed performance, holographic style, modern banking IT context.
- **Design Notes:** Sử dụng tone màu Xanh lá cây (Positive) cho slide này.

---

## Slide 12
- **Tiêu đề:** Hạn chế, Hướng phát triển & Q&A
- **Layout:** Two Columns (Trái: Hạn chế/Hướng phát triển - Phải: Q&A).
- **Nội dung:**
  - **Hạn chế:** Trivy/Terrascan đôi khi sinh ra báo động giả (False Positives), cần nhân sự có chuyên môn tinh chỉnh.
  - **Hướng phát triển:** 
    - Áp dụng AI/Machine Learning để phân tích log bảo mật.
    - Quản lý chính sách dưới dạng mã tập trung bằng OPA (Open Policy Agent).
  - **Thảo luận:** Mời hội đồng đặt câu hỏi.
- **Key Message:** Kết thúc bài trình bày, sẵn sàng bảo vệ đề tài.
- **Speaker Notes:** "Tất nhiên, các công cụ nguồn mở đôi khi vẫn có cảnh báo giả, đòi hỏi kỹ sư phải tinh chỉnh luật quét thường xuyên. Trong tương lai, nhóm đề xuất tích hợp thêm AI để lọc log và áp dụng OPA. Phần trình bày của nhóm 5 xin được kết thúc tại đây. Kính mời thầy và các bạn đặt câu hỏi thảo luận!"
- **Visual Suggestion:** Biểu tượng AI hoặc hình ảnh thể hiện sự hợp tác, kết thúc trang trọng.
- **Image Prompt (English):** Abstract futuristic visualization of Artificial Intelligence analyzing cyber security data logs, glowing neural network nodes and digital shields, deep blue and cyan color palette, highly professional academic presentation closing slide.
- **Design Notes:** Gọn gàng, để lại không gian để khán giả tập trung vào nhóm khi đặt câu hỏi. Tên của 5 thành viên có thể xuất hiện nhỏ ở dưới cùng.
