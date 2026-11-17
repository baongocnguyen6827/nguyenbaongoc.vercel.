# -*- coding: utf-8 -*-
"""
Flask Web Application & API cho AI Agent Bảo Ngọc Retail
Chạy trên localhost để Quản lý và Chuyên viên thao tác trực tiếp.
"""

import os
import json
import io
import pandas as pd
import numpy as np
from flask import Flask, render_template, request, jsonify, send_file
from app.engine import engine, DATA_DIR

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static")
)
app.config['JSON_AS_ASCII'] = False
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.jinja_env.auto_reload = True

@app.route("/")
def index():
    """Trang chủ hiển thị toàn bộ quy trình 3 giai đoạn theo BPMN"""
    return render_template("index.html")

@app.route("/api/system-state", methods=["GET"])
def get_system_state():
    """Lấy trạng thái hiện tại của hệ thống"""
    raw_loaded = engine.raw_df is not None
    cleaned_done = engine.cleaned_df is not None
    verified = engine.human_verification["status"] == "APPROVED"
    report_done = engine.management_report is not None
    audit_done = engine.audit_results is not None
    
    return jsonify({
        "raw_loaded": raw_loaded,
        "cleaned_done": cleaned_done,
        "human_verified": verified,
        "verification_info": engine.human_verification,
        "report_done": report_done,
        "audit_done": audit_done,
        "decisions_count": len(engine.executive_decisions)
    })

@app.route("/api/load-sample", methods=["GET", "POST"])
def load_sample_data():
    """Nạp bộ dữ liệu thô: Mặc định ưu tiên file người dùng tải lên"""
    try:
        uploaded_excel = os.path.join(DATA_DIR, "PhucAn_DuLieuBanHangTho_DaBoSungTruong.xlsx")
        if not os.path.exists(uploaded_excel):
            uploaded_excel = os.path.join(os.path.dirname(os.path.dirname(DATA_DIR)), "PhucAn_DuLieuBanHangTho_DaBoSungTruong.xlsx")
            
        if os.path.exists(uploaded_excel):
            info = engine.load_raw_data(uploaded_excel)
            msg = f"Đã nạp thành công {info['total_rows']:,} dòng từ tệp tải lên: {info['file_name']}!"
        else:
            sample_path = os.path.join(DATA_DIR, "raw_transactions_oct2026.csv")
            info = engine.load_raw_data(sample_path)
            msg = f"Đã nạp thành công {info['total_rows']:,} dòng dữ liệu thô!"
        return jsonify({"success": True, "data": info, "message": msg})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route("/api/load-uploaded", methods=["GET", "POST"])
def load_uploaded_data():
    """Nạp trực tiếp tệp Excel người dùng tải lên"""
    try:
        uploaded_excel = os.path.join(DATA_DIR, "PhucAn_DuLieuBanHangTho_DaBoSungTruong.xlsx")
        if not os.path.exists(uploaded_excel):
            uploaded_excel = os.path.join(os.path.dirname(os.path.dirname(DATA_DIR)), "PhucAn_DuLieuBanHangTho_DaBoSungTruong.xlsx")
        info = engine.load_raw_data(uploaded_excel)
        return jsonify({"success": True, "data": info, "message": f"Đã nạp thành công {info['total_rows']:,} dòng từ tệp {info['file_name']}!"})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route("/api/upload-raw", methods=["POST"])
def upload_raw_data():
    """Upload tệp dữ liệu thô mới (.xlsx, .xls, .csv)"""
    if 'file' not in request.files:
        return jsonify({"success": False, "error": "Không tìm thấy tệp tải lên"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"success": False, "error": "Chưa chọn tệp"}), 400
        
    try:
        orig_filename = file.filename
        _, ext = os.path.splitext(orig_filename)
        ext = ext.lower() if ext else ".csv"
        
        save_path = os.path.join(DATA_DIR, f"uploaded_raw{ext}")
        file.save(save_path)
        info = engine.load_raw_data(save_path)
        info["file_name"] = orig_filename
        engine.active_file_name = orig_filename
        return jsonify({"success": True, "data": info, "message": f"Đã tải lên và nạp thành công {info['total_rows']:,} dòng từ tệp '{orig_filename}'!"})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route("/api/execute-cleaning", methods=["GET", "POST"])
