# Chương 4: Điện toán Đám mây (Cloud Computing) Toàn tập
**Học phần:** Công nghệ mới nổi và Đổi mới (CNM / MIS01)
**Học viện Ngân hàng (Banking Academy of Vietnam - HVNH)**
**Nguồn bài giảng gốc:** `4_Điện toán đám mây.pdf`

---

## Slide 1: Điện toán đám mây

ĐINH Trọng Hiếu

---

## Slide 2: Tổng quan về Điện toán

đám mây
Điện toán đám mây là mô hình cung cấp tài nguyên điện toán như mạng,
máy chủ, lưu trữ, ứng dụng và dịch vụ theo yêu cầu qua Internet. Các dịch vụ
quen thuộc như Gmail, Google Drive, Dropbox, Netflix và các nền tảng AWS,
Azure, GCP đều là những ví dụ điện toán đám mây điển hình.
Điện toán đám mây phát triển từ các trung tâm dữ liệu truyền thống, tiến tới
ảo hóa và mô hình đám mây hiện đại, giúp tối ưu hóa tài nguyên và tăng hiệu
quả sử dụng.

---

## Slide 3: Các mô hình dịch vụ Điện toán đám mây

IaaS - Infrastructure as a
Service
PaaS - Platform as a Service
SaaS - Software as a Service
Nền tảng phát triển và quản lý ứng dụng
Ứng dụng hoàn chỉnh cung cấp qua
Cung cấp tài nguyên cơ bản như máy
mà không cần quản lý cơ sở hạ tầng.
Internet, không cần cài đặt hoặc quản lý
ảo, lưu trữ, mạng. Người dùng kiểm soát
hệ điều hành và ứng dụng.
- Amazon EC2
- Microsoft Azure Virtual Machines
- Google Compute Engine
- AWS Elastic Beanstalk
- Google App Engine
phần mềm.
- Gmail
- 
Salesforce
- Microsoft Azure App Service
- Dropbox
- Google Workspace

---

## Slide 4: Các mô hình triển khai Điện

toán đám mây
Đám mây công cộng
Cơ sở hạ tầng thuộc sở hữu nhà cung cấp, phục vụ công chúng như AWS,
Azure, GCP.
Đám mây riêng
Cơ sở hạ tầng dùng riêng cho tổ chức, có thể quản lý nội bộ hoặc bên thứ ba.
Đám mây lai
Kết hợp đám mây công cộng và riêng, chia sẻ dữ liệu và ứng dụng linh hoạt.
Đám mây cộng đồng
Cơ sở hạ tầng chia sẻ giữa các tổ chức có cùng mối quan tâm về bảo mật hoặc
chính sách.

---

## Slide 5: Lịch sử Điện toán Đám mây

Điện toán đám mây đã phát triển từ những ngày đầu của điện toán, khi máy tính lớn có thể truy cập từ xa thông qua thiết bị đầu cuối.
Tuy nhiên, khái niệm hiện đại về điện toán đám mây như ta biết ngày nay bắt đầu hình thành vào những năm 1990 và đầu những năm
2000, khi công nghệ internet phát triển và nhu cầu về các giải pháp điện toán hiệu quả, có khả năng mở rộng ngày càng tăng.

---

## Slide 6: Máy tính khách/Máy chủ: Tiền thân của Điện toán

Đám mây
Trước khi điện toán đám mây xuất hiện, mô hình máy tính khách/máy chủ là phương pháp chủ đạo. Trong kiến trúc này, máy chủ đóng vai
trò trung tâm cho tất cả các chương trình phần mềm, dữ liệu và điều khiển. Người dùng kết nối với máy chủ để truy cập dữ liệu hoặc chạy
chương trình. Mặc dù điện toán mạng được xây dựng trên nền tảng này, nó vẫn còn hạn chế về hiệu quả tài nguyên và khả năng mở rộng.
Máy chủ trung tâm
Hạn chế
Lưu trữ tất cả phần mềm và dữ liệu
Khó mở rộng và kém hiệu quả về tài nguyên
Kết nối người dùng
Truy cập từ xa thông qua thiết bị đầu cuối

---

## Slide 7: Điện toán Phân tán

Khi máy tính ngày càng được kết nối mạng, ý tưởng về điện toán phân tán phát triển. Mô hình này cho phép nhiều máy tính hợp
tác, chia sẻ tài nguyên và sức mạnh xử lý. Điện toán phân tán mang lại khả năng xử lý song song và tăng hiệu quả bằng cách phân
chia các tác vụ trên nhiều bộ xử lý khác nhau. Sự chuyển đổi từ phương pháp tập trung sang phân tán đã mở ra cánh cửa cho các
cấu trúc máy tính có khả năng mở rộng và thích ứng hơn.
Kết nối mạng
Chia sẻ tài nguyên
Xử lý song song
Máy tính được liên kết với nhau
Hợp tác và phân phối công việc
Tăng hiệu quả và khả năng mở rộng

---

## Slide 8: Điện toán Đám mây

Điện toán đám mây phát triển từ nền tảng của mô hình máy khách/máy chủ và điện toán
phân tán. Mục tiêu chính là cung cấp quyền truy cập theo yêu cầu dựa trên mạng, chủ yếu là
Internet, vào các tài nguyên và dịch vụ máy tính dùng chung. Điện toán đám mây hướng
đến việc cung cấp cho người dùng quyền truy cập linh hoạt, có thể mở rộng và tiết kiệm vào
các tài nguyên máy tính, lưu trữ và ứng dụng. Nó chuyển trọng tâm từ cơ sở hạ tầng và
quyền sở hữu cục bộ sang các dịch vụ từ xa và mô hình kinh doanh trả tiền theo sử dụng.
Truy cập theo yêu cầu
Khả năng mở rộng
Tài nguyên có sẵn khi cần
Dễ dàng tăng giảm tài nguyên
Tiết kiệm chi phí
Mô hình trả tiền theo sử dụng
Dịch vụ từ xa
Truy cập qua Internet

---

## Slide 9: Tầm nhìn Ban đầu về Điện toán Đám mây

Ý tưởng về máy tính như một tiện ích, tương đương với nước hoặc điện, đã được đề xuất từ năm 1961 bởi nhà khoa học máy tính John
McCarthy tại MIT. Ông đề xuất rằng các nguồn tài nguyên máy tính có thể được mua và bán theo yêu cầu. Tuy nhiên, vào thời điểm đó,
công nghệ chưa đủ phát triển để hỗ trợ mục tiêu này. Mặc dù là một ý tưởng tuyệt vời, nó đi trước thời đại; trong vài thập kỷ tiếp theo,
mặc dù có sự quan tâm đến mô hình này, công nghệ vẫn chưa sẵn sàng cho nó.
John McCarthy đề xuất ý tưởng máy tính như tiện ích
1961
Cuối thế kỷ 20
Công nghệ bắt đầu đuổi kịp tầm nhìn
Những năm tiếp theo
Ý tưởng được quan tâm nhưng chưa thể thực hiện

---

## Slide 10: Salesforce.com và Sự Phát triển của Ứng

dụng Đám mây
Salesforce.com đã biến đổi ngành phần mềm vào năm 1999 bằng cách cung cấp các ứng dụng qua internet. Chiến lược sáng tạo
của họ cho phép các doanh nghiệp có được phần mềm thông qua một trang web đơn giản, loại bỏ yêu cầu cài đặt tại chỗ khó
khăn. Đây là một bước quan trọng hướng tới việc biến ý tưởng về điện toán như một tiện ích thành hiện thực, cho phép các công
ty sử dụng các ứng dụng dựa trên đám mây mà không phải lo lắng về việc quản lý cơ sở hạ tầng.
Ứng dụng trên đám mây
Giao diện web
Quản lý từ xa
Truy cập qua internet
Sử dụng thông qua trình duyệt
Không cần cài đặt tại chỗ

---

## Slide 11: Amazon Web Services (AWS) Cách mạng hóa Đám

mây
Amazon Web Services (AWS) ra mắt vào năm 2002, ban đầu cung cấp dịch vụ điện toán và lưu trữ. Tuy nhiên, sự ra mắt của Elastic Compute Cloud
(EC2) vào năm 2006 mới thực sự là cuộc cách mạng hóa điện toán đám mây. EC2 cho phép người dùng thuê máy chủ ảo khi cần, cung cấp giải
pháp có khả năng mở rộng và tiết kiệm chi phí. Sự thành công của AWS minh họa cho lời hứa hẹn của điện toán đám mây và truyền cảm hứng cho
sự phát triển nhanh chóng của các dịch vụ đám mây.
2002
Sau 2006
AWS ra mắt với dịch vụ cơ bản
Phát triển nhanh chóng của dịch vụ đám mây
2006
EC2 được giới thiệu, mang tính cách mạng

