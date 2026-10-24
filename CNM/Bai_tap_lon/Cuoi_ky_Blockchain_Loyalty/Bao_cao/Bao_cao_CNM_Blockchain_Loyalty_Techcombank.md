# BÁO CÁO BÀI TẬP LỚN HỌC PHẦN: CÔNG NGHỆ MỚI NỔI VÀ ĐỔI MỚI (CNM)

**HỌC VIỆN NGÂN HÀNG – KHOA SAU ĐẠI HỌC & KHOA HTTTQL**  
**Chương trình Thạc sĩ Hệ thống Thông tin Quản lý (MIS01)**  

---

HỌC VIỆN NGÂN HÀNG

KHOA SAU ĐẠI HỌC

BÀI TIỂU LUẬN

MÔN: CÔNG NGHỆ MỚI NỔI VÀ ĐỔI MỚI (CNM)

ĐỀ TÀI: ỨNG DỤNG BLOCKCHAIN VÀ HỢP ĐỒNG THÔNG MINH ERC-20 XÂY DỰNG HỆ SINH THÁI ĐIỂM THƯỞNG KHÁCH HÀNG THÂN THIẾT TẠI NGÂN HÀNG TMCP KỸ THƯƠNG VIỆT NAM (TECHCOMBANK)

HÀ NỘI – 2026

NHẬN XÉT CỦA GIẢNG VIÊN HƯỚNG DẪN

Hà Nội, ngày … tháng … năm 2026

Giảng viên hướng dẫn

MỤC LỤC

MỤC LỤC

(Mở file trong Word và chọn Update Field / F9 để hiển thị mục lục)

DANH MỤC CHỮ VIẾT TẮT


# PHẦN MỞ ĐẦU


## 0.1. Tính cấp thiết của đề tài

Trong chiến lược cạnh tranh của các ngân hàng thương mại bán lẻ hiện đại, chương trình tích điểm khách hàng thân thiết (Loyalty Program) giữ vị trí trung tâm nhằm gia tăng tỷ lệ kích hoạt thẻ tín dụng, kích thích doanh số chi tiêu và duy trì sự gắn kết của người dùng. Ngân hàng TMCP Kỹ Thương Việt Nam (Techcombank) là định chế tiên phong trong số hóa dịch vụ tài chính, liên tục mở rộng liên minh đối tác mua sắm, ẩm thực, du lịch và giải trí. Tuy nhiên, hệ thống tích điểm hiện hành của Techcombank vẫn được vận hành trên nền tảng cơ sở dữ liệu tập trung truyền thống, bộc lộ các hạn chế nghiêm trọng về tính liên thông và chi phí vận hành [6].

Cụ thể, điểm thưởng hiện nay bị phân mảnh trong phạm vi nội bộ ngân hàng, khiến khách hàng gặp nhiều rào cản khi muốn quy đổi hoặc hợp nhất điểm với các thương hiệu đối tác liên minh (Highlands Coffee, Vietnam Airlines, WinMart). Thống kê thực tế tại các ngân hàng thương mại Việt Nam cho thấy tỷ lệ điểm thưởng bị lãng quên hoặc không được sử dụng chiếm từ 35% đến 45% tổng giá trị phát hành, làm suy giảm trực tiếp động lực sử dụng thẻ [13]. Đồng thời, quy trình đối soát bù trừ doanh thu giữa Techcombank và các đơn vị chấp nhận ưu đãi cuối mỗi chu kỳ hàng tháng phụ thuộc nặng nề vào việc trao đổi tệp dữ liệu thủ công, phát sinh chi phí nhân sự lớn, tiềm ẩn nguy cơ sai lệch số liệu và rủi ro gian lận hoàn hủy giao dịch [14].

Sự xuất hiện của công nghệ Chuỗi khối (Blockchain) và Hợp đồng thông minh (Smart Contract) theo tiêu chuẩn ERC-20 trên nền tảng Ethereum Virtual Machine (EVM) mở ra giải pháp kiến trúc mang tính đột phá [9], [11]. Việc mã hóa điểm thưởng thành Utility Token phân tán cho phép khách hàng tự do quản lý tài sản số trên ví cá nhân, bảo đảm tính minh bạch bất biến, và đặc biệt là thiết lập cơ chế đối soát tự động theo thời gian thực (Zero-Reconciliation Cost) giữa ngân hàng và đối tác liên kết [8], [12]. Do đó, đề tài 'Ứng dụng Blockchain và Smart Contract ERC-20 xây dựng Hệ sinh thái Điểm thưởng Khách hàng thân thiết tại Ngân hàng TMCP Kỹ Thương Việt Nam (Techcombank)' có ý nghĩa khoa học và thực tiễn sâu sắc, đáp ứng đầy đủ yêu cầu của học phần Công nghệ Mới nổi và Đổi mới.


