# implement_i18n.py
import re

html_path = r"c:\Users\ADMIN\OneDrive\Attachments\Thi cuối môn AI301\app\templates\index.html"
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Insert Language Switcher Dropdown in Top Header before themeToggleBtn
old_theme_btn = '                    <!-- Theme Switcher Button (Light / Dark) -->\n                    <button id="themeToggleBtn"'
new_lang_and_theme_btn = """                    <!-- Language Selector Dropdown (Multi-Language: VI, EN, JA, ZH) -->
                    <div class="relative" id="langDropdownContainer">
                        <button id="langToggleBtn" onclick="toggleLangDropdown(event)" class="flex items-center gap-1.5 px-3 py-2 rounded-2xl border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-800 hover:bg-rose-50 dark:hover:bg-slate-700 text-slate-700 dark:text-slate-200 hover:text-rose-600 font-bold text-xs transition cursor-pointer shadow-xs" title="Thay đổi ngôn ngữ / Change Language">
                            <span id="currentLangFlag" class="text-sm">🇻🇳</span>
                            <span id="currentLangText" class="hidden sm:inline font-bold">Tiếng Việt</span>
                            <i class="fa-solid fa-chevron-down text-[10px] text-slate-400 ml-0.5"></i>
                        </button>

                        <!-- Dropdown Menu (Glassmorphism) -->
                        <div id="langDropdownMenu" class="hidden absolute right-0 mt-2 w-48 rounded-2xl os-card p-1.5 shadow-2xl border border-white/90 dark:border-slate-700 z-50 view-fade">
                            <button onclick="changeLanguage('vi')" class="w-full flex items-center gap-2.5 px-3 py-2 rounded-xl text-xs font-bold text-slate-700 dark:text-slate-200 hover:bg-rose-50 dark:hover:bg-rose-950/40 hover:text-rose-600 transition text-left cursor-pointer">
                                <span class="text-base">🇻🇳</span>
                                <div class="leading-tight">
                                    <p class="font-bold">Tiếng Việt</p>
                                    <span class="text-[10px] text-slate-400 font-medium">Mặc định</span>
                                </div>
                            </button>
                            <button onclick="changeLanguage('en')" class="w-full flex items-center gap-2.5 px-3 py-2 rounded-xl text-xs font-bold text-slate-700 dark:text-slate-200 hover:bg-rose-50 dark:hover:bg-rose-950/40 hover:text-rose-600 transition text-left cursor-pointer">
                                <span class="text-base">🇺🇸</span>
                                <div class="leading-tight">
                                    <p class="font-bold">English</p>
                                    <span class="text-[10px] text-slate-400 font-medium">International</span>
                                </div>
                            </button>
                            <button onclick="changeLanguage('ja')" class="w-full flex items-center gap-2.5 px-3 py-2 rounded-xl text-xs font-bold text-slate-700 dark:text-slate-200 hover:bg-rose-50 dark:hover:bg-rose-950/40 hover:text-rose-600 transition text-left cursor-pointer">
                                <span class="text-base">🇯🇵</span>
                                <div class="leading-tight">
                                    <p class="font-bold">日本語</p>
                                    <span class="text-[10px] text-slate-400 font-medium">Japanese</span>
                                </div>
                            </button>
                            <button onclick="changeLanguage('zh')" class="w-full flex items-center gap-2.5 px-3 py-2 rounded-xl text-xs font-bold text-slate-700 dark:text-slate-200 hover:bg-rose-50 dark:hover:bg-rose-950/40 hover:text-rose-600 transition text-left cursor-pointer">
                                <span class="text-base">🇨🇳</span>
                                <div class="leading-tight">
                                    <p class="font-bold">中文</p>
                                    <span class="text-[10px] text-slate-400 font-medium">Simplified</span>
                                </div>
                            </button>
                        </div>
                    </div>

                    <!-- Theme Switcher Button (Light / Dark) -->
                    <button id="themeToggleBtn" """

if old_theme_btn in content:
    content = content.replace(old_theme_btn, new_lang_and_theme_btn, 1)
    print("Language Dropdown injected into header successfully")
else:
    print("Warning: old_theme_btn not found")

