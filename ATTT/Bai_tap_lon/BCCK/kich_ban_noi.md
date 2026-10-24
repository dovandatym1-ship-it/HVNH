# KỊCH BẢN ĐỌC THUYẾT TRÌNH CHI TIẾT (BẢO MẬT HỆ THỐNG THÔNG TIN - NHÓM 5)

> **Hướng dẫn:** File này đã được mở rộng để đảm bảo mỗi người nói với tốc độ vừa phải sẽ lấp đầy thời lượng khoảng **3 phút/người** (tương đương 350-400 từ). Các bạn hãy tập ngắt nghỉ ở các dấu phẩy, dấu chấm và nhấn mạnh vào các từ in đậm để bài nói sinh động, chuyên nghiệp như một chuyên gia.

---
## 👨‍💼 THÀNH VIÊN 1: ĐỖ VĂN ĐẠT (Slide 1 - Slide 3) ~ 3 Phút

**Slide 1: Trang bìa**
"Kính chào thầy Vũ Duy Hiến và toàn thể các bạn học viên có mặt trong buổi học ngày hôm nay. Tôi là Đỗ Văn Đạt, đại diện cho nhóm 5 xin phép được bắt đầu phần trình bày. Đề tài của nhóm chúng tôi là một chủ đề mang tính ứng dụng rất cao và đang là xu hướng tất yếu của các ngân hàng hiện đại: **'Nghiên cứu áp dụng tự động hoá đánh giá an ninh hạ tầng mã nguồn và container image bằng Trivy, Terrascan trong quy trình GitOps cho hệ thống CRM tại VietinBank'**. Đề tài này không chỉ giải quyết bài toán về kỹ thuật mà còn là bài toán về tối ưu vận hành."

**Slide 2: Chuyển đổi số CRM & Thách thức bảo mật**
"Để bắt đầu, chúng ta hãy nhìn vào bức tranh chuyển đổi số. VietinBank hiện đang triển khai nâng cấp hệ thống Quản trị quan hệ khách hàng (CRM) nhằm đem lại trải nghiệm tốt nhất cho người dùng. Để hệ thống có thể mở rộng nhanh chóng và chịu tải tốt, ngân hàng đã chuyển dịch từ kiến trúc phần mềm nguyên khối sang **kiến trúc Cloud-native và Microservices**. Cùng với đó, quy trình phát triển linh hoạt Agile và CI/CD được áp dụng, giúp tốc độ phát hành phần mềm tính bằng ngày, thậm chí bằng giờ. 

Tuy nhiên, tốc độ cao lại mang đến một **thách thức khổng lồ về mặt bảo mật**. Trước đây, các bộ phận an toàn thông tin thường kiểm tra thủ công ở giai đoạn cuối trước khi phát hành. Nhưng với tốc độ của CI/CD hiện nay, cách làm truyền thống đó trở thành một **'nút thắt cổ chai'**. Rủi ro giờ đây không chỉ nằm ở những dòng code ứng dụng, mà nó lan rộng sang lớp Container, sang các file cấu hình hạ tầng IaC, và toàn bộ chuỗi cung ứng phần mềm. Bề mặt tấn công đang mở rộng hơn bao giờ hết."

**Slide 3: Mục tiêu & Hướng tiếp cận Shift-Left**
"Từ bối cảnh đó, nhóm 5 đặt ra mục tiêu: Xây dựng một quy trình bảo mật không phụ thuộc vào con người, mà phải được **tự động hóa 100%**. Để làm được điều này, chúng tôi áp dụng hướng tiếp cận **'Shift-Left'** - tức là dịch chuyển các lớp kiểm tra an ninh sang phía bên trái của quy trình phát triển, nghĩa là kiểm tra ngay từ lúc lập trình viên vừa gõ code xong. 