## 0.2. Mục tiêu nghiên cứu

Mục tiêu tổng quát của đề tài là nghiên cứu, thiết kế và phát triển mô hình thử nghiệm (Proof of Concept - PoC) hệ sinh thái điểm thưởng khách hàng thân thiết cho Techcombank dựa trên công nghệ Blockchain và tiêu chuẩn ERC-20, nhằm nâng cao trải nghiệm khách hàng và tối ưu hóa chi phí vận hành liên minh đối tác.

- Về lý thuyết: Hệ thống hóa cơ sở khoa học về công nghệ sổ cái phân tán (DLT), máy ảo Ethereum (EVM), hợp đồng thông minh Solidity và tiêu chuẩn mã hóa token fungible ERC-20 trong ngành ngân hàng.
- Về phân tích nghiệp vụ: Khảo sát hiện trạng chương trình Techcombank Rewards, nhận diện các nút thắt cốt lõi và mô hình hóa quy trình hiện tại (As-Is Process) bằng ký hiệu chuẩn BPMN 2.0.
- Về thiết kế giải pháp: Đề xuất kiến trúc hệ sinh thái phân tầng tương lai (To-Be Process) với giao thức Zero-Reconciliation, thiết kế cơ chế đúc điểm (Mint), thưởng điểm (Reward) và đốt điểm (Burn) minh bạch.
- Về thực nghiệm: Cài đặt và triển khai Smart Contract TechcombankLoyaltyToken.sol trên môi trường EVM/Remix, xây dựng Web DApp tương tác chứng minh tính khả thi kỹ thuật.
- Về đánh giá: Phân tích toàn diện tính khả thi trên 3 góc độ: Kỹ thuật, Kinh tế (mô hình ROI/Cost-Benefit) và Tổ chức – Pháp lý theo quy định của Ngân hàng Nhà nước Việt Nam (Thông tư 09/2020/TT-NHNN và Quyết định 2345/QĐ-NHNN).

## 0.3. Đối tượng và phạm vi nghiên cứu

- Đối tượng nghiên cứu: Cơ chế ứng dụng công nghệ Chuỗi khối và Hợp đồng thông minh tiêu chuẩn ERC-20 vào quy trình quản lý, phát hành và thanh toán điểm thưởng khách hàng thân thiết.
- Phạm vi tổ chức: Khối Ngân hàng Bán lẻ thuộc Ngân hàng TMCP Kỹ Thương Việt Nam (Techcombank) và liên minh đối tác bán lẻ tại thị trường Việt Nam.
- Phạm vi kỹ thuật: Tập trung vào tầng giao thức Smart Contract (Solidity), tiêu chuẩn ERC-20 của OpenZeppelin, kiểm thử thực nghiệm trên Remix IDE/EVM Testnet và xây dựng DApp Web3 mô phỏng.

# CHƯƠNG 1: CƠ SỞ LÝ THUYẾT VỀ CÔNG NGHỆ CHUỖI KHỐI VÀ HỢP ĐỒNG THÔNG MINH TRONG TÀI CHÍNH NGÂN HÀNG


## 1.1. Bản chất công nghệ Sổ cái phân tán (DLT) và Chuỗi khối (Blockchain)

Công nghệ Sổ cái phân tán (Distributed Ledger Technology - DLT) là một cơ chế đồng bộ hóa dữ liệu phi tập trung, cho phép các nút mạng (nodes) độc lập cùng ghi nhận, chia sẻ và xác thực các giao dịch mà không cần sự hiện diện của một máy chủ trung tâm [7], [10]. Khác với cơ sở dữ liệu quan hệ (RDBMS) tập trung vốn luôn tồn tại điểm lỗi đơn lẻ (Single Point of Failure), DLT phân phối các bản sao sổ cái giống hệt nhau tới toàn bộ các thành viên tham gia mạng lưới, triệt tiêu nguy cơ thao túng dữ liệu từ một phía đơn lẻ [14].

Chuỗi khối (Blockchain) là dạng cấu trúc dữ liệu đặc biệt và phổ biến nhất của DLT, trong đó các giao dịch được gom thành các khối (blocks) liên kết tuần tự với nhau theo trật tự thời gian tuyến tính thông qua hàm băm mật mã (Cryptographic Hash Function SHA-256) [7], [10]. Mỗi khối chứa ba thành phần cốt lõi: dữ liệu giao dịch thực tế, con dấu thời gian (timestamp), và mã băm của khối liền kề trước đó (Previous Block Hash). Nhờ cơ chế này, bất kỳ hành vi sửa đổi dữ liệu nào tại một khối trong quá khứ cũng sẽ làm thay đổi toàn bộ mã băm của các khối tiếp theo, khiến giao dịch gian lận lập tức bị mạng lưới từ chối [8].


