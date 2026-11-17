# update_feedback_visibility.py
import re

html_path = r"c:\Users\ADMIN\OneDrive\Attachments\Thi cuối môn AI301\app\templates\index.html"
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update .nav-tab, .sidebar-link CSS to be more compact
old_css = """        .nav-tab, .sidebar-link {
            display: inline-flex;
            align-items: center;
            gap: 12px;
            padding: 9px 15px;
            border-radius: 20px;
            font-size: 13px;
            font-weight: 600;
            color: #475569;
            background: #ffffff;
            border: 1px solid #fce7ee;
            transition: all 0.24s cubic-bezier(0.2, 0.8, 0.2, 1);
            cursor: pointer;
            user-select: none;
            white-space: nowrap;
        }"""

new_css = """        .nav-tab, .sidebar-link {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            padding: 6px 11px;
            border-radius: 14px;
            font-size: 12px;
            font-weight: 600;
            color: #475569;
            background: #ffffff;
            border: 1px solid #fce7ee;
            transition: all 0.24s cubic-bezier(0.2, 0.8, 0.2, 1);
            cursor: pointer;
            user-select: none;
            white-space: nowrap;
        }"""

if old_css in content:
    content = content.replace(old_css, new_css, 1)
    print("CSS .nav-tab updated successfully")
else:
    print("Warning: old_css not found")

# 1.1 Update .sb-icon size
old_sb_icon = """.sb-icon {
            width: 32px;
            height: 32px;
            border-radius: 10px;"""

new_sb_icon = """.sb-icon {
            width: 26px;
            height: 26px;
            border-radius: 8px;"""

if old_sb_icon in content:
    content = content.replace(old_sb_icon, new_sb_icon, 1)
    print("CSS .sb-icon updated successfully")
else:
    print("Warning: old_sb_icon not found")

# 2. Add Quick Action Feedback Button in Top Header (right before btnRunPipeline)
old_header_btn = """                    <!-- Primary Action: Chạy AI Pipeline -->
                    <button onclick="runFullAiPipeline()" id="btnRunPipeline" class="btn-pink-pill px-4 py-2 text-xs flex items-center gap-2">"""

new_header_btn = """                    <!-- Quick Action: Feedback Khách Hàng (Always Visible on Top Header) -->
                    <button onclick="switchTab('feedback')" class="btn-pink-pill px-3.5 py-2 text-xs flex items-center gap-2 bg-gradient-to-r from-amber-500 via-rose-500 to-pink-500 text-white font-extrabold shadow-md hover:scale-105 transition cursor-pointer" title="Xem Phản Hồi Khách Hàng & CSAT">
                        <i class="fa-solid fa-star text-yellow-300 animate-pulse"></i>
                        <span class="leading-tight text-left">Feedback KH<br><span class="text-[10px] text-yellow-200 font-bold">4.6★ (Mới)</span></span>
                    </button>

                    <!-- Primary Action: Chạy AI Pipeline -->
                    <button onclick="runFullAiPipeline()" id="btnRunPipeline" class="btn-pink-pill px-4 py-2 text-xs flex items-center gap-2">"""

if old_header_btn in content:
    content = content.replace(old_header_btn, new_header_btn, 1)
    print("Top Header Feedback button added successfully")
else:
    print("Warning: old_header_btn not found")

# 3. Enhance the Feedback button in horizontalNavBar with bright badge & gold border
old_nav_feedback = """                        <!-- Phản Hồi Khách Hàng (Feedback) -->
                        <button onclick="switchTab('feedback')" data-nav="feedback" class="nav-tab group">
                            <span class="sb-icon"><i class="fa-solid fa-comments text-xs"></i></span>
                            <div class="text-left leading-tight">
                                <div class="nav-title font-extrabold text-xs text-slate-800">Phản Hồi Khách Hàng</div>
                                <div class="sb-sub text-[10px] font-medium text-slate-400 mt-0.5">CSAT &amp; Ý kiến KH</div>
                            </div>
                            <span id="sbBadgeFeedback" class="sb-badge px-2 py-0.5 text-[10px] font-extrabold rounded-full bg-amber-100 text-amber-700">4.6★</span>
                        </button>"""