---

## Slide 12: Mở rộng Dịch vụ Đám mây

Sau Amazon, nhiều công ty lớn khác đã tham gia vào lĩnh vực điện toán đám mây. Google Apps bắt đầu cung cấp các ứng dụng
doanh nghiệp dựa trên đám mây vào năm 2009. Microsoft giới thiệu Windows Azure cùng năm đó. Các doanh nghiệp như Oracle
và HP cũng áp dụng điện toán đám mây, cung cấp nhiều dịch vụ khác nhau. Sự hiện diện của những công ty lớn này trong toàn
ngành đã thúc đẩy việc áp dụng điện toán đám mây trong nhiều lĩnh vực.
Google Apps
Windows Azure
Các công ty khác
Ứng dụng văn phòng và cộng tác trên
Nền tảng điện toán đám mây của
Oracle, HP mở rộng dịch vụ đám mây
đám mây
Microsoft

---

## Slide 13: Ứng dụng Điện toán Đám mây Phổ biến

Việc áp dụng điện toán đám mây được thể hiện qua việc các doanh nghiệp ở mọi quy mô đang tận dụng lợi thế của nó. Khả năng
mở rộng, tính linh hoạt, hiệu quả về chi phí và cải thiện khả năng cộng tác là những lợi ích chính. Doanh nghiệp có thể dễ dàng
liên kết dịch vụ, lưu trữ và phân tích dữ liệu lớn, tăng giảm tài nguyên khi cần và triển khai ứng dụng nhanh chóng. Điện toán
đám mây đã thay đổi hoạt động của tổ chức, thúc đẩy đổi mới, tăng tính linh hoạt và giảm chi phí.
Khả năng mở rộng
Tiết kiệm chi phí
Dễ dàng tăng giảm tài nguyên theo nhu cầu
Giảm đầu tư cơ sở hạ tầng ban đầu
3 Cộng tác hiệu quả
4 Đổi mới nhanh chóng
Truy cập và chia sẻ dữ liệu từ mọi nơi
Triển khai ứng dụng và dịch vụ mới dễ dàng

---

## Slide 14: Các nhà cung cấp dịch vụ

Điện toán đám mây phổ
biến
Thị trường điện toán đám mây hiện nay được dẫn đầu bởi ba nhà cung cấp
lớn: Amazon Web Services (AWS), Microsoft Azure và Google Cloud
Platform (GCP).
Họ cung cấp đa dạng dịch vụ và giải pháp đám mây, phục vụ nhu cầu của
doanh nghiệp từ nhỏ đến lớn trên toàn cầu.

---

## Slide 15: Xu hướng và Đổi mới trong Tương lai

Điện toán đám mây tiếp tục phát triển với các công nghệ mới nổi và yêu cầu kinh doanh thay đổi. Điện toán biên đang trở nên phổ biến, cho phép phân tích dữ liệu thời gian thực và độ trễ thấp.
Điện toán không máy chủ tập trung vào viết mã thay vì quản lý cơ sở hạ tầng. Công nghệ container hóa như Docker và Kubernetes cung cấp tính di động và đơn giản trong triển khai. AI và ML dựa
trên đám mây đang định hình tương lai, cho phép phân tích dữ liệu phức tạp, tự động hóa và dự đoán. Các vấn đề về bảo mật, quyền riêng tư dữ liệu và tuân thủ quy định đang được chú trọng, với
các nhà cung cấp đầu tư vào biện pháp bảo mật mạnh mẽ.
Xu hướng
Điện toán biên
Điện toán không máy chủ
AI/ML trên đám mây
Lợi ích
Phân tích thời gian thực
Tập trung vào mã
Phân tích nâng cao
Thách thức
Quản lý phân tán
Phụ thuộc nhà cung cấp
Yêu cầu dữ liệu lớn

---

## Slide 16: Lợi ích của Điện

toán Đám mây
Điện toán đám mây đang mang lại nhiều lợi ích đáng kể cho các
doanh nghiệp và tổ chức. Từ việc cải thiện khả năng sao lưu và phục
hồi dữ liệu, tăng cường sự cộng tác, đến việc cung cấp khả năng tiếp
cận tuyệt vời và tiết kiệm chi phí bảo trì, công nghệ này đang thay đổi
cách chúng ta làm việc và quản lý thông tin.

---

## Slide 17: Lợi ích của Điện toán đám mây

Tiết kiệm chi phí
Không cần đầu tư phần
Tính linh hoạt và mở
rộng
Truy cập mọi lúc mọi
nơi
Dễ khôi phục
cứng và cơ sở hạ tầng ban
Dễ dàng điều chỉnh tài
Dịch vụ có thể truy cập từ
Dễ dàng sao lưu và khôi
đầu.
nguyên theo nhu cầu thực
bất kỳ đâu có kết nối
phục dữ liệu khi cần thiết.
tế.
Internet.
Điện toán đám mây giúp doanh nghiệp tập trung vào nghiệp vụ cốt lõi, giảm gánh nặng quản lý CNTT.

---

## Slide 18: Sao lưu và Phục hồi Dữ liệu

Hiệu quả
Sao lưu Nhanh chóng
Điện toán đám mây cho phép sao lưu dữ liệu một cách nhanh
chóng và tự động, giảm thiểu rủi ro mất dữ liệu.
Lưu trữ An toàn
Dữ liệu được lưu trữ an toàn trên các máy chủ đám mây, bảo vệ
khỏi các mối đe dọa vật lý và kỹ thuật số.
Khôi phục Dễ dàng
Trong trường hợp mất dữ liệu hoặc lỗi hệ thống, việc khôi phục dữ
liệu trở nên đơn giản và nhanh chóng.

---

## Slide 19: Cải thiện Sự Cộng tác

Chia sẻ Thông tin
Làm việc Đồng thời
Lưu trữ Tập trung
Công nghệ đám mây cho phép các
Nhiều người dùng có thể cùng làm
Dữ liệu được lưu trữ tập trung trên
nhóm chia sẻ thông tin một cách dễ
việc trên các tài liệu và dự án một
đám mây, giúp mọi người trong
dàng và nhanh chóng, không bị giới
cách đồng thời, tăng cường hiệu
nhóm luôn có quyền truy cập vào
hạn bởi địa lý.
quả và năng suất.
phiên bản mới nhất của tài liệu.

---

## Slide 20: Khả năng Tiếp cận tốt

Truy cập Mọi lúc, Mọi nơi
Người dùng có thể truy cập dữ liệu của họ từ bất kỳ đâu trên thế giới
có kết nối internet, mang lại sự linh hoạt tối đa.
2 Hỗ trợ Làm việc Từ xa
Điện toán đám mây tạo điều kiện thuận lợi cho việc làm việc từ xa,
cho phép nhân viên làm việc hiệu quả bất kể vị trí địa lý.
3 Đồng bộ hóa Đa thiết bị
Dữ liệu được đồng bộ hóa tự động giữa các thiết bị, đảm bảo người
dùng luôn có thông tin mới nhất trên mọi thiết bị họ sử dụng.

---

## Slide 21: Tiết kiệm chi phí

Giảm Chi phí Phần cứng
Tiết kiệm Chi phí Phần mềm
Doanh nghiệp không cần đầu tư vào cơ sở hạ tầng
Các ứng dụng và phần mềm được cung cấp như một
phần cứng đắt tiền, giúp tiết kiệm đáng kể chi phí ban
dịch vụ, loại bỏ nhu cầu mua và duy trì giấy phép phần
đầu.
mềm riêng lẻ.
Bảo trì Tự động
Tối ưu hóa Nguồn lực IT
Nhà cung cấp dịch vụ đám mây quản lý việc bảo trì và
Đội ngũ IT có thể tập trung vào các dự án chiến lược
cập nhật, giúp doanh nghiệp tiết kiệm thời gian và
thay vì phải lo lắng về việc bảo trì hệ thống hàng ngày.
nguồn lực.

---

## Slide 22: Tính Di động và Linh hoạt

Truy cập Di động
Người dùng có thể dễ dàng truy cập và kiểm soát ứng dụng và dữ liệu dựa trên đám mây từ
điện thoại thông minh và máy tính bảng.
Làm việc Linh hoạt
Khả năng làm việc từ bất kỳ đâu trên nhiều loại thiết bị khác nhau, tăng cường năng suất và
sự linh hoạt.
Đồng bộ hóa Thời gian Thực
Dữ liệu được đồng bộ hóa tự động giữa các thiết bị, đảm bảo thông tin luôn được cập nhật.

