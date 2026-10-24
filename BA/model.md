Mô hình học máy

1

OUTLINE

Part 1

Part 1

GIỚI THIỆU VỀ MACHINE LEARNING

Part 2

Part 2

ỨNG DỤNG MACHINE LEARNING

TRONG PHÂN TÍCH DỮ LIỆU

Part 3

Part 3

DỰ BÁO MÔ HÌNH VỚI CHUỖI THỜI GIAN

PART 1

Giới thiệu về machine
learning

Hiểu khái niệm cơ bản về machine
learning và cách thực hiện

Python

Xử lý dữ liệu trên Python

Hiểu python và ứng dụng của
Python

Biết cách xử lý dữ liệu trên Python

Học máy đang thay đổi thế giới như thế nào?

Dự đoán hành vi người dùng trong thương mại điện tử (Shopee, Tiki, Amazon)

Xe tự lái (Autonomous Driving – Tesla)

Chẩn đoán bệnh qua hình ảnh y khoa

Hệ thống gợi ý phim (Netflix, YouTube)

Chatbot AI, dịch tự động, nhận diện giọng nói

Nhận diện khuôn mặt và bảo mật sinh trắc học

1. Giai đoạn khởi đầu (trước 1950)

•1943 – McCulloch & Pitts: Mô hình nơ-ron nhân tạo đầu tiên (Artificial Neuron).
•1950 – Alan Turing giới thiệu Turing Test, kiểm tra xem máy có thể "nghĩ" như con người không.

2. Giai đoạn sơ khai của AI (1956–1970)

•1956 – Hội nghị Dartmouth: John McCarthy đặt ra thuật ngữ Artificial Intelligence.
•1959 – Arthur Samuel tạo ra chương trình chơi cờ dama biết tự học (machine learning đầu
tiên).
•AI ban đầu tập trung vào logic, tìm kiếm, trò chơi, và chứng minh toán học.

3. Mùa đông AI lần 1 (1970–1980)
•Lạc quan ban đầu quá cao, nhưng máy tính hạn chế.
•Không có đủ dữ liệu, phần cứng yếu.
•Tài trợ nghiên cứu AI bị cắt giảm, niềm tin suy giảm.

4. AI dựa luật và chuyên gia (1980–1987)
•Sự nổi lên của Expert Systems: chương trình dựa trên luật IF-THEN
mô phỏng chuyên gia con người.

5. Mùa đông AI lần 2 (1987–1993)
•Expert Systems thất bại trong thực tế do khó mở rộng và duy trì.
•Thiếu hiệu quả và linh hoạt.

6. Trỗi dậy của học máy (1990–2000)
•Sự thay đổi từ AI biểu tượng sang machine learning: học từ dữ liệu thay vì lập trình luật rõ ràng.
•Sử dụng các thuật toán thống kê: Decision Tree, Naive Bayes, SVM, KNN.

Cột mốc:

•1997 – Máy tính IBM Deep Blue thắng nhà vô địch cờ vua Garry Kasparov.

7. Học sâu và Big Data (2006–nay)

•2006 – Geoffrey Hinton giới thiệu lại Deep Learning (Học sâu) – mạng nơ-ron nhiều tầng.
•2012 – Mạng deep learning (AlexNet) chiến thắng cuộc thi ImageNet, đưa DL trở thành trung tâm AI.

Công nghệ hỗ trợ:

•GPU mạnh mẽ, dữ liệu lớn (Big Data), mã nguồn mở (TensorFlow, PyTorch...).

Các ứng dụng bùng nổ:

•Nhận diện hình ảnh, xử lý ngôn ngữ tự nhiên (GPT, BERT...), xe tự lái, chatbot, y tế, tài chính...

8. AI hiện đại (2020–nay)

•AI tạo sinh (Generative AI): như ChatGPT, Midjourney, Sora…
•Học tăng cường (Reinforcement Learning): giúp máy học qua hành động – nổi bật trong game và robot.
•AutoML, AI Ethics, Explainable AI: tập trung vào dễ hiểu, an toàn và có trách nhiệm.

1. Khái niệm về học máy

VÌ SAO PHẢI PHÂN LOẠI DỮ LIỆU?

Dữ liệu là những ghi nhận về thế giới thực đã được số hoá: con số, chữ viết, hình ảnh, âm

thanh, tín hiệu cảm biến.

Cách dữ liệu được tổ chức quyết định ba việc:

lưu ở đâu — cơ sở dữ liệu quan hệ, kho dữ liệu, hồ dữ liệu (data lake), cơ sở dữ liệu vector;
xử lý bằng gì — SQL, bảng tính, thư viện xử lý ảnh, mô hình ngôn ngữ;
mô hình nào dùng được — hồi quy và cây quyết định cần bảng; mạng nơ-ron sâu mới xử lý

trực tiếp được ảnh và văn bản.

Vì vậy câu hỏi đầu tiên của mọi dự án phân tích không phải là “dùng mô hình gì” mà là “dữ

liệu của tôi thuộc loại nào”.

7

DỮ LIỆU CÓ CẤU TRÚC

Dữ liệu có cấu trúc (structured data) là dữ liệu được tổ chức theo mô hình định sẵn:
mỗi hàng là một quan sát, mỗi cột là một biến có kiểu dữ liệu xác định.

Đặc điểm. Có lược đồ (schema) rõ ràng; kiểu dữ liệu cố định (số, ngày, chuỗi, nhị phân);
truy vấn được bằng SQL; dễ tổng hợp, lọc, tính trung bình.
Nơi lưu trữ. Cơ sở dữ liệu quan hệ (MySQL, PostgreSQL, Oracle), kho dữ liệu (data
warehouse), bảng tính, tệp CSV.
Ví dụ. Bảng giao dịch ngân hàng; hồ sơ nhân sự; danh mục sản phẩm và giá; số liệu điều tra
mức sống hộ gia đình; báo cáo tài chính theo mẫu.
Ưu điểm. Dễ kiểm soát chất lượng, dễ chia sẻ, dùng được ngay với hầu hết mô hình thống
kê cổ điển. Hạn chế. Chỉ mô tả được những gì đã được định nghĩa trước; mọi sắc thái nằm
ngoài lược đồ đều bị mất.

8

VÍ DỤ MỘT BẢNG DỮ LIỆU CÓ CẤU TRÚC

Mã KH

Tuổi

Thu nhập (tr/tháng)

Số năm làm việc

Dư nợ (tr)

Vỡ nợ

KH001

KH002

KH003

KH004

KH005

34

27

45

52

23

18.5

12.0

31.2