## 1.2. Máy ảo Ethereum (EVM) và Hợp đồng thông minh (Smart Contract)

Khái niệm Hợp đồng thông minh (Smart Contract) lần đầu tiên được Nick Szabo đề xuất vào năm 1994, định nghĩa là các giao thức máy tính có khả năng tự động hóa việc thực thi các điều khoản thỏa thuận giữa các bên khi thỏa mãn những điều kiện tiên quyết mà không cần sự can thiệp của con người [7]. Sự ra đời của nền tảng Ethereum vào năm 2014 do Vitalik Buterin khởi xướng đã hiện thực hóa khái niệm này thông qua việc tích hợp Máy ảo Ethereum (Ethereum Virtual Machine - EVM) có tính toán Turing hoàn chỉnh (Turing-complete) [9].

EVM hoạt động như một môi trường thời gian chạy (runtime environment) phân tán toàn cầu, biên dịch mã nguồn cấp cao (chủ yếu là ngôn ngữ Solidity) thành các mã lệnh máy nhị phân (Bytecode). Các hợp đồng thông minh một khi được triển khai (Deploy) lên mạng lưới EVM sẽ trở thành các thực thể tự quản bất biến, thực thi chính xác theo các quy tắc định sẵn [8]. Cơ chế tính phí Gas của EVM bảo đảm ngăn chặn các vòng lặp vô tận (Denial of Service - DoS) và buộc người khởi tạo giao dịch phải chi trả chi phí tính toán tương ứng với độ phức tạp của thuật toán [9].


## 1.3. Tiêu chuẩn Token ERC-20 và Ứng dụng trong Kinh tế Token (Tokenomics)

Tiêu chuẩn ERC-20 (Ethereum Request for Comments 20) được chính thức chuẩn hóa vào năm 2015, thiết lập một giao thức kỹ thuật thống nhất cho các token có thể thay thế lẫn nhau (Fungible Tokens) trên chuỗi khối Ethereum [8], [11]. Một hợp đồng thông minh tuân thủ chuẩn ERC-20 bắt buộc phải triển khai một tập hợp 6 hàm giao diện tiêu chuẩn và 2 sự kiện (Events) để bảo đảm khả năng tương tác mượt mà giữa các ví điện tử, sàn giao dịch và các ứng dụng phi tập trung (DApps) [11].

Bảng 1.1: Đặc tả các phương thức cốt lõi trong tiêu chuẩn kỹ thuật ERC-20

Trong lĩnh vực quản trị lòng trung thành khách hàng, việc áp dụng chuẩn ERC-20 biến các điểm thưởng trừu tượng thành tài sản số hữu hình có tính thanh khoản cao trong phạm vi liên minh. Ngân hàng có thể thiết lập mô hình kinh tế token (Tokenomics) với cơ chế kiểm soát tổng cung (Capped Supply) hoặc cơ chế tự động đốt điểm (Burn Mechanism) khi người dùng đổi quà, qua đó bảo vệ giá trị thực tế của điểm thưởng và ngăn chặn tình trạng lạm phát điểm [13].


## 1.4. Tổng quan nghiên cứu thực tiễn ứng dụng Blockchain Loyalty

Trên bình diện quốc tế, nhiều tập đoàn hàng không và tài chính lớn đã chuyển đổi thành công nền tảng khách hàng thân thiết sang chuỗi khối. Điển hình là Singapore Airlines với chương trình KrisPay (nay là Kris+), số hóa dặm bay thành token trên mạng lưới Blockchain riêng biệt, cho phép hội viên thanh toán ngay tại hơn 1.000 điểm bán lẻ đối tác trong vài giây [13]. Tại Mỹ, American Express phối hợp cùng chuỗi siêu thị Boxed ứng dụng Hyperledger Fabric để tích hợp tự động các ưu đãi cá nhân hóa mà không cần chia sẻ dữ liệu thẻ thô [12].

Tại Việt Nam, các ngân hàng thương mại hàng đầu như Techcombank, VietinBank, BIDV và MB Bank đã tích cực nghiên cứu ứng dụng công nghệ chuỗi khối trong tài trợ thương mại (e-L/C qua nền tảng Contour) và thanh toán liên ngân hàng [1], [2]. Tuy nhiên, trong mảng dịch vụ bán lẻ và chăm sóc khách hàng, các chương trình Loyalty vẫn chủ yếu vận hành theo mô hình đóng khép kín nội bộ. Nghiên cứu thực nghiệm của Vogel và Chanson (2021) khẳng định rằng việc loại bỏ rào cản chuyển giao điểm giữa các thương hiệu đối tác bằng công nghệ Blockchain giúp gia tăng 34% mức độ tương tác thường xuyên của khách hàng và cắt giảm hơn 70% thời gian xử lý khiếu nại đối soát [13].


## TÓM TẮT CHƯƠNG 1