new_nav_feedback = """                        <!-- Phản Hồi Khách Hàng (Feedback) - BOLD & ALWAYS VISIBLE -->
                        <button onclick="switchTab('feedback')" data-nav="feedback" class="nav-tab group border-2 border-amber-300 dark:border-amber-600 bg-amber-50/80 dark:bg-amber-950/40 shadow-xs hover:border-rose-400">
                            <span class="sb-icon bg-amber-100 dark:bg-amber-900/60 text-amber-600"><i class="fa-solid fa-star text-xs text-amber-500"></i></span>
                            <div class="text-left leading-tight">
                                <div class="nav-title font-black text-xs text-amber-900 dark:text-amber-200">Phản Hồi Khách Hàng</div>
                                <div class="sb-sub text-[9px] font-bold text-amber-600 dark:text-amber-400 mt-0.5">CSAT &amp; Ý kiến KH</div>
                            </div>
                            <span id="sbBadgeFeedback" class="sb-badge px-2 py-0.5 text-[10px] font-black rounded-full bg-gradient-to-r from-amber-500 to-rose-500 text-white shadow-xs animate-pulse">4.6★ MỚI</span>
                        </button>"""

if old_nav_feedback in content:
    content = content.replace(old_nav_feedback, new_nav_feedback, 1)
    print("Nav bar Feedback button enhanced successfully")
else:
    print("Warning: old_nav_feedback not found")

# 4. Add Customer Feedback Spotlight Banner directly in Step 3 (Main Dashboard)
old_step3_header = """            <section id="step3View" class="view-section view-fade space-y-6">

                <!-- Main Analysis Card (Matches "Bước 2: AI Phân Tích Chuyên Sâu..." in Screenshot) -->"""