---

## Slide 23: Mô hình Trả tiền Theo

Mức Sử dụng
Đặc điểm
Lợi ích
Linh hoạt trong chi phí
Chỉ trả tiền cho dịch vụ thực
sự sử dụng
Không cần đầu tư ban đầu
Giảm rủi ro tài chính cho
lớn
doanh nghiệp
Dễ dàng mở rộng hoặc thu
Phù hợp với nhu cầu kinh
hẹp
doanh thay đổi

---

## Slide 24: Dung lượng Lưu trữ Có thể

Mở rộng
Lưu trữ Linh hoạt
Doanh nghiệp có thể dễ dàng tăng hoặc giảm dung lượng lưu trữ
theo nhu cầu.
Quản lý Đa dạng Dữ liệu
Hỗ trợ lưu trữ nhiều loại dữ liệu khác nhau như tài liệu, ảnh, âm
thanh, video.
Tối ưu hóa Chi phí
Chỉ trả tiền cho dung lượng thực sự sử dụng, tiết kiệm chi phí
đáng kể.

---

## Slide 25: Tăng cường Bảo mật Dữ

liệu
1 Mã hóa Tiên tiến
Dữ liệu được mã hóa trong quá trình truyền tải và lưu trữ, bảo vệ
khỏi truy cập trái phép.
Kiểm soát Truy cập
Hệ thống quản lý quyền truy cập chặt chẽ, đảm bảo chỉ những
người được ủy quyền mới có thể truy cập dữ liệu.
3 Giám sát Liên tục
Hệ thống được giám sát 24/7 để phát hiện và ngăn chặn các
mối đe dọa bảo mật tiềm ẩn.

---

## Slide 26: Thân thiện với Môi trường

Trung tâm Dữ liệu Hiệu quả
Giảm Khí thải Carbon
Giảm thiểu Rác thải Điện tử
Các nhà cung cấp dịch vụ đám mây
Bằng cách tối ưu hóa việc sử dụng tài
Việc sử dụng tài nguyên chung và kéo
vận hành trung tâm dữ liệu quy mô
nguyên và áp dụng công nghệ tiên
dài tuổi thọ thiết bị trong môi trường
lớn được thiết kế để tiết kiệm năng
tiến, điện toán đám mây góp phần
đám mây giúp giảm đáng kể lượng
lượng, giúp giảm mức sử dụng năng
giảm đáng kể lượng khí thải carbon
rác thải điện tử được tạo ra.
lượng tổng thể.
so với các phương pháp truyền thống.

---

## Slide 27: Hạn chế của điện

toán đám mây
Điện toán đám mây mang lại nhiều lợi ích, nhưng cũng có những hạn
chế. Các tổ chức cần cân nhắc trước khi sử dụng.

---

## Slide 28: Độ tin cậy và thời gian

ngừng hoạt động
Khó khăn kỹ thuật
Nhà cung cấp có thể gặp sự cố do vấn đề kỹ thuật.
Bảo trì
Thời gian bảo trì có thể gây gián đoạn dịch vụ.
Tấn công mạng
Các cuộc tấn công có thể làm ngưng trệ hoạt động.

---

## Slide 29: Phụ thuộc vào Internet

Kết nối nhanh
Cần đường truyền internet tốc độ cao để truy cập dịch vụ đám
mây.
Độ tin cậy
Sự cố kết nối có thể gây gián đoạn hoạt động kinh doanh.
Phụ thuộc
Hoạt động bị ảnh hưởng nếu mất kết nối internet.

---

## Slide 30: Kiểm soát và tùy chỉnh hạn chế

Dịch vụ chuẩn hóa
Ít khả năng tùy chỉnh
Kiểm soát hạn chế
Nhà cung cấp thường cung cấp các
Khó sửa đổi dịch vụ cho phù hợp với
Tổ chức ít kiểm soát cơ sở hạ tầng
dịch vụ và nền tảng tiêu chuẩn.
nhu cầu đặc biệt.
và bảo mật.

---

## Slide 31: Bảo mật dữ liệu và quyền

riêng tư
Dữ liệu nhạy cảm
Lo ngại khi lưu trữ thông tin quan trọng trên đám mây.
Tin tưởng nhà cung cấp
Phải dựa vào quy trình bảo mật của bên thứ ba.
Rủi ro vi phạm
Truy cập trái phép có thể gây hậu quả nghiêm trọng.

---

## Slide 32: Chi phí ẩn và mô hình

định giá
Phí truyền dữ liệu
Chi phí lưu trữ bổ sung
Phí hỗ trợ chuyên biệt
Chi phí tuân thủ quy định
Mô hình trả tiền theo sử dụng có thể tiết kiệm, nhưng cần cảnh giác
với chi phí phát sinh.

---

## Slide 33: Sự phụ thuộc vào nhà cung

cấp
Độ tin cậy
Phụ thuộc vào sự ổn định của nhà cung cấp.
Thay đổi chính sách
Có thể bị ảnh hưởng nếu nhà cung cấp thay đổi điều khoản.
Khó chuyển đổi
Gặp khó khăn khi muốn chuyển sang nhà cung cấp khác.

---

## Slide 34: Vị trí dữ liệu và sự tuân thủ

Lưu trữ toàn cầu
Dữ liệu có thể được lưu trữ ở nhiều quốc gia khác nhau.
Luật pháp khác biệt
Mỗi khu vực có luật bảo vệ dữ liệu riêng.
Vấn đề tuân thủ
Khó đảm bảo tuân thủ khi dữ liệu nằm ở nhiều nơi.

---

## Slide 35: Kiến trúc điện

toán đám mây

---

## Slide 36: Kiến trúc điện toán đám mây

- Điện toán đám mây cho phép lưu trữ và
truy cập thông tin từ xa thông qua mạng
máy tính.
- Kết hợp kiến trúc hướng dịch vụ (SOA)
và hướng sự kiện (Event-Driven
Architecture - EDA).
- Kiến trúc này gồm hai phần chính: Front
End và Back End.

---

## Slide 37: Front End

Giao diện người dùng
Thiết bị truy cập
3 Kết nối
Front End bao gồm các giao
Trình duyệt web, máy khách
Front End kết nối với Back End
diện và ứng dụng phía máy
(mỏng và dày), máy tính bảng,
thông qua mạng internet.
khách để truy cập vào nền
thiết bị di động.
tảng điện toán đám mây.

---

## Slide 38: Back End

Quản lý tài nguyên
Back End  được dùng bởi nhà cung cấp dịch vụ, nhằm quản lý
các tài nguyên cần thiết cho dịch vụ đám mây.
Thành phần
Bao gồm lưu trữ dữ liệu, cơ chế bảo mật, máy ảo, các mô hình
triển khai, các máy chủ, ...
3 Kiểm soát
Cơ chế kiểm soát lưu lượng và vận hành hệ thống.

---

## Slide 39: Các thành phần

của kiến trúc điện
toán đám mây
Kiến trúc điện toán đám mây bao gồm nhiều thành phần quan trọng,
tạo nên một hệ thống phức tạp và hiệu quả. Từ cơ sở hạ tầng của
khách hàng đến bảo mật và quản lý, mỗi phần đóng vai trò thiết yếu
trong việc cung cấp dịch vụ đám mây linh hoạt và đáng tin cậy. Hãy
cùng tìm hiểu chi tiết về từng thành phần này và cách chúng hoạt
động cùng nhau để tạo nên một hệ thống điện toán đám mây hoàn
chỉnh.

---

## Slide 40: Cơ sở hạ tầng của khách hàng

Front-end
Giao diện người dùng
Tương tác
Cơ sở hạ tầng của khách hàng là
Nó cung cấp Giao diện người
Thông qua giao diện này, người
thành phần Front-end trong kiến
dùng đồ họa (GUI) để người dùng
dùng có thể truy cập và sử dụng
trúc điện toán đám mây.
có thể tương tác với đám mây
các dịch vụ đám mây một cách
một cách trực quan và dễ dàng.
thuận tiện.

---

## Slide 41: Ứng dụng và dịch vụ đám mây

Ứng dụng
Dịch vụ
Loại dịch vụ
Phần mềm hoặc nền tảng mà khách
Quản lý loại dịch vụ theo yêu cầu
SaaS, PaaS, IaaS - đáp ứng nhu cầu
hàng muốn truy cập.
của khách hàng.
đa dạng.

---

## Slide 42: Phần mềm dưới dạng dịch vụ

