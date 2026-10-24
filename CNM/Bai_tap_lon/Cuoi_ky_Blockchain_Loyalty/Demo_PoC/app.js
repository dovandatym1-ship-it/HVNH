/**
 * Techcombank Loyalty Ecosystem - Frontend Logic
 * Học phần Công nghệ Mới nổi và Đổi mới (CNM) - HVNH
 */

// STATE
let state = {
    totalSupply: 10000000,
    rewardedPoints: 45500,
    burnedPoints: 12400,
    customerBalance: 1250,
    customerAddress: "0x71C936d5A6C28935c18684E07b8979e2764992A1",
    blockHeight: 684210,
    isMetaMaskConnected: false,
    ledger: [
        {
            time: "15:02:14 20/10/2026",
            block: 684205,
            txHash: "0x3f4a8b...7d12",
            action: "MINT_SUPPLY",
            wallet: "0xBank...Admin",
            points: "+10,000,000",
            status: "INITIALIZED"
        },
        {
            time: "15:05:40 20/10/2026",
            block: 684208,
            txHash: "0x91c2e4...e881",
            action: "REWARD_POS",
            wallet: "0x71C...92A1",
            points: "+200",
            status: "AUTO_SETTLED"
        },
        {
            time: "15:08:22 20/10/2026",
            block: 684209,
            txHash: "0xbb41a0...442f",
            action: "REDEEM_BURN",
            wallet: "0x71C...92A1",
            points: "-200",
            status: "VOUCHER_ISSUED"
        }
    ]
};

// INITIALIZATION
document.addEventListener("DOMContentLoaded", () => {
    updateUI();
    renderLedger();
    setupMetaMaskListener();
});

// TAB SWITCHER
function switchTab(tabId) {
    document.querySelectorAll(".tab-btn").forEach(btn => btn.classList.remove("active"));
    document.querySelectorAll(".tab-content").forEach(content => content.classList.remove("active"));
    
    event.currentTarget.classList.add("active");
    const targetContent = document.getElementById(tabId);
    if (targetContent) targetContent.classList.add("active");
}

// UPDATE UI
function updateUI() {
    document.getElementById("kpiTotalSupply").innerText = state.totalSupply.toLocaleString();
    document.getElementById("kpiRewarded").innerText = state.rewardedPoints.toLocaleString();
    document.getElementById("kpiBurned").innerText = state.burnedPoints.toLocaleString();
    document.getElementById("customerBalance").innerText = state.customerBalance.toLocaleString();
    document.getElementById("customerAddressDisplay").innerText = formatAddress(state.customerAddress);
}

// FORMAT ADDRESS
function formatAddress(addr) {
    if (!addr || addr.length < 10) return addr;
    return addr.slice(0, 6) + "..." + addr.slice(-4);
}

// CALCULATE POINTS FOR REWARD
function calculatePoints() {
    const spend = parseFloat(document.getElementById("cardSpend").value) || 0;
    // Tỷ lệ: Cứ 10.000 VNĐ chi tiêu thẻ = 1 TCB-PTS
    const points = Math.floor(spend / 10000);
    document.getElementById("rewardPointsInput").value = points;
}

// GENERATE DUMMY TX HASH
function generateTxHash() {
    const chars = "0123456789abcdef";
    let hash = "0x";
    for (let i = 0; i < 40; i++) {
        hash += chars[Math.floor(Math.random() * chars.length)];
    }
    return hash;
}

// HANDLE REWARD SUBMIT
function handleRewardSubmit(e) {
    e.preventDefault();
    const points = parseInt(document.getElementById("rewardPointsInput").value) || 0;
    const ref = document.getElementById("txRef").value;
    const addr = document.getElementById("rewardAddress").value;

    if (points <= 0) {
        alert("Số điểm thưởng phải lớn hơn 0");
        return;
    }

    // Tăng state
    state.rewardedPoints += points;
    state.customerBalance += points;
    state.blockHeight += 1;

    const newTx = {
        time: new Date().toLocaleTimeString() + " " + new Date().toLocaleDateString(),
        block: state.blockHeight,
        txHash: generateTxHash(),
        action: "REWARD_POS (" + ref + ")",
        wallet: formatAddress(addr),
        points: "+" + points.toLocaleString(),
        status: "AUTO_SETTLED"
    };

    state.ledger.unshift(newTx);
    updateUI();
    renderLedger();

    alert(`✅ Thành công! Đã chuyển ${points} TCB-PTS vào ví ${formatAddress(addr)} qua Smart Contract rewardPoints().\nTxHash: ${newTx.txHash}`);
}