def execute_cleaning():
    """Giai đoạn 1: AI Agent thực hiện làm sạch dữ liệu tự động"""
    try:
        log = engine.execute_data_cleaning()
        return jsonify({"success": True, "data": log, "message": "Đã làm sạch dữ liệu thành công!"})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route("/api/human-verify", methods=["GET", "POST"])
def human_verify():
    """Giai đoạn 1: Con người kiểm tra lại (Human Verification)"""
    data = request.json or request.args or {}
    approved = str(data.get("approved", "true")).lower() in ["true", "1", "yes"]
    notes = data.get("notes", "")
    res = engine.human_verify(approved, notes)
    return jsonify({"success": True, "data": res, "message": "Đã lưu xác thực của chuyên viên!"})

@app.route("/api/cleaned-data-preview", methods=["GET"])
def cleaned_data_preview():
    """Xem trước các dòng dữ liệu sạch và dữ liệu bị loại trừ (Không bao giờ trả về NaN)"""
    if engine.cleaned_df is None:
        if engine.raw_df is not None:
            engine.execute_data_cleaning()
        else:
            engine.load_raw_data()
            engine.execute_data_cleaning()
        
    page = int(request.args.get("page", 1))
    limit = int(request.args.get("limit", 20))
    status_filter = request.args.get("status", "")
    store_filter = request.args.get("store", "")
    mode = request.args.get("mode", "cleaned") # 'cleaned', 'raw', 'excluded'
    
    if mode == "raw" and engine.raw_df is not None:
        df = engine.raw_df
    elif mode == "excluded" and engine.raw_df is not None:
        if engine.cleaned_df is not None:
            cleaned_ids = set(engine.cleaned_df["transaction_id"])
            df = engine.raw_df[~engine.raw_df["transaction_id"].isin(cleaned_ids)]
        else:
            df = engine.raw_df
    else:
        df = engine.cleaned_df if engine.cleaned_df is not None else engine.raw_df
        
    if df is None:
        return jsonify({"success": False, "error": "Chưa có dữ liệu"}), 400
        
    if status_filter and "status" in df.columns:
        df = df[df["status"] == status_filter]
    if store_filter and "store_id" in df.columns:
        df = df[df["store_id"] == store_filter]
        
    total_records = len(df)
    start_idx = (page - 1) * limit
    end_idx = min(start_idx + limit, total_records)
    
    subset_df = df.iloc[start_idx:end_idx].copy().fillna("")
    records = subset_df.to_dict(orient="records")
    
    clean_records = []
    for r in records:
        clean_r = {}
        for k, v in r.items():
            if pd.isna(v) or v is None or (isinstance(v, float) and (np.isnan(v) or np.isinf(v))):
                clean_r[k] = ""
            elif isinstance(v, (int, np.integer)):
                clean_r[k] = int(v)
            elif isinstance(v, (float, np.floating)):
                clean_r[k] = float(v)
            else:
                clean_r[k] = str(v)
        clean_records.append(clean_r)
        
    return jsonify({
        "success": True,
        "total": total_records,
        "page": page,
        "limit": limit,
        "mode": mode,
        "records": clean_records
    })

@app.route("/api/generate-report", methods=["GET", "POST"])
def generate_report():
    """Giai đoạn 2: Tạo Báo cáo Quản trị đa chiều"""
    try:
        rep = engine.generate_management_report()
        return jsonify({"success": True, "data": rep, "message": "Báo cáo Quản trị đã được khởi tạo thành công!"})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route("/api/cross-check-audit", methods=["GET", "POST"])
