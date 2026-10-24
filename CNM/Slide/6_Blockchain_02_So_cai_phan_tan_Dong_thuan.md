# Chương 6: Blockchain Phần 2 - Cơ chế Đồng thuận & Nền tảng Kỹ thuật
**Học phần:** Công nghệ mới nổi và Đổi mới (CNM / MIS01)
**Học viện Ngân hàng (Banking Academy of Vietnam - HVNH)**
**Nguồn bài giảng gốc:** `6_Blockchain_02.pdf`

---

## Slide 1: Công nghệ mới nổi và đổi mới

Chuỗi khối - Blockchain

---

## Slide 2: 2


---

## Slide 3: Sổ cái phân tán (Distributed Ledger)

- Một sổ cái điện tử: một cơ sở dữ liệu chứa toàn bộ thông tin giao dịch – transaction được cập nhật liên
tục.
- Cấu tạo bởi nhiều khối – block (mỗi khối chứa ít nhất một giao dịch) và các khối này được nối với
nhau thành một chuỗi – chain bằng cách sử dụng mật mã học: khối sau sẽ chứa các thông tin định
danh mật mã của khối trước. Vì vậy, nếu bất kì khối nào trong quá khứ xảy ra vấn đề thì sẽ ảnh hưởng
tới tất cả các khối ở phía sau của chuỗi.
Đặc điểm nổi bật:
- Sổ cái loại bỏ sự cần thiết của cơ quan trung ương hoặc người trung gian để xử lý và xác thực các giao
dịch
- Các bản ghi dữ liệu chỉ được lưu trữ trong sổ cái khi các bên liên quan đạt được sự đồng thuận
- Tất cả những người tham gia sẽ được chia sẻ 1 bản sao của sổ cái bao gồm tất cả các bản ghi được cập
nhật
- Số cái cung cấp lịch sử có thể xác minh và kiểm tra được của tất cả thông tin được lưu trữ trên tập dữ
liệu cụ thể theo trình tự thời gian

---

## Slide 4: Cơ chế đồng thuận

- Cơ chế đồng thuận (Consensus
Mechanism) (hay thuật toán/giao thức đồng
thuận) trong Blockchain là quy trình mà các
nút (nodes) trong mạng lưới phi tập trung đạt
được sự đồng thuận (thống nhất) về trạng
thái của dữ liệu.
- Ví dụ:  Block nào là hợp lệ?  Giao dịch nào sẽ
được ghi vào chuỗi?

---

## Slide 5: Mục tiêu của cơ chế đồng thuận

Mục tiêu chính
Giải thích
Đồng thuận phân tán
Tất cả các nút không cần tin tưởng nhau nhưng vẫn đi đến cùng một kết quả.
Ngăn chặn gian lận
Tránh các hành vi như “double spending” (chi tiêu 2 lần), giả mạo dữ liệu.
Duy trì tính toàn vẹn
Đảm bảo mỗi block mới được thêm vào là hợp lệ, không gây xung đột dữ
liệu.
Không cần bên trung gian Không cần ngân hàng hay tổ chức xác thực trung gian để xác nhận giao dịch.

---

## Slide 6: Hoạt động của cơ chế đồng thuận

- Một node đề xuất block mới.
- Các node khác kiểm tra block:
- Có đúng định dạng?
- Giao dịch có hợp lệ không?
- Cơ chế đồng thuận quyết định có chấp nhận
block này không.
- Nếu có đủ số node đồng thuận (tùy theo cơ
chế), block được thêm vào chuỗi.
Nguồn: https://www.zeeve.io/blog/consensus-mechanisms-in-blockchain/

---

## Slide 7: Hệ thống chịu lỗi Byzantine (BFT)

- Cơ chế đồng thuận giúp blockchain trở thành hệ thống chịu lỗi
Byzantine (Byzantine Fault Tolerance - BFT)

---

## Slide 8: Proof of Work (PoW)

- Proof of Work (PoW) hay bằng chứng công việc là cơ chế đồng
thuận phi tập trung đầu tiên, được sử dụng để bảo mật blockchain
Bitcoin.
- PoW yêu cầu các node sử dụng sức mạnh tính toán của máy tính để
giải các bài toán và tạo ra mã hash.
- Node đầu tiên giải bài toán và giành quyền xác thực giao dịch thì sẽ
được nhận phần thưởng là đồng coin native của blockchain (vd: BTC,
ETH). Quá trình này được gọi là “mining” (đào coin), và node này
được gọi là miner node (thợ đào).
- Nếu một miner node giải được bài toán, xác thực và ghi giao dịch lên
khối mới, khối này sẽ được gửi tới tất cả các node khác trong mạng
lưới.
- Khi có đủ số lượng node xác thực khối, chúng sẽ đạt được sự đồng
thuận và giao dịch sẽ được xử lý.

---

## Slide 9: Proof of Work (PoW)

Hạn chế của PoW:
- PoW sử dụng sức mạnh máy tính để bảo mật cho blockchain, do đó
o Tiêu thụ nhiều điện
o Chi phí phần cứng cao.
- Một block trên blockchain PoW cần nhiều thời gian để được tạo ra và
xác thực, khiến cho thuật toán này
- kém hiệu quả
- tốn tài nguyên
hơn các thuật toán đồng thuận khác.