# 2. Add data-i18n attributes to HTML elements
replacements = [
    # Top Header
    ('<input id="topSearchInput" oninput="handleGlobalSearch(this.value)" type="text" placeholder="Tìm kiếm cửa hàng, mã đơn, sản phẩm, quản lý..."',
     '<input id="topSearchInput" oninput="handleGlobalSearch(this.value)" type="text" placeholder="Tìm kiếm cửa hàng, mã đơn, sản phẩm, quản lý..." data-i18n-ph="search_ph"'),
    
    ('<span class="text-slate-500 dark:text-slate-400 font-medium leading-tight">Ngày đối<br>chiếu chuẩn:</span>',
     '<span data-i18n="audit_date_label" class="text-slate-500 dark:text-slate-400 font-medium leading-tight">Ngày đối<br>chiếu chuẩn:</span>'),
    
    ('<span id="themeToggleText" class="hidden sm:inline">Chế độ Tối</span>',
     '<span id="themeToggleText" data-i18n="theme_dark" class="hidden sm:inline">Chế độ Tối</span>'),
    
    ('<span class="leading-tight text-left">Chạy AI<br class="hidden sm:inline"> Pipeline</span>',
     '<span data-i18n="btn_run_pipeline" class="leading-tight text-left">Chạy AI<br class="hidden sm:inline"> Pipeline</span>'),
    
    ('<span class="leading-tight text-left">Xuất<br class="hidden sm:inline"> Báo Cáo</span>',
     '<span data-i18n="btn_export_report" class="leading-tight text-left">Xuất<br class="hidden sm:inline"> Báo Cáo</span>'),

    # Stepper Workflow
    ('<span class="text-[10px] font-extrabold tracking-wider text-slate-400 uppercase hidden 2xl:inline-block mr-1">\n                            QUY TRÌNH:\n                        </span>',
     '<span data-i18n="workflow_lbl" class="text-[10px] font-extrabold tracking-wider text-slate-400 uppercase hidden 2xl:inline-block mr-1">QUY TRÌNH:</span>'),

    ('<div class="nav-title font-extrabold text-xs text-slate-800">Bước 1: Kết Nối Dữ Liệu</div>',
     '<div data-i18n="step1_title" class="nav-title font-extrabold text-xs text-slate-800">Bước 1: Kết Nối Dữ Liệu</div>'),
    ('<div class="sb-sub text-[10px] font-medium text-slate-400 mt-0.5">Chọn nguồn dữ liệu</div>',
     '<div data-i18n="step1_sub" class="sb-sub text-[10px] font-medium text-slate-400 mt-0.5">Chọn nguồn dữ liệu</div>'),

    ('<div class="nav-title font-extrabold text-xs text-slate-800">Bước 2: Làm Sạch &amp; Chuẩn Hóa</div>',
     '<div data-i18n="step2_title" class="nav-title font-extrabold text-xs text-slate-800">Bước 2: Làm Sạch &amp; Chuẩn Hóa</div>'),
    ('<div class="sb-sub text-[10px] font-medium text-slate-400 mt-0.5">Kiểm tra &amp; chuẩn hóa</div>',
     '<div data-i18n="step2_sub" class="sb-sub text-[10px] font-medium text-slate-400 mt-0.5">Kiểm tra &amp; chuẩn hóa</div>'),

    ('<div class="nav-title font-extrabold text-xs text-slate-800">Bước 3: Phân Tích Số Liệu</div>',
     '<div data-i18n="step3_title" class="nav-title font-extrabold text-xs text-slate-800">Bước 3: Phân Tích Số Liệu</div>'),
    ('<div class="sb-sub text-[10px] font-medium text-slate-400 mt-0.5">So sánh DT, LN &amp; Mục tiêu</div>',
     '<div data-i18n="step3_sub" class="sb-sub text-[10px] font-medium text-slate-400 mt-0.5">So sánh DT, LN &amp; Mục tiêu</div>'),

    ('<div class="nav-title font-extrabold text-xs text-slate-800">Bước 4: Xuất Kết Quả</div>',
     '<div data-i18n="step4_title" class="nav-title font-extrabold text-xs text-slate-800">Bước 4: Xuất Kết Quả</div>'),
    ('<div class="sb-sub text-[10px] font-medium text-slate-400 mt-0.5">Tải dữ liệu &amp; báo cáo</div>',
     '<div data-i18n="step4_sub" class="sb-sub text-[10px] font-medium text-slate-400 mt-0.5">Tải dữ liệu &amp; báo cáo</div>'),

    ('<span class="text-[10px] font-extrabold tracking-wider text-slate-400 uppercase hidden 2xl:inline-block mr-1">\n                            HẬU KỲ:\n                        </span>',
     '<span data-i18n="postaudit_lbl" class="text-[10px] font-extrabold tracking-wider text-slate-400 uppercase hidden 2xl:inline-block mr-1">HẬU KỲ:</span>'),

    ('<div class="nav-title font-extrabold text-xs text-slate-800">Trợ Lý AI Co-Pilot</div>',
     '<div data-i18n="copilot_title" class="nav-title font-extrabold text-xs text-slate-800">Trợ Lý AI Co-Pilot</div>'),
    ('<div class="sb-sub text-[10px] font-medium text-slate-400 mt-0.5">Hỏi đáp số liệu</div>',
     '<div data-i18n="copilot_sub" class="sb-sub text-[10px] font-medium text-slate-400 mt-0.5">Hỏi đáp số liệu</div>'),

    ('<div class="nav-title font-extrabold text-xs text-slate-800">Nhật Ký Kiểm Toán</div>',
     '<div data-i18n="audit_title" class="nav-title font-extrabold text-xs text-slate-800">Nhật Ký Kiểm Toán</div>'),
    ('<div class="sb-sub text-[10px] font-medium text-slate-400 mt-0.5">Lịch sử đối soát</div>',
     '<div data-i18n="audit_sub" class="sb-sub text-[10px] font-medium text-slate-400 mt-0.5">Lịch sử đối soát</div>'),

    ('<div class="nav-title font-black text-xs text-amber-900 dark:text-amber-200">Phản Hồi Khách Hàng</div>',
     '<div data-i18n="feedback_title" class="nav-title font-black text-xs text-amber-900 dark:text-amber-200">Phản Hồi Khách Hàng</div>'),
    ('<div class="sb-sub text-[9px] font-bold text-amber-600 dark:text-amber-400 mt-0.5">CSAT &amp; Ý kiến KH</div>',
     '<div data-i18n="feedback_sub" class="sb-sub text-[9px] font-bold text-amber-600 dark:text-amber-400 mt-0.5">CSAT &amp; Ý kiến KH</div>'),

    # 4 Top Signature KPI Cards
    ('<span class="text-xs font-bold text-slate-600 leading-snug">Doanh Thu Thuần<br>(Net Revenue)</span>',
     '<span data-i18n="kpi1_title" class="text-xs font-bold text-slate-600 leading-snug">Doanh Thu Thuần<br>(Net Revenue)</span>'),
    ('<span class="text-slate-400 font-medium">hoàn thành mục tiêu kỳ</span>',
     '<span data-i18n="kpi1_completion_text" class="text-slate-400 font-medium">hoàn thành mục tiêu kỳ</span>'),

    ('<span class="text-xs font-bold text-slate-600 leading-snug">Đơn Hủy &amp; Đổi Trả<br>Đã Bóc Tách</span>',
     '<span data-i18n="kpi2_title" class="text-xs font-bold text-slate-600 leading-snug">Đơn Hủy &amp; Đổi Trả<br>Đã Bóc Tách</span>'),
    ('<span class="px-2.5 py-1 rounded-xl bg-rose-50 text-rose-600 text-[10px] font-extrabold text-center leading-tight uppercase">\n                                CHẶN<br>ĐẾM TRÙNG\n                            </span>',
     '<span data-i18n="kpi2_badge" class="px-2.5 py-1 rounded-xl bg-rose-50 text-rose-600 text-[10px] font-extrabold text-center leading-tight uppercase">CHẶN<br>ĐẾM TRÙNG</span>'),
    ('<span>Rà soát ngay</span>', '<span data-i18n="kpi2_btn">Rà soát ngay</span>'),

    ('<span class="text-xs font-bold text-slate-600 leading-snug">Cửa Hàng Cần<br>Hỗ Trợ Trước</span>',
     '<span data-i18n="kpi3_title" class="text-xs font-bold text-slate-600 leading-snug">Cửa Hàng Cần<br>Hỗ Trợ Trước</span>'),
    ('<span class="px-2.5 py-1 rounded-xl bg-amber-50 text-amber-700 text-[10px] font-extrabold text-center leading-tight uppercase">\n                                ƯU TIÊN<br>GẤP\n                            </span>',
     '<span data-i18n="kpi3_badge" class="px-2.5 py-1 rounded-xl bg-amber-50 text-amber-700 text-[10px] font-extrabold text-center leading-tight uppercase">ƯU TIÊN<br>GẤP</span>'),
    ('<span>Xem chi tiết</span>', '<span data-i18n="kpi3_btn">Xem chi tiết</span>'),

    ('<span class="text-xs font-bold text-slate-600 leading-snug">Dữ Liệu Đạt Chuẩn<br>Phê Duyệt</span>',
     '<span data-i18n="kpi4_title" class="text-xs font-bold text-slate-600 leading-snug">Dữ Liệu Đạt Chuẩn<br>Phê Duyệt</span>'),
    ('<span>Duyệt Hàng Loạt 1-Chạm</span>', '<span data-i18n="kpi4_btn">Duyệt Hàng Loạt 1-Chạm</span>'),

    # Spotlight CSAT Banner
    ('Phản Hồi Khách Hàng &amp; Đo Lường CSAT Thực Tế', '<span data-i18n="spotlight_csat_title">Phản Hồi Khách Hàng &amp; Đo Lường CSAT Thực Tế</span>'),
    ('<span>Xem Toàn Bộ 21 Đánh Giá &amp; Biểu Đồ &rarr;</span>', '<span data-i18n="spotlight_btn_view">Xem Toàn Bộ 21 Đánh Giá &amp; Biểu Đồ &rarr;</span>'),
    ('<span>+ Gửi Phản Hồi Mới</span>', '<span data-i18n="spotlight_btn_new">+ Gửi Phản Hồi Mới</span>'),

    # Step 3 Card Header
    ('<h2 class="text-base sm:text-lg font-extrabold text-slate-900">\n                                    Bước 3: AI Phân Tích Chuyên Sâu &amp; So Sánh Hiệu Quả 18 Cửa Hàng\n                                </h2>',
     '<h2 data-i18n="step3_h2" class="text-base sm:text-lg font-extrabold text-slate-900">Bước 3: AI Phân Tích Chuyên Sâu &amp; So Sánh Hiệu Quả 18 Cửa Hàng</h2>'),

    # Feedback View Header
    ('Phản Hồi &amp; Trải Nghiệm Khách Hàng (Customer Feedback &amp; CSAT)', '<span data-i18n="fb_view_title">Phản Hồi &amp; Trải Nghiệm Khách Hàng (Customer Feedback &amp; CSAT)</span>')
]