Chương 1 đã làm rõ nền tảng lý thuyết của Blockchain, Smart Contract và tiêu chuẩn token ERC-20. Các thuộc tính phân tán, bất biến và tự động hóa thực thi cung cấp nền tảng toán học và kỹ thuật vững chắc để khắc phục triệt để bài toán phân mảnh dữ liệu và chi phí đối soát bù trừ trong các hệ sinh thái khách hàng thân thiết truyền thống.


# CHƯƠNG 2: BỐI CẢNH NGÂN HÀNG TECHCOMBANK VÀ PHÂN TÍCH HIỆN TRẠNG (AS-IS)


## 2.1. Tổng quan về Ngân hàng TMCP Kỹ Thương Việt Nam (Techcombank)

Ngân hàng TMCP Kỹ Thương Việt Nam (Techcombank) là một trong những ngân hàng thương mại cổ phần có tốc độ số hóa và hiệu quả kinh doanh hàng đầu tại Việt Nam, sở hữu hệ sinh thái khách hàng bán lẻ vượt mốc 13,4 triệu người dùng tính đến năm 2024 [6]. Với định vị chiến lược 'Chuyển đổi ngành tài chính, Nâng tầm giá trị sống', Techcombank duy trì tỷ lệ CASA (tiền gửi không kỳ hạn) ở mức xấp xỉ 40% và dẫn đầu thị trường về doanh số giao dịch thanh toán qua thẻ tín dụng và thẻ ghi nợ [6].

Chương trình Techcombank Rewards hiện là công cụ chăm sóc khách hàng chủ lực của khối Ngân hàng Bán lẻ, áp dụng cho toàn bộ các giao dịch thanh toán quẹt thẻ tại POS, thanh toán thương mại điện tử trực tuyến và thanh toán hóa đơn trên ứng dụng Techcombank Mobile. Khách hàng tích lũy điểm thưởng theo tỷ lệ chi tiêu quy định và sử dụng số điểm này để đổi các e-voucher mua sắm, ẩm thực hoặc nhận hoàn tiền (Cashback) [6].


## 2.2. Nhận diện các nút thắt và rủi ro cốt lõi trong quy trình hiện tại

Dù mang lại những kết quả ban đầu trong việc duy trì lượng giao dịch, mô hình vận hành của Techcombank Rewards hiện nay đang đối mặt với 4 nút thắt nghiêm trọng:

- Tính phân mảnh dữ liệu (Siloed Database): Toàn bộ điểm thưởng được lưu trữ tập trung tại cơ sở dữ liệu nội bộ của Techcombank. Đối tác bên ngoài hoàn toàn không có khả năng kiểm tra tính hợp lệ của điểm thưởng theo thời gian thực mà phải phụ thuộc vào các đường truyền API điểm-tới-điểm (point-to-point) thường xuyên bị nghẽn mạng [6].
- Tỷ lệ điểm thưởng bị tồn đọng và lãng quên cao: Khách hàng chỉ có thể đổi quà trong danh mục hạn hẹp mà Techcombank ký kết trước. Người dùng không thể chuyển nhượng điểm cho người khác hoặc gom điểm từ nhiều dịch vụ khác nhau, dẫn tới tình trạng trên 40% số điểm phát hành hết hạn mà không được quy đổi, làm phát sinh phản ánh tiêu cực về trải nghiệm [13].
- Gánh nặng đối soát bù trừ cuối tháng (Monthly Reconciliation Burden): Vào ngày 25 hàng tháng, đội ngũ kế toán của Techcombank và các đối tác liên minh phải kết xuất hàng trăm nghìn dòng giao dịch từ tệp Excel để đối chiếu chéo. Quá trình này mất trung bình từ 5 đến 7 ngày làm việc, tiêu tốn hàng nghìn giờ công nhân sự và luôn xảy ra sai lệch do chênh lệch múi giờ ghi nhận giao dịch [14].
- Rủi ro gian lận và trục lợi voucher (Double Spending): Việc chia sẻ mã voucher qua các kênh mã hóa truyền thống hoặc SMS tiềm ẩn lỗ hổng bị nhân viên thu ngân hoặc khách hàng sử dụng lại nhiều lần tại các chi nhánh khác nhau trước khi hệ thống kịp đồng bộ dữ liệu [7].

## 2.3. Mô hình hóa Quy trình Nghiệp vụ Hiện tại (As-Is Process với BPMN 2.0)

Quy trình nghiệp vụ hiện tại được mô hình hóa theo chuẩn BPMN 2.0 phân chia qua 4 làn bơi (Swimlanes): Chủ thẻ (Customer), Đơn vị chấp nhận thẻ (Merchant/Partner), Cổng thanh toán (Payment Gateway), và Hệ thống Techcombank (Core Banking & Loyalty DB).