---

## Slide 10: Proof of Stake (PoS)

- Proof of Stake (bằng chứng cổ phần) là thuật toán đồng thuận phổ biến nhất
hiện nay, được giới thiệu bởi Peercoin (2013).
- Proof of Stake yêu cầu các node tham gia xác thực giao dịch phải đặt cược
(stake) một số lượng nhất định đồng coin native của blockchain để giành
quyền tham gia xác thực và tạo khối.
- Số token này nhằm đảm bảo các node hoạt động tốt - nếu node đó offline quá
lâu hoặc có những hành vi gian lận, số token đã stake có thể bị thu một phần
hoặc mất toàn bộ tuỳ thuộc vào mức độ và quy định slashing (phạt).
- Trong cơ chế PoS, node sẽ đóng vai trò là các validator thay vì miner như
trong PoW

---

## Slide 11: Proof of Stake (PoS)

- Các validator trong mạng lưới PoS sẽ
nhận được phí giao dịch làm phần
thưởng.
- Khi một giao dịch diễn ra, các
validator sẽ được chọn để xác thực
giao dịch dựa trên số lượng token và
thời gian stake.
- Stake càng nhiều và thời gian càng lâu
thì tỉ lệ được chọn sẽ càng cao.

---

## Slide 12: Delegated Proof of Stake (DPoS)

- Bằng chứng uỷ quyền cổ phần
(DPoS), là thuật toán đồng thuận
được phát triển từ PoS.
- DPoS cho phép người nắm giữ token
(holder) stake token và chọn một
người đại diện (delegator) để uỷ
quyền xác thực giao dịch, duy trì bảo
mật cho blockchain.
- Holder sẽ được chia sẻ phần thưởng
từ việc gián tiếp vận hành mạng lưới.

---

## Slide 13: Proof of Authority (PoA)

- Proof of Authority (PoA) hay bằng chứng uỷ quyền là thuật toán - đồng thuận dựa trên danh
tiếng, phát triển dựa trên PoS.
- Thay vì “đặt cược”, validator đặt “uy tín” của mình để được tham gia vào mạng lưới node
xác thực giao dịch và khối của blockchain
- Các validator đóng vai trò như những người vận hành của hệ thống.
- PoA đề cao giá trị danh tính, tức là những người được chọn để trở thành validator phải thật sự
đáng tin cậy. Điều này khiến cho các blockchain PoA phải đối mặt với sự đánh đổi giữa tính
phi tập trung và khả năng mở rộng.

---

## Slide 14: Một số cơ chế đồng thuận phổ biến

Cơ chế
Đặc điểm chính
Ứng dụng nổi bật
PoW – Proof of Work
PoS – Proof of Stake
DPoS – Delegated PoS
Dùng sức mạnh tính toán để giải bài
toán mật mã → ai giải trước được ghi
block.
Người xác thực (validator) được chọn
dựa trên lượng to
ken họ nắm giữ.
Bitcoin, Litecoin
Ethereum (sau Merge), Cardano
Người dùng bầu ra một nhóm đại biểu
xác thực block.
EOS, TRON
PBFT – Practical Byzantine Fault Tolerance
Đạt đồng thuận qua bỏ phiếu giữa các node
đáng tin cậy.
Hyperledger Fabric
PoA – Proof of Authority
Dựa trên danh tiếng và danh tính xác minh
của validator.
VeChain, BSC (trong một số giai đoạn)

---

## Slide 15: Mạng ngang hàng (Peer-to-Peer network)

- Hệ thống các nút (nodes) kết nối
ngang hàng (P2P)
- Không có máy chủ trung tâm
- Mỗi nút tham gia linh hoạt vai trò
như một máy khách và một máy
chủ của các nút khác để cùng cung
cấp và kiểm soát dữ liệu giao dịch

---

## Slide 16: Đặc điểm chính của mạng blockchain

- Phi tập trung: Không có máy chủ trung tâm.
- Minh bạch: Dữ liệu được chia sẻ cho tất cả các node.
- Bất biến: Dữ liệu đã ghi thì không thể sửa đổi.
- Khả năng chống lỗi cao: Nếu một node ngừng hoạt động, các node khác
vẫn duy trì mạng.

---

## Slide 17: Node (Nút) trong Blockchain

- Node là thiết bị/máy tính tham gia mạng blockchain
- Có thể lưu trữ, xác minh, và truyền dữ liệu giao dịch
- Mỗi node hoạt động độc lập nhưng đồng bộ với mạng

---

## Slide 18: Các loại node

Loại node
Chức năng chính
Ví dụ sử dụng
Full Node
Lưu toàn bộ blockchain, xác minh block và giao dịch
Bitcoin Core, Geth (ETH)
Light Node
Lưu tiêu đề block, xác minh đơn giản (SPV)
Ví Electrum, ví Trust
Mining Node
Giải thuật toán PoW để tạo block mới
Máy đào Bitcoin
Validator Node
Xác thực block (PoS) dựa trên số coin đã stake
Ethereum 2.0, Cardano
Masternode
Hỗ trợ các dịch vụ đặc biệt, thường cần stake coin
Dash, Zcoin
Archive Node
Lưu toàn bộ lịch sử giao dịch + trạng thái chi tiết
Blockchain explorer

