# Chương 5: Cơ bản về Blockchain - Sổ cái phân tán & Mật mã học
**Học phần:** Công nghệ mới nổi và Đổi mới (CNM / MIS01)
**Học viện Ngân hàng (Banking Academy of Vietnam - HVNH)**
**Nguồn bài giảng gốc:** `5_Blockchain_01.pdf`

---

## Slide 1: Chương 01

CƠ BẢN VỀ BLOCKCHAIN
Tháng 10/2022

---

## Slide 2: Mất mát

Gian lận
Trang 1:
10/02/2025: An chuyển cho Bình 100 triệu
10/02/2025: An chuyển cho Châu 10 triệu
11/02/2025: An nhận từ Bình 20 triệu
Trang 2:
- 15/02/2025: Châu rút 50 triệu
- 16/02/2025: Bình nộp 1 triệu
Hacker tấn
công, thay đổi
dữ liệu
Thiên tai,
lũ lụt

---

## Slide 3: Chống mất mát

- Chống thay đổi

---

## Slide 4: NỘI DUNG

Khái niệm Blockchain  và các thành  phần  kiến trúc
Blockchain
Cơ sở mật mã và an toàn Blockchain  (hash,  hash
pointer,  merkle tree, digital signature)
Tính chất tự động vận hành (Quản trị phi tập trung)
của Blockchain  và các đặc trưng nổi bật khác
Lịch sử hình thành mạng  Blockchain Bitcoin
Tiền Bitcoin sinh ra từ đâu? Cơ chế đào Bitcoin

---

## Slide 5: 01

Khái niệm Blockchain và các thành
phần kiến trúc

---

## Slide 6: KHÁI NIỆM BLOCKCHAIN

Tại sao phải quan tâm Blockchain?
1. Được coi là một “Công nghệ đột phá”
- Bởi những gã khổng lồ công nghệ (vd: IBM,  Microsoft,  Intel, Paypal, Visa)
- Bởi các ông lớn ngân hàng đầu tư (vd: J.P.Morgan, Credict Suisse,  Bank of America)
- Bởi các chính trị gia và các nhà lãnh đạo đất nước (Elsavador,  Dominica, etc)
- Bởi cộng đồng nhiên cứu hàn lâm
2. Các loại tiền điện tử trị giá hàng nghìn tỷ đô la
3. Tiềm năng ứng dụng to lớn và đột phá trong nhiều lĩnh vực khác nhau

---

## Slide 7: KHÁI NIỆM BLOCKCHAIN

“Blockchain  là  một  cơ  sở  dữ  liệu  phân  tán,  lưu  trữ  thông  tin  trong  các  khối
được liên kết với nhau  bằng  mã hóa  và mở rộng theo thời gian.”
- - Wikipedia

---

## Slide 8: KIẾN TRÚC CƠ BẢN CỦA BLOCKCHAIN

Lớp ứng dụng và giao diện người dùng
Smart Contracts – Chaincode  – DApps  – Giao diện người dùng
Lớp đồng thuận
PoW  -  PoS  -  DPoS  -  PoET  -  PBFT
Lớp mạng
Peer – to – peer (P2P)
Lớp dữ liệu
Cấu trúc dữ liệu
Chữ ký số – Hash – Merkel Tree – Giao dịch
Lớp phần  cứng/Hạ tầng
Máy ảo – Containers – Dịch vụ - Gói tin

---

## Slide 9: KHÁI NIỆM BLOCKCHAIN


---

## Slide 10: KHÁI NIỆM BLOCKCHAIN

Cách Blockchain  hoạt động

---

## Slide 11: 02

Cơ sở mật mã và an toàn
Blockchain

---

## Slide 12: HASH – Hàm băm

Về cơ bản hashing là quá trình
biến một dữ liệu đầu vào có độ
dài bất kỳ thành một chuỗi đầu
ra đặc trưng có độ dài cố định.
Vd:
Đầu ra (256 bit)

---

## Slide 13: HASH POINTER – Con trỏ hash