26.8

9.4

8

3

20

25

1

220

150

480

610

80

0

1

0

0

1

Mỗi hàng là một quan sát (một khách hàng). Mỗi cột là một biến, còn gọi là một đặc trưng (feature).
Cột cuối “Vỡ nợ” là nhãn (label) — thứ ta muốn dự đoán.
Với cấu trúc này, câu hỏi “tỷ lệ vỡ nợ của nhóm thu nhập dưới 15 triệu là bao nhiêu?” chỉ mất một
dòng lệnh SQL.

9

DỮ LIỆU PHI CẤU TRÚC

Dữ liệu phi cấu trúc (unstructured data) không tuân theo một lược đồ định sẵn: không có hàng, không có
cột, không có kiểu dữ liệu cố định.

Ví dụ. Văn bản tự do (email, hợp đồng, tin nhắn chăm sóc khách hàng, bình luận mạng xã hội);
hình ảnh (ảnh chụp căn cước, ảnh vệ tinh, ảnh y tế); âm thanh (ghi âm tổng đài); video; tệp PDF
quét.
Vì sao khó. Không truy vấn được bằng SQL; ý nghĩa nằm trong ngữ cảnh chứ không nằm trong
một ô; cùng một nội dung có vô số cách diễn đạt; khối lượng rất lớn.
Nhưng giá trị rất cao. Lý do thật sự khiến khách hàng rời bỏ ngân hàng thường nằm trong email
khiếu nại, chứ không nằm trong bảng giao dịch.
Cách xử lý hiện nay. Dùng mô hình học sâu để chuyển dữ liệu phi cấu trúc thành vector số
(embedding) — sau bước đó, mọi công cụ dành cho dữ liệu có cấu trúc lại dùng được.

1
0

PHẦN LỚN DỮ LIỆU LÀ PHI CẤU TRÚC

Các ước tính của giới công nghệ (IDC, Gartner và các nhà cung cấp lưu trữ) đều cho con số tương tự:
khoảng 80–90% dữ liệu mà một tổ chức nắm giữ là phi cấu trúc, và tỷ trọng này đang tăng.
Cần đọc con số này một cách thận trọng: đây là ước tính của ngành, không phải một phép đo chính xác,
và cách phân loại khác nhau giữa các báo cáo.
Hàm ý thực tiễn: nếu chỉ biết làm việc với bảng biểu, ta đang bỏ qua phần lớn thông tin mà tổ chức của
mình đang có.

1
1

DỮ LIỆU BÁN CẤU TRÚC

Dữ liệu bán cấu trúc (semi-structured data) không có lược đồ bảng cứng
nhắc, nhưng mang thẻ đánh dấu hoặc khoá – giá trị cho biết đâu là thông tin
gì.

Ví dụ. Tệp JSON và XML; nhật ký hệ thống (log); email (có trường Người gửi, Chủ đề, Ngày — nhưng phần thân là
văn bản tự do); dữ liệu từ giao diện lập trình ứng dụng (API); dữ liệu cảm biến IoT.
Đây là dạng phổ biến nhất khi lấy dữ liệu từ Internet hoặc từ hệ thống của bên thứ ba. Bước đầu tiên của hầu hết dự
án là làm phẳng dữ liệu bán cấu trúc thành bảng.
Ranh giới giữa ba loại không tuyệt đối. Một tệp PDF có thể vừa chứa bảng số liệu (có cấu trúc) vừa chứa đoạn
thuyết minh (phi cấu trúc).

1
2

SO SÁNH BA LOẠI DỮ LIỆU

Tiêu chí

Có cấu trúc

Bán cấu trúc

Phi cấu trúc

Tổ chức

Bảng, hàng và cột

Thẻ, khoá – giá trị

Không có lược đồ

Ví dụ

CSV, bảng SQL

JSON, XML, log

Ảnh, video, văn bản

Truy vấn

Nơi lưu

Tỷ trọng

Độ khó

SQL

Cần phân tích cú pháp

Cần mô hình học sâu

Kho dữ liệu

Hồ dữ liệu, NoSQL

Hồ dữ liệu, CSDL vector

Nhỏ

Thấp

Trung bình

Trung bình

Rất lớn

Cao

Càng sang phải, dữ liệu càng giàu thông tin nhưng càng khó khai thác. Học máy hiện
đại chính là công cụ giúp thu hẹp khoảng cách đó.

1
3

TỪ DỮ LIỆU THÔ ĐẾN ĐẶC TRƯNG

Mô hình học máy không “đọc” dữ liệu thô. Chúng chỉ làm việc với các con số. Bước biến

dữ liệu thô thành bảng số gọi là kỹ thuật đặc trưng (feature engineering).

Biến phân loại (giới tính, tỉnh thành) → mã hoá thành các biến 0/1;
Ngày tháng → tách thành thứ trong tuần, tháng, số ngày kể từ một mốc;
Văn bản → đếm từ, hoặc chuyển thành vector nhúng (embedding);
Ảnh → ma trận điểm ảnh, hoặc vector đặc trưng do mạng nơ-ron sinh ra.

Trong thực tế, chất lượng đặc trưng quan trọng hơn độ phức tạp của mô hình. Một mô
hình đơn giản với đặc trưng tốt thường thắng một mô hình phức tạp với đặc trưng
kém.

1
4

CHẤT LƯỢNG DỮ LIỆU

• Thiếu dữ liệu. Ô trống có thể ngẫu nhiên, nhưng thường không: người thu nhập cao hay bỏ

trống câu hỏi về thu nhập. Xoá bừa các hàng thiếu sẽ làm lệch mẫu.

• Nhiễu và sai sót. Nhập sai đơn vị, sai dấu thập phân, giá trị bất thường (outlier). Luôn vẽ

phân phối của từng biến trước khi làm bất cứ điều gì khác.

• Thiên lệch mẫu. Dữ liệu chỉ từ khách hàng đã được duyệt vay không nói gì về những người

bị từ chối — mô hình học từ đó sẽ tái tạo lại đúng định kiến cũ.

Nguyên tắc bất di bất dịch: rác vào thì rác ra. Không mô hình nào cứu được dữ liệu tồi.

1
5

THẢO LUẬN

Một ngân hàng muốn dự đoán khách hàng nào sắp đóng tài khoản.
1. Liệt kê 5 nguồn dữ liệu ngân hàng có thể dùng. Xếp mỗi nguồn vào một trong ba loại:
có cấu trúc, bán cấu trúc, phi cấu trúc.
2. Từ lịch sử giao dịch, hãy đề xuất 4 đặc trưng có thể tạo ra.
3. Chỉ ra một biến mà nếu đưa vào mô hình sẽ gây rò rỉ dữ liệu, và giải thích vì sao.