(SaaS)
Truy cập trực tuyến
Chạy trực tiếp thông qua trình duyệt web.
Lưu trữ đám mây
Không cần tải xuống và cài đặt ứng dụng.
Ví dụ
Google Apps, Salesforce, Dropbox, Slack, Hubspot.

---

## Slide 43: Nền tảng dưới dạng dịch vụ (PaaS)

Nền tảng phát triển
Khác biệt với SaaS
Ví dụ
Cung cấp môi trường để tạo phần
Tập trung vào nền tảng hơn là phần
Windows Azure, Force.com, Magento
mềm.
mềm sẵn có.
Commerce Cloud, OpenShift.

---

## Slide 44: Cơ sở hạ tầng dưới dạng

dịch vụ (IaaS)
Chức năng
Ưu điểm
Ví dụ
Quản lý dữ liệu, phần mềm
trung gian, môi trường thời
gian chạy
Linh hoạt, kiểm soát cao
Amazon Web Services (AWS)
EC2, Google Compute Engine
(GCE)

---

## Slide 45: Runtime Cloud

Môi trường thực thi
Runtime Cloud cung cấp môi trường thực thi cho các
ứng dụng và dịch vụ đám mây.
Quản lý máy ảo
Nó quản lý việc tạo, vận hành và hủy bỏ các máy ảo
theo nhu cầu của người dùng.
Tối ưu hóa tài nguyên
Đám mây thời gian chạy đảm bảo việc phân bổ và sử
dụng tài nguyên một cách hiệu quả.

---

## Slide 46: Lưu trữ đám mây

Dung lượng lớn
Lưu trữ đám mây cung cấp dung lượng khổng lồ để lưu trữ và
quản lý dữ liệu của người dùng và ứng dụng.
Tính linh hoạt
Người dùng có thể dễ dàng mở rộng hoặc thu hẹp dung lượng
lưu trữ theo nhu cầu thực tế.
Bảo mật và sao lưu
Hệ thống lưu trữ đám mây thường đi kèm với các tính năng
bảo mật cao cấp và sao lưu tự động.

---

## Slide 47: Cơ sở hạ tầng đám mây

Máy chủ
Cung cấp sức mạnh tính toán cho toàn bộ hệ thống đám mây.
Mạng
Kết nối các thành phần và cho phép truyền dữ liệu nhanh chóng.
Ảo hóa
Phần mềm ảo hóa giúp tối ưu hóa việc sử dụng tài nguyên vật lý.
Cơ sở hạ tầng đám mây bao gồm các thành phần phần cứng và phần mềm như máy chủ, lưu trữ, thiết bị mạng, phần
mềm ảo hóa và các tài nguyên lưu trữ khác cần thiết để hỗ trợ mô hình điện toán đám mây. Nó cung cấp các dịch vụ ở
cấp độ máy chủ, cấp độ ứng dụng và cấp độ mạng.

---

## Slide 48: Quản lý đám mây

Giám sát
Theo dõi hiệu suất và tình trạng của các thành phần đám mây.
Điều phối
Thiết lập và duy trì sự phối hợp giữa các thành phần khác nhau.
Tối ưu hóa
Điều chỉnh cấu hình để đảm bảo hiệu suất tốt nhất.
Báo cáo
Tạo báo cáo về việc sử dụng và hiệu suất của hệ thống.

---

## Slide 49: Bảo mật đám mây

Mã hóa dữ liệu
Xác thực đa yếu tố
Tường lửa
Giám sát liên tục
Bảo vệ thông tin nhạy cảm
Tăng cường bảo mật truy cập
Ngăn chặn truy cập trái phép
Phát hiện và ứng phó với các mối đe dọa
Bảo mật là thành phần back-end tích hợp của điện toán đám mây. Nó triển khai các cơ chế bảo mật ở phía sau để đảm
bảo an toàn cho dữ liệu và tài nguyên của người dùng. Các biện pháp bảo mật này bao gồm mã hóa dữ liệu, xác thực đa
yếu tố, tường lửa và giám sát liên tục để phát hiện và ngăn chặn các mối đe dọa tiềm ẩn.

---

## Slide 50: Mạng Internet

Kết nối toàn cầu
Truyền dữ liệu
Liên kết các thành phần
Internet là mạng lưới kết nối toàn cầu,
Mạng Internet đóng vai trò quan
Internet là phương tiện để front-end
cho phép truy cập đám mây từ mọi
trọng trong việc truyền tải dữ liệu
và back-end có thể tương tác và giao
nơi.
giữa người dùng và đám mây.
tiếp với nhau trong hệ thống đám
mây.

---

## Slide 51: Tổng kết về kiến trúc điện toán đám mây

Front-end
Quản lý và Bảo mật
Bao gồm cơ sở hạ tầng của khách hàng và
Đảm bảo hoạt động hiệu quả và an toàn của
giao diện người dùng.
toàn bộ hệ thống.
Back-end
Kết nối
Gồm ứng dụng, dịch vụ, đám mây thời gian
Internet đóng vai trò quan trọng trong việc liên
chạy, lưu trữ và cơ sở hạ tầng.
kết tất cả các thành phần.
Kiến trúc điện toán đám mây là một hệ thống phức tạp, bao gồm nhiều thành phần tương tác chặt chẽ với nhau. Từ giao diện người
dùng đến cơ sở hạ tầng back-end, mỗi phần đều đóng vai trò quan trọng trong việc cung cấp dịch vụ đám mây linh hoạt, hiệu quả và
an toàn. Sự kết hợp hài hòa giữa các thành phần này tạo nên nền tảng cho các ứng dụng và dịch vụ đám mây hiện đại.

---

## Slide 52: Dịch vụ và Công

nghệ Điện toán
Đám mây
Điện toán đám mây đang thay đổi cách chúng ta sử dụng công nghệ. Ảo
hóa là một công nghệ quan trọng trong lĩnh vực này.

---

## Slide 53: Ảo hóa

Kiến trúc hướng dịch vụ
Điện toán lưới
Máy tính tiện ích
Container và điều phối
Dữ liệu lớn
Điện toán không máy chủ
Internet vạn vật (IoT)

---

## Slide 54: Ảo hóa

Định nghĩa
Ảo hóa tạo môi trường ảo để chạy nhiều ứng dụng và hệ điều hành
trên cùng một máy chủ.
Máy ảo
Máy ảo là máy tính phần mềm hoạt động như máy tính vật lý, thực
hiện các tác vụ theo yêu cầu.

---

## Slide 55: Ảo hóa Phần cứng

Khái niệm
Nhiều máy ảo chạy trên một máy chủ vật lý duy nhất.
Lợi ích
Tách biệt tài nguyên phần cứng vật lý, hợp nhất máy chủ và sử
dụng tài nguyên hiệu quả.

---

## Slide 56: Ảo hóa Máy chủ

Bước 1
Chia máy chủ vật lý thành nhiều máy chủ ảo hoặc VM.
Bước 2
Mỗi máy chủ ảo chạy hệ điều hành và ứng dụng riêng.
Kết quả
Tăng hiệu quả máy chủ và hợp lý hóa quản trị.

---

## Slide 57: Ảo hóa Lưu trữ

Mục đích
Lợi ích
Tạo nhóm lưu trữ ảo hóa bằng cách trừu tượng hóa tài
Cải thiện khả năng mở rộng, tính linh hoạt và đơn giản
nguyên lưu trữ vật lý.
hóa quản lý.

---

## Slide 58: Ảo hóa Hệ điều hành

Vùng chứa
Cho phép hệ điều hành lưu trữ nhiều phiên bản không gian người dùng tách biệt.
Hiệu suất
Thời gian khởi động nhanh hơn và chi phí thấp hơn.
Nhẹ nhàng
Cung cấp khả năng ảo hóa vừa nhẹ vừa hiệu quả.

---

## Slide 59: Ảo hóa Dữ liệu

Trích xuất
Lấy dữ liệu từ nhiều nguồn khác nhau.
Tích hợp
Tạo bức tranh ảo gắn kết từ dữ liệu đã trích xuất.
Truy cập
Người dùng và chương trình có thể truy cập và thay đổi dữ
liệu.

---

## Slide 60: Ảo hóa hoạt động như thế

nào?
- Ảo hóa là một công nghệ quan trọng cho phép các công ty tối ưu hóa việc sử dụng tài nguyên
máy tính của họ.
- Bằng cách hợp nhất các máy chủ vật lý, ảo hóa giúp giảm chi phí phần cứng và cải thiện hiệu
quả sử dụng tài nguyên.
- Ảo hóa cũng cho phép triển khai nhanh chóng các máy ảo (VM) mới cho các mục đích khác
nhau mà không cần đầu tư vào phần cứng mới.