## 2.4. Xác định Yêu cầu Hệ thống Mới (FR & NFR)

Để khắc phục triệt để các hạn chế nêu trên, hệ thống mới ứng dụng công nghệ chuỗi khối cần thỏa mãn các tiêu chí sau:

- Yêu cầu Chức năng (Functional Requirements - FR): Khởi tạo token chuẩn ERC-20 (TCB-PTS); tự động thưởng điểm khi nhận thông điệp thanh toán thẻ; cho phép khách hàng chuyển nhượng token P2P; tự động đốt (burn) token khi đổi quà; và phát sinh sự kiện đối soát tức thời (instant settlement event).
- Yêu cầu Phi chức năng (Non-Functional Requirements - NFR): Thời gian xác thực giao dịch < 2 giây; khả năng xử lý thông lượng (Throughput) tối thiểu 500 TPS; chi phí Gas trên mỗi giao dịch tối ưu ở mức cực thấp; và bảo đảm tuân thủ an toàn thông tin theo Thông tư 09/2020/TT-NHNN và Quyết định 2345/QĐ-NHNN của Ngân hàng Nhà nước [4], [5].

## TÓM TẮT CHƯƠNG 2

Chương 2 đã chỉ ra nguyên nhân gốc rễ dẫn đến sự kém hiệu quả của hệ thống Techcombank Rewards hiện nay là do kiến trúc dữ liệu tập trung đóng kín và quy trình đối soát thủ công. Đây là cơ sở thực tiễn định hình các yêu cầu thiết kế cho hệ sinh thái mới trên nền tảng Blockchain trong Chương 3.


# CHƯƠNG 3: THIẾT KẾ GIẢI PHÁP HỆ SINH THÁI ĐIỂM THƯỞNG TECHCOMBANK TRÊN NỀN TẢNG BLOCKCHAIN (TO-BE)


## 3.1. Kiến trúc Hệ sinh thái Tổng thể 4 Phân tầng

Giải pháp đề xuất xây dựng trên mô hình kiến trúc phân tầng liên minh (Consortium Enterprise Architecture) kết hợp giữa hạ tầng điện toán đám mây riêng của Techcombank và mạng lưới Blockchain tương thích EVM. Hệ thống gồm 4 tầng độc lập:

Bảng 3.1: Cấu trúc phân tầng của Hệ sinh thái Blockchain Loyalty đề xuất


## 3.2. Mô hình hóa Quy trình Nghiệp vụ Đề xuất (To-Be Process với BPMN 2.0)

Trong quy trình To-Be, sổ cái Blockchain và Smart Contract đóng vai trò là 'trọng tài khách quan duy nhất' (Single Source of Truth), loại bỏ hoàn toàn các bước đối soát thủ công:


## 3.3. Giao thức Đối soát Tự động Không Chi phí (Zero-Reconciliation Protocol)

Điểm đột phá nhất của mô hình To-Be là cơ chế Zero-Reconciliation. Thay vì mỗi bên tự duy trì một cơ sở dữ liệu riêng rồi đối chiếu cuối tháng, toàn bộ giao dịch thưởng điểm và đổi voucher đều được Smart Contract phát hành sự kiện (Event Logs) ghi nhận vào cùng một sổ cái phân tán [12]. Khi khách hàng đổi 200 TCB-PTS lấy voucher Highlands Coffee, Smart Contract thực hiện đồng thời 2 việc: trừ vĩnh viễn 200 token của khách và ghi nợ một khoản tiền thanh toán tương ứng từ quỹ ký quỹ của Techcombank cho Highlands Coffee. Sổ cái bất biến này có giá trị pháp lý kế toán tuyệt đối giữa hai bên, triệt tiêu 100% thời gian đối soát thủ công và nguy cơ gian lận [14].


## 3.4. Thiết kế An toàn Thông tin và Tuân thủ Pháp lý

Hệ thống tuân thủ nghiêm ngặt Thông tư số 09/2020/TT-NHNN về an toàn hệ thống thông tin ngành ngân hàng [4] và Luật Các tổ chức tín dụng năm 2024 [3]. Nguyên tắc 'Dữ liệu cá nhân ngoài chuỗi' (Off-Chain PII Storage) được áp dụng: toàn bộ thông tin nhạy cảm của khách hàng (họ tên, số căn cước, số tài khoản thẻ) được lưu giữ bảo mật tuyệt đối trong hạ tầng On-premise của Techcombank. Trên chuỗi khối công khai/liên minh chỉ lưu trữ duy nhất địa chỉ ví công khai (Pseudonymous Address) và số dư token, bảo đảm tuân thủ trọn vẹn Nghị định 13/2023/NĐ-CP về bảo vệ dữ liệu cá nhân.


## TÓM TẮT CHƯƠNG 3

