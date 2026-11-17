# -*- coding: utf-8 -*-
"""
Script sinh dữ liệu mẫu chân thực cho Công ty Bán lẻ Phúc An (Phúc An Retail)
Quy mô: 18 cửa hàng, ~60.000 dòng giao dịch/tháng, chứa đầy đủ các bẫy thực tế
để AI Agent giải quyết và làm sạch.
"""

import os
import random
import datetime
import pandas as pd
import numpy as np
import json

random.seed(42)
np.random.seed(42)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "app", "data")
os.makedirs(DATA_DIR, exist_ok=True)

# 1. Danh sách 18 Cửa hàng Phúc An
STORES = [
    {"store_id": "PA-01", "store_name": "Phúc An Hoàn Kiếm", "region": "Miền Bắc", "city": "Hà Nội", "manager": "Nguyễn Văn Tuấn", "tier": "Tier 1"},
    {"store_id": "PA-02", "store_name": "Phúc An Cầu Giấy", "region": "Miền Bắc", "city": "Hà Nội", "manager": "Trần Thị Mai", "tier": "Tier 1"},
    {"store_id": "PA-03", "store_name": "Phúc An Ba Đình", "region": "Miền Bắc", "city": "Hà Nội", "manager": "Lê Hoàng Long", "tier": "Tier 2"},
    {"store_id": "PA-04", "store_name": "Phúc An Hà Đông", "region": "Miền Bắc", "city": "Hà Nội", "manager": "Phạm Quốc Bảo", "tier": "Tier 2"},
    {"store_id": "PA-05", "store_name": "Phúc An Hồng Bàng", "region": "Miền Bắc", "city": "Hải Phòng", "manager": "Vũ Hải Đăng", "tier": "Tier 2"},
    {"store_id": "PA-06", "store_name": "Phúc An Hạ Long", "region": "Miền Bắc", "city": "Quảng Ninh", "manager": "Đỗ Thu Trang", "tier": "Tier 3"},
    {"store_id": "PA-07", "store_name": "Phúc An Hải Châu", "region": "Miền Trung", "city": "Đà Nẵng", "manager": "Nguyễn Thanh Tùng", "tier": "Tier 1"},
    {"store_id": "PA-08", "store_name": "Phúc An Thanh Khê", "region": "Miền Trung", "city": "Đà Nẵng", "manager": "Hồ Minh Quân", "tier": "Tier 2"},
    {"store_id": "PA-09", "store_name": "Phúc An TP Huế", "region": "Miền Trung", "city": "Huế", "manager": "Hoàng Kim Oanh", "tier": "Tier 2"},
    {"store_id": "PA-10", "store_name": "Phúc An Nha Trang", "region": "Miền Trung", "city": "Khánh Hòa", "manager": "Bùi Đức Thịnh", "tier": "Tier 2"},
    {"store_id": "PA-11", "store_name": "Phúc An Quy Nhơn", "region": "Miền Trung", "city": "Bình Định", "manager": "Võ Thị Hằng", "tier": "Tier 3"},
    {"store_id": "PA-12", "store_name": "Phúc An Quận 1", "region": "Miền Nam", "city": "TP.HCM", "manager": "Lâm Quốc Hưng", "tier": "Tier 1"},
    {"store_id": "PA-13", "store_name": "Phúc An Quận 7", "region": "Miền Nam", "city": "TP.HCM", "manager": "Trương Ngọc Lan", "tier": "Tier 1"},
    {"store_id": "PA-14", "store_name": "Phúc An Bình Thạnh", "region": "Miền Nam", "city": "TP.HCM", "manager": "Phan Hữu Nghĩa", "tier": "Tier 2"},
    {"store_id": "PA-15", "store_name": "Phúc An Tân Bình", "region": "Miền Nam", "city": "TP.HCM", "manager": "Đặng Thị Thùy", "tier": "Tier 2"},
    {"store_id": "PA-16", "store_name": "Phúc An Thủ Đức", "region": "Miền Nam", "city": "TP.HCM", "manager": "Ngô Gia Huy", "tier": "Tier 1"},
    {"store_id": "PA-17", "store_name": "Phúc An Biên Hòa", "region": "Miền Nam", "city": "Đồng Nai", "manager": "Lý Cẩm Nhung", "tier": "Tier 2"},
    {"store_id": "PA-18", "store_name": "Phúc An Ninh Kiều", "region": "Miền Nam", "city": "Cần Thơ", "manager": "Huỳnh Tấn Đạt", "tier": "Tier 2"},
]