---

## Slide 61: Cài đặt Hypervisor

Bước đầu tiên trong quá trình ảo hóa là cài đặt hypervisor - một phần mềm chuyên dụng đóng vai trò quan trọng trong việc quản lý và
phân bổ tài nguyên của máy chủ vật lý. Hypervisor hoạt động như một lớp trung gian giữa phần cứng vật lý và các máy ảo, đảm bảo rằng
mỗi VM nhận được đúng lượng tài nguyên cần thiết.
Hypervisor quản lý các tài nguyên quan trọng như CPU, bộ nhớ và lưu trữ, phân phối chúng một cách hiệu quả giữa các VM đang chạy
trên máy chủ. Điều này cho phép tối ưu hóa việc sử dụng tài nguyên và tăng hiệu suất tổng thể của hệ thống.
Cài đặt Hypervisor
Phần mềm hypervisor được cài đặt trực tiếp trên máy
chủ vật lý.
Quản lý tài nguyên
Hypervisor bắt đầu quản lý và phân bổ tài nguyên của
máy chủ vật lý.
Khởi tạo Hypervisor
Hypervisor được cấu hình và khởi động, sẵn sàng quản
lý tài nguyên.

---

## Slide 62: Tạo máy ảo

Sau khi hypervisor được cài đặt, bước tiếp theo là tạo các máy ảo (VM). Mỗi VM hoạt động như một máy tính độc lập với hệ điều hành
và ứng dụng riêng. Hypervisor tạo ra một môi trường ảo cho mỗi VM, cho phép chúng hoạt động như thể chúng đang chạy trên phần
cứng vật lý riêng biệt.
Một điểm quan trọng của quá trình tạo VM là sự cô lập. Mỗi VM được cô lập hoàn toàn với các VM khác, đảm bảo rằng bất kỳ sự cố
hoặc thay đổi nào trong một VM không ảnh hưởng đến hiệu suất hoặc bảo mật của các VM khác trên cùng một máy chủ vật lý.
Tạo VM
Cài đặt OS
Hypervisor tạo ra một môi trường ảo cho mỗi VM, phân bổ
Hệ điều hành được cài đặt trên mỗi VM, cho phép nó hoạt
tài nguyên cần thiết.
động độc lập.
Cô lập VM
Cài đặt ứng dụng
Các VM được cô lập với nhau, đảm bảo an toàn và ổn định
Các ứng dụng cụ thể được cài đặt trên mỗi VM theo nhu cầu
cho hệ thống.
sử dụng.

---

## Slide 63: Phân bổ và quản lý tài nguyên

Một trong những nhiệm vụ quan trọng nhất của hypervisor là phân bổ và quản lý tài nguyên một cách động. Hypervisor
liên tục theo dõi nhu cầu tài nguyên của mỗi VM và điều chỉnh phân bổ tài nguyên theo thời gian thực. Điều này đảm bảo
rằng mỗi VM nhận được đúng lượng tài nguyên cần thiết để hoạt động hiệu quả, đồng thời ngăn chặn việc một VM độc
quyền toàn bộ tài nguyên của máy chủ.
Quá trình này cho phép sử dụng hiệu quả tài nguyên của máy chủ vật lý, tối ưu hóa hiệu suất tổng thể và đảm bảo rằng tất
cả các VM có thể hoạt động mượt mà mà không bị gián đoạn.
Giám sát tài nguyên
Phân bổ động
Tối ưu hóa hiệu suất
Hypervisor liên tục theo dõi việc sử
Dựa trên nhu cầu, hypervisor điều
Bằng cách phân bổ tài nguyên hiệu
dụng tài nguyên của mỗi VM, bao
chỉnh phân bổ tài nguyên cho mỗi
quả, hypervisor đảm bảo hiệu suất
gồm CPU, bộ nhớ và lưu trữ.
VM theo thời gian thực.
tối ưu cho tất cả các VM trên máy
chủ.

---

## Slide 64: Thiết lập mạng ảo

Ảo hóa không chỉ giới hạn ở việc tạo ra các máy ảo, mà còn mở rộng đến việc thiết lập mạng ảo. Mạng ảo cho phép các VM giao tiếp
với nhau và với các mạng bên ngoài một cách liền mạch, như thể chúng được kết nối với một mạng vật lý thực sự.
Việc thiết lập mạng ảo cung cấp nhiều lợi ích, bao gồm tính linh hoạt trong cấu hình mạng, khả năng cô lập lưu lượng mạng giữa các
VM khác nhau và khả năng tạo ra các môi trường mạng phức tạp mà không cần đầu tư vào phần cứng mạng bổ sung.
Tạo mạng ảo
Cấu hình kết nối
Hypervisor tạo ra các mạng
Các VM được cấu hình để
Thiết lập định
tuyến
Quản lý lưu lượng
Giám sát và quản lý lưu
ảo để kết nối các VM.
kết nối với mạng ảo phù
Cấu hình định tuyến giữa
lượng mạng giữa các VM và
hợp.
các mạng ảo và mạng bên
với bên ngoài.
ngoài.

---

## Slide 65: Công cụ quản lý và tự động hóa

Các nền tảng ảo hóa hiện đại thường đi kèm với các công cụ quản lý mạnh mẽ, giúp đơn giản hóa quá trình quản lý và vận
hành hệ thống ảo hóa. Những công cụ này cung cấp giao diện trực quan cho phép người quản trị dễ dàng tạo, cấu hình và
giám sát các máy ảo.
Ngoài ra, các công cụ tự động hóa trong các nền tảng ảo hóa cho phép triển khai và mở rộng ứng dụng một cách nhanh
chóng và hiệu quả. Điều này đặc biệt hữu ích trong các môi trường đòi hỏi tính linh hoạt cao và khả năng đáp ứng nhanh
với nhu cầu thay đổi.
Bảng điều khiển
Tự động hóa
Phân tích
Bảo mật
Giao diện trực quan để
Công cụ để tự động hóa
Công cụ phân tích hiệu suất
Tính năng bảo mật tích hợp
quản lý và giám sát VM.
việc triển khai và quản lý
và sử dụng tài nguyên.
để bảo vệ môi trường ảo
VM.
hóa.

---

## Slide 66: Lợi ích của ảo hóa

Ảo hóa mang lại nhiều lợi ích đáng kể cho doanh nghiệp. Đầu tiên, nó giúp giảm chi phí phần cứng bằng cách cho phép hợp
nhất nhiều máy chủ vật lý thành một số ít máy chủ mạnh mẽ hơn. Điều này không chỉ tiết kiệm chi phí mua sắm mà còn giảm
chi phí vận hành và bảo trì.
Ngoài ra, ảo hóa cải thiện đáng kể việc sử dụng tài nguyên, cho phép các doanh nghiệp tận dụng tối đa công suất của phần
cứng hiện có. Nó cũng tăng tính linh hoạt và khả năng mở rộng, cho phép triển khai nhanh chóng các máy ảo mới khi cần
thiết.
Tiết kiệm chi phí
2 Hiệu quả tài nguyên
Giảm chi phí phần cứng và vận hành thông qua việc
Tối ưu hóa việc sử dụng tài nguyên máy chủ, tăng
hợp nhất máy chủ.
hiệu suất tổng thể.
Linh hoạt và mở rộng
4 Cải thiện bảo mật
Dễ dàng triển khai và mở rộng các máy ảo theo nhu
Cô lập các máy ảo giúp tăng cường bảo mật và giảm
cầu.
thiểu rủi ro.

---

## Slide 67: Thách thức và giải pháp trong ảo hóa

Mặc dù mang lại nhiều lợi ích, ảo hóa cũng đặt ra một số thách thức. Một trong những vấn đề phổ biến là hiệu suất có thể bị ảnh
hưởng nếu tài nguyên không được phân bổ đúng cách. Để giải quyết điều này, cần có chiến lược phân bổ tài nguyên hiệu quả và
giám sát liên tục.
Bảo mật cũng là một mối quan tâm lớn trong môi trường ảo hóa. Việc cô lập các máy ảo và triển khai các biện pháp bảo mật
mạnh mẽ là cần thiết để bảo vệ dữ liệu và ứng dụng. Ngoài ra, quản lý phức tạp của môi trường ảo hóa đòi hỏi kỹ năng chuyên
môn và công cụ quản lý phù hợp.
Thách thức
Hiệu suất
Bảo mật
Quản lý phức tạp
Chi phí ban đầu
Giải pháp
Phân bổ tài nguyên thông minh, giám sát liên tục
Cô lập VM, triển khai biện pháp bảo mật mạnh
Đào tạo nhân viên, sử dụng công cụ quản lý tiên tiến
Lập kế hoạch dài hạn, đánh giá ROI

