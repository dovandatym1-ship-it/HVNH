# Chương 7: Blockchain Phần B1 - Bitcoin, Ethereum & Smart Contracts
**Học phần:** Công nghệ mới nổi và Đổi mới (CNM / MIS01)
**Học viện Ngân hàng (Banking Academy of Vietnam - HVNH)**
**Nguồn bài giảng gốc:** `7_Blockchain_03.pdf`

---

## Slide 1: Phần B: Bitcoin, Hợp đồng thông

minh, Tài chính phi tập trung, Web3
Buổi 6: Bitcoin, Hợp đồng thông minh & Ứng dụng phi tập trung
4.11 Tiền bitcoin sinh ra từ đâu, cơ chế đào bitcoin
4.12 Thực hành
4.13 Blockchain thế hệ 2 – Ethereum
4.14 Smart Contract và DApp
4.15 Chuẩn ERC-20 và các đồng tiền kỹ thuật số dạng token
4.16 Chuẩn ERC-721 và tài sản số NFT (Non-Fungible token)
- Xem và đọc giao dịch bitcoin
- Cài đặt ví Metamask, sử dụng ETH trên testnet
4.18 Thực hành
- Phát hành ERC20 token,
- Phát hành ERC721-NFT
Giảng viên: Đỗ Văn Thuật, PhD

---

## Slide 2: Tiền bitcoin sinh ra từ đâu?

https://www.blockchain.com/explorer/blocks/btc/0 hoặc https://bitaps.com/0
- Bitcoin is against infinitely money-print by central banks and inflation
- Bitcoin is decentralized P2P network for store of value and money transfer

---

## Slide 3: Tiền bitcoin sinh ra từ đâu?

https://www.blockchain.com/explorer/blocks/btc/0 hoặc https://bitaps.com/0
- Coinbase = Block reward: new generated Bitcoin
- Bitcoin halving: reward per block 50 / 25 / 12.5 / 6.25 / 3.125
- Bitcoin limit: total max supply 21,000,000 BTC
- Current supply: 19M BTC

---

## Slide 4: Cơ chế đào bitcoin?

- Block reward
- Fee reward
- Mining
https://www.blockchain.com/explorer/charts/hash-rate

---

## Slide 5: Cơ chế đào bitcoin?

https://www.blockchain.com/explorer/charts/hash-rate
Block hash = HASH (timestamp, prev.blockhash, txhash, nonce)
- SHA-256
- Nonce
- Mining
- Target difficulty
Target 3 zeros: 000
- Valid: 000… , 0000…
- Invalid: 00…
Block hash = ID

---

## Slide 6: Đọc giao dịch Bitcoin


---

## Slide 7: Ethereum: blockchain thế hệ 2

- From Bitcoin scripts to a Turing-complete & programmable blockchain
- Smartcontract, decentralized finance/identity/application
- Smartcontract platform
- World computer
✓ Vitalik Buterin (1994)
✓ Gavin Wood (1980)
✓ Ethereum Virtual Machine (EVM)
✓ PoW to PoS
https://ethereum.org/vi/whitepaper/
https://ethereum.github.io/yellowpaper/paper.pdf

---

## Slide 8: Smartcontract & dapps

- A contract = rules to be executed
- EVM-contract
- Solidity language
- A decentralized application
(dapp) = multi-contracts
deployed on EVM
dapps
contracts
EVM runtime
Ethereum Network

---

## Slide 9: ERC-standards

ERC = Ethereum Request for Comment
ERC-20: fungible tokens for accounting
ERC-721: non-fungible token (NFT)
Examples:
- ERC-20: USDT, USDC ($126B)
- ERC-721: NFT artworks

---

## Slide 10: Cài đặt ví Metamask và giao dịch ETH testnet

- Install Metamask extension
- Search Sepolia testnet
- Add Sepolia testnet to Metamask

---

## Slide 11: Phát hành token (tiền) mã hóa

Thực hành
- Lập trình smartcontract
- Triển khai contract ERC20 phát hành token
- Triển khai contract ERC721 phát hành NFT

---