# 2. Danh mục 20 Sản phẩm và Giá vốn (COGS)
PRODUCTS = [
    # Gia dụng thông minh (Biên lợi nhuận cao: 35-45%)
    {"product_id": "PRD-01", "product_name": "Robot hút bụi lau nhà PA-Robo X9", "category": "Gia dụng thông minh", "cost_price": 4200000, "selling_price": 6990000},
    {"product_id": "PRD-02", "product_name": "Nồi chiên không dầu điện tử 6.5L", "category": "Gia dụng thông minh", "cost_price": 1100000, "selling_price": 1890000},
    {"product_id": "PRD-03", "product_name": "Máy lọc không khí Plasma Air Pro", "category": "Gia dụng thông minh", "cost_price": 2800000, "selling_price": 4590000},
    {"product_id": "PRD-04", "product_name": "Máy ép chậm tinh chất hoa quả 250W", "category": "Gia dụng thông minh", "cost_price": 1350000, "selling_price": 2290000},
    {"product_id": "PRD-05", "product_name": "Ấm siêu tốc giữ nhiệt thông minh 1.8L", "category": "Gia dụng thông minh", "cost_price": 380000, "selling_price": 650000},
    
    # Thiết bị số & Phụ kiện (Biên lợi nhuận thấp: 18-28%)
    {"product_id": "PRD-06", "product_name": "Tai nghe Bluetooth True Wireless Neo", "category": "Thiết bị số & Phụ kiện", "cost_price": 520000, "selling_price": 690000},
    {"product_id": "PRD-07", "product_name": "Sạc dự phòng 20000mAh PD 22.5W", "category": "Thiết bị số & Phụ kiện", "cost_price": 320000, "selling_price": 420000},
    {"product_id": "PRD-08", "product_name": "Loa Bluetooth di động Bass Plus", "category": "Thiết bị số & Phụ kiện", "cost_price": 650000, "selling_price": 850000},
    {"product_id": "PRD-09", "product_name": "Vòng tay theo dõi sức khỏe FitTrack", "category": "Thiết bị số & Phụ kiện", "cost_price": 720000, "selling_price": 990000},
    {"product_id": "PRD-10", "product_name": "Cáp sạc nhanh 3-in-1 chống rối 65W", "category": "Thiết bị số & Phụ kiện", "cost_price": 110000, "selling_price": 150000},

    # Chăm sóc cá nhân (Biên lợi nhuận rất cao: 42-52%)
    {"product_id": "PRD-11", "product_name": "Bàn chải điện sóng âm Sonic Care", "category": "Chăm sóc cá nhân", "cost_price": 390000, "selling_price": 790000},
    {"product_id": "PRD-12", "product_name": "Máy tăm nước du lịch chống nước IPX7", "category": "Chăm sóc cá nhân", "cost_price": 420000, "selling_price": 890000},
    {"product_id": "PRD-13", "product_name": "Máy sấy tóc ion âm bảo vệ tóc 1800W", "category": "Chăm sóc cá nhân", "cost_price": 310000, "selling_price": 620000},
    {"product_id": "PRD-14", "product_name": "Máy cạo râu đa năng 3 lưỡi kép", "category": "Chăm sóc cá nhân", "cost_price": 280000, "selling_price": 550000},
    {"product_id": "PRD-15", "product_name": "Máy massage cổ vai gáy nhiệt hồng ngoại", "category": "Chăm sóc cá nhân", "cost_price": 650000, "selling_price": 1290000},

    # Đồ gia đình cao cấp (Biên lợi nhuận trung bình khá: 32-40%)
    {"product_id": "PRD-16", "product_name": "Bộ nồi Inox 304 5 đáy cao cấp", "category": "Đồ gia đình cao cấp", "cost_price": 1500000, "selling_price": 2390000},
    {"product_id": "PRD-17", "product_name": "Chảo chống dính vân đá Ceramic 28cm", "category": "Đồ gia đình cao cấp", "cost_price": 380000, "selling_price": 590000},
    {"product_id": "PRD-18", "product_name": "Bình giữ nhiệt Lock & Fresh 800ml", "category": "Đồ gia đình cao cấp", "cost_price": 190000, "selling_price": 320000},
    {"product_id": "PRD-19", "product_name": "Bộ dao bếp Nhật Bản 6 món thép SK5", "category": "Đồ gia đình cao cấp", "cost_price": 580000, "selling_price": 950000},
    {"product_id": "PRD-20", "product_name": "Hộp cơm cắm điện hâm nóng 3 tầng", "category": "Đồ gia đình cao cấp", "cost_price": 260000, "selling_price": 420000},
]

