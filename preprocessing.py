# Xử lý dữ liệu: chuẩn hóa cột 'Gia', thêm cột 'loai_san_pham'
import pandas as pd
df = pd.read_excel("phones.xlsx")
# Bỏ ký tự 'đ', dấu chấm và chuyển về kiểu số nguyên
df['Gia'] = df['Gia'].str.replace('.', '', regex=False).str.replace('đ', '', regex=False).str.replace(',', '', regex=False)
df['Gia'] = pd.to_numeric(df['Gia'], errors='coerce')  # Chuyển sang kiểu số

# Thêm cột 'loai_san_pham' với giá trị mặc định là 'Điện thoại'
df['loai_san_pham'] = 'Điện thoại'

# Đổi tên cột 'Ten' thành 'ten' để tiện xử lý
df = df.rename(columns={'Ten': 'ten'})

# Lưu thành file CSV
output_path = "dien_thoai.csv"
df.to_csv(output_path, index=False, encoding='utf-8-sig')

output_path