---

## Slide 68: Xu hướng tương lai trong ảo hóa

Ảo hóa tiếp tục phát triển với nhiều xu hướng mới nổi. Một trong những xu hướng quan trọng là sự tích hợp ngày càng sâu rộng
với điện toán đám mây, cho phép các doanh nghiệp kết hợp linh hoạt giữa cơ sở hạ tầng tại chỗ và đám mây. Điều này mở ra khả
năng mở rộng và linh hoạt chưa từng có.
Trí tuệ nhân tạo (AI) và học máy cũng đang được tích hợp vào các nền tảng ảo hóa, cải thiện khả năng tự động hóa và tối ưu hóa.
Ngoài ra, ảo hóa mạng và bảo mật tiếp tục phát triển, cung cấp các giải pháp toàn diện hơn cho doanh nghiệp.
Tích hợp đám mây
AI và tự động hóa
Bảo mật nâng cao
Kết hợp liền mạch giữa ảo hóa tại chỗ và
Sử dụng AI để tối ưu hóa quản lý và hiệu
Các giải pháp bảo mật tiên tiến tích hợp
điện toán đám mây.
suất trong môi trường ảo hóa.
sâu vào nền tảng ảo hóa.

---

## Slide 69: 12 Lợi Ích của Ảo Hóa trong

Điện Toán Đám Mây
Ảo hóa đang thay đổi cách doanh nghiệp quản lý và triển khai tài
nguyên CNTT. Nó mang lại nhiều lợi ích từ bảo mật đến tiết kiệm chi
phí.

---

## Slide 70: Tiết Kiệm Chi Phí và Kế Hoạch Dự Phòng

Tiết Kiệm Chi Phí
Kế Hoạch Dự Phòng
- Tạo máy ảo mới thay vì mua phần cứng.
- Tạo snapshots và sao lưu máy ảo.
- Giảm đầu tư ban đầu và chi phí liên tục (năng lượng tiêu thụ,
- Khôi phục nhanh chóng để duy trì hoạt động.
bảo trì, phòng máy chủ,...).
- 
Ít phải lo lắng hơn về khả năng mất dữ liệu và thời gian ngừng
hoạt động của hệ thống.

---

## Slide 71: Khả Năng Mở Rộng và

Bảo Mật
1 Mở Rộng Dễ Dàng
Thêm tài nguyên như CPU, RAM hoặc lưu trữ chỉ bằng cách
thêm máy ảo mới.
Bảo Mật Tốt Hơn
Môi trường biệt lập cho mỗi máy ảo giúp ngăn chặn lan
truyền mối đe dọa.

---

## Slide 72: Quản Lý Đơn Giản và Di

Chuyển Hệ Thống
Quản Lý Tập Trung
Quản lý tất cả máy ảo từ một bảng điều khiển duy
nhất.
Di Chuyển Dễ Dàng
Chuyển toàn bộ hệ thống giữa các máy chủ mà
không cần cài đặt lại.

---

## Slide 73: Triển Khai Nhanh và Hỗ Trợ Làm Việc Từ Xa

Triển Khai Nhanh
Khởi tạo máy ảo mới chỉ trong vài phút với các mẫu được cấu hình sẵn.
Làm Việc Từ Xa
Truy cập an toàn vào máy tính để bàn, ứng dụng và dữ liệu từ xa.
Mở Rộng Toàn Cầu
Thuê nhân viên từ xa và khai thác tài năng trên toàn thế giới.

---

## Slide 74: Khả Năng Tương Thích và

Kiểm Tra Ứng Dụng
Tương Thích Đa Nền Tảng
Chạy ứng dụng trên nhiều hệ điều hành khác nhau thông qua máy ảo.
Kiểm Tra An Toàn
Thử nghiệm trong môi trường sandbox mà không ảnh hưởng đến hệ
thống chính.
Giảm Thiểu Rủi Ro
Cải thiện đảm bảo chất lượng và đẩy nhanh quá trình thử nghiệm.

---

## Slide 75: Cân Bằng Tải Động và

Hỗ Trợ Ứng Dụng Cũ
Phân Phối Thông Minh
Tự động phân tích và phân bổ lại tác vụ giữa các máy ảo.
Tối Ưu Hóa Tài Nguyên
Đảm bảo không có máy nào bị quá tải, tăng hiệu suất tổng thể.
Duy Trì Ứng Dụng Cũ
Tạo môi trường ảo cho phần mềm lỗi thời, kéo dài tuổi thọ đầu
tư.

---

## Slide 76: Tổng Kết Lợi Ích Ảo Hóa

Tiết kiệm chi phí
Bảo mật tốt hơn
Quản lý đơn giản
Mở rộng linh hoạt
Triển khai nhanh
Hỗ trợ làm việc từ xa
Tương thích đa nền tảng
Kiểm tra an toàn
Cân bằng tải động

---

## Slide 77: Kết luận về ảo hóa

Ảo hóa đã trở thành một công nghệ không thể thiếu trong môi trường CNTT hiện đại. Bằng cách cho phép sử dụng hiệu
quả tài nguyên, giảm chi phí và tăng tính linh hoạt, ảo hóa đã mang lại những lợi ích đáng kể cho doanh nghiệp ở mọi quy
mô. Từ việc cài đặt hypervisor đến quản lý tài nguyên động và thiết lập mạng ảo, mỗi khía cạnh của ảo hóa đều đóng góp
vào việc tạo ra một hệ thống CNTT mạnh mẽ và hiệu quả hơn.
Khi công nghệ tiếp tục phát triển, ảo hóa sẽ ngày càng trở nên quan trọng trong việc định hình tương lai của cơ sở hạ tầng
CNTT. Với sự tích hợp của AI, điện toán đám mây và các công nghệ tiên tiến khác, ảo hóa sẽ tiếp tục mở ra những khả năng
mới cho doanh nghiệp, giúp họ đáp ứng nhanh chóng với những thách thức và cơ hội trong thế giới số hóa ngày càng phức
tạp.

---

## Slide 78: Kiến trúc Hướng Dịch vụ

(SOA)
1 Ưu điểm
SOA dễ bảo trì, độc lập với nền tảng và có khả năng mở rộng
cao.
2 Vai trò
Nhà cung cấp dịch vụ và người sử dụng dịch vụ là hai vai trò
chính.
3 Linh hoạt
Cho phép truy cập giải pháp đám mây theo nhu cầu kinh
doanh thay đổi.

---

## Slide 79: Điện toán Lưới – Grid Computing

Điện toán lưới, còn gọi là điện toán phân tán, kết hợp nhiều tài nguyên từ nhiều vị trí. Nó sử dụng các nút song song để tạo thành cụm
máy tính.
Mạng lưới
Cụm đa dạng
Các máy tính kết nối tạo thành mạng lưới phức tạp.
Cụm máy tính có kích thước khác nhau, chạy nhiều hệ điều hành.

---

## Slide 80: Các loại Máy trong Điện toán Lưới

Nút điều khiển
Nhà cung cấp
Người dùng
Nhóm máy chủ quản lý toàn bộ
Máy tính đóng góp tài nguyên vào
Máy tính sử dụng tài nguyên trên
mạng lưới.
nhóm tài nguyên mạng.
mạng lưới.

---

## Slide 81: Ứng dụng của Điện toán Lưới

ATM
Cơ sở hạ tầng
Nghiên cứu tiếp thị
Hệ thống ATM sử dụng điện toán
Hỗ trợ cơ sở hạ tầng phụ trợ cho
Phân tích dữ liệu lớn trong nghiên
lưới để xử lý giao dịch.
doanh nghiệp.
cứu thị trường.

---

## Slide 82: Điện toán Tiện ích

Điện toán tiện ích là mô hình dịch vụ CNTT phổ biến nhất. Nó cung cấp tài nguyên điện toán theo yêu cầu dựa trên
phương pháp trả tiền theo mức sử dụng.
Dịch vụ
Chi phí
Hiệu quả
Cung cấp dịch vụ tính toán, lưu
trữ và lập trình thông qua API.
Giảm thiểu chi phí liên quan đến
Tối đa hóa việc sử dụng hiệu quả
CNTT.
các tài nguyên.

---

## Slide 83: Ưu điểm của Điện toán

Tiện ích
Tiết kiệm
Giảm đáng kể chi phí CNTT cho doanh nghiệp.
Linh hoạt
Cung cấp tính linh hoạt cao hơn trong sử dụng tài nguyên.
Quản lý
Dễ dàng quản lý và điều chỉnh theo nhu cầu.

