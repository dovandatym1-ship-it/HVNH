"""
Script tự động cài đặt thư viện mẫu PPT

Tự động clone/cập nhật kho lưu trữ mẫu và cài đặt các phụ thuộc.
Cách dùng: python setup.py
"""
import subprocess
import sys
import os

REPO_URL = "https://github.com/wuhua2026/ppt-templates.git"
INSTALL_DIR = os.path.join(os.path.expanduser("~"), ".ppt-templates")


def run(cmd, check=True):
    """Thực thi lệnh shell và trả về kết quả"""
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if check and result.returncode != 0:
        print(f"  [LỖI] {result.stderr.strip()}")
    return result


def setup():
    """Cài đặt hoặc cập nhật thư viện mẫu"""
    print("=" * 50)
    print("  Chương trình cài đặt Thư viện Mẫu PPT")
    print("=" * 50)

    # Kiểm tra xem đã cài đặt chưa
    if os.path.exists(INSTALL_DIR):
        print(f"\nĐã phát hiện thư viện mẫu tại: {INSTALL_DIR}")
        print("Đang cập nhật...")
        run(f'cd "{INSTALL_DIR}" && git pull')
        print("Cập nhật hoàn tất!")
    else:
        print(f"\nĐang clone thư viện mẫu về: {INSTALL_DIR}")
        run(f'git clone {REPO_URL} "{INSTALL_DIR}"')
        print("Clone hoàn tất!")

    # Cài đặt phụ thuộc Python
    print("\nCài đặt phụ thuộc Python...")
    run(f"{sys.executable} -m pip install python-pptx Pillow lxml -q")

    # Cài đặt phụ thuộc JS (nếu Node.js khả dụng)
    js_dir = os.path.join(INSTALL_DIR, "js")
    if os.path.exists(js_dir):
        result = run("node --version", check=False)
        if result.returncode == 0:
            print("Cài đặt phụ thuộc JavaScript...")
            run(f'cd "{js_dir}" && npm install --silent', check=False)

    print("\n" + "=" * 50)
    print("  Cài đặt hoàn tất!")
    print(f"  Vị trí thư viện mẫu: {INSTALL_DIR}")
    print("=" * 50)


if __name__ == "__main__":
    setup()
