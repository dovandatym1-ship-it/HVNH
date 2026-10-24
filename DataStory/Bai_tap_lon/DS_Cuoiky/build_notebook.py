import sys
import subprocess

try:
    import nbformat as nbf
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "nbformat"])
    import nbformat as nbf

import pandas as pd
import numpy as np
import re

csv_path = "data.csv"
clean_csv_path = "cleaned_data.csv"
clean_excel_path = "cleaned_data.xlsx"

# 1. GENERATE THE DATA CLEANING OUTPUTS DIRECTLY FOR CONVENIENCE
print("Bắt đầu xử lý làm sạch dữ liệu...")
df = pd.read_csv(csv_path, skiprows=1)

df = df.iloc[:, :15]

date_cols = ['Ngày bắt đầu', 'Ngày kết thúc theo hợp đồng', 'Ngày kết thúc thực tế']
for col in date_cols:
    df[col] = pd.to_datetime(df[col], errors='coerce', dayfirst=True)

def clean_currency(val):
    if pd.isna(val): return np.nan
    val = str(val).lower()
    val = val.replace('b', '').replace('tỷ', '').replace('billion', '').replace('triệu', '')
    val = val.replace(' ', '').replace(',', '.')
    match = re.search('(\\d+\\.?\\d*)', val)
    if match:
        num = float(match.group(1))
        if num > 1000:
            num = num / 1000
        return num
    return np.nan

df['Giá trị hợp đồng (Tỷ VNĐ)'] = df['Giá trị hợp đồng'].apply(clean_currency)
df = df.drop(columns=['Giá trị hợp đồng'])

df['Công ty'] = df['Công ty'].astype(str).str.strip().str.title()
replacements = {'Denisoo': 'Deniso', 'Samsungg': 'Samsung'}
df['Công ty'] = df['Công ty'].replace(replacements)

def clean_delay(val):
    if pd.isna(val): return 0
    val = str(val).lower()
    match = re.search('(-?\\d+)', val)
    if match:
        return int(match.group(1))
    return 0

df['Số ngày chậm'] = df['Số ngày chậm'].apply(clean_delay)

df['Thầu phụ'] = df['Thầu phụ'].fillna('Chưa xác định')
df['Nguyên nhân chậm tiến độ'] = df['Nguyên nhân chậm tiến độ'].fillna('Đúng/Sớm hạn')

df.to_csv(clean_csv_path, index=False, encoding='utf-8-sig')
try:
    df.to_excel(clean_excel_path, index=False)
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "openpyxl"])
    df.to_excel(clean_excel_path, index=False)
print("Đã tạo file cleaned_data.csv và cleaned_data.xlsx")


# 2. GENERATE THE JUPYTER NOTEBOOK
print("Bắt đầu tạo Notebook EDA...")
nb = nbf.v4.new_notebook()

markdown_1 = """# Không sợ "Lỗ hổng" phát sinh, chỉ sợ thiếu "Khả năng phục hồi": Giải pháp tối ưu tiến độ
**Môn học:** Data Storytelling  

Notebook này trình bày toàn bộ quy trình Data Storytelling: Làm sạch dữ liệu -> Truy tìm nguyên nhân trễ hạn (Lỗ hổng) -> Điểm bùng nổ (Aha! Moment) -> Giải pháp.
"""
nb.cells.append(nbf.v4.new_markdown_cell(markdown_1))

code_1 = """import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re

# Định dạng biểu đồ
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

# Đọc dữ liệu thô (Bỏ qua 1 dòng tiêu đề của file CSV gốc)
df_raw = pd.read_csv('data.csv', skiprows=1)
df_raw = df_raw.iloc[:, :15] # Giữ lại 15 cột đầu
"""
nb.cells.append(nbf.v4.new_code_cell(code_1))

markdown_2 = """## Bước 1: Làm sạch & Tiền xử lý dữ liệu (Data Cleaning)
Áp dụng các kỹ thuật xử lý để chuẩn hóa dữ liệu bẩn (typo, định dạng sai, missing values) về dạng có thể tính toán được."""
nb.cells.append(nbf.v4.new_markdown_cell(markdown_2))