1
6

HỌC MÁY LÀ GÌ?

Arthur Samuel (1959) — lĩnh vực nghiên cứu trao cho máy tính khả năng học mà không cần
được lập trình một cách tường minh.

Tom Mitchell (1997) — một chương trình máy tính được nói là học từ kinh nghiệm E đối với
một lớp nhiệm vụ T và thước đo hiệu năng P, nếu hiệu năng của nó tại các nhiệm vụ trong T, đo
bằng P, được cải thiện nhờ kinh nghiệm E.

Ví dụ áp dụng định nghĩa của Mitchell cho bài toán lọc thư rác:
T = phân loại thư đến là rác hay không rác. E = tập thư đã được người dùng đánh dấu.
P = tỷ lệ phân loại đúng trên những thư chưa từng thấy.

1
7

LẬP TRÌNH TRUYỀN THỐNG VÀ HỌC MÁY

Lập trình truyền thống: con người viết quy tắc, máy áp dụng lên dữ liệu để cho ra kết
quả. Học máy đảo ngược sơ đồ: ta đưa vào dữ liệu cùng kết quả đã biết, máy tìm ra quy
tắc.

1
8

AI, HỌC MÁY
VÀ HỌC SÂU

Trí tuệ nhân tạo (AI) — mọi kỹ thuật giúp máy thực hiện những việc vốn cần trí tuệ con người, kể cả hệ chuyên gia dựa
trên luật.
Học máy (ML) — nhánh của AI trong đó máy học từ dữ liệu thay vì được lập trình luật.
Học sâu (Deep Learning) — nhánh của học máy dùng mạng nơ-ron nhiều lớp; đây là công nghệ đứng sau nhận dạng ảnh,
dịch máy và các mô hình ngôn ngữ lớn.
Ba khái niệm này lồng vào nhau, không phải ba thứ song song. Nói “dự án AI” khi thực chất đang làm hồi quy logistic là
cách dùng từ gây hiểu nhầm.

1
9

BA THÀNH PHẦN CỦA MỘT MÔ HÌNH HỌC MÁY

1. DỮ LIỆU
tập các quan sát, mỗi quan
sát gồm các đặc trưng, và
(nếu có) một nhãn

2. MÔ HÌNH
một họ hàm số có tham
số, mô tả cách đặc trưng
liên hệ với nhãn

3. HÀM MẤT MÁT
thước đo mức độ sai của
mô hình, dùng để chọn ra
bộ tham số tốt nhất

Huấn luyện (training) chính là quá trình đi tìm bộ tham số làm cho hàm mất mát nhỏ nhất trên dữ liệu huấn
luyện.
Ba thành phần này có mặt trong mọi thuật toán học máy, từ hồi quy tuyến tính cho tới mô hình ngôn ngữ lớn. Cái thay
đổi chỉ là họ hàm và cách tối ưu.
Điểm nối với thống kê: ước lượng bình phương nhỏ nhất (OLS) chính là “mô hình tuyến tính + hàm mất mát bình
phương sai số”.

2
0

2. Quy trình mô hình học máy

Bước

Nội dung

Sai lầm thường gặp

1

2

3

4

5

6

7

8

Xác định bài toán và thước đo thành
công

Thu thập và mô tả dữ liệu

Bắt đầu từ mô hình thay vì từ câu hỏi

Không kiểm tra nguồn gốc và tính đại
diện

Làm sạch, xử lý thiếu và ngoại lai

Xoá hết hàng thiếu, làm lệch mẫu

Tạo đặc trưng

Vô tình đưa vào biến gây rò rỉ dữ liệu

Chia tập huấn luyện / kiểm định / kiểm
tra

Chia sau khi đã xử lý toàn bộ dữ liệu

Huấn luyện và tinh chỉnh siêu tham số

Tinh chỉnh trên tập kiểm tra

Đánh giá trên tập kiểm tra

Chọn chỉ số không phù hợp bài toán

Triển khai và giám sát

Không theo dõi khi phân phối dữ liệu đổi

2
1

CHIA DỮ LIỆU THÀNH BA TẬP

Tập huấn luyện (training set) dùng để ước lượng tham số của mô hình.
Tập kiểm định (validation set) dùng để chọn siêu tham số — độ sâu của cây, số cụm, mức phạt — và để so
sánh các mô hình với nhau.
Tập kiểm tra (test set) chỉ được dùng đúng một lần, ở cuối cùng, để báo cáo hiệu năng. Nếu dùng nó để
chọn mô hình thì con số báo cáo sẽ lạc quan hơn thực tế.
Vì sao không đánh giá ngay trên tập huấn luyện? Vì mô hình đã “nhìn thấy” những dữ liệu đó — kết quả sẽ
tốt một cách giả tạo. Ta cần biết mô hình chạy ra sao trên dữ liệu chưa từng thấy.
Tỷ lệ thường dùng: 60/20/20 hoặc 70/15/15. Không có con số bắt buộc — dữ liệu càng nhiều thì tỷ lệ dành
cho kiểm định và kiểm tra càng có thể nhỏ.

2
2

CÁCH 1: CHIA NGẪU NHIÊN (RANDOM SPLIT)

Quy trình. (1) Trộn ngẫu nhiên toàn bộ quan sát; (2) cắt theo tỷ lệ đã chọn; (3) cố định hạt giống ngẫu nhiên (random seed)
để kết quả lặp lại được.
Trộn trước khi cắt là bắt buộc: dữ liệu thường được sắp xếp theo mã khách hàng, theo chi nhánh hoặc theo nhãn — cắt thẳng sẽ
tạo ra hai tập hoàn toàn khác nhau về bản chất.

2
3

ƯU VÀ NHƯỢC CỦA CHIA NGẪU NHIÊN

ƯU ĐIỂM

NHƯỢC ĐIỂM

• rất đơn giản, chỉ một dòng lệnh;
• nhanh — chỉ huấn luyện mô hình một lần;
• phù hợp khi dữ liệu rất lớn, vì khi đó mỗi
tập đều đủ đại diện;
• dễ giải thích cho người ngoài chuyên môn.

• kết quả phụ thuộc vào một lần bốc thăm
may rủi: đổi seed có thể đổi kết luận;
• khi dữ liệu ít, tập kiểm tra quá nhỏ nên ước
lượng hiệu năng rất nhiễu;
• “lãng phí” dữ liệu: 20–40% số quan sát
không được dùng để huấn luyện;
• có thể làm lệch tỷ lệ lớp hoặc tách nhầm
các quan sát có liên hệ với nhau.