Hash Pointer – Con trỏ hash: là con trỏ thông thường nhưng có kèm theo giá trị hash của nội
dung được trỏ tới
Con trỏ hash được dùng để xây dựng các cấu trúc dữ liệu tương tự với con trỏ thông thường,
vd như linked list hoặc cây nhị phân (binary search  tree).  Với giá trị hash của dữ liệu được trỏ
tới, con trỏ hash giúp ta kiểm tra rằng nội dung của thông tin không bị thay đổi.

---

## Slide 14: HASH POINTER – Con trỏ hash

Cấu trúc dữ liệu dựa trên hash pointer
Các khối có thể được liên kết với nhau bằng cách sử dụng con trỏ băm => một sổ cái chống giả mạo

---

## Slide 15: MERKLE TREE

Merkle   Tree  là   một   cấu   trúc  dữ  liệu
được  sử  dụng  trong  các  ứng  dụng  khoa
học  máy  tính.  Đó  là  một  cấu  trúc  dữ  liệu
toán  học  được  tạo  thành    từ    các  hàm
băm  của  nhiều  block  dữ  liệu  khác  nhau
tóm  tắt  tất  cả  các  giao  dịch  trong  một
block.  Nó  cũng  cho  phép  xác  minh  nội
dung nhanh chóng,  an  toàn  và  nhất  quán
trên các bộ dữ liệu lớn.

---

## Slide 16: MERKLE TREE

Merkle   Tree  là   một   cấu   trúc  dữ  liệu
được  sử  dụng  trong  các  ứng  dụng  khoa
học  máy  tính.  Đó  là  một  cấu  trúc  dữ  liệu
toán  học  được  tạo  thành    từ    các  hàm
băm  của  nhiều  block  dữ  liệu  khác  nhau
tóm  tắt  tất  cả  các  giao  dịch  trong  một
block.  Nó  cũng  cho  phép  xác  minh  nội
dung nhanh chóng,  an  toàn  và  nhất  quán
trên các bộ dữ liệu lớn.

---

## Slide 17: DIGITAL SIGNATURE – Chữ ký số

Chữ ký số là một cơ chế mã hóa được sử dụng để xác minh tính xác thực và
tính toàn vẹn của dữ liệu kỹ thuật số

---

## Slide 18: 03

Các đặc trưng nổi bật của
Blockchain

---

## Slide 19: CÁC ĐẶC TRƯNG CỦA BLOCKCHAIN

Phi tập trung
Nâng cao bảo mật
Giảm vai trò bên thứ 3
Thanh toán nhanh
Phân tán dữ liệu
Không thể thu hồi và
có thể kiểm tra được
Sổ cái kỹ thuật số
Không thể thay đổi và
không thể từ chối
Không cần tin tưởng
Minh bạch và
Chứng minh được

---

## Slide 20: KHẢ NĂNG TỰ ĐỘNG VẬN HÀNH – QUẢN TRỊ PHI TẬP TRUNG

Tổ chức truyền thống
Tổ chức tự trị phi tập trung – DAO*
- DAO - Decentralized Autonomous Organization

---

## Slide 21: DAO – MÔ HÌNH TỔ CHỨC TỰ TRỊ PHI TẬP TRUNG

DAO là tổ chức tự trị phi tập trung. Khác với các tổ chức truyền thống (như Facebook, Google,...),
DAO ứng dụng các bộ quy tắc được mã hóa bằng code, chúng có thể hoạt động một cách độc lập
mà không cần sự can thiệp của con người. Mọi quy tắc hoạt động của DAO đều tiến hành dựa vào
cơ chế bỏ phiếu từ cộng đồng. Đề xuất nào có nhiều phiếu tán thành nhất sẽ được thực hiện.
DAO Code:
- Theo dõi quyền sở hữu token DAO
- Xác định quản trị
- Quản lý việc bỏ phiếu
Contractor code:
- Xác định mô hình kinh doanh (nếu có)
- Xác định các thông số hoạt động
- Xác định chính sách thanh toán

---

## Slide 22: DAO – ƯU VÀ NHƯỢC ĐIỂM

ƯU ĐIỂM
Cơ cấu
tự trị
Công
bằng
Trung
lập
Trách
nhiệm giải
trình
NHƯỢC  ĐIỂM
Tập trung
quyền
biểu quyết
Thường bị
trì hoãn
Quyết
định sai
lầm
Lổ hổng
của code

---

## Slide 23: DAO – HƯỚNG PHÁT TRIỂN