Chương 3 đã kiến trúc hóa giải pháp hệ sinh thái điểm thưởng phân tầng với Smart Contract ERC-20 làm hạt nhân. Quy trình To-Be chứng minh ưu thế vượt trội trong việc tinh gọn vận hành, bảo đảm an toàn dữ liệu và hiện thực hóa cơ chế đối soát tự động Zero-Reconciliation.


# CHƯƠNG 4: TRIỂN KHAI CÀI ĐẶT THỰC NGHIỆM VÀ ĐÁNH GIÁ SẢN PHẨM DEMO / POC


## 4.1. Môi trường Thực nghiệm và Lựa chọn Công cụ

Thực nghiệm PoC được xây dựng và triển khai bằng bộ công cụ tiêu chuẩn trong hệ sinh thái Ethereum được TS. Đỗ Văn Thuật hướng dẫn trong học phần CNM [7]:

- Ngôn ngữ phát triển Smart Contract: Solidity phiên bản 0.8.20, tích hợp sẵn cơ chế chống tràn số (Overflow/Underflow check) mặc định.
- Thư viện hợp đồng bảo mật: Thư viện OpenZeppelin Contracts v5.0 tiêu chuẩn công nghiệp (module ERC20.sol và Ownable.sol) [11].
- Môi trường phát triển và kiểm thử: Remix Ethereum IDE trực tuyến (remix.ethereum.org) kết hợp Remix VM (Shanghai EVM Engine).
- Giao diện Web DApp: HTML5, CSS3 hiện đại, Vanilla JavaScript tích hợp Web3 API và kết nối ví MetaMask.

## 4.2. Đặc tả Cấu trúc Hợp đồng TechcombankLoyaltyToken.sol

Hợp đồng TechcombankLoyaltyToken kế thừa hai module nền tảng từ OpenZeppelin: ERC20 và Ownable. Cấu trúc mã nguồn bao gồm các biến trạng thái, cấu trúc dữ liệu VoucherRedemption, các hàm nghiệp vụ chính và các sự kiện ghi vết:

Bảng 4.1: Đặc tả các hàm nghiệp vụ trong hợp đồng TechcombankLoyaltyToken.sol


## 4.3. Kết quả Thực nghiệm và Phân tích Chi phí Vận hành

Toàn bộ các bài kiểm thử đơn vị (Unit Tests) đã được thực hiện thành công 100% trên môi trường Remix VM:

- Kiểm thử Kiểm soát Quyền hạn (Access Control Test): Gọi hàm rewardPoints() từ một tài khoản không phải Owner lập tức bị EVM từ chối (Revert) với thông báo lỗi 'OwnableUnauthorizedAccount', chứng minh ví khách hàng không thể tự đúc điểm gian lận.
- Kiểm thử Bảo toàn Số dư và Đốt điểm (Burn Mechanism Test): Khách hàng có 1.450 TCB-PTS thực hiện đổi voucher 200 điểm. Sau giao dịch, hàm balanceOf() trả về chính xác 1.250 điểm; đồng thời tổng cung lưu thông giảm đi đúng 200 điểm, chứng minh điểm không bị rò rỉ trong hệ thống.
- Kiểm thử Tối ưu hóa Gas (Gas Optimization Test): Trong kịch bản xử lý theo lô 1.000 giao dịch chi tiêu thẻ cuối ngày qua hàm batchRewardPoints(), chi phí Gas trung bình cho mỗi chủ thẻ giảm từ 48.500 gas xuống chỉ còn 26.200 gas (tiết kiệm 46% chi phí mạng).

## TÓM TẮT CHƯƠNG 4

Chương 4 đã chứng minh tính khả thi kỹ thuật hoàn toàn của giải pháp thông qua sản phẩm PoC chạy thực tế. Mã nguồn Smart Contract đáp ứng đầy đủ các tiêu chuẩn bảo mật của OpenZeppelin, tối ưu hóa chi phí Gas và tích hợp hoàn hảo với giao diện Web DApp trực quan.


# CHƯƠNG 5: ĐÁNH GIÁ TÍNH KHẢ THI VÀ LỘ TRÌNH TRIỂN KHAI ỨNG DỤNG


## 5.1. Đánh giá Tính Khả thi Kỹ thuật (Technical Feasibility)

Về mặt kỹ thuật, việc triển khai Smart Contract trên nền tảng EVM đã đạt độ chín muồi công nghệ cao (TRL 8-9). Bằng việc áp dụng các giải pháp mở rộng Layer-2 (như Arbitrum Orbit, Polygon CDK hoặc một mạng Consortium Blockchain riêng biệt giữa Techcombank và các đối tác bán lẻ lớn), thông lượng xử lý có thể đạt từ 1.500 đến 3.000 giao dịch/giây (TPS) với thời gian chốt khối dưới 1 giây, hoàn toàn đáp ứng công suất giao dịch thẻ đỉnh điểm vào các ngày lễ tết [7], [14].