// HANDLE BATCH REWARD
function handleBatchReward() {
    const batchPoints = 1270;
    state.rewardedPoints += batchPoints;
    state.customerBalance += 350; // Giả sử 1 người trong batch
    state.blockHeight += 1;

    const newTx = {
        time: new Date().toLocaleTimeString() + " " + new Date().toLocaleDateString(),
        block: state.blockHeight,
        txHash: generateTxHash(),
        action: "BATCH_REWARD (3 Chủ thẻ)",
        wallet: "Multiple (0x8a9, 0x42c, 0x91d)",
        points: "+" + batchPoints.toLocaleString(),
        status: "AUTO_SETTLED"
    };

    state.ledger.unshift(newTx);
    updateUI();
    renderLedger();

    alert(`⚡ Batch Settlement hoàn tất! Đã giải ngân ${batchPoints} TCB-PTS cho 3 chủ thẻ trong duy nhất 1 Block.\nTiết kiệm 68% phí Gas so với gọi đơn lẻ.`);
}

// REDEEM VOUCHER ACTION
function redeemVoucherAction(partner, cost, codePrefix) {
    if (state.customerBalance < cost) {
        alert(`❌ Số dư không đủ! Bạn cần ${cost} TCB-PTS nhưng hiện chỉ có ${state.customerBalance} TCB-PTS.`);
        return;
    }

    // Đốt điểm
    state.customerBalance -= cost;
    state.burnedPoints += cost;
    state.blockHeight += 1;

    const voucherCode = codePrefix + "-" + Math.floor(1000 + Math.random() * 9000);
    const txHash = generateTxHash();

    const newTx = {
        time: new Date().toLocaleTimeString() + " " + new Date().toLocaleDateString(),
        block: state.blockHeight,
        txHash: txHash,
        action: `REDEEM_BURN (${partner})`,
        wallet: formatAddress(state.customerAddress),
        points: "-" + cost.toLocaleString(),
        status: "ZERO_REC_CONFIRMED"
    };

    state.ledger.unshift(newTx);
    updateUI();
    renderLedger();

    // Hiển thị hộp thông báo
    const box = document.getElementById("voucherSuccessBox");
    const details = document.getElementById("voucherSuccessDetails");
    details.innerHTML = `
        <strong>Đối tác:</strong> ${partner} | <strong>Chi phí:</strong> -${cost} TCB-PTS (Đã Burn)<br>
        <strong>Mã Voucher E-Voucher:</strong> <span style="font-size:1.2rem; font-weight:800; color:#C00000;">${voucherCode}</span><br>
        <strong>Mã xác thực Smart Contract (TxHash):</strong> <code>${txHash}</code><br>
        <em>Hệ thống đã tự động bù trừ đối soát với ${partner} theo thời gian thực trên sổ cái Blockchain.</em>
    `;
    box.style.display = "block";
    box.scrollIntoView({ behavior: 'smooth' });
}

// RENDER LEDGER TABLE
function renderLedger() {
    const tbody = document.getElementById("ledgerBody");
    tbody.innerHTML = "";

    state.ledger.forEach(item => {
        const tr = document.createElement("tr");
        tr.innerHTML = `
            <td>${item.time}</td>
            <td><strong>#${item.block}</strong></td>
            <td><code>${formatAddress(item.txHash)}</code></td>
            <td><span class="badge ${item.action.includes('REWARD') || item.action.includes('MINT') ? 'badge-success' : 'badge-light'}">${item.action}</span></td>
            <td>${item.wallet}</td>
            <td style="font-weight:700; color:${item.points.startsWith('+') ? '#059669' : '#C00000'};">${item.points}</td>
            <td><span class="badge badge-success">${item.status}</span></td>
        `;
        tbody.appendChild(tr);
    });
}

// EXPORT CSV
function exportLedgerCSV() {
    let csv = "ThoiGian,Block,TxHash,HanhDong,Vi,Diem,TrangThai\n";
    state.ledger.forEach(r => {
        csv += `"${r.time}",${r.block},"${r.txHash}","${r.action}","${r.wallet}","${r.points}","${r.status}"\n`;
    });

    const blob = new Blob(["\uFEFF" + csv], { type: "text/csv;charset=utf-8;" });
    const link = document.createElement("a");
    link.href = URL.createObjectURL(blob);
    link.download = `Techcombank_Loyalty_Ledger_${new Date().toISOString().slice(0,10)}.csv`;
    link.click();
}

// METAMASK INTEGRATION (IF INSTALLED)
async function setupMetaMaskListener() {
    const btn = document.getElementById("btnConnectWallet");
    btn.addEventListener("click", async () => {
        if (typeof window.ethereum !== "undefined") {
            try {
                const accounts = await window.ethereum.request({ method: "eth_requestAccounts" });
                if (accounts.length > 0) {
                    state.customerAddress = accounts[0];
                    state.isMetaMaskConnected = true;
                    document.getElementById("walletBtnText").innerText = "🦊 " + formatAddress(accounts[0]);
                    document.getElementById("networkName").innerText = "MetaMask Web3 Connected";
                    updateUI();
                    alert(`Đã kết nối ví MetaMask thành công:\n${accounts[0]}`);
                }
            } catch (err) {
                console.error(err);
                alert("Người dùng đã từ chối kết nối ví!");
            }
        } else {
            alert("Trình duyệt chưa cài MetaMask. Ứng dụng đang chạy mượt mà ở chế độ Mô phỏng EVM In-Memory (Zero Configuration)!");
        }
    });
}