---

## Slide 84: Các Tổ chức Lớn trong Điện toán Tiện ích

Các công ty công nghệ hàng đầu như Google và Amazon đã phát triển dịch vụ tiện ích riêng. Họ cung cấp giải pháp lưu trữ và ứng
dụng điện toán tiên tiến.
Google Cloud
Amazon Web Services
Nền tảng đám mây của Google với nhiều dịch vụ đa dạng.
Dịch vụ đám mây hàng đầu từ Amazon với quy mô toàn cầu.

---

## Slide 85: Mối quan hệ giữa các Công

nghệ
Điện toán lưới, điện toán đám mây và dịch vụ CNTT được quản lý đều tuân theo
khái niệm điện toán tiện ích. Chúng chia sẻ nguyên tắc cung cấp tài nguyên theo
nhu cầu.
Điện toán Lưới
Nền tảng cho việc chia sẻ tài nguyên phân tán.
Điện toán Đám mây
Phát triển từ điện toán lưới, cung cấp dịch vụ qua internet.
Điện toán Tiện ích
Mô hình kinh doanh áp dụng cho cả điện toán lưới và đám mây.

---

## Slide 86: Container và

Điều phối
Container
Container là công nghệ ảo hóa nhẹ cho phép ứng dụng chạy đáng
tin cậy trên nhiều môi trường. Chúng cung cấp môi trường riêng
biệt và an toàn cho ứng dụng.

---

## Slide 87: Định nghĩa Container

Ảo hóa nhẹ
Container là dạng ảo hóa nhẹ, không cần hệ điều hành đầy đủ.
Môi trường riêng biệt
Cung cấp môi trường thời gian chạy riêng biệt và an toàn cho
ứng dụng.
Đa nền tảng
Cho phép ứng dụng chạy trên nhiều môi trường điện toán khác
nhau.

---

## Slide 88: Đặc trưng của Container

Tính di động
Dễ dàng di chuyển giữa các môi trường điện toán khác nhau.
Hiệu quả tài nguyên
Sử dụng ít tài nguyên hơn so với máy ảo thông thường.
Khả năng tương thích
Tương thích với nhiều ngôn ngữ lập trình và công cụ.
Cô lập
Cung cấp môi trường an toàn và bảo mật cho ứng dụng.
Khả năng mở rộng
Container dễ dàng tăng, giảm quy mô để phù hợp với nhu cầu thay đổi.

---

## Slide 89: Công cụ Điều phối Container

Docker
Kubernetes
Giải pháp khác
Nền tảng container nổi tiếng cung
Hệ thống điều phối container với
Apache Mesos, Amazon ECS và
cấp thời gian chạy và công cụ tạo
container.
tính năng tiên tiến để kiểm soát
khối lượng công việc.
Google Container Engine (GKE) là
các lựa chọn thay thế.

---

## Slide 90: Lợi ích của Container trong

Điện toán Đám mây
1 Khả năng mở rộng
Dễ dàng mở rộng hoặc thu hẹp để thích ứng với nhu cầu thay đổi.
2 Hỗ trợ DevOps
Giúp tạo và thử nghiệm ứng dụng theo cách lặp lại và chuẩn hóa.
3 Tính nhất quán
Cung cấp môi trường nhất quán cho ứng dụng, bất kể nơi triển khai.
4 Tính di động
Có thể chạy trên nhiều nền tảng và hệ điều hành khác nhau.
5 Hiệu quả
So với máy tính ảo thông thường, container nhẹ hơn và sử dụng ít tài nguyên hơn

---

## Slide 91: Hiệu quả của Container

Nhẹ hơn
Container nhẹ hơn so với máy ảo thông thường.
Sử dụng tài nguyên tốt hơn
Nhiều container có thể chạy trên một máy chủ duy nhất.
Tiết kiệm chi phí
Giảm chi phí nhờ sử dụng tài nguyên hiệu quả hơn.

---

## Slide 92: Trường hợp sử dụng: Đám

mây lai
Triển khai linh hoạt
Container cho phép triển khai ứng dụng trên cả đám mây
công cộng và riêng tư.
Tối ưu hóa
Chọn đám mây tốt nhất cho từng khối lượng công việc.
Nhất quán
Duy trì tính nhất quán và khả năng di động giữa các môi
trường.

---

## Slide 93: Hiện đại hóa Ứng dụng

Cũ
Đưa ứng dụng vào container
Triển khai trên đám mây
Giảm chi phí
Tăng tính linh hoạt
Nâng cao hiệu suất
Cải thiện khả năng mở rộng

---

## Slide 94: Ứng dụng Gốc Đám mây

Kiến trúc Microservices
Điều phối Container
DevOps
Ứng dụng gốc đám mây thường sử
dụng kiến trúc microservices.
Kubernetes là công cụ phổ biến để
điều phối các ứng dụng gốc đám
Container hóa hỗ trợ quy trình
DevOps trong phát triển ứng dụng
mây.
gốc đám mây.

---

## Slide 95: Microservices và Container

Đóng gói độc lập
Triển khai linh hoạt
Quản lý hiệu quả
Microservices có thể được đóng
Dễ dàng cập nhật hoặc thay thế
Container hóa giúp quản lý và
gói vào container riêng lẻ.
từng microservice mà không
mở rộng microservices dễ dàng
ảnh hưởng toàn hệ thống.
hơn.

---

## Slide 96: Dữ liệu lớn và

phân tích trong
điện toán đám
mây
Dữ liệu lớn và phân tích là thành phần quan trọng của điện toán
đám mây. Chúng giúp xử lý khối lượng dữ liệu khổng lồ, phức tạp
một cách hiệu quả.

---

## Slide 97: Đặc trưng của dữ liệu lớn

Khối lượng
Dữ liệu lớn có khối lượng cực lớn, đo bằng terabyte hoặc petabyte.
Tốc độ
Cần xử lý theo thời gian thực hoặc gần thời gian thực.
Tính đa dạng
Bao gồm dữ liệu có cấu trúc, bán cấu trúc và không có cấu trúc.

---

## Slide 98: Lợi ích của dữ liệu lớn

trên đám mây
1 Hiệu quả chi phí
Chỉ trả tiền cho tài nguyên thực sự sử dụng, giảm chi phí xử
lý.
2 Khả năng mở rộng
Đáp ứng nhu cầu xử lý và lưu trữ dữ liệu lớn linh hoạt.
3 Tích hợp đơn giản
Dễ dàng tích hợp với các công nghệ như Hadoop và Spark.

---

## Slide 99: Trường hợp sử dụng dữ liệu lớn

Phát hiện gian lận
Phân tích khách hàng
Phân tích dữ liệu lớn giúp phát hiện
Hiểu rõ hơn về hành vi, sở thích và
Tối ưu hóa chuỗi cung
ứng
gian lận trong giao dịch tài chính.
nhu cầu của người tiêu dùng.
Giảm chi phí và tăng năng suất
trong quản lý chuỗi cung ứng.

---

## Slide 100: Hadoop và Spark

Hadoop
Kiến trúc nguồn mở xử lý dữ liệu lớn trên các cụm
máy tính phân tán.
MapReduce
Phương pháp lập trình của Hadoop để xử lý các tập
dữ liệu lớn.
Spark
Nền tảng xử lý dữ liệu lớn tập trung vào tốc độ và khả
năng sử dụng.

---

## Slide 101: Công cụ học máy trên

đám mây
Xử lý ngôn ngữ tự nhiên
Phân tích và hiểu ngôn ngữ con người tự động.
Nhận dạng hình ảnh
Xác định và phân loại đối tượng trong hình ảnh.
Phân tích dự đoán
Dự đoán xu hướng và kết quả trong tương lai.

---

## Slide 102: Lợi ích của phân tích dữ

liệu trên đám mây
Tiết kiệm chi phí
Thay thế cơ sở hạ tầng và phần mềm tại chỗ đắt tiền.
Linh hoạt
Thử nghiệm nhiều kỹ thuật phân tích mà không cần đầu tư dài
hạn.
Khả năng truy cập
Hợp tác từ xa dễ dàng với truy cập qua internet.

---

## Slide 103: Tương lai của dữ liệu

lớn trên đám mây
Tốc độ xử lý
Nhanh hơn đáng kể so với
giải pháp tại chỗ
Đổi mới
Phát triển liên tục công nghệ
và khả năng mới
Khả năng mở rộng
Tăng giảm quy mô linh hoạt
theo nhu cầu

---

## Slide 104: Điện toán không

