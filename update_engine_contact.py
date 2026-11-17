# update_engine_contact.py
engine_path = r"c:\Users\ADMIN\OneDrive\Attachments\Thi cuối môn AI301\app\engine.py"
with open(engine_path, "r", encoding="utf-8") as f:
    content = f.read()

target = '        # 1. Hỏi danh sách cửa hàng cần hỗ trợ trước / ưu tiên'
contact_logic = '''        # 0. Hỏi về thông tin liên hệ / Hotline / Email / Địa chỉ
        if any(w in msg for w in ["liên hệ", "số điện thoại", "sđt", "phone", "email", "địa chỉ", "hotline", "contact", "bảo ngọc", "nguyễn bảo ngọc"]):
            return """### 📞 Thông Tin Liên Hệ — Bảo Ngọc AI (Retail Agent OS)
- **Người phụ trách:** **Nguyễn Bảo Ngọc** (Bảo Ngọc Retail)
- **Số điện thoại (Hotline):** `0362848956` *(Hỗ trợ trực tiếp & Zalo)*
- **Email:** `baongocnguyen686827@gmail.com`
- **Địa chỉ:** `Hà Nội, Việt Nam`
- **Thời gian tiếp nhận:** Thứ 2 – Chủ Nhật (08:00 – 22:00) | Kênh kỹ thuật khẩn cấp: 24/7

> 💡 *Anh/chị cũng có thể nhấn nút **"Liên Hệ"** ở thanh Header trên cùng hoặc xem thông tin chi tiết tại chân trang (Footer)!*"""

        # 1. Hỏi danh sách cửa hàng cần hỗ trợ trước / ưu tiên'''

if target in content:
    content = content.replace(target, contact_logic, 1)
    with open(engine_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("AI Co-pilot contact response updated successfully")
else:
    print("Warning: target not found in engine.py")