prod_map = {p["product_id"]: p for p in PRODUCTS}

# 3. Mục tiêu kinh doanh tháng 10/2026 (Targets)
# Đặt mục tiêu theo quy mô từng cửa hàng
STORE_TARGETS = []
target_base_rev = {
    "Tier 1": (3200000000, 4200000000),
    "Tier 2": (2200000000, 3100000000),
    "Tier 3": (1500000000, 2100000000),
}

for s in STORES:
    tier = s["tier"]
    min_r, max_r = target_base_rev[tier]
    target_rev = round(random.randint(min_r // 1000000, max_r // 1000000) * 1000000, -6)
    # Target GP khoảng 35% - 40% của Revenue
    target_gp = round(target_rev * random.uniform(0.36, 0.40), -6)
    STORE_TARGETS.append({
        "store_id": s["store_id"],
        "store_name": s["store_name"],
        "period": "2026-10",
        "target_revenue": int(target_rev),
        "target_gross_profit": int(target_gp),
    })

# 4. Sinh dữ liệu thô tháng 10/2026 (60.000 dòng)
def generate_raw_october():
    records = []
    total_needed = 60000
    
    # Ngày trong tháng 10: 2026-10-01 đến 2026-10-31
    start_date = datetime.date(2026, 10, 1)
    end_date = datetime.date(2026, 10, 31)
    
    # Các trường hợp bẫy được thiết kế:
    # PA-02: Tỷ lệ đổi trả rất cao (hàng lỗi)
    # PA-13: Bán lệch cơ cấu (toàn bán phụ kiện lãi mỏng -> doanh thu cao nhưng lãi gộp tụt)
    # PA-08: Doanh thu thấp, sụt giảm mạnh
    # PA-12: Cửa hàng xuất sắc
    
    # 54.000 dòng ban đầu
    base_count = 54500
    
    channels = ["Tại cửa hàng", "Online - Giao hàng", "Shopee Mall", "TikTok Shop"]
    payment_methods = ["Tiền mặt", "Chuyển khoản QR", "Thẻ tín dụng", "Ví MoMo", "VNPay"]
    
    for i in range(1, base_count + 1):
        # Chọn store với phân bổ có chủ đích
        store = random.choice(STORES)
        s_id = store["store_id"]
        
        # Ngày giao dịch (hầu hết tháng 10, có 650 dòng bị kéo nhầm từ tháng 9 hoặc tháng 11)
        if random.random() < 0.012:  # ~650 dòng lệch kỳ
            if random.random() < 0.5:
                # Cuối tháng 9
                trans_date = datetime.date(2026, 9, random.randint(25, 30))
            else:
                # Đầu tháng 11
                trans_date = datetime.date(2026, 11, random.randint(1, 4))
        else:
            trans_date = start_date + datetime.timedelta(days=random.randint(0, 30))
            
        # Cơ cấu sản phẩm
        if s_id == "PA-13":
            # PA-13 bán 75% phụ kiện giá rẻ lãi mỏng
            if random.random() < 0.75:
                prod = random.choice([p for p in PRODUCTS if p["category"] == "Thiết bị số & Phụ kiện"])
            else:
                prod = random.choice(PRODUCTS)
        else:
            prod = random.choice(PRODUCTS)
            
        qty = random.choices([1, 2, 3, 4, 5], weights=[0.70, 0.18, 0.08, 0.03, 0.01])[0]
        unit_price = prod["selling_price"]
        unit_cost = prod["cost_price"]
        discount_rate = random.choices([0.0, 0.05, 0.10, 0.15], weights=[0.60, 0.25, 0.10, 0.05])[0]
        
        gross_amount = int(qty * unit_price)
        discount_amount = int(gross_amount * discount_rate)
        total_amount = gross_amount - discount_amount
        
        # Trạng thái đơn
        # PA-02 tỷ lệ return/cancel cao đột biến
        if s_id == "PA-02":
            status_choice = random.choices(["COMPLETED", "RETURNED", "CANCELLED"], weights=[0.78, 0.16, 0.06])[0]
        else:
            status_choice = random.choices(["COMPLETED", "RETURNED", "CANCELLED"], weights=[0.91, 0.05, 0.04])[0]
            
        trans_id = f"TX2610-{i:06d}"
        
        return_reason = ""
        if status_choice == "RETURNED":
            if prod["category"] == "Gia dụng thông minh":
                return_reason = random.choice(["Lỗi kỹ thuật - Không khởi động", "Cảm biến báo lỗi liên tục", "Hàng móp méo khi vận chuyển"])
            else:
                return_reason = random.choice(["Khách đổi ý không lấy", "Sản phẩm không vừa ý", "Đặt nhầm mã sản phẩm"])
        elif status_choice == "CANCELLED":
            return_reason = random.choice(["Khách huỷ trước khi nhận", "Trùng đơn đặt hàng", "Hết hàng tại kho"])

        records.append({
            "transaction_id": trans_id,
            "transaction_date": trans_date.strftime("%Y-%m-%d"),
            "store_id": s_id,
            "store_name": store["store_name"],
            "region": store["region"],
            "product_id": prod["product_id"],
            "product_name": prod["product_name"],
            "category": prod["category"],
            "quantity": qty,
            "unit_price": unit_price,
            "unit_cost": unit_cost,
            "discount_amount": discount_amount,
            "total_amount": total_amount,
            "status": status_choice,
            "channel": random.choice(channels),
            "payment_method": random.choice(payment_methods),
            "note": return_reason
        })

    # Bây giờ thêm ~1.500 dòng DUPLICATE (nhân viên ghép file bị đúp)
    dup_samples = random.sample(records[:20000], 1600)
    for r in dup_samples:
        dup_record = dict(r)
        records.append(dup_record)
        
    # Bổ sung các dòng đơn bị hủy / đổi trả cho đủ ~60.000 dòng
    remaining = total_needed - len(records)
    for j in range(remaining):
        store = random.choice(STORES)
        prod = random.choice(PRODUCTS)
        qty = random.randint(1, 2)
        unit_price = prod["selling_price"]
        unit_cost = prod["cost_price"]
        total_amount = qty * unit_price
        trans_date = start_date + datetime.timedelta(days=random.randint(0, 30))
        status_choice = random.choices(["CANCELLED", "RETURNED", "COMPLETED"], weights=[0.45, 0.35, 0.20])[0]
        
        records.append({
            "transaction_id": f"TX2610-EXTRA-{j:04d}",
            "transaction_date": trans_date.strftime("%Y-%m-%d"),
            "store_id": store["store_id"],
            "store_name": store["store_name"],
            "region": store["region"],
            "product_id": prod["product_id"],
            "product_name": prod["product_name"],
            "category": prod["category"],
            "quantity": qty,
            "unit_price": unit_price,
            "unit_cost": unit_cost,
            "discount_amount": 0,
            "total_amount": total_amount,
            "status": status_choice,
            "channel": random.choice(channels),
            "payment_method": random.choice(payment_methods),
            "note": "Đơn rà soát bổ sung" if status_choice == "COMPLETED" else "Hủy/Đổi trả theo phiếu"
        })
        
    random.shuffle(records)
    return records

# 5. Sinh dữ liệu chuẩn kỳ so sánh (Tháng 09/2026 - 30 ngày)
def generate_prior_period_sep():
    # Tập dữ liệu tháng 9 để so sánh tăng trưởng MoM
    # Tính theo cửa hàng để có số liệu cơ sở
    prior_stats = {}
    for s in STORES:
        s_id = s["store_id"]
        # Phù hợp với tier
        tier = s["tier"]
        min_r, max_r = target_base_rev[tier]
        base_rev = random.randint(int(min_r * 0.9), int(max_r * 1.05))
        
        # Tình trạng đặc biệt:
        # PA-08 tháng 9 bán rất tốt (2.8 tỷ), tháng 10 sụt giảm nghiêm trọng
        if s_id == "PA-08":
            base_rev = 2850000000
        elif s_id == "PA-13":
            # PA-13 tháng 9 doanh thu 2.9 tỷ, LN 1.1 tỷ
            base_rev = 2900000000
        elif s_id == "PA-02":
            # PA-02 tháng 9 bình thường, ít hàng lỗi
            base_rev = 3400000000
            
        base_gp = int(base_rev * random.uniform(0.35, 0.40))
        if s_id == "PA-13":
            base_gp = int(base_rev * 0.38) # Tháng 9 margin 38%
            
        prior_stats[s_id] = {
            "store_id": s_id,
            "store_name": s["store_name"],
            "period": "2026-09",
            "days_in_period": 30,
            "net_revenue": base_rev,
            "gross_profit": base_gp,
            "gross_margin": round(base_gp / base_rev * 100, 2),
            "return_rate": round(random.uniform(3.5, 5.5), 2),
            "completed_orders": random.randint(2200, 3800)
        }
    return list(prior_stats.values())

# 6. Quy tắc kinh doanh (Business Rules)
BUSINESS_RULES = {
    "report_period": {
        "period_name": "Tháng 10/2026",
        "start_date": "2026-10-01",
        "end_date": "2026-10-31",
        "days": 31
    },
    "comparison_period": {
        "period_name": "Tháng 09/2026",
        "start_date": "2026-09-01",
        "end_date": "2026-09-30",
        "days": 30
    },
    "cleaning_rules": [
        {
            "rule_id": "RULE-DEDUP",
            "name": "Lọc trùng giao dịch",
            "description": "Loại bỏ các dòng có cùng transaction_id xuất hiện từ lần thứ 2 trở đi.",
            "action": "Drop exact duplicates on transaction_id"
        },
        {
            "rule_id": "RULE-CANCEL",
            "name": "Loại bỏ đơn bị hủy",
            "description": "Tách các đơn hàng có trạng thái CANCELLED ra khỏi doanh thu và giá vốn.",
            "action": "Exclude status == 'CANCELLED'"
        },
        {
            "rule_id": "RULE-RETURN",
            "name": "Xử lý hàng đổi trả",
            "description": "Ghi nhận dòng RETURNED để giảm trừ doanh thu gộp (Net Revenue = Gross Sales - Returns) và hoàn nhập giá vốn (Net COGS = Sold COGS - Returned COGS).",
            "action": "Deduct from Revenue and COGS"
        },
        {
            "rule_id": "RULE-PERIOD-SYNC",
            "name": "Đồng bộ chuẩn hóa kỳ thời gian",
            "description": "Chỉ lấy các giao dịch có transaction_date nằm trong khoảng [2026-10-01, 2026-10-31]. Chuẩn hóa tốc độ bán hàng theo ngày khi so với tháng 9 (31 ngày vs 30 ngày).",
            "action": "Filter transaction_date between start_date and end_date"
        }
    ],
    "calculation_formulas": {
        "gross_sales": "Tổng total_amount của các đơn COMPLETED",
        "returns_amount": "Tổng total_amount của các đơn RETURNED",
        "net_revenue": "Gross Sales - Returns Amount",
        "cogs": "Tổng (unit_cost * quantity) của COMPLETED - RETURNED",
        "gross_profit": "Net Revenue - Net COGS",
        "gross_margin_pct": "(Gross Profit / Net Revenue) * 100",
        "revenue_target_pct": "(Net Revenue / Target Revenue) * 100",
        "gp_target_pct": "(Gross Profit / Target Gross Profit) * 100",
        "return_rate_pct": "(Returns Amount / (Gross Sales + Returns Amount)) * 100",
        "revenue_growth_pct": "((Net Revenue Oct / Net Revenue Sep) - 1) * 100 (đã điều chỉnh số ngày)"
    },
    "audit_thresholds": {
        "high_return_warning_pct": 8.0,
        "high_return_critical_pct": 12.0,
        "target_miss_warning_pct": 85.0,
        "target_miss_critical_pct": 75.0,
        "negative_growth_critical_pct": -10.0,
        "margin_drop_warning_pct": -3.0
    }
}

if __name__ == "__main__":
    print("Đang tạo dữ liệu mẫu cho Phúc An Retail...")
    
    # Lưu danh mục cửa hàng
    df_stores = pd.DataFrame(STORES)
    df_stores.to_csv(os.path.join(DATA_DIR, "stores.csv"), index=False, encoding="utf-8-sig")
    print(f"- Đã lưu {len(df_stores)} cửa hàng vào stores.csv")
    
    # Lưu danh mục sản phẩm & giá vốn
    df_products = pd.DataFrame(PRODUCTS)
    df_products.to_csv(os.path.join(DATA_DIR, "products_cogs.csv"), index=False, encoding="utf-8-sig")
    print(f"- Đã lưu {len(df_products)} sản phẩm và giá vốn vào products_cogs.csv")
    
    # Lưu mục tiêu kinh doanh
    df_targets = pd.DataFrame(STORE_TARGETS)
    df_targets.to_csv(os.path.join(DATA_DIR, "targets_oct2026.csv"), index=False, encoding="utf-8-sig")
    print(f"- Đã lưu mục tiêu kinh doanh vào targets_oct2026.csv")
    
    # Lưu quy tắc nghiệp vụ
    with open(os.path.join(DATA_DIR, "business_rules.json"), "w", encoding="utf-8") as f:
        json.dump(BUSINESS_RULES, f, ensure_ascii=False, indent=2)
    print("- Đã lưu business_rules.json")
    
    # Lưu dữ liệu kỳ trước (tháng 9)
    prior_data = generate_prior_period_sep()
    df_prior = pd.DataFrame(prior_data)
    df_prior.to_csv(os.path.join(DATA_DIR, "prior_period_sep2026.csv"), index=False, encoding="utf-8-sig")
    print(f"- Đã lưu dữ liệu so sánh kỳ trước (T9/2026) vào prior_period_sep2026.csv")
    
    # Sinh 60.000 dòng dữ liệu thô tháng 10
    raw_data = generate_raw_october()
    df_raw = pd.DataFrame(raw_data)
    df_raw.to_csv(os.path.join(DATA_DIR, "raw_transactions_oct2026.csv"), index=False, encoding="utf-8-sig")
    print(f"- Đã sinh và lưu {len(df_raw)} dòng giao dịch thô vào raw_transactions_oct2026.csv")
    
    print("Hoàn tất khởi tạo dữ liệu mẫu!")