máy chủ: Cách
mạng hóa phát
triển ứng dụng
Điện toán không máy chủ là một mô hình điện toán đám mây mới.
Nó cho phép nhà phát triển tập trung vào mã nguồn, không cần quản
lý cơ sở hạ tầng.

---

## Slide 105: Kiến trúc điện toán không

máy chủ
Quản lý cơ sở hạ tầng
Nhà cung cấp đám mây quản lý toàn bộ cơ sở hạ tầng.
Tập trung vào mã
Nhà phát triển chỉ cần tạo và phân phối mã.
Kích hoạt theo sự kiện
Các hành động được kích hoạt bởi sự kiện cụ thể.

---

## Slide 106: Đặc trưng của điện toán

không máy chủ
Không quản lý cơ sở hạ tầng
Nhà cung cấp đám mây quản lý toàn bộ cơ sở hạ tầng.
2 Giảm thời gian ra thị trường
Triển khai và mở rộng ứng dụng nhanh chóng.
Kiến trúc hướng sự kiện
Phản ứng với các sự kiện cụ thể.
4 Giá trả theo mức sử dụng
Chỉ trả tiền cho tài nguyên thực sự sử dụng.

---

## Slide 107: Mô hình tính toán theo sự kiện

Sự kiện kích hoạt
Yêu cầu người dùng hoặc thay đổi dữ liệu kích hoạt xử lý.
Phân bổ tài nguyên
Nhà cung cấp đám mây tự động phân bổ tài nguyên cần thiết.
Thực thi chức năng
Chức năng được thực thi để xử lý sự kiện.
Giải phóng tài nguyên
Tài nguyên được giải phóng sau khi hoàn thành.

---

## Slide 108: Cấu trúc giá trả theo lần gọi

Tính phí theo sử dụng
Chỉ tính phí cho mức sử dụng thực tế của ứng dụng hoặc dịch vụ.
Tiết kiệm chi phí
Hiệu quả cho ứng dụng có lưu lượng truy cập thấp hoặc không thường
xuyên.
Linh hoạt
Phù hợp với nhu cầu thay đổi của doanh nghiệp.

---

## Slide 109: Lợi ích của điện toán không máy chủ

Thời gian ra thị trường
nhanh
Khả năng mở rộng tốt
Giảm chi phí
Nhà phát triển tập trung vào mã,
lượng yêu cầu.
trả tiền cho tài nguyên sử dụng.
Tự động mở rộng dựa trên khối
Tiết kiệm chi phí hoạt động và chỉ
không cần quản lý cơ sở hạ tầng.

---

## Slide 110: Ứng dụng trong xử lý dữ liệu và

phân tích
Xử lý dữ liệu lớn
Phân tích khối lượng dữ liệu khổng lồ với công cụ như Apache Spark.
Phân tích thời gian thực
Thực hiện phân tích dữ liệu theo thời gian thực.
Tích hợp đám mây
Tận dụng các dịch vụ đám mây như AWS Lambda.

---

## Slide 111: Ứng dụng trong Internet vạn

vật (IoT)
Thu thập dữ liệu
Quản lý dữ liệu từ các thiết bị IoT.
Xử lý thời gian thực
Xử lý dữ liệu IoT theo thời gian thực.
Phân tích và lưu trữ
Phân tích và lưu trữ dữ liệu IoT hiệu quả.

---

## Slide 112: Ứng dụng trong phát triển web và di động

Hệ thống phụ trợ
Phân phối nội dung
Xác thực
Hỗ trợ hệ thống phụ trợ cho ứng
Quản lý việc phân phối nội dung
Xử lý xác thực người dùng an toàn
dụng web và di động.
hiệu quả.
và nhanh chóng.

---

## Slide 113: Ứng dụng trong chatbot và trợ lý ảo

Xử lý ngôn ngữ tự nhiên
Tạo phản hồi
Tích hợp AI
Sử dụng điện toán không máy chủ để
Tạo phản hồi nhanh chóng cho truy
Tích hợp trí tuệ nhân tạo vào chatbot
xử lý ngôn ngữ tự nhiên hiệu quả.
vấn của người dùng.
và trợ lý ảo.

---

## Slide 114: Internet vạn vật

(IoT)
IoT kết nối các thiết bị thông minh, tạo ra hệ sinh thái dữ liệu phong
phú. Nền tảng IoT dựa trên đám mây quản lý và phân tích dữ liệu
này một cách an toàn, linh hoạt.

---

## Slide 115: Nền tảng và dịch vụ IoT

dựa trên đám mây
1 Xử lý dữ liệu
Cung cấp công cụ phân tích mạnh mẽ như xử lý luồng thời
gian thực và học máy.
2 Bảo mật
Tích hợp khả năng bảo mật như mã hóa và kiểm soát truy cập.
3 Quản lý thiết bị
Cung cấp công cụ quản lý nhiều thiết bị, bao gồm cung cấp và
giám sát.

---

## Slide 116: Lợi thế của IoT dựa trên đám mây

Khả năng mở rộng
Tốc độ ra thị trường
Hiệu quả chi phí
Dễ dàng tăng giảm quy mô để đáp
Giải pháp nhanh chóng để phát
Mô hình trả tiền theo sử dụng, giảm
ứng khối lượng dữ liệu ngày càng
triển và quản lý ứng dụng IoT.
đầu tư ban đầu vào cơ sở hạ tầng.
tăng.

---

## Slide 117: Các nền tảng IoT dựa trên đám mây phổ biến

AWS IoT
Microsoft Azure IoT
Google Cloud IoT
IBM Watson IoT
Nền tảng IoT toàn diện của
Giải pháp IoT tích hợp của
Dịch vụ IoT mạnh mẽ từ
Nền tảng IoT thông minh của
Amazon Web Services.
Microsoft.
Google Cloud Platform.
IBM.

---

## Slide 118: Tích hợp điện toán đám

mây với IoT
Kết nối thiết bị
Thiết bị IoT được kết nối với dịch vụ đám mây.
Lưu trữ dữ liệu
Dữ liệu từ thiết bị được lưu trữ trên đám mây.
Xử lý và phân tích
Dữ liệu được xử lý và phân tích bằng công cụ đám
mây.

---

## Slide 119: Công cụ phát triển IoT

trên đám mây
Bộ công cụ phát triển
Cung cấp các công cụ cần thiết để xây dựng ứng dụng IoT.
SDK
Bộ công cụ phát triển phần mềm cho nhiều ngôn ngữ lập trình.
API
Giao diện lập trình ứng dụng để tương tác với dịch vụ đám mây.

---

## Slide 120: Lợi ích của giải pháp IoT dựa trên

đám mây
Tiết kiệm chi phí
Giảm đầu tư vào cơ sở hạ tầng.
Khả năng mở rộng
Dễ dàng điều chỉnh theo nhu cầu.
Bảo mật nâng cao
Các tính năng bảo mật tích hợp.
Phân tích thời gian thực
Xử lý dữ liệu nhanh chóng.

---

## Slide 121: Ứng dụng trong nhà thông minh

Điều khiển ánh sáng
Kiểm soát nhiệt độ
An ninh
Tự động hóa và điều chỉnh ánh sáng
Quản lý nhiệt độ thông minh và tiết
Hệ thống camera và cảm biến kết nối
trong nhà.
kiệm năng lượng.
đám mây.

---

## Slide 122: IoT trong công nghiệp

và y tế
Lĩnh vực
Ứng dụng
Lợi ích
Công nghiệp
Giám sát thiết bị
Giảm thời gian
chết
Y tế
Theo dõi bệnh
Can thiệp sớm
nhân

---

## Slide 123: IoT trong nông nghiệp và thành phố

thông minh
Nông nghiệp thông minh
Thành phố thông minh
Theo dõi cây trồng, điều kiện thời tiết và độ ẩm đất. Tối
Giám sát giao thông, bãi đậu xe và phương tiện công
ưu hóa tưới tiêu và bón phân.
cộng. Tối ưu hóa cơ sở hạ tầng đô thị.

---

## Slide 124: Các bước áp dụng

Hiểu mô hình điện toán đám mây
Nắm bắt các đặc điểm, mô hình dịch vụ và triển khai để lựa chọn phù hợp.
Đánh giá lợi ích và thách thức
Cân nhắc tiết kiệm chi phí, linh hoạt cùng các rủi ro về bảo mật và quản
lý.
Lựa chọn nhà cung cấp phù hợp
Chọn nhà cung cấp dịch vụ uy tín như AWS, Azure hoặc GCP dựa trên
nhu cầu doanh nghiệp.
Triển khai và tối ưu
Thực hiện kế hoạch triển khai, giám sát và tối ưu để đạt hiệu quả
cao nhất.

---