Chúng tôi đã thiết kế một giải pháp tự động quét lỗ hổng bằng các công cụ như Trivy, Terrascan và tích hợp trực tiếp vào quy trình triển khai GitOps. Qua đó, lỗi bảo mật sẽ bị chặn đứng trước khi nó kịp bước chân vào môi trường sản xuất. Vậy cụ thể, hệ thống CRM VietinBank đang có cấu trúc phức tạp ra sao mà buộc chúng ta phải bảo vệ nghiêm ngặt như vậy? Tôi xin nhường lời cho bạn Trần Ngọc Dũng sẽ phân tích sâu hơn về kiến trúc hệ thống."

---
## 👩‍💼 THÀNH VIÊN 2: TRẦN NGỌC DŨNG (Slide 4 - Slide 5) ~ 3 Phút

**Slide 4: Tổng quan Kiến trúc CRM VietinBank**
"Xin cảm ơn bạn Đạt. Xin chào thầy và các bạn, tôi là Trần Ngọc Dũng. Để hiểu vì sao rủi ro lại lớn, chúng ta cần nhìn vào **kiến trúc thực tế của hệ thống CRM**. Hiện tại, CRM 1.0 của VietinBank được tổ chức theo kiến trúc phân lớp, chạy hoàn toàn trên nền tảng điều phối container là Kubernetes hoặc OpenShift. 

Như các bạn thấy trên sơ đồ, thay vì một khối duy nhất, ứng dụng bị chia nhỏ thành hàng chục, hàng trăm Microservices. Các Microservices này không đứng độc lập mà liên tục giao tiếp với nhau và với các hệ thống lõi khác như Core Banking, Data Lake thông qua nền tảng API Gateway và Kafka. Việc phân rã này mang lại tính linh hoạt tuyệt vời cho hệ thống. Nhưng ở góc độ bảo mật, nó tạo ra **hàng ngàn điểm kết nối mạng và hàng ngàn API**. Mỗi một điểm kết nối đó, mỗi một microservice đó, đều có thể là một cánh cửa mở để hacker xâm nhập nếu không được kiểm soát tốt."

**Slide 5: Phân loại tài sản thông tin & Dữ liệu nhạy cảm**
"Với kiến trúc đồ sộ như vậy, chúng ta đang phải bảo vệ những tài sản gì? Trong hệ thống CRM, tài sản vô giá nhất, cốt lõi nhất chắc chắn là **Dữ liệu định danh khách hàng (PII)** cùng lịch sử giao dịch của họ. Nếu lộ lọt, hậu quả về uy tín và pháp lý là không thể đong đếm. 

Tuy nhiên, đó là phần nổi của tảng băng. Để bảo vệ dữ liệu khách hàng, chúng ta phải bảo vệ những **tài sản hạ tầng vô hình** nhưng cực kỳ nhạy cảm. Đó là các Container Image chứa mã nguồn. Đó là các tệp Kubernetes Manifest chứa cấu hình mạng. Và đặc biệt là các **Secrets** – tức là mật khẩu, API Keys dùng để các hệ thống nội bộ xác thực với nhau. Nếu lập trình viên vô ý để lộ một API Key trên kho chứa mã nguồn Git, kẻ tấn công có thể lợi dụng Key đó để qua mặt mọi tường lửa, chui thẳng vào cơ sở dữ liệu. Vậy cụ thể những lỗ hổng này có nguy cơ xảy ra ở mức độ nào? Bạn Tạ Ngọc Tuệ sẽ tiếp tục bài trình bày với phần phân tích rủi ro."

---
## 👨‍💻 THÀNH VIÊN 3: TẠ NGỌC TUỆ (Slide 6 - Slide 7) ~ 3 Phút

**Slide 6: Nhận diện rủi ro tại các lớp**
"Cảm ơn Dũng. Tôi là Tạ Ngọc Tuệ. Qua việc bóc tách tài sản hệ thống, nhóm chúng tôi đã khoanh vùng được các điểm rủi ro lớn nhất tại 3 khu vực. Ở lớp ngoài cùng là Lớp truy cập và API, rủi ro phổ biến là đánh cắp phiên đăng nhập hoặc cấu hình phân quyền API lỏng lẻo. 