new_step3_header = """            <section id="step3View" class="view-section view-fade space-y-6">

                <!-- ⭐ CSAT & CUSTOMER FEEDBACK SPOTLIGHT BANNER (Hiển thị trực tiếp ngay trên Dashboard chính Bước 3) -->
                <div class="os-card p-5 bg-gradient-to-r from-white via-rose-50/40 to-amber-50/50 dark:from-slate-900 dark:via-slate-800/80 dark:to-slate-900 border-2 border-amber-300 dark:border-amber-600/70 shadow-md">
                    <div class="flex flex-col lg:flex-row lg:items-center justify-between gap-4">
                        <!-- Left: CSAT Score & Store Highlights -->
                        <div class="flex items-start gap-4">
                            <div class="w-14 h-14 rounded-2xl bg-gradient-to-br from-amber-400 via-rose-500 to-pink-500 text-white flex flex-col items-center justify-center flex-shrink-0 shadow-md">
                                <span class="text-xl font-black leading-none">4.1★</span>
                                <span class="text-[9px] font-black uppercase tracking-wider mt-0.5">CSAT</span>
                            </div>
                            <div>
                                <div class="flex flex-wrap items-center gap-2">
                                    <h3 class="font-black text-sm sm:text-base text-slate-900 dark:text-white flex items-center gap-1.5">
                                        <i class="fa-solid fa-comments text-amber-500"></i>
                                        Phản Hồi Khách Hàng &amp; Đo Lường CSAT Thực Tế
                                    </h3>
                                    <span class="px-2.5 py-0.5 rounded-full text-[10px] font-black bg-rose-100 text-rose-700 dark:bg-rose-950/60 dark:text-rose-300 border border-rose-200">
                                        21 Đánh Giá Đa Kênh
                                    </span>
                                    <span class="px-2.5 py-0.5 rounded-full text-[10px] font-black bg-emerald-100 text-emerald-700 dark:bg-emerald-950/60 dark:text-emerald-300 border border-emerald-200">
                                        76.2% Hài Lòng
                                    </span>
                                </div>
                                <div class="mt-2.5 grid grid-cols-1 md:grid-cols-2 gap-2 text-xs">
                                    <div class="p-2.5 rounded-xl bg-white/90 dark:bg-slate-800/90 border border-rose-200 dark:border-slate-700 flex items-start gap-2 shadow-2xs">
                                        <i class="fa-solid fa-triangle-exclamation text-rose-500 mt-0.5 text-xs flex-shrink-0"></i>
                                        <div>
                                            <b class="text-rose-600 font-extrabold">ST09 (Bắc Từ Liêm):</b> 
                                            <span class="text-slate-600 dark:text-slate-300">Khách phản ánh móp lon sữa Meiji &amp; Aptamil date cận (còn 2 tháng) &rarr; Giải mã tỷ lệ đổi trả vọt <b class="text-rose-600">14.8%</b>.</span>
                                        </div>
                                    </div>
                                    <div class="p-2.5 rounded-xl bg-white/90 dark:bg-slate-800/90 border border-amber-200 dark:border-slate-700 flex items-start gap-2 shadow-2xs">
                                        <i class="fa-solid fa-box-open text-amber-500 mt-0.5 text-xs flex-shrink-0"></i>
                                        <div>
                                            <b class="text-amber-600 font-extrabold">ST18 (Cần Thơ):</b> 
                                            <span class="text-slate-600 dark:text-slate-300">Khách phàn nàn thiếu bỉm Merries/Moony size M &amp; L vào cuối tuần &rarr; Giải mã mức sụt giảm DT <b class="text-amber-600">-33.9% MoM</b>.</span>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- Right Actions -->
                        <div class="flex flex-wrap sm:flex-nowrap items-center gap-2.5 flex-shrink-0 self-start lg:self-center">
                            <button onclick="switchTab('feedback')" class="btn-pink-pill px-4 py-2.5 text-xs flex items-center gap-2 shadow-md hover:scale-105 transition cursor-pointer font-extrabold">
                                <i class="fa-solid fa-arrow-right-to-bracket"></i>
                                <span>Xem Toàn Bộ 21 Đánh Giá &amp; Biểu Đồ &rarr;</span>
                            </button>
                            <button onclick="openFeedbackModal()" class="btn-outline-clean px-3.5 py-2.5 text-xs flex items-center gap-2 font-bold cursor-pointer hover:border-rose-400">
                                <i class="fa-solid fa-plus text-rose-500"></i>
                                <span>+ Gửi Phản Hồi Mới</span>
                            </button>
                        </div>
                    </div>
                </div>

                <!-- Main Analysis Card (Matches "Bước 2: AI Phân Tích Chuyên Sâu..." in Screenshot) -->"""

if old_step3_header in content:
    content = content.replace(old_step3_header, new_step3_header, 1)
    print("Step 3 CSAT Spotlight banner added successfully")
else:
    print("Warning: old_step3_header not found")

# 5. In switchTab: add smooth scroll to top
old_switch_target = """            const target = document.getElementById(tab + 'View');
            if (target) {
                target.classList.remove('hidden');
                target.classList.remove('view-fade');
                void target.offsetWidth;
                target.classList.add('view-fade');
            }"""

new_switch_target = """            const target = document.getElementById(tab + 'View');
            if (target) {
                target.classList.remove('hidden');
                target.classList.remove('view-fade');
                void target.offsetWidth;
                target.classList.add('view-fade');
                window.scrollTo({ top: 0, behavior: 'smooth' });
            }"""

if old_switch_target in content:
    content = content.replace(old_switch_target, new_switch_target, 1)
    print("switchTab smooth scroll added successfully")
else:
    print("Warning: old_switch_target not found")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated index.html successfully!")

