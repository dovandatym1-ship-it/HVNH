# Chuyên đề 04: Chuỗi khối (Blockchain), Hợp đồng Thông minh, DeFi & Web3
**Học phần:** Công nghệ Mới nổi và Đổi mới (CNM / MIS01)  
**Học viện Ngân hàng (Banking Academy of Vietnam - HVNH)**  
**Giảng viên:** TS. Đinh Trọng Hiếu & TS. Đỗ Văn Thuật

---

## 1. Bản chất Kỹ thuật của Công nghệ Chuỗi khối (Blockchain)

### 1.1. Giải quyết Bài toán Sổ cái Tập trung
* **Hệ thống tập trung truyền thống (Centralized Ledger):** Dữ liệu lưu tại máy chủ trung tâm của một đơn vị ủy thác (Ngân hàng, Cơ quan thuế). Rủi ro:
  - Điểm lỗi đơn lẻ (Single Point of Failure): Máy chủ sập thì toàn bộ dịch vụ tê liệt.
  - Nguy cơ bị tấn công mạng, xóa sửa dữ liệu trái phép từ nội bộ (Gian lận nội bộ).
  - Khủng hoảng niềm tin và chi phí trung gian cao.
* **Sổ cái phân tán (Distributed Ledger Technology - DLT):** Mỗi thành viên trong mạng lưới P2P đều giữ một bản sao sổ cái được đồng bộ liên tục; dữ liệu được bảo vệ bằng mật mã học, đạt được 3 thuộc tính cốt lõi: **Phi tập trung (Decentralized) – Minh bạch (Transparent) – Bất biến (Immutable)**.

### 1.2. Cấu trúc Kỹ thuật của một Khối (Block Structure)
Một khối dữ liệu trong Blockchain bao gồm 2 phần chính:
1. **Phần Đầu Khối (Block Header):**
   - **Previous Block Hash:** Mã băm của khối ngay trước đó (liên kết thành chuỗi móc xích).
   - **Merkle Root:** Mã băm đại diện tổng hợp của toàn bộ các giao dịch trong khối.
   - **Timestamp:** Thời gian khối được tạo lập.
   - **Difficulty Target:** Mục tiêu độ khó giải toán của mạng lưới.
   - **Nonce (Number used once):** Số ngẫu nhiên mà các thợ đào thay đổi liên tục để tìm ra mã băm khối thỏa mãn điều kiện độ khó.
2. **Thân Khối (Block Body):**
   - Danh sách chi tiết toàn bộ các giao dịch hợp lệ được đóng gói trong khối đó.

### 1.3. Mật mã học Nền tảng: Hàm băm SHA-256 & Cây Merkle
* **Hàm băm mật mã học (Cryptographic Hash Function - SHA-256):**
  - Chuyển đổi đầu vào bất kỳ thành một chuỗi ký tự cố định 256-bit (64 ký tự thập lục phân).
  - Tính một chiều (Pre-image resistance): Dễ dàng tính từ dữ liệu ra hash, nhưng bất khả thi về mặt tính toán để đảo ngược từ hash về dữ liệu gốc.
  - Hiệu ứng thác đổ (Avalanche Effect): Chỉ cần thay đổi 1 dấu chấm nhỏ ở đầu vào, mã hash đầu ra thay đổi hoàn toàn ngẫu nhiên.
  - Chống va chạm (Collision resistance): Không thể tìm được 2 đầu vào khác nhau sinh ra cùng một mã hash.
* **Cây Merkle (Merkle Tree):**
  - Cấu trúc dữ liệu cây nhị phân, trong đó mỗi nút lá là mã băm của một giao dịch cụ thể, và các nút cha là mã băm kết hợp của 2 nút con.
  - **Mã băm gốc (Merkle Root)** nằm tại đỉnh cây: Giúp xác thực một giao dịch bất kỳ có nằm trong khối hay không với độ phức tạp tính toán siêu nhanh $O(\log_2 n)$ mà không cần tải toàn bộ dữ liệu khối (áp dụng cho Light Node / SPV).

