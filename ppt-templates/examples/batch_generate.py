"""
Ví dụ sinh hàng loạt - Kho Mẫu Slide PPT

Ví dụ này minh họa cách sinh hàng loạt toàn bộ mẫu slide.

Ghi chú triển khai: Phiên bản trước đây duy trì logic sinh trùng lặp với scripts/generate_all.py,
việc duy trì song song hai nơi dễ dẫn đến sai lệch. Hiện đã chuyển sang ủy quyền trực tiếp
cho script xây dựng chính; tệp này chỉ giữ vai trò điểm vào ví dụ, logic thống nhất do scripts/generate_all.py đảm nhiệm.

Cách chạy:
    python examples/batch_generate.py              # Sinh toàn bộ mẫu vào templates/
    python examples/batch_generate.py --theme blue  # Chỉ sinh chủ đề chỉ định
    python examples/batch_generate.py --type cover  # Chỉ sinh loại chỉ định
"""

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MAIN_SCRIPT = ROOT / "scripts" / "generate_all.py"


def main():
    if not MAIN_SCRIPT.is_file():
        print(f"[LỖI] Không tìm thấy script xây dựng chính: {MAIN_SCRIPT}")
        return 1
    # Chuyển tiếp toàn bộ tham số dòng lệnh, hành vi hoàn toàn tương đương gọi trực tiếp script chính
    return subprocess.call([sys.executable, str(MAIN_SCRIPT)] + sys.argv[1:])


if __name__ == "__main__":
    raise SystemExit(main())