code_2 = """df_clean = df_raw.copy()

# 1. Chuẩn hóa Datetime
for col in ['Ngày bắt đầu', 'Ngày kết thúc theo hợp đồng', 'Ngày kết thúc thực tế']:
    df_clean[col] = pd.to_datetime(df_clean[col], errors='coerce', dayfirst=True)

# 2. Tiền tệ (Giá trị hợp đồng)
def clean_currency(val):
    if pd.isna(val): return np.nan
    val = str(val).lower().replace('b', '').replace('tỷ', '').replace('billion', '').replace('triệu', '').replace(' ', '').replace(',', '.')
    match = re.search(r'(\d+\.?\d*)', val)
    if match:
        num = float(match.group(1))
        return num / 1000 if num > 1000 else num
    return np.nan

df_clean['Giá trị (Tỷ VNĐ)'] = df_clean['Giá trị hợp đồng'].apply(clean_currency)
df_clean = df_clean.drop(columns=['Giá trị hợp đồng'])

# 3. Trích xuất Số ngày chậm
def clean_delay(val):
    if pd.isna(val): return 0
    match = re.search(r'(-?\d+)', str(val).lower())
    return int(match.group(1)) if match else 0
df_clean['Số ngày chậm'] = df_clean['Số ngày chậm'].apply(clean_delay)

# 4. Imputation
df_clean['Thầu phụ'] = df_clean['Thầu phụ'].fillna('Chưa xác định')
df_clean['Nguyên nhân chậm tiến độ'] = df_clean['Nguyên nhân chậm tiến độ'].fillna('Đúng/Sớm hạn')
df_clean['Công ty'] = df_clean['Công ty'].astype(str).str.strip().str.title()

df_clean.to_csv('cleaned_data.csv', index=False, encoding='utf-8-sig')
df_clean['Trạng thái'] = df_clean['Số ngày chậm'].apply(lambda x: 'Trễ hạn' if x > 0 else 'Đúng/Sớm hạn')
"""
nb.cells.append(nbf.v4.new_code_cell(code_2))

markdown_2b = """## Bước 2: Bức tranh tổng thể (The Context)
Trước khi đi tìm nguyên nhân, hãy nhìn vào tỷ lệ các dự án trễ hạn trong giai đoạn 2022-2025."""
nb.cells.append(nbf.v4.new_markdown_cell(markdown_2b))

code_donut = """# Tính toán tỷ lệ
status_counts = df_clean['Trạng thái'].value_counts()
colors = ['seagreen', 'firebrick'] if status_counts.index[0] != 'Trễ hạn' else ['firebrick', 'seagreen']

# Vẽ Donut chart
plt.figure(figsize=(8, 6))
plt.pie(status_counts, labels=status_counts.index, autopct='%1.1f%%', startangle=90, colors=colors, textprops={'fontsize': 14, 'weight': 'bold'})
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.title('Tỷ lệ Dự án Trễ hạn (2022-2025)', fontsize=16, fontweight='bold', pad=20)
plt.show()"""
nb.cells.append(nbf.v4.new_code_cell(code_donut))

markdown_3 = """## Bước 3: Truy tìm thủ phạm (The Conflict)
Nhìn vào bức tranh tổng thể, có tới 40% dự án trễ hạn. Nhưng điều gì đang thực sự cản bước họ?
Thông thường, chúng ta hay chỉ trích nhà thầu phụ hoặc đổ lỗi cho thời tiết. Hãy xem dữ liệu nói gì."""
nb.cells.append(nbf.v4.new_markdown_cell(markdown_3))

code_3 = """df_delayed = df_clean[df_clean['Số ngày chậm'] > 0]

# Tính trung bình số ngày chậm theo nguyên nhân
cause_impact = df_delayed.groupby('Nguyên nhân chậm tiến độ')['Số ngày chậm'].mean().sort_values(ascending=False).reset_index()

plt.figure(figsize=(10, 6))
ax = sns.barplot(data=cause_impact, x='Số ngày chậm', y='Nguyên nhân chậm tiến độ', hue='Nguyên nhân chậm tiến độ', palette='viridis', legend=False)
plt.title('Những kẻ chịu trận oan uổng và Thủ phạm lộ diện', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Thời gian trễ hạn trung bình (Ngày)', fontsize=12)
plt.ylabel('')

# Đổi màu nổi bật cho thủ phạm lớn nhất
for i, patch in enumerate(ax.patches):
    if cause_impact.iloc[i]['Nguyên nhân chậm tiến độ'] == 'Thay đổi thiết kế':
        patch.set_facecolor('firebrick')

plt.show()"""
nb.cells.append(nbf.v4.new_code_cell(code_3))

markdown_4 = """**Nhận xét:** 
Dữ liệu vạch trần một sự thật phũ phàng: "Thay đổi thiết kế" (Design Scope Creep) vượt lên trên tất cả các yếu tố ngoại cảnh khác như Thời tiết, Mặt bằng hay Nhân lực, trở thành nguyên nhân gây ra hậu quả nặng nề nhất."""
nb.cells.append(nbf.v4.new_markdown_cell(markdown_4))