Chính bốn nhược điểm này dẫn tới kiểm định chéo (cross-validation).

2
4

KHI CHIA NGẪU NHIÊN LÀ SAI: PHÂN TẦNG

Khi một lớp rất hiếm — gian lận, vỡ nợ, bệnh hiếm — chia ngẫu nhiên thuần tuý có thể khiến tỷ lệ lớp
trong các tập lệch hẳn nhau, thậm chí tập kiểm tra gần như không còn quan sát nào thuộc lớp hiếm.
Chia phân tầng (stratified split) bốc thăm riêng trong từng lớp, nhờ đó tỷ lệ lớp trong tập huấn
luyện và tập kiểm tra bằng đúng tỷ lệ của toàn bộ dữ liệu.

2
5

KHI CHIA NGẪU NHIÊN LÀ SAI: NHÓM VÀ THỜI GIAN

Dữ liệu có nhóm. Nếu một khách hàng có nhiều giao dịch, chia ngẫu nhiên sẽ đặt vài giao dịch của cùng
người vào cả hai tập — mô hình “nhận ra” người đó và điểm số bị thổi phồng. Cách đúng: chia theo nhóm
(group split), cả nhóm nằm trọn trong một tập.
Dữ liệu theo thời gian. Không được trộn: dùng dữ liệu tương lai để dự báo quá khứ là vô nghĩa. Cách đúng là
chia theo mốc thời gian, huấn luyện trên quá khứ và kiểm định trên tương lai, như sơ đồ trên (cửa sổ mở
rộng).

2
6

CÁCH 2: KIỂM ĐỊNH CHÉO k PHẦN (k-FOLD)

Chia dữ liệu thành k phần bằng nhau rồi lặp lại việc huấn luyện – đánh giá k lần, mỗi lần để một
phần khác nhau làm tập kiểm định.

2
7

Các loại dữ liệu trong Machine Learning
Dữ liệu là nền tảng của ML, và được phân loại dựa trên cấu trúc và mục đích sử dụng. Các loại
dữ liệu chính bao gồm:

a. Dữ liệu có nhãn (Labeled Data)
Định nghĩa: Dữ liệu có nhãn bao gồm cả đầu vào (input) và đầu ra (output) mong muốn, được
sử dụng trong học có giám sát.
Cấu trúc:
· Đặc điểm (Features): Các biến đầu vào (ví dụ: tuổi, thu nhập, lịch sử giao dịch).
· Nhãn (Labels): Giá trị đầu ra cần dự đoán (ví dụ: trạng thái khoản vay - approved/rejected).
Ví dụ trong ngân hàng: Dữ liệu khách hàng với các đặc điểm (tuổi, thu nhập, số dư tài khoản)
và nhãn (điểm tín dụng: tốt/xấu).
Ứng dụng: Dự đoán rủi ro tín dụng, phân loại khách hàng.
Thách thức: Yêu cầu dữ liệu có nhãn chất lượng cao, tốn thời gian và chi phí để gắn nhãn.

b. Dữ liệu không có nhãn (Unlabeled Data)

Định nghĩa: Dữ liệu không có nhãn chỉ chứa các đặc điểm (features) mà không có đầu ra

xác định, dùng trong học không giám sát.

Cấu trúc: Chỉ có các đặc điểm (ví dụ: lịch sử giao dịch, hành vi chi tiêu).

Ví dụ trong ngân hàng: Dữ liệu giao dịch với các cột: transaction_amount, date, location,

nhưng không có nhãn xác định giao dịch là bình thường hay gian lận.

Ứng dụng: Phân cụm khách hàng, phát hiện gian lận.

Thách thức: Khó đánh giá kết quả vì không có nhãn để so sánh.

Phân nhóm khách hàng (Customer Segmentation)
Tình huống:
Một công ty thương mại điện tử muốn chia khách hàng thành các nhóm để cá nhân hóa chiến dịch tiếp thị. Dữ
liệu có gồm: số lần mua hàng, số tiền đã chi, tần suất truy cập website, thời gian truy cập...
Bài toán:
Hãy sử dụng dữ liệu hành vi khách hàng để phân nhóm các khách hàng thành các cụm có hành vi tương đồng.

Loại dữ liệu: Không có nhãn (unsupervised learning) – không biết trước nhóm nào là "VIP",

"thường", "không tiềm năng".

2. Phát hiện gian lận (Anomaly Detection)
Tình huống:
Ngân hàng muốn phát hiện các giao dịch đáng ngờ trong dữ liệu hàng triệu giao dịch tài chính. Dữ liệu chỉ gồm
thông tin về số tiền, thời gian, vị trí, tần suất giao dịch,...
Bài toán:
Tìm các giao dịch bất thường mà không có dữ liệu nào được dán nhãn là "gian lận".

3. Phân loại chủ đề tin tức (Topic Modeling)
Tình huống:
Một tòa soạn muốn tổ chức hàng ngàn bài báo cũ thành các chủ đề như chính trị, kinh tế, thể thao, giải trí,... nhưng không có
thông tin gán nhãn chủ đề trước đó.
Bài toán:
Phân tích nội dung bài viết để chia thành các nhóm chủ đề chính.

Loại dữ liệu: Không có nhãn – mô hình sẽ tự tìm ra các chủ đề (topics) tiềm ẩn trong dữ liệu văn
bản.

4. Nhận diện cụm sản phẩm (Product Clustering)
Tình huống:
Một chuỗi siêu thị muốn nhóm các sản phẩm tương đồng để tối ưu hóa trưng bày trên kệ hoặc gợi ý mua hàng.
Bài toán:
Sử dụng dữ liệu như giá, chủng loại, tần suất mua, trọng lượng... để phân cụm sản phẩm.

Loại dữ liệu: Không có nhãn – không có thông tin sản phẩm thuộc cụm nào từ
trước.

k-FOLD: CÁC BƯỚC THỰC HIỆN

Bước 1. Tách riêng tập kiểm tra ra trước và khoá lại. Kiểm định chéo được thực hiện trên phần dữ liệu còn lại.
Bước 2. Trộn ngẫu nhiên phần còn lại rồi chia thành k phần (fold) bằng nhau, thường k = 5 hoặc k = 10.
Bước 3. Với mỗi i = 1, …, k: huấn luyện mô hình trên k − 1 phần, đánh giá trên phần thứ i, ghi lại chỉ số hiệu năng Pᵢ.
Bước 4. Tính trung bình và độ lệch chuẩn của k giá trị:

P̄ = (P₁ + P₂ + … + P_k) / k        và        s = độ lệch chuẩn của {Pᵢ}

Bước 5. Chọn mô hình hoặc siêu tham số có P̄ tốt nhất, huấn luyện lại trên toàn bộ dữ liệu ngoài tập kiểm tra, rồi đánh giá một
lần duy nhất trên tập kiểm tra.
Độ lệch chuẩn s cũng quan trọng: nếu s lớn, hiệu năng của mô hình rất nhạy với việc chia dữ liệu — dấu hiệu dữ liệu quá ít
hoặc mô hình thiếu ổn định.

3
2

CHỌN k VÀ CÁC BIẾN THỂ CỦA k-FOLD

Biến thể

Cách làm

Dùng khi

k-fold thường

k = 5 hoặc k = 10

Trường hợp mặc định

Phân tầng (stratified)

Giữ tỷ lệ lớp trong từng phần

Phân loại mất cân bằng

Leave-one-out (LOOCV)

k = n, mỗi lần bỏ ra đúng một quan sát

Dữ liệu rất ít; tốn kém

Lặp lại (repeated)

Chạy k-fold nhiều lần, seed khác nhau

Muốn ước lượng ổn định hơn

Theo nhóm (group)

Cả nhóm nằm trọn trong một phần

Nhiều quan sát của cùng một đối
tượng

Theo thời gian

Cửa sổ mở rộng hoặc trượt, không trộn

Chuỗi thời gian, dữ liệu có thứ tự

Đánh đổi khi chọn k. k nhỏ → chạy nhanh nhưng mỗi lần chỉ dùng ít dữ liệu để huấn luyện, ước
lượng hiệu năng bị thiên lệch bi quan. k lớn → huấn luyện gần như trên toàn bộ dữ liệu nên ít
thiên lệch, nhưng tốn thời gian và các lần đánh giá tương quan mạnh với nhau. k = 5 hoặc 10 là
thoả hiệp được dùng phổ biến nhất.

3
3

BÀI 1

KIỂM ĐỊNH CHÉO LỒNG NHAU

Nếu dùng cùng một vòng kiểm định chéo để vừa chọn siêu tham số vừa báo cáo hiệu năng, con số báo cáo sẽ lạc quan

— vì siêu tham số đã được chọn sao cho hợp với chính những phần dữ liệu đó.

Kiểm định chéo lồng nhau (nested cross-validation) tách hai việc này thành hai vòng:

vòng trong — chạy k-fold trên phần huấn luyện để chọn siêu tham số;
vòng ngoài — chạy k-fold để đánh giá toàn bộ quy trình, kể cả bước chọn siêu tham số vừa rồi.

Kết quả là một ước lượng không thiên lệch về hiệu năng của cả quy trình xây dựng mô hình, chứ không riêng của một

mô hình cụ thể.

Chi phí: nếu vòng ngoài 5 phần và vòng trong 5 phần thì phải huấn luyện 25 lần cho mỗi bộ siêu tham số. Thường chỉ

dùng khi dữ liệu ít và kết luận cần độ tin cậy cao.

3
4

BÀI 1

SO SÁNH HAI CÁCH CHIA

Tiêu chí

Chia ngẫu nhiên một lần

Kiểm định chéo k-fold

Số lần huấn luyện

Chi phí tính toán

1

Thấp

k (thường 5 hoặc 10)

Cao gấp k lần

Dùng hết dữ liệu?

Không — phần kiểm định bị bỏ ra

Có — mọi quan sát đều được dùng

Độ ổn định ước lượng

Phụ thuộc một lần bốc thăm

Ổn định hơn nhiều

Cho biết độ biến động?

Không

Có — qua độ lệch chuẩn của k lần

Phù hợp khi

Dữ liệu rất lớn, mô hình đắt

Dữ liệu vừa và nhỏ

Không loại trừ nhau. Cách làm chuẩn trong thực tế là kết hợp cả hai: tách tập kiểm tra ra một
lần bằng chia ngẫu nhiên, rồi dùng kiểm định chéo trên phần còn lại để chọn mô hình.

3
5

3. Các mô hình học máy

Các loại mô hình học máy

Học máy có giám sát là
các thuật toán áp dụng
khi sử dụng các biến
đầu vào để dự đoán hay
phân loại đầu ra dựa
vào dữ liệu có nhãn
(labeled data) của biến
đầu ra

Học máy không giám sát

Học máy không giám
sát là các thuật toán áp
dụng khi chỉ có biến đầu
vào và không có biến
đầu ra dựa vào dữ liệu
không có nhãn
(unlabeled data) của
biến đầu ra

HỌC KHÔNG GIÁM SÁT: PHÂN CỤM

k-means chia dữ liệu thành k cụm sao cho các quan sát trong cùng một cụm gần nhau nhất. Ứng dụng điển
hình: phân khúc khách hàng, nhóm chi nhánh có hành vi tương tự, nén ảnh.
Không có “đáp án đúng” để đối chiếu — chất lượng phân cụm phải được đánh giá bằng chỉ số nội tại và,
quan trọng hơn, bằng ý nghĩa nghiệp vụ của các cụm tìm được.

4
2

HỌC KHÔNG GIÁM SÁT: GIẢM CHIỀU

Phân tích thành phần chính (PCA) tìm một số ít chiều mới, là tổ hợp tuyến tính của các biến gốc, giữ lại phần lớn thông tin.
Dùng để trực quan hoá, để nén dữ liệu, và để xử lý hiện tượng nhiều biến tương quan mạnh với nhau.
Cái giá phải trả: các chiều mới không còn ý nghĩa kinh tế trực tiếp — “thành phần chính thứ nhất” không phải là một biến ta có
thể giải thích cho khách hàng.

4
3

Học củng cố Reinforcement là một nhánh của học máy, trong đó một tác nhân (agent) học
cách đưa ra quyết định bằng cách tương tác với môi trường (environment) để tối ưu hóa
phần thưởng (reward).

3. Các mô hình học máy

CHỌN MÔ HÌNH NÀO?

Tình huống

Hướng lựa chọn

Dữ liệu bảng, cần giải thích rõ ràng

Hồi quy tuyến tính / logistic, cây quyết định

Dữ liệu bảng, ưu tiên độ chính xác

Rừng ngẫu nhiên, gradient boosting

Ảnh, âm thanh, video

Mạng nơ-ron sâu (CNN)

Văn bản, ngôn ngữ tự nhiên

Transformer, mô hình ngôn ngữ lớn