Cấu trúc
Vận hành
Cấu trúc đóng
Tham gia cứng nhắc
Hệ thống phân cấp tĩnh
Nhanh chóng do tập trung hóa
Chuyên môn hóa
Có thể mở rộng
Cấu trúc mở
Tham gia linh hoạt
Không có phân cấp
Chậm do rối loạn
Không có chuyên môn hoá
Khó mở rộng
Mở với cơ chế lọc tốt
Tham gia linh hoạt
Hệ thống phân cấp rõ ràng
Nhanh chóng do khả năng thích ứng
Chuyên môn hóa
Có thể mở rộng

---

## Slide 24: 04

Lịch sử hình thành mạng
Blockchain Bitcoin

---

## Slide 25: LỊCH SỬ HÌNH THÀNH BLOCKCHAIN

1. Giai đoạn khởi nguồn: Ý tưởng và công nghệ nền (1991–2008)
- 1991 – 1992:
Stuart Haber và W. Scott Stornetta đề xuất một hệ thống "timestamping" tài liệu số
không thể thay đổi.
→ Đây là ý tưởng đầu tiên về một chuỗi dữ liệu có tính bất biến, chống sửa đổi.
- 1998:
Nick Szabo mô tả khái niệm "Bit Gold" – một hệ thống tiền kỹ thuật số phi tập trung,
hoạt động gần giống với Blockchain, nhưng không thành công về mặt triển khai.
- 2004:
Hal Finney phát triển "Reusable Proof of Work" – cho phép người dùng tái sử dụng kết
quả xử lý để xác thực dữ liệu. Đây là tiền đề cho cơ chế Proof of Work (PoW).

---

## Slide 26: LỊCH SỬ HÌNH THÀNH BLOCKCHAIN

2. Giai đoạn đột phá: Bitcoin và Blockchain thế hệ 1.0 (2008–2013)
- 2008:
Satoshi Nakamoto (một cá nhân hoặc nhóm người ẩn danh) phát hành whitepaper:
"Bitcoin: A Peer-to-Peer Electronic Cash System", mô tả một hệ thống tiền mã hóa
dựa trên mạng ngang hàng (P2P) và sổ cái phân tán.
- 2009:
Khối đầu tiên (Genesis Block) của Bitcoin được tạo ra.
→ Lần đầu tiên, Blockchain được triển khai thành công trong thực tế.
- 2010:
Giao dịch đầu tiên bằng Bitcoin trong đời thực: 10.000 BTC mua 2 chiếc pizza – được
gọi là “Bitcoin Pizza Day”.
- 2011–2013:
Các loại tiền mã hóa khác (Altcoins) như Litecoin, Namecoin, Ripple (XRP) xuất hiện,
mở rộng ý tưởng Blockchain ngoài Bitcoin.

---

## Slide 27: LỊCH SỬ HÌNH THÀNH BLOCKCHAIN

3. Giai đoạn mở rộng: Blockchain 2.0 và Smart Contract (2014–2017)
- 2014:
Vitalik Buterin công bố dự án Ethereum – nền tảng cho phép tạo ra các hợp đồng
thông minh (Smart Contract): chương trình tự thực thi theo điều kiện định sẵn trên
Blockchain.
- 2015:
Ethereum mainnet chính thức ra mắt. Đây là bước ngoặt vì:
- Blockchain không chỉ lưu trữ giao dịch, mà còn là nền tảng ứng dụng
phi tập trung (DApp).
- Lập trình viên có thể tạo token, ứng dụng tài chính, game, v.v.
- 2016:
Sự kiện DAO Hack – tổ chức tự trị phi tập trung đầu tiên trên Ethereum bị tấn công,
gây mất 50 triệu USD.
→ Ethereum chia tách thành Ethereum (ETH) và Ethereum Classic (ETC).

---

## Slide 28: LỊCH SỬ HÌNH THÀNH BLOCKCHAIN