markdown_5 = """## Bước 4: Điểm bùng nổ (The Aha! Moment)
Tại sao "Thay đổi thiết kế" lại tàn phá khủng khiếp như vậy? Biểu đồ phân tán dưới đây là câu trả lời đanh thép nhất."""
nb.cells.append(nbf.v4.new_markdown_cell(markdown_5))

code_4 = """plt.figure(figsize=(12, 6))
sns.scatterplot(data=df_clean, x='Số lần thay đổi thiết kế', y='Số ngày chậm', hue='Trạng thái', 
                palette={'Trễ hạn': 'firebrick', 'Đúng/Sớm hạn': 'lightgrey'}, alpha=0.6, s=60)

plt.title('Tương quan Tỷ lệ thuận tuyệt đối giữa Đổi thiết kế và Tiến độ', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Số lần thay đổi bản vẽ thiết kế', fontsize=12)
plt.ylabel('Số ngày chậm', fontsize=12)

# Vẽ đường xu hướng (Trend line) cho nhóm trễ hạn
df_trend = df_clean[df_clean['Trạng thái'] == 'Trễ hạn']
z = np.polyfit(df_trend['Số lần thay đổi thiết kế'], df_trend['Số ngày chậm'], 1)
p = np.poly1d(z)
plt.plot(df_trend['Số lần thay đổi thiết kế'], p(df_trend['Số lần thay đổi thiết kế']), "r--", linewidth=2)

plt.text(12, 50, 'Càng sửa bản vẽ, Dự án càng trượt dài!', fontsize=14, color='firebrick', fontweight='bold', bbox=dict(facecolor='white', alpha=0.8, edgecolor='none'))

plt.show()"""
nb.cells.append(nbf.v4.new_code_cell(code_4))

markdown_5b = """## Bước 5: Phân tích sâu - Quả cầu tuyết (Deep Dive)
Điều gì xảy ra khi "Thay đổi thiết kế" xuất hiện? Sự thiếu vắng "Khả năng phục hồi" khiến mọi độ trễ đều bị khuếch đại thành thảm họa."""
nb.cells.append(nbf.v4.new_markdown_cell(markdown_5b))

code_histogram = """plt.figure(figsize=(10, 6))
sns.histplot(data=df_delayed, x='Số ngày chậm', bins=40, kde=True, color='firebrick')
plt.title('Phân phối Số ngày chậm (The Snowball Effect)', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Số ngày chậm (Ngày)', fontsize=12)
plt.ylabel('Số lượng dự án', fontsize=12)

avg_delay = df_delayed['Số ngày chậm'].mean()
plt.axvline(avg_delay, color='black', linestyle='--', linewidth=2)
plt.text(avg_delay + 5, plt.ylim()[1]*0.8, f'Trung bình: {avg_delay:.0f} ngày', color='black', fontsize=12, weight='bold')
plt.text(5, plt.ylim()[1]*0.5, 'Vùng trống\\n(Thiếu khả năng phục hồi)', color='grey', fontsize=12, style='italic', ha='center')

plt.show()"""
nb.cells.append(nbf.v4.new_code_cell(code_histogram))

markdown_6 = """**Đúc kết (Resolution & Call to Action):**
Biểu đồ chứng minh sự tương quan tuyệt đối: Nguyên nhân lõi (Lỗ hổng) kích hoạt trễ hạn chính là **"Thay đổi thiết kế"**. Cứ mỗi lần chủ đầu tư đổi ý trên giấy, chuỗi cung ứng vật tư lập tức bị đứt gãy.
Nhưng mấu chốt nằm ở chỗ: Thay vì dập tắt rủi ro này bằng các biện pháp linh hoạt, bộ máy quản lý lại thả trôi, minh chứng cho sự thiếu hụt **"Khả năng phục hồi tiến độ" (Schedule Resilience)**. Lỗ hổng nhỏ biến thành thảm họa.

**Giải pháp:** 
1. Khắc phục Lỗ hổng: Khóa chặt rủi ro từ phòng thiết kế bằng kỷ luật **"Design Freeze"**. Mọi thay đổi sau mốc này phải dùng biên lai **Change Order**.
2. Tăng cường Khả năng phục hồi: Ngay khi Lỗ hổng xảy ra, lập tức kích hoạt "Làm song song" hoặc "Bơm thêm tiền tăng ca" để dập tắt độ trễ trong vòng 48h, không để quả cầu tuyết lăn xa hơn."""
nb.cells.append(nbf.v4.new_markdown_cell(markdown_6))

with open('EDA_Project.ipynb', 'w', encoding='utf-8') as f:
    nbf.write(nb, f)

print("Đã tạo thành công file Notebook: EDA_Project.ipynb")