---

## Slide 19: Quá trình giao tiếp giữa các node trong mạng

1.
2.
3.
4.
Một giao dịch mới được khởi tạo bởi một node.
Giao dịch đó được gửi (broadcast) tới các node khác.
Các node xác minh giao dịch (chữ ký, số dư, v.v.).
Node đào (hoặc validator) sẽ chọn giao dịch để tạo block
mới.
5.
6.
Block hợp lệ được gửi cho toàn mạng.
Tất cả node cập nhật blockchain của mình với block mới.

---

## Slide 20: Lợi ích của mạng phân tán và đa node

Ưu điểm
Giải thích
Bảo mật cao
Không có điểm lỗi đơn → khó bị hack
Minh bạch
Mọi node đều có thể kiểm chứng dữ liệu
Dễ mở rộng và thay thế (linh hoạt)
Thêm/bớt node mà không ảnh hưởng toàn mạng
Tính sẵn sàng (khả năng chịu lỗi) cao
Dù nhiều node ngắt kết nối, hệ thống vẫn hoạt động

---

## Slide 21: Các mô hình Blockchain


---

## Slide 22: Blockchain công khai (Public Blockchain)

Là mô hình phi tập trung hoàn toàn, ai cũng có thể tham gia, đọc – ghi dữ liệu và xác
thực giao dịch.
Đặc điểm:
- Bất kỳ ai cũng có thể:
- Truy cập dữ liệu
- Tham gia xác nhận giao dịch (mining/validating)
- Cơ chế đồng thuận thường là Proof of Work (PoW) hoặc Proof of Stake (PoS).
- Không cần sự tin tưởng vào bên thứ ba.
Ưu điểm:
Nhược điểm:
- Phi tập trung, minh bạch
- Tốc độ xử lý chậm
- Bảo mật cao (nếu có nhiều node)
- Tốn năng lượng (đặc biệt với PoW)

---

## Slide 23: Blockchain riêng tư (Private Blockchain)

Là blockchain được kiểm soát bởi một tổ chức hoặc cá nhân, chỉ cho phép
các thực thể được cấp quyền truy cập.
Đặc điểm:
- Truy cập bị giới hạn (chỉ các node được phép)
- Thường dùng trong doanh nghiệp hoặc nội bộ tổ chức
- Có thể tùy chỉnh cao (hiệu năng, quyền riêng tư)
Ưu điểm:
- Hiệu suất cao
Nhược điểm:
- Thiếu tính phi tập trung
- Quyền kiểm soát chặt chẽ
- Phụ thuộc vào tổ chức trung tâm → rủi ro
- Dễ tuân thủ pháp lý
gian lận

---

## Slide 24: Blockchain liên kết (Consortium/Federated Blockchain)

Là mô hình kết hợp, nơi một nhóm tổ chức cùng quản lý mạng blockchain (thay vì công
khai hoặc hoàn toàn riêng tư).
Đặc điểm:
- Một số node được chỉ định điều hành (semi-decentralized)
- Thường dùng trong hệ thống liên doanh, liên ngân hàng
Ưu điểm:
Nhược điểm:
- Cân bằng giữa phi tập trung và hiệu quả
- Phức tạp trong quản trị
- Độ tin cậy cao trong các tổ chức tham gia
- Yêu cầu lòng tin giữa các bên

---

## Slide 25: So sánh ba mô hình Blockchain

Giống nhau
Có một sổ cái (mã hoá)
chỉ cho phép bổ sung
Có một mạng ngang hàng
(P2P)
Có một cơ chế
đồng thuận*
- Private chain có thể không cần consensus vẫn có thể hoạt động

---

## Slide 26: So sánh ba mô hình Blockchain

Private
Public
Sửa đổi (ghi đè) dữ liệu?
Không
Không
Ai có thể đọc dữ liệu trên
Blockchain?
Bất kỳ ai
Ai có thể ghi dữ liệu?
Bất kỳ ai
Đồng thuận
Có
Chỉ những người dùng
được mời
Những người tham gia
được chấp thuận
Có hoặc không
Consortium
Không
Tuỳ thuộc
Những người tham gia được chấp
thuận
Có
Quyền sở hữu?
Không ai
Một tổ chức duy nhất
Nhiều tổ chức
Người tham gia có bị tiết lộ
danh tính?
Tốc độ giao dịch
Tính phi tập trung
Bảo mật (chống giả mạo)
Không
Chậm
Cao
Cao
Có
Nhanh
Thấp
Trung bình
Có (tuỳ thuộc tổ chức)
Nhanh
Trung bình
Cao
Ứng dụng phổ biến
Tiền mã hóa, DApps
Quản trị nội bộ DN
Liên ngân hàng, chuỗi cung ứng

---

## Slide 27: Phù hợp với

doanh nghiệp
Blockchain mở
Blockchain đóng

---

## Slide 28: 29


---

## Slide 29: 30


---
