# apply_glassmorphism.py
import re

html_path = r"c:\Users\ADMIN\OneDrive\Attachments\Thi cuối môn AI301\app\templates\index.html"
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update <body ...> to include Ambient Glowing Orbs and glass setup
old_body_tag = """<body class="min-h-screen flex flex-col">

    <!-- ===================================================================== -->
    <!-- TOP APPLICATION CONTAINER (Full Width, Horizontal Stepper Navigation)  -->
    <!-- ===================================================================== -->
    <div class="flex-1 flex flex-col min-h-screen w-full">"""

new_body_tag = """<body class="min-h-screen flex flex-col relative overflow-x-hidden selection:bg-rose-500 selection:text-white">

    <!-- Ambient Glowing Color Orbs for Real Crystal Glassmorphism Refraction Depth -->
    <div class="fixed inset-0 pointer-events-none overflow-hidden z-0" aria-hidden="true">
        <div class="absolute -top-32 left-[12%] w-[42rem] h-[42rem] rounded-full bg-gradient-to-br from-rose-300/40 to-pink-400/30 dark:from-rose-600/20 dark:to-pink-700/15 blur-[120px] animate-pulse" style="animation-duration: 9s;"></div>
        <div class="absolute top-[28%] -right-28 w-[38rem] h-[38rem] rounded-full bg-gradient-to-bl from-pink-300/35 to-rose-200/40 dark:from-purple-600/18 dark:to-pink-600/15 blur-[130px] animate-pulse" style="animation-duration: 12s;"></div>
        <div class="absolute bottom-16 left-[6%] w-[36rem] h-[36rem] rounded-full bg-gradient-to-tr from-amber-200/40 to-rose-300/35 dark:from-rose-700/18 dark:to-amber-600/15 blur-[110px] animate-pulse" style="animation-duration: 10s;"></div>
    </div>

    <!-- ===================================================================== -->
    <!-- TOP APPLICATION CONTAINER (Full Width, Horizontal Stepper Navigation)  -->
    <!-- ===================================================================== -->
    <div class="flex-1 flex flex-col min-h-screen w-full relative z-10">"""

if old_body_tag in content:
    content = content.replace(old_body_tag, new_body_tag, 1)
    print("Body and Ambient Orbs added successfully")
else:
    print("Warning: old_body_tag not found")

# 2. Update Header class to be translucent frosted glass
old_header_class = '<header class="sticky top-0 z-30 bg-white/95 dark:bg-slate-900/95 backdrop-blur-md border-b border-pink-100 dark:border-slate-800 px-4 sm:px-7 py-3 transition-colors">'
new_header_class = '<header class="sticky top-0 z-30 bg-white/70 dark:bg-slate-900/70 backdrop-blur-2xl border-b border-white/70 dark:border-white/10 px-4 sm:px-7 py-3 transition-colors shadow-xs">'

if old_header_class in content:
    content = content.replace(old_header_class, new_header_class, 1)
    print("Header class updated to glassmorphism")
else:
    print("Warning: old_header_class not found")

# 3. Update Horizontal Nav Bar class to be translucent frosted glass
old_nav_class = '<nav id="horizontalNavBar" class="sticky top-[61px] z-20 bg-white/95 dark:bg-slate-900/95 backdrop-blur-md border-b border-pink-100 dark:border-slate-800 shadow-xs transition-colors">'
new_nav_class = '<nav id="horizontalNavBar" class="sticky top-[61px] z-20 bg-white/65 dark:bg-slate-900/65 backdrop-blur-2xl border-b border-white/60 dark:border-white/10 shadow-xs transition-colors">'

if old_nav_class in content:
    content = content.replace(old_nav_class, new_nav_class, 1)
    print("Nav bar class updated to glassmorphism")
else:
    print("Warning: old_nav_class not found")

# 4. Replace entire <style> block with comprehensive Glassmorphism System
# Find start and end of <style>
style_start = content.find("<style>")
style_end = content.find("</style>")