Không có nhãn, muốn tìm nhóm

k-means và các thuật toán phân cụm khác

Quá nhiều biến tương quan

PCA hoặc các phương pháp giảm chiều

Dữ liệu rất ít

Mô hình đơn giản, kiểm định chéo, thêm dữ liệu

Nguyên tắc làm việc: luôn bắt đầu bằng mô hình đơn giản nhất làm mốc so sánh, rồi mới thử mô hình phức tạp hơn —
và chỉ giữ mô hình phức tạp nếu nó thật sự tốt hơn đáng kể.

4
5

•Bias (Độ chệch):
Bias là sai số xảy ra do mô hình quá đơn giản hóa vấn đề (underfitting). Một mô hình có bias cao thường bỏ qua các mối quan hệ phức tạp trong
dữ liệu, dẫn đến việc dự đoán không chính xác trên cả tập huấn luyện và tập kiểm tra. Ví dụ, một mô hình tuyến tính áp dụng cho dữ liệu phi
tuyến tính sẽ có bias cao vì không thể nắm bắt được sự phức tạp của dữ liệu.
•Variance (Phương sai):
Variance đo lường mức độ nhạy cảm của mô hình đối với các thay đổi nhỏ trong dữ liệu huấn luyện. Một mô hình có variance cao (overfitting) sẽ
học quá chi tiết các đặc điểm của dữ liệu huấn luyện, bao gồm cả nhiễu, dẫn đến việc hoạt động tốt trên tập huấn luyện nhưng kém trên tập kiểm
tra. Ví dụ, một cây quyết định quá sâu có thể ghi nhớ dữ liệu huấn luyện thay vì học các mẫu tổng quát.

Dưới khớp và chưa khớp

Dưới khớp (underfitting). Mô hình quá đơn giản, sai cả trên tập huấn luyện lẫn tập kiểm tra. Cách
chữa: tăng độ phức tạp, thêm đặc trưng.
Quá khớp (overfitting). Mô hình học thuộc cả phần nhiễu, rất tốt trên tập huấn luyện nhưng kém
trên dữ liệu mới. Cách chữa: thêm dữ liệu, giảm độ phức tạp, dùng phạt (regularisation), dừng sớm.
Mục tiêu của học máy không phải là khớp thật tốt dữ liệu đã có, mà là dự đoán tốt dữ liệu chưa
từng thấy. Đây là khác biệt căn bản so với thống kê mô tả.

4
8

Underfitting (Dưới khớp)
•Định nghĩa:
Underfitting xảy ra khi mô hình quá đơn giản để học được cấu trúc từ dữ liệu. Nó không nắm bắt được
mối quan hệ giữa các biến đầu vào và đầu ra một cách đầy đủ.
•Nguyên nhân phổ biến:

•Mô hình quá đơn giản (ví dụ: dùng hồi quy tuyến tính cho một bài toán phi tuyến).
•Dữ liệu chưa được xử lý hoặc chưa đủ đặc trưng (feature).
•Huấn luyện chưa đủ thời gian (training chưa đầy đủ).

•Biểu hiện:

•Sai số cao trên cả tập huấn luyện và tập kiểm tra.
•Mô hình không học được điều gì có ích từ dữ liệu.

•Ví dụ:
Dự đoán điểm số sinh viên chỉ dựa vào số lần đến lớp, mà bỏ qua các yếu tố như thời gian học, điểm
bài tập, v.v.

Overfitting (Quá khớp)
•Định nghĩa:
Overfitting xảy ra khi mô hình quá phức tạp, học quá kỹ dữ liệu huấn luyện, bao gồm cả nhiễu và những điểm
không đại diện cho xu hướng thực tế.
•Nguyên nhân phổ biến:

• Mô hình quá phức tạp (nhiều lớp, nhiều tham số).
• Quá ít dữ liệu huấn luyện.
• Không sử dụng các kỹ thuật regularization hoặc validation.

•Biểu hiện:

• Sai số thấp trên tập huấn luyện.
• Sai số cao trên tập kiểm tra → mô hình hoạt động kém trên dữ liệu mới.

•Ví dụ:
Mô hình nhớ từng điểm dữ liệu thay vì học ra quy luật → như học vẹt, không tổng quát hóa được.

Optimal Fitting (Khớp tối ưu – vừa đủ)
•Định nghĩa:
Đây là trạng thái lý tưởng, nơi mô hình học được đúng mức từ dữ liệu: đủ để nắm bắt xu hướng tổng
thể mà không học theo nhiễu.
•Biểu hiện:

• Sai số thấp trên cả tập huấn luyện và kiểm tra.
• Mô hình có khả năng tổng quát hóa tốt (generalize well) trên dữ liệu chưa thấy.

•Làm thế nào để đạt được optimal fitting?

• Dùng cross-validation.
• Chọn mô hình có độ phức tạp phù hợp.
• Dùng kỹ thuật regularization.
• Cung cấp đủ dữ liệu huấn luyện.

Các bước cơ bản thực hiện mô hình machie learning
1. Xác định bài toán
2. Thu thập dữ liệu – Gathering data/Data collection
3. Tiền xử lý dữ liệu – Data preprocessing

Làm sạch dữ liệu – Data cleaning (Loại bỏ hoặc xử lý giá trị thiếu, giá trị ngoại lệ)
Chuyển đổi dữ liệu – Data transformation (Label Encoding, One-Hot Encoding)
Chuẩn hóa dữ liệu – Data normalization (Standardization, Normalization)
Trích xuất đặc trưng – Feature extraction (Feature selection, Feature engineering)

4. Phân chia tập dữ liệu thành tập train và tập test
5. Lựa chọn và huấn luyện mô hình (sử dụng tập train)
6. Huấn luyện mô hình
7. Đánh giá mô hình – Model evaluation (sử dụng tập test)
• Phân loại: Accuracy, Precision, Recall, F1-score, AUC
• Hồi quy: RMSE, MAE, R²
8. Hiệu chỉnh mô hình
Grid Search
•
• Random Search
• Cross-validation
9. Triển khai mô hình: Dự báo, phân lớp

3.1. Mô hình hồi quy

Hồi quy tuyến tính

Tìm các tham số sao cho tổng bình phương phần dư là nhỏ nhất

Đánh giá mô hình

Cây quyết định (Decision Tree Regression)

Decision Tree Hồi quy là mô hình học máy dựa trên cấu trúc cây phân tách để dự đoán giá trị số liên

tục (liên quan đến bài toán hồi quy). Mô hình chia dữ liệu thành các vùng nhỏ, sao cho mỗi vùng có