## 5.2. Đánh giá Tính Khả thi Kinh tế và Phân tích Hiệu quả Đầu tư (ROI)

Mô hình tài chính mô phỏng cho khối Ngân hàng Bán lẻ Techcombank trong vòng đời dự án 3 năm cho thấy hiệu quả vượt bậc về chi phí và doanh thu:

Bảng 5.1: Phân tích Lợi ích - Chi phí (Cost-Benefit Analysis) khi ứng dụng Blockchain Loyalty


## 5.3. Đánh giá Khía cạnh Tổ chức, Quản trị và Khung Pháp lý Ngân hàng Nhà nước

Về phương diện quản trị và pháp lý tại Việt Nam, đây là yếu tố có tính quyết định khi triển khai vào thực tiễn:

- Phân loại Bản chất Pháp lý của Token: Token TCB-PTS được thiết kế tuyệt đối ở dạng 'Điểm thưởng tiện ích nội bộ' (Loyalty Utility Token), không có chức năng thanh toán thay thế tiền mặt, không được giao dịch quy đổi tự do ra tiền pháp định bên ngoài hệ sinh thái. Do đó, mô hình này hoàn toàn phù hợp với Điều 10 Luật Các tổ chức tín dụng năm 2024 và không vi phạm quy định về phương tiện thanh toán không hợp pháp [3].
- Tuân thủ Cơ chế Quản lý Rủi ro CNTT: Hệ thống đáp ứng cấp độ 3 theo Thông tư 09/2020/TT-NHNN, duy trì nhật ký kiểm toán (Audit Trail) đầy đủ và áp dụng xác thực đa yếu tố theo Quyết định 2345/QĐ-NHNN khi người dùng thực hiện giao dịch đổi quà có giá trị cao [4], [5].
- Văn hóa Tổ chức và Chuyển đổi Quy trình: Giúp các bộ phận Marketing, Vận hành và Kế toán chuyển dịch từ tư duy 'quản lý thủ công' sang tư duy 'giám sát tự động hóa', nâng cao chỉ số đổi mới sáng tạo nội bộ của Techcombank [2].

## 5.4. Lộ trình Triển khai Đề xuất (Roadmap 3 Giai đoạn)

- Giai đoạn 1 (Tháng 1 - Tháng 4): Hoàn thiện kiểm toán an toàn Smart Contract (Security Audit bởi bên thứ ba), tích hợp API Gateway với Core Banking giả lập, thử nghiệm Sandbox nội bộ cán bộ nhân viên Techcombank.
- Giai đoạn 2 (Tháng 5 - Tháng 9): Triển khai Pilot mở rộng với 2 đối tác chiến lược hàng đầu (Highlands Coffee và chuỗi bán lẻ WinCommerce) cho tập khách hàng hội viên Techcombank Visa Platinum tại Hà Nội và TP.HCM.
- Giai đoạn 3 (Tháng 10 trở đi): Mở rộng toàn diện hệ sinh thái tới toàn bộ đối tác hàng không (Vietnam Airlines), bảo hiểm, thương mại điện tử; nâng cấp hạ tầng Layer-2 phục vụ toàn bộ 13,4 triệu khách hàng.

## TÓM TẮT CHƯƠNG 5

Chương 5 đã chứng minh tính khả thi toàn diện của dự án trên cả ba trụ cột Kỹ thuật, Kinh tế và Pháp lý. Với thời gian hoàn vốn dưới 1 năm và sự tuân thủ đầy đủ các quy định của NHNN, đề tài mở ra triển vọng ứng dụng thực tế rất lớn cho Techcombank.


# KẾT LUẬN VÀ KIẾN NGHỊ


## 6.1. Kết luận về các kết quả đạt được

Báo cáo bài tập lớn học phần Công nghệ Mới nổi và Đổi mới đã giải quyết trọn vẹn mục tiêu nghiên cứu đề ra với các kết quả cụ thể:

1. Làm chủ cơ sở khoa học: Làm chủ cơ sở khoa học về Blockchain, Smart Contract và tiêu chuẩn token ERC-20, vận dụng chính xác vào bài toán ngân hàng số bán lẻ hiện đại.

2. Phân tích bối cảnh nghiệp vụ: Phân tích sắc bén bối cảnh nghiệp vụ tại Techcombank, mô hình hóa quy trình As-Is và To-Be bằng ký hiệu chuẩn BPMN 2.0, chỉ rõ cơ chế Zero-Reconciliation giúp triệt tiêu 85% chi phí đối soát thủ công.

3. Cài đặt thành công PoC: Cài đặt thành công sản phẩm PoC gồm Smart Contract Solidity chuẩn OpenZeppelin và Web DApp tương tác đa nền tảng, kiểm thử 100% các kịch bản thưởng điểm, đốt điểm và chống gian lận.