if style_start != -1 and style_end != -1:
    new_style_block = """<style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&display=swap');

        * { box-sizing: border-box; }
        
        /* Ambient Glass Canvas with Fixed Multi-Radial Gradients */
        body {
            font-family: 'Plus Jakarta Sans', sans-serif;
            background-color: #fce7ee;
            background-image:
                radial-gradient(at 10% 12%, rgba(255, 143, 177, 0.45) 0px, transparent 55%),
                radial-gradient(at 90% 15%, rgba(255, 209, 220, 0.65) 0px, transparent 50%),
                radial-gradient(at 30% 70%, rgba(254, 205, 211, 0.5) 0px, transparent 55%),
                radial-gradient(at 85% 85%, rgba(244, 63, 110, 0.28) 0px, transparent 60%);
            background-attachment: fixed;
            color: #1e293b;
            overflow-x: hidden;
            transition: background-color 0.3s ease, color 0.3s ease;
        }

        /* Dark Mode Theme Rules - Midnight Glass with Neon Rose & Violet */
        html.dark body, body.dark {
            background-color: #0b0f19 !important;
            background-image:
                radial-gradient(at 12% 15%, rgba(244, 63, 110, 0.25) 0px, transparent 55%),
                radial-gradient(at 85% 25%, rgba(139, 92, 246, 0.22) 0px, transparent 50%),
                radial-gradient(at 40% 80%, rgba(225, 29, 90, 0.2) 0px, transparent 55%),
                radial-gradient(at 85% 85%, rgba(56, 189, 248, 0.15) 0px, transparent 50%) !important;
            background-attachment: fixed !important;
            color: #e2e8f0 !important;
        }

        /* Top Header & Horizontal Nav Bar Glass Effect */
        header {
            background: rgba(255, 255, 255, 0.68) !important;
            backdrop-filter: blur(24px) saturate(180%) !important;
            -webkit-backdrop-filter: blur(24px) saturate(180%) !important;
            border-bottom: 1px solid rgba(255, 255, 255, 0.75) !important;
            box-shadow: 0 4px 20px -2px rgba(244, 63, 110, 0.05) !important;
        }
        body.dark header {
            background: rgba(15, 23, 42, 0.68) !important;
            backdrop-filter: blur(24px) saturate(180%) !important;
            -webkit-backdrop-filter: blur(24px) saturate(180%) !important;
            border-bottom: 1px solid rgba(255, 255, 255, 0.08) !important;
            box-shadow: 0 4px 20px -2px rgba(0, 0, 0, 0.3) !important;
        }

        #horizontalNavBar {
            background: rgba(255, 255, 255, 0.62) !important;
            backdrop-filter: blur(24px) saturate(180%) !important;
            -webkit-backdrop-filter: blur(24px) saturate(180%) !important;
            border-bottom: 1px solid rgba(255, 255, 255, 0.75) !important;
            box-shadow: 0 4px 16px -4px rgba(244, 63, 110, 0.04) !important;
        }
        body.dark #horizontalNavBar {
            background: rgba(15, 23, 42, 0.62) !important;
            backdrop-filter: blur(24px) saturate(180%) !important;
            -webkit-backdrop-filter: blur(24px) saturate(180%) !important;
            border-bottom: 1px solid rgba(255, 255, 255, 0.08) !important;
            box-shadow: 0 4px 16px -4px rgba(0, 0, 0, 0.3) !important;
        }

        /* LUXURY CRYSTAL GLASSMORPHISM CARDS (.os-card) */
        .os-card {
            background: rgba(255, 255, 255, 0.68) !important;
            backdrop-filter: blur(22px) saturate(190%) !important;
            -webkit-backdrop-filter: blur(22px) saturate(190%) !important;
            border: 1px solid rgba(255, 255, 255, 0.85) !important;
            border-radius: 24px;
            box-shadow: 0 12px 36px 0 rgba(244, 63, 110, 0.07), inset 0 1px 1px 0 rgba(255, 255, 255, 0.95) !important;
            transition: transform 0.28s cubic-bezier(0.2, 0.8, 0.2, 1), box-shadow 0.28s cubic-bezier(0.2, 0.8, 0.2, 1), border-color 0.25s ease, background-color 0.25s ease;
        }
        .os-card-hover:hover {
            transform: translateY(-3px);
            background: rgba(255, 255, 255, 0.82) !important;
            border-color: rgba(244, 63, 110, 0.35) !important;
            box-shadow: 0 20px 48px -10px rgba(244, 63, 110, 0.18), inset 0 1px 2px 0 rgba(255, 255, 255, 1) !important;
        }

        body.dark .os-card {
            background: rgba(30, 41, 59, 0.6) !important;
            backdrop-filter: blur(22px) saturate(190%) !important;
            -webkit-backdrop-filter: blur(22px) saturate(190%) !important;
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
            box-shadow: 0 12px 36px 0 rgba(0, 0, 0, 0.5), inset 0 1px 1px 0 rgba(255, 255, 255, 0.12) !important;
        }
        body.dark .os-card-hover:hover {
            background: rgba(30, 41, 59, 0.78) !important;
            border-color: rgba(244, 63, 110, 0.5) !important;
            box-shadow: 0 20px 48px -10px rgba(244, 63, 110, 0.3), inset 0 1px 2px 0 rgba(255, 255, 255, 0.2) !important;
        }

        /* NAVIGATION STEPPER TABS - CRYSTAL GLASS PILLS */
        .nav-tab, .sidebar-link {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            padding: 6px 12px;
            border-radius: 16px;
            font-size: 12px;
            font-weight: 600;
            color: #475569;
            background: rgba(255, 255, 255, 0.6) !important;
            backdrop-filter: blur(14px) saturate(160%) !important;
            -webkit-backdrop-filter: blur(14px) saturate(160%) !important;
            border: 1px solid rgba(255, 255, 255, 0.85) !important;
            box-shadow: 0 2px 8px rgba(244, 63, 110, 0.04), inset 0 1px 1px rgba(255, 255, 255, 0.9) !important;
            transition: all 0.24s cubic-bezier(0.2, 0.8, 0.2, 1);
            cursor: pointer;
            user-select: none;
            white-space: nowrap;
        }
        .nav-tab:hover, .sidebar-link:hover {
            background: rgba(255, 241, 245, 0.85) !important;
            color: #e11d5a !important;
            border-color: rgba(244, 63, 110, 0.35) !important;
            transform: translateY(-2px);
            box-shadow: 0 6px 16px -4px rgba(244, 63, 110, 0.2), inset 0 1px 1px rgba(255, 255, 255, 1) !important;
        }
        .nav-tab.active, .sidebar-link.active {
            background: linear-gradient(135deg, rgba(255, 93, 143, 0.95) 0%, rgba(244, 63, 110, 0.95) 60%, rgba(225, 29, 90, 0.98) 100%) !important;
            color: #ffffff !important;
            border-color: rgba(255, 255, 255, 0.45) !important;
            font-weight: 700;
            box-shadow: 0 10px 22px -6px rgba(244, 63, 110, 0.55), inset 0 1px 1px rgba(255, 255, 255, 0.6) !important;
            transform: translateY(-2px);
        }
        .nav-tab.active .nav-title, .sidebar-link.active .nav-title {
            color: #ffffff !important;
        }
        .nav-tab.active .sb-icon, .sidebar-link.active .sb-icon {
            background: rgba(255, 255, 255, 0.24) !important;
            color: #ffffff !important;
        }
        .nav-tab.active .sb-badge, .sidebar-link.active .sb-badge {
            background: rgba(255, 255, 255, 0.26) !important;
            color: #ffffff !important;
        }
        .nav-tab.active .sb-sub, .sidebar-link.active .sb-sub {
            color: rgba(255, 255, 255, 0.88) !important;
        }
        .nav-tab.active i.fa-chevron-right, .sidebar-link.active i.fa-chevron-right {
            color: #ffffff !important;
        }

        body.dark .nav-tab {
            background: rgba(30, 41, 59, 0.5) !important;
            backdrop-filter: blur(14px) !important;
            -webkit-backdrop-filter: blur(14px) !important;
            border-color: rgba(255, 255, 255, 0.08) !important;
            color: #94a3b8 !important;
        }
        body.dark .nav-tab .nav-title {
            color: #f1f5f9;
        }
        body.dark .nav-tab:hover {
            background: rgba(244, 63, 110, 0.2) !important;
            border-color: rgba(244, 63, 110, 0.5) !important;
            color: #fb7185 !important;
        }
        body.dark .nav-tab.active {
            background: linear-gradient(135deg, rgba(255, 93, 143, 0.95) 0%, rgba(244, 63, 110, 0.95) 60%, rgba(225, 29, 90, 0.98) 100%) !important;
            color: #ffffff !important;
            border-color: rgba(255, 255, 255, 0.3) !important;
        }

        .sb-icon {
            width: 26px;
            height: 26px;
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            background: rgba(255, 241, 245, 0.8);
            color: #f43f6e;
            flex-shrink: 0;
            transition: all 0.2s ease;
        }
        body.dark .sb-icon {
            background: rgba(15, 23, 42, 0.6) !important;
            color: #f43f6e !important;
        }

        /* PRIMARY CORAL-PINK PILL BUTTON - FROSTED GLOSS */
        .btn-pink-pill {
            background: linear-gradient(135deg, rgba(255, 93, 143, 0.96) 0%, rgba(244, 63, 110, 0.96) 55%, rgba(225, 29, 90, 0.98) 100%) !important;
            backdrop-filter: blur(12px) !important;
            -webkit-backdrop-filter: blur(12px) !important;
            border: 1px solid rgba(255, 255, 255, 0.35) !important;
            color: #ffffff !important;
            border-radius: 16px;
            font-weight: 700;
            box-shadow: 0 8px 22px -4px rgba(244, 63, 110, 0.55), inset 0 1px 1px rgba(255, 255, 255, 0.45) !important;
            transition: all 0.24s cubic-bezier(0.2, 0.8, 0.2, 1);
        }
        .btn-pink-pill:hover {
            filter: brightness(1.08);
            transform: translateY(-1px);
            box-shadow: 0 12px 28px -4px rgba(244, 63, 110, 0.7), inset 0 1px 2px rgba(255, 255, 255, 0.6) !important;
        }
        .btn-pink-pill:active {
            transform: scale(0.97);
        }

        /* SECONDARY OUTLINED BUTTON - CRYSTAL GLASS */
        .btn-outline-clean {
            background: rgba(255, 255, 255, 0.62) !important;
            backdrop-filter: blur(12px) !important;
            -webkit-backdrop-filter: blur(12px) !important;
            color: #1e293b !important;
            border: 1.5px solid rgba(255, 255, 255, 0.85) !important;
            border-radius: 16px;
            font-weight: 700;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.03), inset 0 1px 1px rgba(255, 255, 255, 0.9) !important;
            transition: all 0.2s ease;
        }
        .btn-outline-clean:hover {
            border-color: #fda4b8 !important;
            background: rgba(255, 245, 248, 0.85) !important;
            color: #e11d5a !important;
            transform: translateY(-1px);
        }
        body.dark .btn-outline-clean {
            background: rgba(30, 41, 59, 0.55) !important;
            color: #e2e8f0 !important;
            border-color: rgba(255, 255, 255, 0.1) !important;
        }
        body.dark .btn-outline-clean:hover {
            border-color: #f43f6e !important;
            background: rgba(244, 63, 110, 0.2) !important;
            color: #fb7185 !important;
        }

        /* INPUTS, SELECTS, DATE PICKERS - FROSTED GLASS */
        input, select, textarea {
            background: rgba(255, 255, 255, 0.6) !important;
            backdrop-filter: blur(12px) !important;
            -webkit-backdrop-filter: blur(12px) !important;
            border: 1px solid rgba(255, 255, 255, 0.85) !important;
            box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.02) !important;
            transition: all 0.2s ease;
        }
        input:focus, select:focus, textarea:focus {
            background: rgba(255, 255, 255, 0.92) !important;
            border-color: rgba(244, 63, 110, 0.5) !important;
            box-shadow: 0 0 0 3px rgba(244, 63, 110, 0.15) !important;
        }
        body.dark input, 
        body.dark select, 
        body.dark textarea {
            background: rgba(15, 23, 42, 0.6) !important;
            backdrop-filter: blur(12px) !important;
            -webkit-backdrop-filter: blur(12px) !important;
            border-color: rgba(255, 255, 255, 0.1) !important;
            color: #f8fafc !important;
        }
        body.dark input:focus, body.dark select:focus, body.dark textarea:focus {
            background: rgba(15, 23, 42, 0.85) !important;
            border-color: rgba(244, 63, 110, 0.6) !important;
            box-shadow: 0 0 0 3px rgba(244, 63, 110, 0.25) !important;
        }

        /* BLUSH TABLE HEADER & ROWS - FROSTED GLASS */
        .table-blush thead tr {
            background: rgba(253, 232, 238, 0.78) !important;
            backdrop-filter: blur(14px) !important;
            -webkit-backdrop-filter: blur(14px) !important;
            color: #475569;
        }
        .table-blush thead th {
            font-size: 11px;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 0.04em;
            padding: 14px 16px;
            color: #334155;
        }
        .table-blush tbody tr {
            border-bottom: 1px solid rgba(253, 242, 245, 0.75);
            transition: background-color 0.18s ease;
        }
        .table-blush tbody tr:hover {
            background-color: rgba(255, 241, 245, 0.65) !important;
        }

        body.dark .table-blush thead tr {
            background: rgba(43, 24, 40, 0.78) !important;
            backdrop-filter: blur(14px) !important;
            -webkit-backdrop-filter: blur(14px) !important;
            color: #f8fafc !important;
        }
        body.dark .table-blush thead th {
            color: #f1f5f9 !important;
        }
        body.dark .table-blush tbody tr {
            border-bottom: 1px solid rgba(255, 255, 255, 0.05) !important;
        }
        body.dark .table-blush tbody tr:hover {
            background-color: rgba(244, 63, 110, 0.12) !important;
        }

        /* MODALS - FROSTED GLASS DIALOGS */
        #decisionModal, #feedbackModal {
            backdrop-filter: blur(14px) !important;
            -webkit-backdrop-filter: blur(14px) !important;
            background: rgba(15, 23, 42, 0.38) !important;
        }
        #decisionModal > div > div, #feedbackModal > div > div {
            background: rgba(255, 255, 255, 0.85) !important;
            backdrop-filter: blur(28px) saturate(190%) !important;
            -webkit-backdrop-filter: blur(28px) saturate(190%) !important;
            border: 1px solid rgba(255, 255, 255, 0.9) !important;
            box-shadow: 0 25px 60px -15px rgba(244, 63, 110, 0.25), inset 0 1px 2px rgba(255, 255, 255, 1) !important;
        }
        body.dark #decisionModal > div > div, body.dark #feedbackModal > div > div {
            background: rgba(30, 41, 59, 0.85) !important;
            backdrop-filter: blur(28px) saturate(190%) !important;
            -webkit-backdrop-filter: blur(28px) saturate(190%) !important;
            border: 1px solid rgba(255, 255, 255, 0.12) !important;
            box-shadow: 0 25px 60px -15px rgba(0, 0, 0, 0.7) !important;
        }

        /* GENERAL DARK MODE PALETTE ADJUSTMENTS */
        body.dark .text-slate-900 { color: #f8fafc !important; }
        body.dark .text-slate-800 { color: #f1f5f9 !important; }
        body.dark .text-slate-700 { color: #e2e8f0 !important; }
        body.dark .text-slate-600 { color: #cbd5e1 !important; }
        body.dark .text-slate-500 { color: #94a3b8 !important; }
        body.dark .text-slate-400 { color: #64748b !important; }

        body.dark input::placeholder {
            color: #64748b !important;
        }

        body.dark .bg-rose-50 {
            background-color: rgba(244, 63, 110, 0.15) !important;
            color: #fb7185 !important;
        }
        body.dark .bg-amber-50 {
            background-color: rgba(245, 158, 11, 0.15) !important;
            color: #fbbf24 !important;
        }
        body.dark .bg-emerald-50 {
            background-color: rgba(16, 185, 129, 0.15) !important;
            color: #34d399 !important;
        }

        body.dark #themeToggleBtn {
            background: rgba(30, 41, 59, 0.6) !important;
            border-color: rgba(255, 255, 255, 0.1) !important;
            color: #f1f5f9 !important;
        }
        body.dark #themeToggleBtn:hover {
            border-color: #fbbf24 !important;
            background-color: rgba(251, 191, 36, 0.15) !important;
            color: #fbbf24 !important;
        }

        body.dark #copilotMessages .bg-white {
            background-color: rgba(15, 23, 42, 0.65) !important;
            border-color: rgba(255, 255, 255, 0.08) !important;
            color: #e2e8f0 !important;
        }

        body.dark #copilotMessages .bg-blush-50 {
            background-color: rgba(244, 63, 110, 0.15) !important;
            border-color: rgba(244, 63, 110, 0.3) !important;
            color: #f1f5f9 !important;
        }

        /* ANIMATIONS & SCROLLBAR */
        .view-fade {
            animation: viewSlideUp 0.38s cubic-bezier(0.16, 1, 0.3, 1);
        }
        @keyframes viewSlideUp {
            from { opacity: 0; transform: translateY(12px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .live-dot {
            box-shadow: 0 0 0 0 rgba(244, 63, 110, 0.7);
            animation: pulsePink 1.8s infinite;
        }
        @keyframes pulsePink {
            70% { box-shadow: 0 0 0 8px rgba(244, 63, 110, 0); }
            100% { box-shadow: 0 0 0 0 rgba(244, 63, 110, 0); }
        }

        /* Custom Frosted Scrollbar */
        .custom-scroll::-webkit-scrollbar { width: 6px; height: 6px; }
        .custom-scroll::-webkit-scrollbar-track { background: transparent; }
        .custom-scroll::-webkit-scrollbar-thumb { background: rgba(251, 207, 232, 0.7); border-radius: 999px; backdrop-filter: blur(4px); }
        .custom-scroll::-webkit-scrollbar-thumb:hover { background: #f472b6; }
        body.dark .custom-scroll::-webkit-scrollbar-thumb { background: rgba(51, 65, 85, 0.7); }
        body.dark .custom-scroll::-webkit-scrollbar-thumb:hover { background: #f43f6e; }

        @media print {
            aside, header, #horizontalNavBar, #toastContainer, .no-print { display: none !important; }
            main { margin-left: 0 !important; padding: 0 !important; }
            .view-section { display: block !important; }
        }
    </style>"""

    content = content[:style_start] + new_style_block + content[style_end + len("</style>"):]
    print("New Glassmorphism Style Block injected successfully")
else:
    print("Error: Could not locate <style> tags")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(content)

print("index.html updated with Glassmorphism System successfully!")

