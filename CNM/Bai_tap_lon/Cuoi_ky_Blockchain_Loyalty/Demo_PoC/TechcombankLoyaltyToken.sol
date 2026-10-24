// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title TechcombankLoyaltyToken (TCB-PTS)
 * @author Nhóm Học viên Cao học MIS01 - Học viện Ngân hàng
 * @notice Hợp đồng thông minh quản lý Hệ sinh thái Điểm thưởng Khách hàng thân thiết
 *         chuẩn ERC-20 phục vụ Bài tập lớn môn Công nghệ Mới nổi và Đổi mới (CNM).
 * @dev Kế thừa tiêu chuẩn ERC-20 và OpenZeppelin Ownable.
 */
contract TechcombankLoyaltyToken is ERC20, Ownable {

    // Cấu trúc dữ liệu ghi nhận Voucher đổi thưởng của đối tác
    struct VoucherRedemption {
        address customer;
        string partnerName;
        string voucherCode;
        uint256 costInPoints;
        uint256 timestamp;
        bool isUsed;
    }

    // Biến trạng thái
    uint256 public constant INITIAL_BANK_SUPPLY = 10_000_000 * 10 ** 18; // 10 triệu điểm thưởng ban đầu
    uint256 public totalRedemptionsCount;

    // Mapping lưu trữ lịch sử đổi voucher theo mã băm giao dịch
    mapping(bytes32 => VoucherRedemption) public redemptions;
    mapping(address => bool) public authorizedPartners;

    // Sự kiện phục vụ đối soát tự động theo thời gian thực (Zero-Reconciliation)
    event PointsRewarded(address indexed customer, uint256 points, string transactionRef);
    event BatchPointsRewarded(uint256 totalCustomers, uint256 totalPoints);
    event VoucherRedeemed(bytes32 indexed redemptionId, address indexed customer, string partnerName, string voucherCode, uint256 costInPoints);
    event PartnerStatusUpdated(address indexed partnerAddress, bool isAuthorized);
    event VoucherValidated(bytes32 indexed redemptionId, address indexed partner, uint256 timestamp);

    /**
     * @notice Khởi tạo hợp đồng thông minh
     * @param initialOwner Địa chỉ ví quản trị viên Techcombank
     */
    constructor(address initialOwner) 
        ERC20("Techcombank Loyalty Point", "TCB-PTS") 
        Ownable(initialOwner) 
    {
        // Đúc toàn bộ tổng cung ban đầu về ví quản trị của Ngân hàng
        _mint(initialOwner, INITIAL_BANK_SUPPLY);
    }

    /**
     * @notice Phân quyền cho đối tác trong hệ sinh thái (Highlands Coffee, Vietnam Airlines, Shopee...)
     */
    function setPartnerStatus(address partnerAddress, bool isAuthorized) external onlyOwner {
        require(partnerAddress != address(0), "Dia chi doi tac khong hop le");
        authorizedPartners[partnerAddress] = isAuthorized;
        emit PartnerStatusUpdated(partnerAddress, isAuthorized);
    }

    /**
     * @notice Ngân hàng thưởng điểm khi khách hàng chi tiêu qua thẻ tín dụng / thanh toán số
     * @param customer Địa chỉ ví số của khách hàng
     * @param points Số điểm thưởng (1 điểm = 1 * 10^18 wei-points)
     * @param transactionRef Mã tham chiếu giao dịch thẻ lõi (Core Banking Reference)
     */
    function rewardPoints(address customer, uint256 points, string calldata transactionRef) external onlyOwner {
        require(customer != address(0), "Dia chi khach hang khong hop le");
        require(points > 0, "So diem thuong phai lon hon 0");

        uint256 rawAmount = points * 10 ** decimals();
        require(balanceOf(owner()) >= rawAmount, "Quy diem thuong ngan hang khong du");

        _transfer(owner(), customer, rawAmount);
        emit PointsRewarded(customer, points, transactionRef);
    }

    /**
     * @notice Thưởng điểm hàng loạt (Batch Reward) giúp tối ưu hóa chi phí Gas
     * @param customers Danh sách khách hàng được thưởng điểm
     * @param points Danh sách số điểm tương ứng
     */
    function batchRewardPoints(address[] calldata customers, uint256[] calldata points) external onlyOwner {
        require(customers.length == points.length, "Do dai danh sach khong khop");
        uint256 totalPointsRewarded = 0;

        for (uint256 i = 0; i < customers.length; i++) {
            uint256 rawAmount = points[i] * 10 ** decimals();
            _transfer(owner(), customers[i], rawAmount);
            totalPointsRewarded += points[i];
            emit PointsRewarded(customers[i], points[i], "BATCH_SETTLEMENT");
        }

        emit BatchPointsRewarded(customers.length, totalPointsRewarded);
    }

    /**
     * @notice Khách hàng đổi điểm thưởng lấy Voucher ưu đãi từ đối tác
     * @dev Điểm thưởng sẽ bị đốt (Burn) khỏi lưu thông để bảo vệ giá trị kinh tế token
     * @param costInPoints Chi phí điểm của voucher
     * @param partnerName Tên đối tác phát hành ưu đãi
     * @param voucherCode Mã voucher trả về cho khách hàng
     */
    function redeemVoucher(
        uint256 costInPoints, 
        string calldata partnerName, 
        string calldata voucherCode
    ) external returns (bytes32 redemptionId) {
        require(costInPoints > 0, "Chi phi doi diem phai lon hon 0");
        uint256 rawCost = costInPoints * 10 ** decimals();
        require(balanceOf(msg.sender) >= rawCost, "So du diem thuong khong du");

        // Đốt điểm thưởng khỏi ví người dùng
        _burn(msg.sender, rawCost);

        // Tạo mã băm định danh duy nhất cho giao dịch đổi quà
        redemptionId = keccak256(
            abi.encodePacked(msg.sender, partnerName, voucherCode, block.timestamp, totalRedemptionsCount)
        );

        redemptions[redemptionId] = VoucherRedemption({
            customer: msg.sender,
            partnerName: partnerName,
            voucherCode: voucherCode,
            costInPoints: costInPoints,
            timestamp: block.timestamp,
            isUsed: false
        });

        totalRedemptionsCount++;
        emit VoucherRedeemed(redemptionId, msg.sender, partnerName, voucherCode, costInPoints);
        return redemptionId;
    }

    /**
     * @notice Đối tác xác thực và sử dụng Voucher khi khách hàng thanh toán tại cửa hàng
     */
    function validateAndUseVoucher(bytes32 redemptionId) external {
        VoucherRedemption storage item = redemptions[redemptionId];
        require(item.timestamp > 0, "Voucher khong ton tai");
        require(!item.isUsed, "Voucher da duoc su dung truoc do");

        item.isUsed = true;
        emit VoucherValidated(redemptionId, msg.sender, block.timestamp);
    }

    /**
     * @notice Tra cứu số dư điểm thưởng định dạng số nguyên dễ đọc
     */
    function getDisplayBalance(address account) external view returns (uint256) {
        return balanceOf(account) / (10 ** decimals());
    }
}