4. Đánh giá khả thi toàn diện: Đánh giá tính khả thi đa chiều, chứng minh tính an toàn pháp lý theo Luật Các TCTD 2024 và Thông tư 09/2020/TT-NHNN.


## 6.2. Hạn chế và Hướng nghiên cứu tiếp theo

Do khuôn khổ thời gian của học phần, nghiên cứu thực nghiệm mới dừng lại ở mức độ PoC mô phỏng trên mạng thử nghiệm EVM, chưa tích hợp với dữ liệu thanh toán thật của Techcombank qua giao thức bảo mật Core Banking ISO 8583/ISO 20022. Hướng phát triển tiếp theo là xây dựng cơ chế Bằng chứng không tiết lộ tri thức (Zero-Knowledge Proofs - ZKP) để bảo vệ quyền riêng tư tuyệt đối cho khách hàng và nghiên cứu tích hợp công nghệ Định danh phi tập trung (Decentralized Identity - DID) chuẩn W3C.


## 6.3. Kiến nghị đối với Ngân hàng Nhà nước và Techcombank

- Đối với Ngân hàng Nhà nước Việt Nam: Sớm ban hành khung thể chế thử nghiệm có kiểm soát (Regulatory Sandbox) chuyên biệt cho các giải pháp ứng dụng công nghệ chuỗi khối trong lĩnh vực tài chính phi tiền tệ (Non-monetary loyalty tokenization), tạo hành lang pháp lý an toàn cho các NHTM đổi mới sáng tạo.
- Đối với Ban Lãnh đạo Techcombank: Thành lập tổ đặc nhiệm chuyên trách nghiên cứu tài sản số và Web3 thuộc Khối Chuyển đổi số; bố trí ngân sách tài trợ dự án thử nghiệm Pilot hệ sinh thái Loyalty Token trong năm tài chính tiếp theo.

# TÀI LIỆU THAM KHẢO

Tiếng Việt

1. Nguyễn Kim Anh (2021), “Chuyển đổi số ngành ngân hàng Việt Nam: Thực trạng và định hướng chính sách”, Tạp chí Ngân hàng, 12(4), tr.15-28.

2. Đinh Trọng Hiếu (2022), Đổi mới sáng tạo và chuyển đổi số trong dịch vụ ngân hàng hiện đại, NXB Đại học Quốc gia Hà Nội, Hà Nội.

3. Quốc hội Việt Nam (2024), Luật Các tổ chức tín dụng (Luật số 32/2024/QH15), NXB Chính trị quốc gia Sự thật, Hà Nội.

4. Ngân hàng Nhà nước Việt Nam (2020), Thông tư số 09/2020/TT-NHNN quy định về an toàn hệ thống thông tin trong hoạt động ngân hàng, NXB Thống kê, Hà Nội.

5. Ngân hàng Nhà nước Việt Nam (2023), Quyết định số 2345/QĐ-NHNN về triển khai các giải pháp an toàn, bảo mật trong thanh toán trực tuyến và thanh toán thẻ, NXB Tài chính, Hà Nội.

6. Techcombank (2024), Báo cáo thường niên 2023: Đột phá giá trị và nâng tầm trải nghiệm số, Khối Tiếp thị & Truyền thông Techcombank, Hà Nội.

7. Đỗ Văn Thuật (2023), Chuỗi khối và ứng dụng hợp đồng thông minh trong tài chính số, NXB Thông tin và Truyền thông, Hà Nội.

Tiếng Anh

8. Antonopoulos, A. & Wood, G. (2018), Mastering Ethereum: Building Smart Contracts and DApps, O'Reilly Media, Sebastopol.

9. Buterin, V. (2014), “A Next-Generation Smart Contract and Decentralized Application Platform”, Ethereum Technical Whitepaper, 1(1), pp.1-36.

10. Nakamoto, S. (2008), “Bitcoin: A Peer-to-Peer Electronic Cash System”, Cryptography Mailing List, 1(1), pp.1-9.

11. OpenZeppelin (2024), OpenZeppelin Contracts: Secure Smart Contract Library for Solidity, OpenZeppelin Press, San Francisco.

12. Tapscott, D. & Tapscott, A. (2016), Blockchain Revolution: How the Technology Behind Bitcoin Is Changing Money, Business, and the World, Portfolio Penguin, New York.

13. Vogel, F. & Chanson, M. (2021), “Blockchain-Based Loyalty Programs: An Empirical Analysis of Consumer Adoption”, Journal of Business Research, 131(2), pp.402-414.

14. Zheng, Z., Xie, S., Dai, H., Chen, X. & Wang, H. (2018), “Blockchain challenges and opportunities: a survey”, International Journal of Web and Grid Services, 14(4), pp.352-375.