Tuy nhiên, **tử huyệt thực sự** lại nằm sâu bên trong lớp Container và Chuỗi cung ứng phần mềm CI/CD. Trong thực tế phát triển, để cho nhanh, lập trình viên thường tái sử dụng các Base Image và thư viện nguồn mở có sẵn trên mạng. Rất nhiều trong số đó đã chứa sẵn các lỗ hổng bảo mật chưa được vá (gọi là CVE). Thứ hai, đó là các lỗi cấu hình hạ tầng IaC, ví dụ cấu hình một container chạy dưới quyền cao nhất (Root), hay vô tình mở một cổng mạng (Port) không cần thiết. Trong môi trường Kubernetes, một container bị chiếm quyền Root đồng nghĩa với việc toàn bộ cụm máy chủ có thể sụp đổ."

**Slide 7: Ma trận rủi ro trọng yếu đối với CRM**
"Để lượng hóa những nguy cơ này, chúng tôi đã sử dụng **tiêu chuẩn đánh giá rủi ro NIST SP 800-30**. Chúng tôi đối chiếu khả năng xảy ra và mức độ tác động để lập nên ma trận rủi ro. Các bạn có thể thấy ở đây, có 2 rủi ro bị bôi đỏ chót, đạt **mức điểm 20 - mức cao nhất**. 

Đó chính là rủi ro triển khai một Image chứa mã độc, và rủi ro cấu hình sai Kubernetes Manifest. Sở dĩ điểm cao như vậy vì khả năng xảy ra lỗi do con người (human error) là rất cao, và hậu quả của nó là tin tặc có thể leo thang đặc quyền, đánh cắp toàn bộ dữ liệu CRM, khiến ngân hàng vi phạm nghiêm trọng quy định an toàn thông tin của Ngân hàng Nhà nước. Rõ ràng, chúng ta không thể dựa vào việc 'nhắc nhở' lập trình viên cẩn thận hơn, mà phải có công cụ tự động ngăn chặn bằng kỹ thuật. Sau đây, bạn Nguyễn Linh Chi sẽ trình bày về giải pháp DevSecOps mà nhóm đề xuất."

---
## 👩‍💼 THÀNH VIÊN 4: NGUYỄN LINH CHI (Slide 8 - Slide 10) ~ 3 Phút

**Slide 8: Công cụ kiểm tra: Trivy, Terrascan & Cosign**
"Chào thầy và các bạn, tôi là Nguyễn Linh Chi. Để xử lý bài toán tự động hóa kiểm tra an ninh, thay vì dùng các giải pháp thương mại đắt đỏ, nhóm đề xuất một hệ sinh thái mã nguồn mở mạnh mẽ đang rất thịnh hành. Chúng ta có **Trivy** - một công cụ chuyên quét sâu vào các lớp của Container Image để moi ra mọi lỗ hổng CVE và các mật khẩu bị hardcode. Tiếp theo là **Terrascan** - một bộ máy phân tích mã tĩnh chuyên dụng cho Terraform và Kubernetes, giúp bắt quả tang mọi cấu hình vi phạm nguyên tắc bảo mật. Và cuối cùng là **Cosign** - một công cụ dùng để ký số điện tử lên Container, đóng dấu niêm phong bảo đảm Image đó là hàng thật, không bị giả mạo."

**Slide 9: Kiến trúc DevSecOps & Luồng thực thi**
"Ba công cụ này phối hợp với nhau tạo ra một quy trình **Pipeline 9 bước hoàn toàn tự động**, đây cũng là cốt lõi của đề tài. Khi một lập trình viên vừa đẩy mã nguồn lên kho chứa, hệ thống CI sẽ tự động kích hoạt. Nó build ra Container Image, rồi ném Image đó cho Trivy quét, đồng thời đưa tệp cấu hình cho Terrascan quét. 