4. Giai đoạn phát triển đa ngành: Blockchain 3.0 (2018–2020)
- Blockchain mở rộng ra ngoài lĩnh vực tài chính:
- Supply Chain: IBM Food Trust, VeChain
- Y tế: lưu trữ hồ sơ bệnh án an toàn
- Bầu cử điện tử: thử nghiệm ở Estonia, West Virginia (Mỹ)
- Năng lượng tái tạo, bảo hiểm, bản quyền âm nhạc...
- Nhiều tổ chức lớn tham gia:
IBM, Microsoft (Azure Blockchain)
- 
- Facebook (Libra → Diem, nhưng bị dừng)
- JP Morgan, Santander sử dụng blockchain nội bộ

---

## Slide 29: LỊCH SỬ HÌNH THÀNH BLOCKCHAIN

5. Giai đoạn bùng nổ Web3 – DeFi – NFT – DAO (2020–2022)
- DeFi (Tài chính phi tập trung):
Cho phép người dùng vay, cho vay, trao đổi tài sản mà không qua trung gian ngân
hàng.
- NFT (Non-Fungible Token):
Bùng nổ trong nghệ thuật số, trò chơi (Axie Infinity, OpenSea), định danh tài sản kỹ
thuật số duy nhất.
- DAO (Decentralized Autonomous Organization):
Mô hình tổ chức vận hành qua hợp đồng thông minh, ra quyết định dựa trên biểu
quyết.

---

## Slide 30: LỊCH SỬ HÌNH THÀNH BLOCKCHAIN

6. Giai đoạn hiện tại & tương lai gần (2023 trở đi)
- Tập trung vào khả năng mở rộng, tiết kiệm năng lượng, tương tác chuỗi chéo:
- Ethereum chuyển sang Proof of Stake (The Merge – 2022)
- Blockchain thế hệ mới như Polkadot, Cosmos, Solana, Avalanche
- Ứng dụng trong quản trị công, AI, chứng nhận số, định danh (Self-
sovereign Identity)
- Web3 tiếp tục là xu hướng: mạng internet phi tập trung với dữ liệu thuộc quyền sở
hữu người dùng.
- Các quốc gia & doanh nghiệp lớn đang số hóa tài sản và ứng dụng Blockchain vào
chuỗi cung ứng, pháp lý, tài chính số hóa.

---

## Slide 31: LỊCH SỬ HÌNH THÀNH MẠNG BLOCKCHAIN BITCOIN

David Chaum
Giao thức giống
với Blockchain
Haber, Stornetta,
Dave Bayer
Merkle trees
Satoshi Nakamoto
Bitcoin (4/1)
Whitepaper (31/10)
1982
1991
1992
1992
2008
2009
Chuỗi của các
khối
Stuart Haber và
W. Scott Stornetta
ECDSA
Scott Vanstone
Bitcoin mainnet
Khối đầu tiên

---

## Slide 32: 05

Tiền Bitcoin sinh ra từ đâu?
Cơ chế đào Bitcoin

---

## Slide 33: TIỀN BITCOIN SINH RA TỪ ĐÂU

SỰ ĐỔI MỚI CỦA SATOSHI NAKAMOTO
- Bitcoin cố gắng giải quyết hai vấn đề mà các mạng phi tập trung thường gặp phải:
- Các bản ghi giao dịch không nhất quán do các nút khác nhau nắm giữ
- Những kẻ giả danh có thể phát đi những thông điệp sai và chia rẽ mạng lưới

---

## Slide 34: CƠ CHẾ ĐÀO BITCOIN


---

## Slide 35: CƠ CHẾ ĐÀO BITCOIN


---

## Slide 36: ĐÓNG GÓP CỦA SATOSHI NAKAMOTO VỚI THẾ GIỚI

- Tổng hợp các kĩ thuật mã hoá vào phần mềm Bitcoin Core => Blockchain /sổ
cái chống tấn công và kiểm duyệt đầu tiên của thế giới
- Giới thiệu cơ chế đồng thuận PoW (Nakamoto Consensus)
- Hiện thực hoá tiền kĩ thuật số (Không do Ngân hàng trung ương phát hành)
=> DIGITAL GOLD, CRYPTOCURRENCIES
- Khai sinh triết lý phi tập trung và nền tảng công nghệ Blockchain
- Bitcoin & Cryptocurrency: a 21st Century Miracle -

---

## Slide 37: Phần B

BÀI THỰC HÀNH
1. Xem và đọc giao dịch Bitcoin trên explorer
2. Cài đặt ví Metamask, sử dụng ETH trên testnet