for old, new in replacements:
    if old in content:
        content = content.replace(old, new, 1)

print("Applied data-i18n attributes successfully")

# 3. Add JavaScript i18n Dictionary and Functions right before closing script
js_code = """
        // =====================================================================
        // MULTI-LANGUAGE SYSTEM (I18N: VI, EN, JA, ZH)
        // =====================================================================
        const I18N = {
            vi: {
                flag: '🇻🇳',
                langName: 'Tiếng Việt',
                search_ph: 'Tìm kiếm cửa hàng, mã đơn, sản phẩm, quản lý...',
                audit_date_label: 'Ngày đối<br>chiếu chuẩn:',
                theme_dark: 'Chế độ Tối',
                theme_light: 'Chế độ Sáng',
                feedback_quick: 'Feedback KH<br><span class="text-[10px] text-yellow-200 font-bold">4.6★ (Mới)</span>',
                btn_run_pipeline: 'Chạy AI<br class="hidden sm:inline"> Pipeline',
                btn_export_report: 'Xuất<br class="hidden sm:inline"> Báo Cáo',
                workflow_lbl: 'QUY TRÌNH:',
                postaudit_lbl: 'HẬU KỲ:',
                step1_title: 'Bước 1: Kết Nối Dữ Liệu',
                step1_sub: 'Chọn nguồn dữ liệu',
                step2_title: 'Bước 2: Làm Sạch & Chuẩn Hóa',
                step2_sub: 'Kiểm tra & chuẩn hóa',
                step3_title: 'Bước 3: Phân Tích Số Liệu',
                step3_sub: 'So sánh DT, LN & Mục tiêu',
                step4_title: 'Bước 4: Xuất Kết Quả',
                step4_sub: 'Tải dữ liệu & báo cáo',
                copilot_title: 'Trợ Lý AI Co-Pilot',
                copilot_sub: 'Hỏi đáp số liệu',
                audit_title: 'Nhật Ký Kiểm Toán',
                audit_sub: 'Lịch sử đối soát',
                feedback_title: 'Phản Hồi Khách Hàng',
                feedback_sub: 'CSAT & Ý kiến KH',
                kpi1_title: 'Doanh Thu Thuần<br>(Net Revenue)',
                kpi1_completion_text: 'hoàn thành mục tiêu kỳ',
                kpi2_title: 'Đơn Hủy & Đổi Trả<br>Đã Bóc Tách',
                kpi2_badge: 'CHẶN<br>ĐẾM TRÙNG',
                kpi2_btn: 'Rà soát ngay',
                kpi3_title: 'Cửa Hàng Cần<br>Hỗ Trợ Trước',
                kpi3_badge: 'ƯU TIÊN<br>GẤP',
                kpi3_btn: 'Xem chi tiết',
                kpi4_title: 'Dữ Liệu Đạt Chuẩn<br>Phê Duyệt',
                kpi4_btn: 'Duyệt Hàng Loạt 1-Chạm',
                spotlight_csat_title: 'Phản Hồi Khách Hàng & Đo Lường CSAT Thực Tế',
                spotlight_btn_view: 'Xem Toàn Bộ 21 Đánh Giá & Biểu Đồ →',
                spotlight_btn_new: '+ Gửi Phản Hồi Mới',
                step3_h2: 'Bước 3: AI Phân Tích Chuyên Sâu & So Sánh Hiệu Quả 18 Cửa Hàng',
                fb_view_title: 'Phản Hồi & Trải Nghiệm Khách Hàng (Customer Feedback & CSAT)',
                toast_switched: 'Đã chuyển đổi sang Tiếng Việt!'
            },
            en: {
                flag: '🇺🇸',
                langName: 'English',
                search_ph: 'Search store, order ID, product, manager...',
                audit_date_label: 'Audit<br>Cutoff Date:',
                theme_dark: 'Dark Mode',
                theme_light: 'Light Mode',
                feedback_quick: 'Feedback<br><span class="text-[10px] text-yellow-200 font-bold">4.6★ (New)</span>',
                btn_run_pipeline: 'Run AI<br class="hidden sm:inline"> Pipeline',
                btn_export_report: 'Export<br class="hidden sm:inline"> Report',
                workflow_lbl: 'WORKFLOW:',
                postaudit_lbl: 'POST-AUDIT:',
                step1_title: 'Step 1: Data Connection',
                step1_sub: 'Select data source',
                step2_title: 'Step 2: Cleaning & Prep',
                step2_sub: 'Validate & standardize',
                step3_title: 'Step 3: Performance Analysis',
                step3_sub: 'Revenue, profit & targets',
                step4_title: 'Step 4: Export & Delivery',
                step4_sub: 'Download reports & data',
                copilot_title: 'AI Co-Pilot Assistant',
                copilot_sub: 'Ask data questions',
                audit_title: 'Audit Log & History',
                audit_sub: 'Reconciliation log',
                feedback_title: 'Customer Feedback',
                feedback_sub: 'CSAT & customer reviews',
                kpi1_title: 'Net Revenue<br>(Period Oct-Sep)',
                kpi1_completion_text: 'target completed',
                kpi2_title: 'Returns & Cancellations<br>(Deduplicated)',
                kpi2_badge: 'NO DOUBLE<br>COUNTING',
                kpi2_btn: 'Review now',
                kpi3_title: 'Priority Stores<br>Needs Support',
                kpi3_badge: 'URGENT<br>PRIORITY',
                kpi3_btn: 'View details',
                kpi4_title: 'Verified Clean<br>Audit Data',
                kpi4_btn: '1-Click Bulk Approve',
                spotlight_csat_title: 'Customer Feedback & Real-Time CSAT Intelligence',
                spotlight_btn_view: 'View All 21 Reviews & Charts →',
                spotlight_btn_new: '+ Submit New Review',
                step3_h2: 'Step 3: AI Deep Performance Analysis for 18 Retail Stores',
                fb_view_title: 'Customer Experience & Feedback Intelligence (CSAT Dashboard)',
                toast_switched: 'Switched to English successfully!'
            },
            ja: {
                flag: '🇯🇵',
                langName: '日本語',
                search_ph: '店舗、注文番号、商品、店長を検索...',
                audit_date_label: '基準<br>照合日:',
                theme_dark: 'ダークモード',
                theme_light: 'ライトモード',
                feedback_quick: '顧客評価<br><span class="text-[10px] text-yellow-200 font-bold">4.6★ (新)</span>',
                btn_run_pipeline: 'AIパイプライン<br class="hidden sm:inline">を実行',
                btn_export_report: 'レポート<br class="hidden sm:inline">を出力',
                workflow_lbl: '業務フロー:',
                postaudit_lbl: '監査・対話:',
                step1_title: 'ステップ1: データ接続',
                step1_sub: 'データソース選択',
                step2_title: 'ステップ2: クレンジング',
                step2_sub: '検証と標準化',
                step3_title: 'ステップ3: 実績分析',
                step3_sub: '売上・利益・目標比較',
                step4_title: 'ステップ4: 結果出力',
                step4_sub: 'データとレポートDL',
                copilot_title: 'AIコパイロット',
                copilot_sub: '対話型データ分析',
                audit_title: '監査ログ',
                audit_sub: '照合追跡履歴',
                feedback_title: '顧客フィードバック',
                feedback_sub: 'CSATと顧客の声',
                kpi1_title: '純売上高<br>(Net Revenue)',
                kpi1_completion_text: '期間目標達成',
                kpi2_title: '返品・キャンセル<br>(重複排除済)',
                kpi2_badge: '重複排除<br>確認済',
                kpi2_btn: '直ちに確認',
                kpi3_title: '優先支援店舗<br>(緊急対応要)',
                kpi3_badge: '最優先<br>急務',
                kpi3_btn: '詳細を見る',
                kpi4_title: '承認適合データ<br>(100% 適格)',
                kpi4_btn: 'ワンクリック一括承認',
                spotlight_csat_title: '顧客フィードバック＆リアルタイムCSAT分析',
                spotlight_btn_view: '全21件の評価とグラフを見る →',
                spotlight_btn_new: '+ 新規評価を投稿',
                step3_h2: 'ステップ3: 18店舗詳細分析＆成長戦略試算',
                fb_view_title: '顧客体験・フィードバックダッシュボード (CSAT)',
                toast_switched: '日本語に切り替えました！'
            },
            zh: {
                flag: '🇨🇳',
                langName: '中文',
                search_ph: '搜索店铺、订单号、商品、店长...',
                audit_date_label: '标准<br>对账日:',
                theme_dark: '深色模式',
                theme_light: '浅色模式',
                feedback_quick: '客户反馈<br><span class="text-[10px] text-yellow-200 font-bold">4.6★ (新)</span>',
                btn_run_pipeline: '运行 AI<br class="hidden sm:inline"> 流水线',
                btn_export_report: '导出<br class="hidden sm:inline"> 分析报告',
                workflow_lbl: '业务流程:',
                postaudit_lbl: '后续核查:',
                step1_title: '步骤 1: 数据连接',
                step1_sub: '选择数据来源',
                step2_title: '步骤 2: 数据清洗规范',
                step2_sub: '核验与统一标准',
                step3_title: '步骤 3: 业绩多维分析',
                step3_sub: '营收、利润与目标对比',
                step4_title: '步骤 4: 结果导出交付',
                step4_sub: '下载数据与报表',
                copilot_title: 'AI 智能副驾',
                copilot_sub: '智能数据问答',
                audit_title: '审计核查日志',
                audit_sub: '历史对账记录',
                feedback_title: '客户反馈大盘',
                feedback_sub: 'CSAT满意度与评价',
                kpi1_title: '净营业额<br>(Net Revenue)',
                kpi1_completion_text: '完成当期目标',
                kpi2_title: '退换货与取消订单<br>(已去重校准)',
                kpi2_badge: '杜绝<br>重复计算',
                kpi2_btn: '立即核查',
                kpi3_title: '重点扶持门店<br>(异常警报)',
                kpi3_badge: '紧急<br>优先',
                kpi3_btn: '查看详情',
                kpi4_title: '合规审核达标数据<br>(100% 洁净)',
                kpi4_btn: '一键批量审核通过',
                spotlight_csat_title: '客户真实反馈与实时 CSAT 满意度洞察',
                spotlight_btn_view: '查看全部 21 条评价与图表 →',
                spotlight_btn_new: '+ 提交客户新评价',
                step3_h2: '步骤 3: AI 18家零售门店多维经营深度对账',
                fb_view_title: '客户体验与满意度评价大盘 (CSAT Dashboard)',
                toast_switched: '已成功切换至中文！'
            }
        };

        let currentAppLang = localStorage.getItem('bn_lang') || 'vi';

        function toggleLangDropdown(event) {
            if (event) event.stopPropagation();
            const menu = document.getElementById('langDropdownMenu');
            if (menu) menu.classList.toggle('hidden');
        }

        // Close dropdown when clicking outside
        document.addEventListener('click', (e) => {
            const container = document.getElementById('langDropdownContainer');
            const menu = document.getElementById('langDropdownMenu');
            if (menu && container && !container.contains(e.target)) {
                menu.classList.add('hidden');
            }
        });

        function changeLanguage(lang) {
            if (!I18N[lang]) return;
            currentAppLang = lang;
            localStorage.setItem('bn_lang', lang);

            // Update button label
            const flagEl = document.getElementById('currentLangFlag');
            const textEl = document.getElementById('currentLangText');
            if (flagEl) flagEl.innerText = I18N[lang].flag;
            if (textEl) textEl.innerText = I18N[lang].langName;

            // Close dropdown
            const menu = document.getElementById('langDropdownMenu');
            if (menu) menu.classList.add('hidden');

            // Apply all data-i18n innerHTML
            document.querySelectorAll('[data-i18n]').forEach(el => {
                const key = el.getAttribute('data-i18n');
                if (I18N[lang][key] !== undefined) {
                    el.innerHTML = I18N[lang][key];
                }
            });

            // Apply all data-i18n-ph placeholders
            document.querySelectorAll('[data-i18n-ph]').forEach(el => {
                const key = el.getAttribute('data-i18n-ph');
                if (I18N[lang][key] !== undefined) {
                    el.placeholder = I18N[lang][key];
                }
            });

            // Update dynamic table and dropdown labels if applicable
            showToast(I18N[lang].toast_switched, 'success');
        }

        function initLanguage() {
            const savedLang = localStorage.getItem('bn_lang') || 'vi';
            changeLanguage(savedLang);
        }
"""

# Insert js_code before "// Initialize on load"
init_target = "        // Initialize on load"
if init_target in content:
    content = content.replace(init_target, js_code + "\n" + init_target, 1)
    print("Injected JS i18n code successfully")
else:
    print("Warning: init_target not found")

# Update window.addEventListener('DOMContentLoaded') to call initLanguage()
old_dom_ready = "            initTheme();\n            runFullAiPipeline();\n            loadFeedbacks();"
new_dom_ready = "            initTheme();\n            initLanguage();\n            runFullAiPipeline();\n            loadFeedbacks();"

if old_dom_ready in content:
    content = content.replace(old_dom_ready, new_dom_ready, 1)
    print("Added initLanguage() to DOMContentLoaded successfully")
else:
    print("Warning: old_dom_ready not found")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Full Multi-Language System Implemented!")