### 1.4. Mật mã Khóa Công khai & Chữ ký số
* Thuật toán đường cong elip **ECDSA (secp256k1)**:
  - **Private Key (Khóa bí mật):** Chuỗi 256-bit ngẫu nhiên, bí mật tuyệt đối, dùng để ký giao dịch (tương đương chữ ký cá nhân).
  - **Public Key (Khóa công khai):** Được suy ra từ Private Key bằng phép nhân điểm trên đường cong elip (toán học một chiều).
  - **Địa chỉ ví (Address):** Được tạo ra bằng cách băm Public Key qua SHA-256 và RIPEMD-160.
* **Chữ ký số (Digital Signature):** Người gửi dùng Private Key để ký giao dịch. Toàn bộ mạng lưới dùng Public Key của người gửi để xác minh chữ ký mà không hề biết Private Key của họ, đảm bảo tính toàn vẹn và chống chối bỏ.

---

## 2. Cơ chế Đồng thuận (Consensus Mechanisms) & Mạng P2P

Cơ chế đồng thuận là thuật toán đảm bảo tất cả các nút phân tán độc lập đạt được sự thống nhất về trạng thái dữ liệu sổ cái duy nhất mà không cần tin tưởng lẫn nhau (giải quyết bài toán Các vị tướng Byzantine - Byzantine Generals' Problem).

| Cơ chế | Nguyên lý hoạt động | Ưu điểm | Nhược điểm | Dự án tiêu biểu |
| :--- | :--- | :--- | :--- | :--- |
| **Proof of Work (PoW)** | Các máy đào cạnh tranh giải bài toán mật mã (tìm Nonce để hash khối < Target). Nút giải được đầu tiên được quyền tạo khối và nhận thưởng. | Bảo mật cực cao, phi tập trung triệt để, đã kiểm chứng thời gian dài. | Tiêu tốn điện năng khổng lồ, tốc độ xử lý giao dịch chậm (Bitcoin ~7 TPS). | Bitcoin (BTC), Litecoin, Kaspa |
| **Proof of Stake (PoS)** | Thay vì dùng phần cứng đào, các nút đặt cược (stake) đồng tiền mã hóa để trở thành Validator. Hệ thống chọn ngẫu nhiên dựa trên tỷ lệ stake để tạo khối. | Tiết kiệm 99.95% năng lượng, tốc độ nhanh hơn, mở rộng tốt hơn. | Nguy cơ tập trung hóa quyền lực (người giàu càng giàu), rủi ro "Nothing at Stake". | Ethereum (sau The Merge), Cardano, Polkadot |
| **Delegated PoS (DPoS)** | Người nắm giữ token biểu quyết bầu ra một số lượng đại biểu cố định (ví dụ 21 Validator) để thay mặt tạo khối. | Tốc độ xử lý cực cao (hàng nghìn TPS), thời gian xác nhận block chỉ 1-3s. | Tính phi tập trung kém hơn, dễ bị liên minh thông đồng thao túng. | TRON, EOS |
| **PBFT / Raft / PoA** | Bỏ phiếu xác thực theo vòng giữa các nút đã được cấp quyền định danh trước (Authorized Nodes). | Độ trễ giao dịch gần như tức thì, không tốn tài nguyên đào, kiểm soát bảo mật tốt. | Chỉ dùng cho mạng riêng tư hoặc liên minh, không mở tự do cho công chúng. | Hyperledger Fabric, R3 Corda, VeChain |
| **Proof of History (PoH)** | Tạo dòng thời gian mật mã học có thể kiểm chứng trước khi đạt đồng thuận, giúp các nút không cần chờ đợi trao đổi thời gian. | Tốc độ siêu việt (lên tới 50.000 - 65.000 TPS). | Hạ tầng máy chủ đòi hỏi phần cứng cực kỳ đắt tiền. | Solana (SOL) |

---

## 3. Lịch sử Tiến hóa: Từ Bitcoin đến Ethereum, Smart Contracts & Web3

```
+-------------------------------------------------------------------------+
|                  CÁC THẾ HỆ PHÁT TRIỂN CỦA BLOCKCHAIN                   |
+-------------------------------------------------------------------------+
| Blockchain 1.0 (2008)  | Tiền tệ số (Digital Currency)                 |
|                        | Tiêu biểu: Bitcoin - Sổ cái ghi nhận chuyển tiền|
+------------------------+------------------------------------------------+
| Blockchain 2.0 (2015)  | Hợp đồng thông minh & Ứng dụng phi tập trung  |
|                        | Tiêu biểu: Ethereum, EVM, DApps, ERC-20, NFT   |
+------------------------+------------------------------------------------+
| Blockchain 3.0 (Hiện nay)| Khả năng tương tác liên chuỗi, Web3, DeFi     |
|                        | Tiêu biểu: Layer-2 Rollups, Polkadot, Cosmos   |
+-------------------------------------------------------------------------+
```

### 3.1. Bitcoin (Blockchain 1.0)
* Phát minh năm 2008 bởi nhân vật ẩn danh **Satoshi Nakamoto** qua Whitepaper: *"Bitcoin: A Peer-to-Peer Electronic Cash System"*.
* Mục tiêu: Tiền tệ điện tử ngang hàng chống lại sự lạm phát và in tiền vô tội vạ của các ngân hàng trung ương sau khủng hoảng tài chính 2008.
* **Cơ chế giới hạn nguồn cung:** Tổng cung tối đa cố định **21.000.000 BTC**.
* **Bitcoin Halving:** Cứ sau mỗi 210.000 khối (khoảng 4 năm), phần thưởng tạo khối (Block Reward) bị giảm đi một nửa (từ 50 BTC -> 25 -> 12.5 -> 6.25 -> 3.125 BTC vào năm 2024).

### 3.2. Ethereum & Hợp đồng Thông minh (Smart Contract - Blockchain 2.0)
* Đề xuất năm 2013 bởi Vitalik Buterin.
* **Hợp đồng thông minh (Smart Contract):** Đoạn mã chương trình tự động thực thi khi thỏa mãn các điều kiện định sẵn mà không cần bất kỳ bên trung gian nào can thiệp:
  $$	ext{Nếu Điều kiện A xảy ra} \longrightarrow 	ext{Tự động thực hiện Hành động B}$$
* **EVM (Ethereum Virtual Machine):** Máy tính ảo toàn cầu thực thi mã byte của hợp đồng thông minh.
* **Ngôn ngữ lập trình:** **Solidity** (hướng đối tượng, cú pháp tương tự JavaScript/C++).
* **Cơ chế Gas:** Đơn vị đo lường năng lực tính toán cần thiết để thực thi giao dịch, ngăn chặn các vòng lặp vô tận (Infinite Loop / tấn công DoS). Người dùng phải trả phí: $	ext{Phí giao dịch} = 	ext{Gas Used} 	imes 	ext{Gas Price}$.

### 3.3. Các Chuẩn Token Tiêu biểu trên Ethereum
* **ERC-20 (Fungible Token):** Chuẩn cho các token có thể thay thế lẫn nhau hoàn toàn (ví dụ: USDT, DAI, UNI). Mỗi token có giá trị tương đương nhau, thích hợp làm tiền tệ, điểm thưởng loyalty, cổ phần biểu quyết quản trị (DAO).
* **ERC-721 (Non-Fungible Token - NFT):** Chuẩn cho các tài sản số độc bản không thể thay thế (Unique). Mỗi token có một `tokenId` duy nhất và liên kết với metadata riêng biệt. Dùng để chứng nhận quyền sở hữu tác phẩm nghệ thuật, bất động sản số, chứng chỉ học thuật, bằng cấp.

---

## 4. Tài chính Phi tập trung (DeFi) & Web3

### 4.1. Hệ sinh thái DeFi
DeFi tái thiết lập các nghiệp vụ ngân hàng truyền thống trên nền tảng Smart Contracts mà không cần ngân hàng trung gian:
1. **Sàn giao dịch phi tập trung (DEX) & AMM:** Thay vì dùng sổ lệnh mua/bán (Order-Book) khớp lệnh qua nhà tạo lập thị trường, DEX sử dụng **Nhà tạo lập thị trường tự động (Automated Market Maker - AMM)** dựa trên thuật toán tích số hằng số:
   $$x 	imes y = k$$
   Trong đó $x$ và $y$ là số lượng của 2 token trong bể thanh khoản (Liquidity Pool), $k$ là hằng số. Giá token tự động điều chỉnh theo cung - cầu khi có giao dịch hoán đổi (Swap).
2. **Cho vay & Đi vay phi tập trung (Lending/Borrowing):** Các giao thức như Aave, Compound cho phép người gửi nạp tiền mã hóa vào bể để nhận lãi suất, và người vay thế chấp vượt mức (Over-collateralized) để rút tiền mặt/stablecoin mà không cần xét duyệt tín dụng hay sao kê thu nhập.
3. **Tiền mã hóa ổn định giá (Stablecoins):**
   - Thế chấp bằng tiền định danh Fiat (Fiat-collateralized): USDT (Tether), USDC (Circle) theo tỷ lệ 1:1.
   - Thế chấp bằng tiền mã hóa phi tập trung (Crypto-collateralized): DAI (MakerDAO) thế chấp vượt mức bằng ETH/WBTC.

### 4.2. Web3 & Danh tính Tự chủ (Self-Sovereign Identity - SSI)
* **Web 1.0 (1990 - 2004):** "Read" - Trang web tĩnh, người dùng chỉ đọc thông tin một chiều.
* **Web 2.0 (2004 - nay):** "Read & Write" - Kỷ nguyên mạng xã hội tương tác hai chiều, nhưng toàn bộ dữ liệu người dùng bị thâu tóm và độc quyền bởi các tập đoàn công nghệ lớn (Google, Meta).
* **Web 3.0:** "Read, Write & Own" - Người dùng sở hữu dữ liệu, danh tính và tài sản số của chính mình thông qua khóa mật mã và công nghệ Blockchain.
* **W3C Decentralized Identifiers (DID) & Verifiable Credentials (VC):** Cho phép người dùng lưu trữ danh tính và các chứng chỉ số (bằng cấp, sao kê tín dụng, chứng nhận eKYC) trong ví điện tử cá nhân và xuất trình cho các bên kiểm chứng mà không làm lộ thông tin nhạy cảm.

---

## 5. Ứng dụng Thực tế trong Ngành Tài chính - Ngân hàng

1. **Tài trợ Thương mại & Thư tín dụng điện tử (e-L/C):** Nền tảng Contour (sử dụng R3 Corda) kết nối các ngân hàng toàn cầu (BNP Paribas, HSBC, Standard Chartered) và tại Việt Nam (VietinBank, BIDV), rút ngắn thời gian phát hành và thanh toán L/C từ 5-10 ngày xuống còn **dưới 24 giờ**, loại bỏ hoàn toàn chi phí chuyển phát chứng từ giấy.
2. **Thanh toán & Chuyển kiều hối Xuyên biên giới:** Mạng lưới RippleNet giải quyết chuyển tiền quốc tế tức thì với chi phí rẻ hơn 60% so với mạng SWIFT truyền thống.
3. **Token hóa Tài sản Thực (Real World Asset - RWA Tokenization):** Chuyển đổi các tài sản tài chính truyền thống (Trái phiếu chính phủ, Tín phiếu kho bạc Mỹ, Cổ phiếu, Bất động sản thương mại) thành các token số trên Blockchain, cho phép chia nhỏ sở hữu (Fractional Ownership), tăng thanh khoản và giao dịch 24/7.
4. **Tiền Kỹ thuật số Ngân hàng Trung ương (CBDC):** Được bảo chứng trực tiếp bởi Ngân hàng Trung ương (ví dụ: e-CNY của Trung Quốc, dự án mBridge của BIS), giúp hiện đại hóa hạ tầng thanh toán bán buôn và bán lẻ quốc gia.