giá trị đầu ra càng đồng nhất càng tốt.

Thành phần chính của mỗi cây bao gồm các nút (node) và các nhánh, ba bước cơ bản của thuật toán là

chia tách cây, dừng và điều chỉnh.

Các loại nút: (a) Nút gốc, còn được gọi là nút quyết định, đại diện cho một lựa chọn sẽ dẫn đến việc chia

nhỏ tất cả các bản ghi thành hai hoặc nhiều tập hợp con loại trừ lẫn nhau. (b) Các nút bên trong, đại diện

cho một trong những lựa chọn có thể có tại một thời điểm trong cấu trúc cây; cạnh trên của nút được kết

nối với nút cha của nó và cạnh dưới được kết nối với các nút con hoặc nút lá của nó. (c) Nút lá, còn được

gọi là nút cuối, biểu thị kết quả cuối cùng các quyết định hoặc sự kiện.

Nguyên lý hoạt động:

• Tìm điểm chia (split) trên một biến đầu vào

sao cho giảm sai số dự báo lớn nhất

(thường dùng tiêu chí giảm MSE).

• Chia nhánh dữ liệu theo điều kiện.

• Lặp lại quá trình này cho đến khi đạt điều

kiện dừng (số lượng mẫu tối thiểu, độ sâu

cây, hoặc sai số nhỏ).

• Dự báo bằng giá trị trung bình của nhánh

lá mà dữ liệu thuộc vào.

 Ưu điểm:

Dễ hiểu và trực quan hóa (diễn giải tốt)

Xử lý dữ liệu phi tuyến rất tốt

Không yêu cầu chuẩn hóa dữ liệu

Tự động chọn biến quan trọng

 Nhược điểm:

Dễ overfitting nếu cây quá sâu

Nhạy cảm với dữ liệu nhiễu

Khó tổng quát hóa tốt trên tập dữ liệu mới

Mô hình rừng ngẫu nhiên (Random forest - RF)

Mô hình rừng ngẫu nhiên là một trong kỹ thuật mở rộng trên cây quyết định phát triển từ thuật

toán Bagging, được đề xuất lần đầu tiên bởi Breiman và cộng sự (1984). Random forest mở

rộng phương pháp cây quyết định bằng cách lấy ngẫu nhiên một lượng lớn số lượng cây từ dữ

liệu. Tại mỗi nút của cây, một tập hợp con của các biến đầu vào được chọn ngẫu nhiên để tạo

các nút của cây. Vì các biến đầu vào cho mỗi cây quyết định được chọn một cách ngẫu nhiên,

nó làm giảm sự tương quan giữa các cây và tránh vấn đề quá mức (overfitting).

Nguyên lý hoạt động:

• Bootstrap sampling: Lấy mẫu ngẫu

nhiên có hoàn lại từ tập huấn luyện

để tạo từng cây con.

• Random feature selection: Tại mỗi

nút phân chia, chỉ xét một tập con

ngẫu nhiên các biến thay vì toàn bộ

biến.

• Huấn luyện nhiều cây Decision Tree

(thường từ 100 đến 1000 cây).

• Dự báo đầu ra là trung bình dự báo

của tất cả các cây

 Ưu điểm:

Hiệu quả cao, độ chính xác tốt hơn Decision Tree đơn lẻ

Giảm overfitting nhờ kỹ thuật bagging

Xử lý tốt dữ liệu phi tuyến

Tự động đánh giá mức độ quan trọng của biến (feature

importance)

 Nhược điểm:

Khó giải thích hơn Decision Tree đơn lẻ

Tốn tài nguyên tính toán nếu nhiều cây

Thời gian huấn luyện lâu hơn

3.2. Mô hình phân lớp

Mô hình phân lớp là mô hình học máy được sử dụng để dự đoán nhãn đầu ra dạng phân

loại (categorical).

Ví dụ:

Khách hàng có vỡ nợ / không vỡ nợ

Email là spam / không spam

Giao dịch là gian lận / không gian lận

Hồi quy logistic

Hồi quy logistic là một trong những phương pháp thống kê phổ biến nhất dùng để phân lớp các
biến nhị phân được sử dụng để dự đoán xác suất một đối tượng thuộc vào một trong hai lớp (ví
dụ: vỡ nợ / không vỡ nợ).

• Ưu điểm của Logistic Regression:
Dễ hiểu, dễ giải thích
Hiệu quả với dữ liệu tuyến tính
Tính toán nhanh
Có thể thêm Regularization (L1, L2)
• Nhược điểm:
Hiệu suất kém nếu quan hệ phi tuyến tính
Nhạy cảm với outliers
Giả định tuyến tính giữa logit và biến đầu vào

p


1

p





x
  
e
1 1



0

x
2 2 ...
 



x
n n

Ma trận nhầm lẫn

TP (true positive) là số dự đoán tích cực, được

dự báo đúng là tích cực.

TN (true negative) là số dự đoán âm và mô hình

được dự đoán đúng

FP (false positive) (dương tính giả) là số lượng

trường hợp thực tế là âm, nhưng mô hình dự

đoán sai là dương, FN (false negative) (âm tính

giả) là số ượng trường hợp thực tế là dương,

nhưng mô hình lại dự đoán sai là âm.

CHAPTER 2

HEADER 1

Lorem ipsum dolor sit amet, consectetuer
adipiscing elit, sed diam nonummy nibh
euismod tincidunt ut
laoreet dolore
magna aliquam erat volutpat. Ut wisi enim
ad minim veniam, quis nostrud exerci
tation ullamcorper suscipit lobortis nisl ut
aliquip ex ea commodo consequat. Duis
autem vel eum iriure dolor in hendrerit in
vulputate velit esse molestie consequat, vel
illum dolore eu feugiat nulla facilisis at vero
eros et accumsan et iusto odio dignissim
qui blandit praesent luptatum zzril delenit
augue duis dolore te feugait nulla facilisi.

4

Học viện Ngân hàng
Học viện Ngân hàng

Header 2
Lorem  ipsum  dolor  sit  amet,  consectetuer  adipiscing  elit,  sed
diam  nonummy  nibh  euismod  tincidunt  ut  laoreet  dolore
magna aliquam erat volutpat. Ut wisi enim ad minim veniam,
quis nostrud exerci  tation ullamcorper suscipit lobortis  nisl ut
aliquip ex ea commodo consequat. Duis autem vel eum iriure
dolor  in  hendrerit  in  vulputate  velit  esse  molestie  consequat,
vel  illum  dolore  eu  feugiat  nulla  facilisis  at  vero  eros  et
accumsan  et
iusto  odio  dignissim  qui  blandit  praesent
luptatum zzril delenit augue duis dolore te feugait nulla facilisi.