Tại đây, chúng ta thiết lập một cơ chế gọi là **'Security Gate' - bức tường lửa tự động**. Nếu Trivy hay Terrascan phát hiện bất kỳ lỗi nào ở mức Critical hay High, luồng CI sẽ báo 'Failed' ngay lập tức, chặn đứng việc phát hành. Lập trình viên bắt buộc phải sửa lỗi để được đi tiếp. Chỉ khi toàn bộ mã nguồn sạch 100%, Image mới được đẩy đi và được Cosign đóng dấu niêm phong bằng chữ ký số điện tử."

**Slide 10: Vai trò của GitOps (ArgoCD)**
"Nhưng như vậy vẫn chưa đủ an toàn nếu ai đó có thể vào Production sửa thủ công. Do đó, bước cuối cùng chúng tôi sử dụng mô hình **GitOps với công cụ ArgoCD**. Ngoại trừ ArgoCD, không một lập trình viên hay kỹ sư hệ thống nào được cấp quyền can thiệp vào cụm Kubernetes. ArgoCD sẽ đóng vai trò người vận chuyển tự động. Hơn thế nữa, nó được cài đặt một bộ lọc (Admission Controller) để **từ chối thả cửa** cho bất kỳ Image nào không có chữ ký hợp lệ của Cosign. Từ khâu viết code cho đến khâu chạy thực tế, mã độc hoàn toàn bị cách ly. Phần đánh giá tính hiệu quả thực tiễn, tôi xin mời bạn Trương An Ninh."

---
## 👨‍🏫 THÀNH VIÊN 5: TRƯƠNG AN NINH (Slide 11 - Slide 12) ~ 3 Phút

**Slide 11: Hiệu quả & Lợi ích đạt được**
"Chào thầy và các bạn, tôi là Trương An Ninh. Qua thiết kế kiến trúc như trên, chúng ta có thể thấy giải pháp này mang lại những lợi ích đột phá cho hệ thống CRM. Thứ nhất, cơ chế Shift-Left giúp chúng ta **phát hiện và loại bỏ đến 80% rủi ro** ngay từ trong trứng nước, chi phí và thời gian sửa lỗi của lập trình viên giảm đi rất nhiều so với việc hệ thống đã lên Production rồi mới bị phát hiện lỗi.

Thứ hai, việc tự động hóa toàn bộ quá trình quét và triển khai giúp ngân hàng duy trì được tốc độ phát hành cực nhanh của phương pháp Agile mà không phải đánh đổi bằng sự yếu kém của an ninh mạng. Và điều quan trọng nhất, hệ thống CRM được bảo vệ toàn vẹn từ trong ra ngoài, giúp VietinBank tuân thủ hoàn toàn các tiêu chuẩn quốc tế như ISO 27001 và các quy định khắt khe của Ngân hàng Nhà nước."

**Slide 12: Hạn chế, Hướng phát triển & Q&A**
"Tất nhiên, trong thực tế vận hành, giải pháp này vẫn còn một số điểm giới hạn. Việc sử dụng các công cụ rà quét tự động đôi khi sinh ra các cảnh báo giả (False Positives), gây ức chế cho lập trình viên. Nó đòi hỏi các chuyên gia bảo mật phải thường xuyên ngồi lại để tinh chỉnh các bộ luật (Rules) cho phù hợp với đặc thù nghiệp vụ.

Về định hướng tương lai, nhóm chúng tôi đề xuất áp dụng công nghệ **Trí tuệ nhân tạo (AI/ML)** để hệ thống có khả năng tự học các cảnh báo giả, từ đó lọc log thông minh hơn. Đồng thời, triển khai thêm OPA (Open Policy Agent) để đưa toàn bộ các chính sách bảo mật của ngân hàng thành các dòng lệnh (Policy as Code). 

Trên đây là toàn bộ công trình nghiên cứu của Nhóm 5 về đề tài DevSecOps và GitOps. Chúng em xin chân thành cảm ơn sự hướng dẫn tận tình của thầy Vũ Duy Hiến và sự chú ý lắng nghe của các bạn học viên. Sau đây, kính mời hội đồng và các bạn đặt câu hỏi để nhóm có cơ hội làm rõ hơn các vấn đề của đề tài!"