def cross_check_audit():
    """Giai đoạn 3: Đối chiếu chéo & Phát hiện bất thường & Xếp hạng ưu tiên"""
    try:
        audit = engine.perform_cross_check_audit()
        return jsonify({"success": True, "data": audit, "message": "Kiểm toán đối chiếu hoàn tất!"})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route("/api/chat", methods=["POST"])
def chat():
    """AI Agent Co-pilot Chatbot hỗ trợ Nguyễn Bảo Ngọc"""
    data = request.json or {}
    message = data.get("message", "")
    if not message:
        return jsonify({"success": False, "reply": "Vui lòng nhập câu hỏi."}), 400
        
    try:
        reply = engine.chat_with_agent(message)
        return jsonify({"success": True, "reply": reply})
    except Exception as e:
        return jsonify({"success": False, "reply": f"Lỗi xử lý: {str(e)}"}), 500

@app.route("/api/executive-decision", methods=["POST"])
def executive_decision():
    """Bước 4: Nguyễn Bảo Ngọc ký duyệt Quyết định can thiệp hỗ trợ"""
    data = request.json or {}
    store_ids = data.get("store_ids", [])
    action_plan = data.get("action_plan", "")
    assigned_lead = data.get("assigned_lead", "")
    budget = data.get("budget", 0)
    notes = data.get("notes", "")
    
    if not store_ids:
        return jsonify({"success": False, "error": "Vui lòng chọn ít nhất một cửa hàng cần hỗ trợ"}), 400
        
    try:
        decision = engine.record_executive_decision(store_ids, action_plan, assigned_lead, budget, notes)
        return jsonify({"success": True, "data": decision, "message": f"Đã ban hành Quyết định {decision['decision_id']} thành công!"})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route("/api/decisions-list", methods=["GET"])
def get_decisions():
    """Lấy danh sách các quyết định đã ban hành"""
    return jsonify({"success": True, "data": engine.executive_decisions})

@app.route("/api/feedbacks", methods=["GET"])
def get_feedbacks():
    """Lấy danh sách phản hồi của khách hàng và các chỉ số CSAT"""
    store_id = request.args.get("store_id", "ALL")
    rating = request.args.get("rating", "ALL")
    category = request.args.get("category", "ALL")
    sentiment = request.args.get("sentiment", "ALL")
    feedbacks = engine.get_customer_feedbacks(store_id, rating, category, sentiment)
    summary = engine.get_feedback_summary()
    return jsonify({
        "success": True,
        "summary": summary,
        "feedbacks": feedbacks
    })

@app.route("/api/feedback", methods=["POST"])
def add_feedback():
    """Khách hàng hoặc chuyên viên thêm phản hồi mới"""
    data = request.json or {}
    customer_name = data.get("customer_name", "Khách hàng")
    phone = data.get("phone", "0900000000")
    store_id = data.get("store_id", "ST01")
    rating = data.get("rating", 5)
    category = data.get("category", "Dịch vụ & Tư vấn")
    comment = data.get("comment", "")

    if not comment:
        return jsonify({"success": False, "error": "Vui lòng nhập nội dung phản hồi."}), 400

    new_fb = engine.add_customer_feedback(customer_name, phone, store_id, rating, category, comment)
    return jsonify({
        "success": True,
        "data": new_fb,
        "summary": engine.get_feedback_summary(),
        "message": "Đã lưu phản hồi của khách hàng thành công!"
    })

@app.route("/api/export-cleaned-csv", methods=["GET"])
def export_cleaned_csv():
    """Tải xuống tệp CSV dữ liệu đã làm sạch"""
    cleaned_path = os.path.join(DATA_DIR, "cleaned_transactions_oct2026.csv")
    if not os.path.exists(cleaned_path):
        if engine.cleaned_df is not None:
            engine.cleaned_df.to_csv(cleaned_path, index=False, encoding="utf-8-sig")
        else:
            return "Chưa có dữ liệu làm sạch", 404
            
    return send_file(cleaned_path, mimetype="text/csv", as_attachment=True, download_name="BaoNgoc_Cleaned_Transactions_Oct2026.csv")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5050, debug=False)