Lorem ipsum dolor sit amet, cons ectetuer adipiscing elit, sed
diam  nonummy  nibh  euismod  tincidunt  ut  laoreet  dolore
magna aliquam erat volutpat. Ut wisi enim ad minim veniam,
quis nostrud exerci  tation ullamcorper suscipit lobortis  nisl ut
aliquip ex ea commodo consequat.

Lorem  ipsum  dolor  sit  amet,  consectetuer  adipiscing  elit,  sed
diam  nonummy  nibh  euismod  tincidunt  ut  laoreet  dolore
magna aliquam

CHAPTER 2

HEADER 1

Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh
euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.

Header 1
Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam
nonummy  nibh  euismod  tincidunt  ut
laoreet  dolore  magna
aliquam erat volutpat. Ut wisi enim ad minim veniam, quis nostrud
exerci  tation  ullamcorper  suscipit  lobortis  nisl  ut  aliquip  ex  ea
commodo consequat.  Duis  autem vel  eum  iriure dolor in  hendrerit
in  vulputate  velit  esse  molestie  consequat,  vel  illum  dolore  eu
feugiat  nulla  facilisis  at  vero  eros  et  accumsan  et  iusto  odio
dignissim  qui  blandit  praesent  luptatum  zzril  delenit  augue  duis
dolore te feugait nulla facilisi.

Header 2
Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam
nonummy  nibh  euismod  tincidunt  ut
laoreet  dolore  magna
aliquam erat volutpat. Ut wisi enim ad minim veniam, quis nostrud
exerci  tation  ullamcorper  suscipit  lobortis  nisl  ut  aliquip  ex  ea
commodo consequat.  Duis  autem vel  eum  iriure dolor in  hendrerit
in  vulputate  velit  esse  molestie  consequat,  vel  illum  dolore  eu
feugiat  nulla  facilisis  at  vero  eros  et  accumsan  et  iusto  odio
dignissim  qui  blandit  praesent  luptatum  zzril  delenit  augue  duis
dolore te feugait nulla facilisi.

Lorem ipsum dolor sit amet, cons ectetuer adipiscing elit, sed diam
nonummy  nibh  euismod  tincidunt  ut
laoreet  dolore  magna
aliquam erat volutpat.

Lorem ipsum dolor sit amet, cons ectetuer adipiscing elit, sed diam
nonummy  nibh  euismod  tincidunt  ut
laoreet  dolore  magna
aliquam erat volutpat.

3 Học viện Ngân hàng
5 Học viện Ngân hàng

CHAPTER 2

HEADER 1

Header 2
Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam
nonummy  nibh  euismod  tincidunt  ut
laoreet  dolore  magna
aliquam erat volutpat. Ut wisi enim ad minim veniam, quis nostrud
exerci  tation  ullamcorper  suscipit  lobortis  nisl  ut  aliquip  ex  ea
commodo consequat.  Duis  autem vel  eum  iriure dolor in  hendrerit
in  vulputate  velit  esse  molestie  consequat,  vel  illum  dolore  eu
feugiat  nulla  facilisis  at  vero  eros  et  accumsan  et  iusto  odio
dignissim  qui  blandit  praesent  luptatum  zzril  delenit  augue  duis
dolore te feugait nulla facilisi.

Lorem ipsum dolor sit amet, cons ectetuer adipiscing elit, sed diam
nonummy  nibh  euismod  tincidunt  ut
laoreet  dolore  magna
aliquam erat volutpat. Ut wisi enim ad minim veniam, quis nostrud
exerci  tation  ullamcorper  suscipit  lobortis  nisl  ut  aliquip  ex  ea
commodo consequat.

Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam
nonummy  nibh  euismod  tincidunt  ut
laoreet  dolore  magna
aliquam

3 Học viện Ngân hàng
6 Học viện Ngân hàng

50%

40%

30%

20%

10%

0%

2021

2022

2023

2024

CHAPTER 3

HEADER 1

Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam
erat volutpat. Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo
consequat. Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat, vel illum dolore eu feugiat nulla facilisis
at vero eros et accumsan et iusto odio dignissim qui blandit praesent luptatum zzril delenit augue duis dolore te feugait nulla facilisi.

Lorem ipsum dolor sit amet, cons ectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam
erat volutpat. Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo
consequat.

Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam
erat volutpat. Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo
consequat. Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat, vel illum dolore eu feugiat nulla facilisis
at vero eros et accumsan et iusto odio dignissim qui blandit praesent luptatum zzril delenit augue duis dolore te feugait nulla facilisi.

Lorem ipsum dolor sit amet, cons ectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam
erat volutpat. Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo
consequat.

Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam
erat volutpat. Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo
consequat.
3 Học viện Ngân hàng
7 Học viện Ngân hàng

CHAPTER 3

Lorem ipsum dolor sit amet, cons ectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.

8 Học viện Ngân hàng
3 Học viện Ngân hàng
8 Học viện Ngân hàng

CHAPTER 3

HEADER 1

nostrud

Lorem ipsum dolor sit amet, consectetuer
adipiscing elit, sed diam nonummy nibh
euismod tincidunt ut laoreet dolore magna
aliquam erat volutpat. Ut wisi enim ad
minim veniam,
exerci
quis
tation ullamcorper suscipit lobortis nisl ut
aliquip ex ea commodo consequat. Duis
autem vel eum iriure dolor in hendrerit in
vulputate velit esse molestie consequat,
illum dolore eu feugiat nulla facilisis at
vel
vero eros et accumsan et
iusto odio
dignissim qui blandit praesent luptatum
zzril delenit augue duis dolore te feugait
nulla facilisi.

Lorem ipsum dolor sit amet, cons ectetuer
adipiscing elit, sed diam nonummy nibh
euismod tincidunt ut laoreet dolore magna
aliquam erat volutpat.

8 Học viện Ngân hàng
3 Học viện Ngân hàng
9 Học viện Ngân hàng

Lorem ipsum dolor sit amet

Lorem ipsum dolor sit amet

Lorem ipsum dolor sit amet

Lorem ipsum dolor sit amet

Lorem ipsum dolor sit amet

THANK YOU FOR
WATCHING

Học viện Ngân hàng
12 P. Chùa Bộc, P. Quang Trung,
Q. Đống Đa, TP. Hà Nội

T: 1900 561 595 F: 1900 561 595
E: truyenthong@hvnh.edu.vn
W: www.hvnh.edu.vn