---

## Slide 38: 01

Xem và đọc giao dịch Bitcoin
trên explorer

---

## Slide 39: 1. XEM VÀ ĐỌC GIAO DỊCH BITCOIN TRÊN EXPLORER

https://www.blockchain.com/explorer

---

## Slide 40: 02

Cài đặt ví Metamask,
sử dụng ETH trên testnet

---

## Slide 41: 2. CÀI ĐẶT METAMASK, DÙNG ETH TRÊN TESTNET GOERLI

Thực hành trên trình duyệt
(Ứng dụng mobile sẽ có đôi chỗ khác biệt)
B1. Cài đặt Metamask
B2. Tạo mới / nhập ví cũ (nếu có)
B3. Thêm testnet Goerli vào ví Metamask
B4. Thêm foucet
B5. Gửi ETH
Metamask

---

## Slide 42: 2. CÀI ĐẶT METAMASK, DÙNG ETH TRÊN TESTNET GOERLI

Bước 1
Cài metamask
https://metamask.io/
download/
(Hoặc: Chrome web
store)

---

## Slide 43: 2. CÀI ĐẶT METAMASK, DÙNG ETH TRÊN TESTNET GOERLI

Bước 2
Tạo mới / nhập ví cũ
Chọn Import wallet nếu đã có ví Metamask trước đó
Chọn Create a wallet nếu muốn tạo ví mới
=> Nhập mật khẩu Metamask trên trình duyệt
Lưu lại 12 cụm từ ở nơi
an toàn
Nhập lại 12 cụm từ theo đúng thứ
tự để xác nhận

---

## Slide 44: 2. CÀI ĐẶT METAMASK, DÙNG ETH TRÊN TESTNET GOERLI

Bước 3
Thêm testnet
Chọn mũi tên xổ xuống
Chọn Show/Hide  test network
Chọn On cho mục “Show test
networks”
Chọn nút “X” quay lại home
Chọn mũi tên xổ xuống
Chọn Goerli test network

---

## Slide 45: 2. CÀI ĐẶT METAMASK, DÙNG ETH TRÊN TESTNET GOERLI

Bước 4
Thêm faucet
https://goerlifaucet.com/
Tạo mới tài khoản alchemy để
nhận faucet ETH
Copy địa chỉ ví Metamask
Dán địa chỉ vào ô trống
Chọn “Send Me ETH”

---

## Slide 46: 2. CÀI ĐẶT METAMASK, DÙNG ETH TRÊN TESTNET GOERLI

Bước 5
Gửi ETH
Chọn “Send” để gửi token
Nhập vào địa chỉ ví nhận
Kiểm tra mạng, địa chỉ
Nhập số lượng token gửi
Chọn “Next”
Kiểm tra gas fee (Tăng lên
nếu cần chuyển nhanh)
Xác nhận “Confirm”

---

## Slide 47: 2. CÀI ĐẶT METAMASK, DÙNG ETH TRÊN TESTNET GOERLI

Chọn tab “Activity” để xem
các hành động của ví
Sau khi chuyển thành công,
click vào giao dịch sẽ có thông
tin giao dịch, chọn “View on
blockchain explorer”
Thông tin giao dịch trên
explorer Etherscan
Hoàn tất

---

## Slide 48: CÁC NGUỒN THAM KHẢO

- https://vi.wikipedia.org/wiki/Blockchain
- https://mlsdev.com/blog/156-how-to-build-your-own-blockchain-architecture
- https://subscription.packtpub.com/book/data/9781789804164/1/ch01lvl1sec07/layered-
structure-of-the-blockchain-architecture
- https://codelearn.io/sharing/hash-la-gi-va-hash-dung-de-lam-gi
- http://emanvietnam.vn/cong-nghe/blockchain-02-con-tro-hash-blockchain.html
- https://coin98.net/daos
- https://101blockchains.com/pros-and-cons-of-dao/
- https://vnrebates.net/dao-la-gi-tai-sao-dao-la-tuong-lai-cua-thi-truong-crypto.html
- https://www.researchgate.net/figure/The-key-features-of-Blockchain-
technology_fig1_357644158
- Slide template: https://slidesgo.com/

---
