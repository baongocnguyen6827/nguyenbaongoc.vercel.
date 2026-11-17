# -*- coding: utf-8 -*-
"""
Script to generate the updated app/templates/index.html
with the 4 operational steps replacing Phase 1, 2, 3:
1. Bước 1: Kết nối (chọn nguồn dữ liệu)
2. Bước 2: Làm sạch & Chuẩn hóa (kiểm tra và chuẩn hóa dữ liệu)
3. Bước 3: Phân tích (số liệu)
4. Bước 4: Xuất kết quả (tải dữ liệu và báo cáo)
"""

html_content = '''<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Phúc An Retail - Hệ Thống AI Agent Quản Trị Bán Lẻ & Đối Soát 18 Cửa Hàng</title>
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Font Awesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <!-- Chart.js -->
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <!-- Canvas Confetti -->
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        brand: {
                            50: '#eff6ff',
                            100: '#dbeafe',
                            500: '#3b82f6',
                            600: '#2563eb',
                            700: '#1d4ed8',
                            800: '#1e40af',
                            900: '#1e3a8a',
                        }
                    }
                }
            }
        }
    </script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');
        body { font-family: 'Plus Jakarta Sans', sans-serif; background-color: #f8fafc; }
        .tab-btn.active { border-bottom: 3px solid #2563eb; color: #1d4ed8; font-weight: 700; }
        .custom-scrollbar::-webkit-scrollbar { width: 6px; height: 6px; }
        .custom-scrollbar::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 4px; }
        .animate-pulse-slow { animation: pulse 3s cubic-bezier(0.4, 0, 0.6, 1) infinite; }
    </style>
</head>
<body class="text-slate-800 flex flex-col min-h-screen">

    <!-- Top Header -->
    <header class="bg-gradient-to-r from-blue-900 via-indigo-900 to-slate-900 text-white shadow-lg sticky top-0 z-50">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between items-center h-16">
                <div class="flex items-center space-x-3">
                    <div class="w-10 h-10 rounded-xl bg-blue-500/20 border border-blue-400 flex items-center justify-center text-blue-300 text-xl font-bold">
                        <i class="fa-solid fa-store"></i>
                    </div>
                    <div>
                        <div class="flex items-center space-x-2">
                            <span class="font-bold text-lg tracking-tight">CÔNG TY BÁN LẺ PHÚC AN</span>
                            <span class="text-xs bg-blue-500/30 text-blue-200 px-2 py-0.5 rounded-full border border-blue-400/30 font-medium">Retail BPMN AI Agent</span>
                        </div>
                        <p class="text-xs text-blue-200/80">Hệ thống xử lý ~60.000 dòng giao dịch & Quản trị đối soát 18 cửa hàng</p>
                    </div>
                </div>

                <!-- Roles & Live Status -->
                <div class="flex items-center space-x-4">
                    <div class="hidden md:flex items-center space-x-2 bg-slate-800/80 border border-slate-700 px-3 py-1.5 rounded-lg text-xs">
                        <span class="text-slate-400">Kỳ Báo Cáo:</span>
                        <span class="font-bold text-amber-300">Tháng 10/2026 (31 ngày)</span>
                        <span class="text-slate-500">|</span>
                        <span class="text-slate-400">Kỳ So Sánh:</span>
                        <span class="font-semibold text-slate-300">Tháng 09/2026 (30 ngày)</span>
                    </div>

                    <div class="flex items-center space-x-2 bg-blue-950/60 border border-blue-700/50 px-3 py-1.5 rounded-lg text-xs">
                        <span class="w-2 h-2 rounded-full bg-emerald-400 animate-ping"></span>
                        <span class="text-emerald-300 font-medium" id="agentStatusBadge">AI Agent Sẵn sàng</span>
                    </div>

                    <a href="#quickDecisionModal" onclick="openDecisionModal()" class="bg-gradient-to-r from-emerald-500 to-teal-600 hover:from-emerald-600 hover:to-teal-700 text-white font-medium text-xs px-3.5 py-2 rounded-lg shadow-sm flex items-center space-x-1.5 transition">
                        <i class="fa-solid fa-stamp"></i>
                        <span>Ký Duyệt Hỗ Trợ</span>
                    </a>
                </div>
            </div>
        </div>

        <!-- BPMN 3 Swimlanes Visual Banner -->
        <div class="bg-slate-900/90 border-t border-slate-800 text-xs px-4 py-2">
            <div class="max-w-7xl mx-auto flex flex-wrap justify-between items-center gap-2">
                <div class="flex items-center space-x-2 text-slate-300">
                    <span class="font-bold text-blue-400"><i class="fa-solid fa-diagram-project mr-1"></i> BPMN Lanes:</span>
                    <span class="bg-blue-900/40 border border-blue-700/40 px-2 py-0.5 rounded text-blue-200"><i class="fa-solid fa-user mr-1 text-blue-300"></i> Làn 1: Chuyên Viên Báo Cáo</span>
                    <span class="text-slate-500">→</span>
                    <span class="bg-indigo-900/40 border border-indigo-700/40 px-2 py-0.5 rounded text-indigo-200"><i class="fa-solid fa-robot mr-1 text-indigo-300"></i> Làn 2: AI Agent / API</span>
                    <span class="text-slate-500">→</span>
                    <span class="bg-amber-900/40 border border-amber-700/40 px-2 py-0.5 rounded text-amber-200"><i class="fa-solid fa-user-tie mr-1 text-amber-300"></i> Làn 3: Giám Đốc Kinh Doanh</span>
                </div>
                <div class="flex items-center space-x-3 text-slate-400">
                    <span>18 Cửa hàng Toàn quốc</span>
                    <span>•</span>
                    <span>Quy tắc chuẩn: Net Revenue = Gross - Returns</span>
                </div>
            </div>
        </div>

        <!-- 4 BƯỚC VẬN HÀNH NAVIGATION TABS (THAY THẾ GIAI ĐOẠN 1, 2, 3) -->
        <div class="bg-white border-b border-slate-200 text-slate-600">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex space-x-4 sm:space-x-8 overflow-x-auto">
                <button onclick="switchTab('step1')" id="tabBtnStep1" class="tab-btn active py-3.5 text-xs sm:text-sm font-semibold flex items-center space-x-2 text-blue-600 whitespace-nowrap">
                    <span class="w-6 h-6 rounded-full bg-blue-100 text-blue-700 text-xs flex items-center justify-center font-bold">1</span>
                    <span>Bước 1: Kết Nối (Chọn Nguồn Dữ Liệu)</span>
                    <span id="badgeStep1" class="text-[10px] px-1.5 py-0.5 rounded-full bg-emerald-100 text-emerald-700 font-semibold ml-1">Đã kết nối</span>
                </button>
                <button onclick="switchTab('step2')" id="tabBtnStep2" class="tab-btn py-3.5 text-xs sm:text-sm font-medium flex items-center space-x-2 text-slate-500 hover:text-slate-900 whitespace-nowrap">
                    <span class="w-6 h-6 rounded-full bg-slate-100 text-slate-600 text-xs flex items-center justify-center font-bold">2</span>
                    <span>Bước 2: Làm Sạch & Chuẩn Hóa</span>
                    <span id="badgeStep2" class="text-[10px] px-1.5 py-0.5 rounded-full bg-slate-100 text-slate-500 font-semibold ml-1">Chưa làm sạch</span>
                </button>
                <button onclick="switchTab('step3')" id="tabBtnStep3" class="tab-btn py-3.5 text-xs sm:text-sm font-medium flex items-center space-x-2 text-slate-500 hover:text-slate-900 whitespace-nowrap">
                    <span class="w-6 h-6 rounded-full bg-slate-100 text-slate-600 text-xs flex items-center justify-center font-bold">3</span>
                    <span>Bước 3: Phân Tích (Số Liệu)</span>
                    <span id="badgeStep3" class="text-[10px] px-1.5 py-0.5 rounded-full bg-slate-100 text-slate-500 font-semibold ml-1">Chưa tạo</span>
                </button>
                <button onclick="switchTab('step4')" id="tabBtnStep4" class="tab-btn py-3.5 text-xs sm:text-sm font-medium flex items-center space-x-2 text-slate-500 hover:text-slate-900 whitespace-nowrap">
                    <span class="w-6 h-6 rounded-full bg-slate-100 text-slate-600 text-xs flex items-center justify-center font-bold">4</span>
                    <span>Bước 4: Xuất Kết Quả (Tải Dữ Liệu & Báo Cáo)</span>
                    <span id="badgeStep4" class="text-[10px] px-1.5 py-0.5 rounded-full bg-slate-100 text-slate-500 font-semibold ml-1">Khẩn cấp</span>
                </button>
                <button onclick="switchTab('copilot')" id="tabBtnCopilot" class="tab-btn py-3.5 text-xs sm:text-sm font-medium flex items-center space-x-2 text-slate-500 hover:text-slate-900 ml-auto whitespace-nowrap">
                    <i class="fa-solid fa-wand-magic-sparkles text-indigo-500"></i>
                    <span>AI Co-Pilot Trợ Lý</span>
                </button>
            </div>
        </div>
    </header>

    <!-- Main Content Body -->
    <main class="flex-1 max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-6">

        <!-- 4 BƯỚC VẬN HÀNH PHÂN TÍCH DỮ LIỆU CỦA AI AGENT (Interactive Process Roadmap) -->
        <div class="bg-white rounded-xl p-4 border border-slate-200 shadow-sm mb-6">
            <div class="flex items-center justify-between mb-3 border-b border-slate-100 pb-2">
                <span class="text-xs font-bold text-slate-800 flex items-center">
                    <i class="fa-solid fa-list-check text-blue-600 mr-2 text-sm"></i>
                    4 BƯỚC VẬN HÀNH PHÂN TÍCH DỮ LIỆU CỦA AI AGENT:
                </span>
                <span class="text-[11px] text-slate-400 font-medium">Quy trình tự động hóa khép kín chuẩn BPMN Phúc An Retail (Nhấp từng bước để chuyển nhanh)</span>
            </div>
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3 text-xs">
                <!-- Bước 1 -->
                <div onclick="switchTab('step1')" id="cardNavStep1" class="p-3 rounded-lg border-2 border-blue-600 bg-blue-50/70 cursor-pointer hover:shadow-md transition flex items-start space-x-2.5">
                    <div class="w-6 h-6 rounded-full bg-blue-600 text-white flex items-center justify-center font-bold text-xs flex-shrink-0 shadow-sm">1</div>
                    <div>
                        <span class="font-bold text-blue-900 block">1. Kết Nối</span>
                        <p class="text-slate-600 text-[11px] mt-0.5">Chọn nguồn dữ liệu, tải lên Excel/CSV hoặc dùng tệp 1.006 dòng / 60k dòng thô.</p>
                    </div>
                </div>

                <!-- Bước 2 -->
                <div onclick="switchTab('step2')" id="cardNavStep2" class="p-3 rounded-lg border border-slate-200 bg-slate-50 hover:bg-indigo-50/50 cursor-pointer hover:shadow-md transition flex items-start space-x-2.5">
                    <div class="w-6 h-6 rounded-full bg-indigo-600 text-white flex items-center justify-center font-bold text-xs flex-shrink-0 shadow-sm">2</div>
                    <div>
                        <span class="font-bold text-slate-800 block">2. Làm Sạch & Chuẩn Hóa</span>
                        <p class="text-slate-600 text-[11px] mt-0.5">Kiểm tra và chuẩn hóa dữ liệu: lọc trùng, bỏ đơn hủy, trừ hàng trả, đồng bộ kỳ & xác thực.</p>
                    </div>
                </div>

                <!-- Bước 3 -->
                <div onclick="switchTab('step3')" id="cardNavStep3" class="p-3 rounded-lg border border-slate-200 bg-slate-50 hover:bg-purple-50/50 cursor-pointer hover:shadow-md transition flex items-start space-x-2.5">
                    <div class="w-6 h-6 rounded-full bg-purple-600 text-white flex items-center justify-center font-bold text-xs flex-shrink-0 shadow-sm">3</div>
                    <div>
                        <span class="font-bold text-slate-800 block">3. Phân Tích (Số Liệu)</span>
                        <p class="text-slate-600 text-[11px] mt-0.5">Tính Doanh thu thuần, Giá vốn, Lợi nhuận gộp, % Đạt mục tiêu 18 CH & 4 Biểu đồ trực quan.</p>
                    </div>
                </div>

                <!-- Bước 4 -->
                <div onclick="switchTab('step4')" id="cardNavStep4" class="p-3 rounded-lg border border-slate-200 bg-slate-50 hover:bg-emerald-50/50 cursor-pointer hover:shadow-md transition flex items-start space-x-2.5">
                    <div class="w-6 h-6 rounded-full bg-emerald-600 text-white flex items-center justify-center font-bold text-xs flex-shrink-0 shadow-sm">4</div>
                    <div>
                        <span class="font-bold text-slate-800 block">4. Xuất Kết Quả</span>
                        <p class="text-slate-600 text-[11px] mt-0.5">Tải dữ liệu sạch (CSV), xuất báo cáo quản trị, đối soát 100% & ký duyệt can thiệp.</p>
                    </div>
                </div>
            </div>
        </div>

        <!-- ============================================================== -->
        <!-- BƯỚC 1: KẾT NỐI (CHỌN NGUỒN DỮ LIỆU)                            -->
        <!-- ============================================================== -->
        <div id="step1View" class="space-y-6">
            <!-- Step Header Banner -->
            <div class="bg-white rounded-xl p-5 border border-slate-200 shadow-sm flex flex-col md:flex-row md:items-center justify-between gap-4">
                <div>
                    <div class="flex items-center space-x-2">
                        <span class="px-2.5 py-0.5 bg-blue-100 text-blue-800 text-xs font-bold rounded">BƯỚC 1: KẾT NỐI</span>
                        <h2 class="text-lg font-bold text-slate-800">Kết Nối Nguồn Dữ Liệu Bán Hàng & Đổi Trả (Excel / CSV)</h2>
                    </div>
                    <div class="flex items-center space-x-2 mt-1.5">
                        <span class="px-2 py-0.5 bg-emerald-100 text-emerald-800 text-[11px] font-bold rounded flex items-center">
                            <i class="fa-solid fa-file-excel mr-1 text-emerald-600"></i> Đang kết nối: <span id="activeFileNameBadge" class="ml-1 underline font-mono">PhucAn_DuLieuBanHangTho_DaBoSungTruong.xlsx</span>
                        </span>
                        <span class="text-xs text-slate-400">|</span>
                        <span class="text-xs text-slate-500">18 Cửa hàng Phúc An • 20 Nhóm sản phẩm • Tháng 10/2026 vs Tháng 09/2026</span>
                    </div>
                </div>
                <div class="flex flex-wrap items-center gap-2">
                    <button onclick="loadUploadedData()" id="btnLoadUploaded" class="bg-emerald-600 hover:bg-emerald-700 text-white font-medium text-xs px-3.5 py-2.5 rounded-lg shadow-sm flex items-center space-x-2 transition">
                        <i class="fa-solid fa-file-circle-check"></i>
                        <span>Nạp File Tải Lên (.xlsx)</span>
                    </button>
                    <button onclick="loadSampleData()" id="btnLoadSample" class="bg-blue-600 hover:bg-blue-700 text-white font-medium text-xs px-3.5 py-2.5 rounded-lg shadow-sm flex items-center space-x-2 transition">
                        <i class="fa-solid fa-database"></i>
                        <span>Nạp File Mẫu 60k Dòng</span>
                    </button>
                    <button onclick="switchTab('step2')" class="bg-gradient-to-r from-indigo-600 to-blue-600 hover:from-indigo-700 hover:to-blue-700 text-white font-semibold text-xs px-4 py-2.5 rounded-lg shadow-sm flex items-center space-x-1.5 transition">
                        <span>Sang Bước 2: Làm Sạch & Chuẩn Hóa</span>
                        <i class="fa-solid fa-arrow-right"></i>
                    </button>
                </div>
            </div>

            <!-- Interactive File Upload Box (Kéo thả hoặc Duyệt tệp trực tiếp trên Web) -->
            <div class="bg-white rounded-xl p-5 border border-slate-200 shadow-sm space-y-4">
                <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-100 pb-3">
                    <div class="flex items-center space-x-2">
                        <div class="w-8 h-8 rounded-lg bg-blue-50 text-blue-600 flex items-center justify-center font-bold">
                            <i class="fa-solid fa-cloud-arrow-up text-base"></i>
                        </div>
                        <div>
                            <h3 class="font-bold text-sm text-slate-800">Tải Lên Tệp Dữ Liệu Bán Hàng & Đổi Trả (Excel / CSV)</h3>
                            <p class="text-xs text-slate-500">Chấp nhận tệp định dạng .xlsx, .xls, .csv từ máy tính của bạn</p>
                        </div>
                    </div>
                    <span class="text-xs text-slate-400 font-mono">Dung lượng tối đa: 100MB</span>
                </div>

                <!-- Drag & Drop Zone -->
                <div id="dropZone" ondragover="handleDragOver(event)" ondragleave="handleDragLeave(event)" ondrop="handleFileDrop(event)" onclick="triggerFileInput()" class="border-2 border-dashed border-blue-300 hover:border-blue-500 bg-blue-50/40 hover:bg-blue-50/70 rounded-xl p-6 text-center cursor-pointer transition flex flex-col items-center justify-center space-y-2">
                    <input type="file" id="fileUploadInput" accept=".xlsx,.xls,.csv" onchange="handleFileSelected(event)" class="hidden">
                    <div class="w-12 h-12 rounded-full bg-blue-100 text-blue-600 flex items-center justify-center text-xl shadow-inner">
                        <i class="fa-solid fa-file-arrow-up"></i>
                    </div>
                    <div>
                        <p class="font-bold text-xs text-slate-800">Kéo và thả tệp Excel / CSV vào đây hoặc <span class="text-blue-600 underline">nhấp để duyệt tệp từ máy tính</span></p>
                        <p class="text-[11px] text-slate-500 mt-0.5">Hệ thống tự động nhận diện các cột (Mã đơn, Ngày GD, Cửa hàng, Sản phẩm, Trạng thái, Hoàn tiền...)</p>
                    </div>
                    <div id="selectedFileInfo" class="hidden mt-2 p-2 px-3 bg-white border border-blue-200 rounded-lg shadow-sm flex items-center space-x-3 text-xs">
                        <i class="fa-solid fa-file-excel text-emerald-600 text-base" id="selectedFileIcon"></i>
                        <span id="selectedFileName" class="font-semibold text-slate-800">--</span>
                        <span id="selectedFileSize" class="text-slate-400 font-mono text-[11px]">--</span>
                        <button type="button" onclick="cancelSelectedFile(event)" class="text-slate-400 hover:text-rose-500 ml-2">
                            <i class="fa-solid fa-xmark"></i>
                        </button>
                    </div>
                </div>

                <!-- Upload Action Row -->
                <div class="flex flex-wrap items-center justify-between gap-3 pt-1">
                    <div class="flex items-center space-x-2 text-xs text-slate-500">
                        <i class="fa-solid fa-circle-info text-blue-500"></i>
                        <span>Sau khi tải lên thành công, bạn có thể xem trước dữ liệu thô và chuyển sang Bước 2 để chuẩn hóa.</span>
                    </div>
                    <div class="flex items-center space-x-2">
                        <button type="button" onclick="uploadSelectedFile()" id="btnUploadSubmit" class="bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-700 hover:to-indigo-700 text-white font-semibold text-xs px-5 py-2.5 rounded-lg shadow-sm flex items-center space-x-2 transition opacity-50 cursor-not-allowed" disabled>
                            <i class="fa-solid fa-upload"></i>
                            <span>Tải Lên & Kết Nối Nguồn Dữ Liệu</span>
                        </button>
                    </div>
                </div>
            </div>

            <!-- Stats Overview Card Của Nguồn Dữ Liệu Kết Nối -->
            <div class="grid grid-cols-1 md:grid-cols-4 gap-4">
                <div class="bg-white rounded-xl p-4 border border-slate-200 shadow-sm">
                    <div class="flex justify-between items-center text-slate-500 text-xs">
                        <span>Tổng số dòng thô kết nối</span>
                        <i class="fa-solid fa-database text-blue-500"></i>
                    </div>
                    <div class="text-2xl font-bold text-slate-800 mt-2" id="statRawRows">--</div>
                    <div class="text-xs text-slate-500 mt-1" id="statRawRevenue">Doanh thu thô: --</div>
                </div>

                <div class="bg-white rounded-xl p-4 border border-slate-200 shadow-sm">
                    <div class="flex justify-between items-center text-slate-500 text-xs">
                        <span>Phạm vi mạng lưới</span>
                        <i class="fa-solid fa-shop text-indigo-500"></i>
                    </div>
                    <div class="text-2xl font-bold text-indigo-700 mt-2">18 Cửa hàng</div>
                    <div class="text-xs text-indigo-600 mt-1">Hà Nội, TP.HCM & các tỉnh</div>
                </div>

                <div class="bg-white rounded-xl p-4 border border-slate-200 shadow-sm">
                    <div class="flex justify-between items-center text-slate-500 text-xs">
                        <span>Danh mục sản phẩm</span>
                        <i class="fa-solid fa-boxes-stacked text-purple-500"></i>
                    </div>
                    <div class="text-2xl font-bold text-purple-700 mt-2">20 Sản phẩm</div>
                    <div class="text-xs text-purple-600 mt-1">Đã gắn giá vốn & biên lãi</div>
                </div>

                <div class="bg-white rounded-xl p-4 border border-slate-200 shadow-sm">
                    <div class="flex justify-between items-center text-slate-500 text-xs">
                        <span>Trạng thái kết nối API</span>
                        <i class="fa-solid fa-circle-check text-emerald-500"></i>
                    </div>
                    <div class="text-2xl font-bold text-emerald-600 mt-2" id="statApiConnected">Sẵn sàng</div>
                    <div class="text-xs text-emerald-700 mt-1">Kỳ T10/2026 vs T09/2026</div>
                </div>
            </div>

            <!-- Bảng Xem Trước Dữ Liệu Thô (Raw Data Preview Table) -->
            <div class="bg-white rounded-xl border border-slate-200 shadow-sm p-5 space-y-4">
                <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-100 pb-3">
                    <div class="flex items-center space-x-2">
                        <i class="fa-solid fa-table text-blue-600 text-base"></i>
                        <div>
                            <h3 class="font-bold text-slate-800 text-sm">Xem Trước Dữ Liệu Thô Vừa Kết Nối</h3>
                            <p class="text-[11px] text-slate-500">Dữ liệu giao dịch gốc từ nguồn trước khi thực hiện làm sạch & chuẩn hóa</p>
                        </div>
                    </div>
                    
                    <div class="flex items-center space-x-2">
                        <button onclick="loadDataPreview('raw', 1)" class="px-3 py-1.5 rounded-lg text-xs font-bold bg-slate-800 text-white shadow-sm transition">
                            <i class="fa-solid fa-rotate mr-1"></i> Làm Mới Bảng
                        </button>
                    </div>
                </div>

                <!-- Table Header with count and pagination -->
                <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 text-xs">
                    <span class="font-semibold text-slate-700" id="previewTotalCountStep1">Đang tải dữ liệu nguồn...</span>
                    
                    <div class="flex items-center space-x-2">
                        <div class="flex items-center space-x-1">
                            <button onclick="prevPreviewPage()" class="px-2.5 py-1 rounded border border-slate-300 text-slate-600 hover:bg-slate-100 disabled:opacity-40 disabled:cursor-not-allowed">
                                <i class="fa-solid fa-chevron-left"></i>
                            </button>
                            <span id="previewPageIndicatorStep1" class="px-2 py-1 text-slate-600 font-mono text-[11px]">Trang 1 / 1</span>
                            <button onclick="nextPreviewPage()" class="px-2.5 py-1 rounded border border-slate-300 text-slate-600 hover:bg-slate-100 disabled:opacity-40 disabled:cursor-not-allowed">
                                <i class="fa-solid fa-chevron-right"></i>
                            </button>
                        </div>
                    </div>
                </div>

                <div class="overflow-x-auto custom-scrollbar border border-slate-200 rounded-lg max-h-96">
                    <table class="w-full text-left text-xs text-slate-600">
                        <thead class="bg-slate-100 text-slate-700 font-bold uppercase tracking-wider sticky top-0 z-10">
                            <tr>
                                <th class="py-2.5 px-3">Mã Đơn</th>
                                <th class="py-2.5 px-3">Ngày GD</th>
                                <th class="py-2.5 px-3">Mã CH</th>
                                <th class="py-2.5 px-3">Tên Cửa Hàng</th>
                                <th class="py-2.5 px-3">Sản Phẩm</th>
                                <th class="py-2.5 px-3 text-center">SL</th>
                                <th class="py-2.5 px-3 text-right">Thành Tiền</th>
                                <th class="py-2.5 px-3 text-center">Trạng Thái</th>
                                <th class="py-2.5 px-3">Ghi Chú / Lý Do</th>
                            </tr>
                        </thead>
                        <tbody id="previewTableBodyStep1" class="divide-y divide-slate-200 font-mono">
                            <tr>
                                <td colspan="9" class="text-center py-6 text-slate-400 font-sans">
                                    <i class="fa-solid fa-spinner fa-spin mr-2"></i> Đang tải dữ liệu...
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>

                <!-- Next Step Action Card -->
                <div class="pt-2 flex justify-end">
                    <button onclick="switchTab('step2')" class="bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-700 hover:to-indigo-700 text-white font-bold text-xs px-6 py-3 rounded-xl shadow-md flex items-center space-x-2 transition">
                        <span>Tiếp Tục Sang Bước 2: Làm Sạch & Chuẩn Hóa Dữ Liệu</span>
                        <i class="fa-solid fa-arrow-right"></i>
                    </button>
                </div>
            </div>
        </div>

        <!-- ============================================================== -->
        <!-- BƯỚC 2: LÀM SẠCH & CHUẨN HÓA (KIỂM TRA & CHUẨN HÓA DỮ LIỆU)    -->
        <!-- ============================================================== -->
        <div id="step2View" class="hidden space-y-6">
            <!-- Step Header Banner -->
            <div class="bg-white rounded-xl p-5 border border-slate-200 shadow-sm flex flex-col md:flex-row md:items-center justify-between gap-4">
                <div>
                    <div class="flex items-center space-x-2">
                        <span class="px-2.5 py-0.5 bg-indigo-100 text-indigo-800 text-xs font-bold rounded">BƯỚC 2: LÀM SẠCH & CHUẨN HÓA</span>
                        <h2 class="text-lg font-bold text-slate-800">Kiểm Tra, Chuẩn Hóa Dữ Liệu Tự Động & Xác Thực Con Người</h2>
                    </div>
                    <p class="text-xs text-slate-500 mt-1">
                        Áp dụng các quy tắc tự động: RULE-DEDUP (lọc trùng lặp), RULE-PERIOD-SYNC (đồng bộ kỳ T10 vs T9), RULE-CANCEL (loại đơn hủy), RULE-RETURN (chuẩn hóa đổi trả & giá vốn kho).
                    </p>
                </div>
                <div class="flex flex-wrap items-center gap-2">
                    <button onclick="executeCleaning()" id="btnExecuteClean" class="bg-indigo-600 hover:bg-indigo-700 text-white font-medium text-xs px-4 py-2.5 rounded-lg shadow-sm flex items-center space-x-2 transition">
                        <i class="fa-solid fa-filter"></i>
                        <span>AI Agent Làm Sạch Dữ Liệu</span>
                    </button>
                    <a href="/api/export-cleaned-csv" id="btnExportCleaned" class="bg-emerald-600 hover:bg-emerald-700 text-white font-medium text-xs px-3.5 py-2.5 rounded-lg shadow-sm flex items-center space-x-1.5 transition opacity-50 pointer-events-none">
                        <i class="fa-solid fa-file-arrow-down"></i>
                        <span>Xuất Sheets Sạch (CSV)</span>
                    </a>
                    <button onclick="switchTab('step3')" class="bg-gradient-to-r from-purple-600 to-indigo-600 hover:from-purple-700 hover:to-indigo-700 text-white font-semibold text-xs px-4 py-2.5 rounded-lg shadow-sm flex items-center space-x-1.5 transition">
                        <span>Sang Bước 3: Phân Tích</span>
                        <i class="fa-solid fa-arrow-right"></i>
                    </button>
                </div>
            </div>

            <!-- Stats Overview Cards Sau Khi Làm Sạch -->
            <div class="grid grid-cols-1 md:grid-cols-4 gap-4">
                <div class="bg-white rounded-xl p-4 border border-slate-200 shadow-sm">
                    <div class="flex justify-between items-center text-slate-500 text-xs">
                        <span>Tổng dòng thô ban đầu</span>
                        <i class="fa-solid fa-database text-blue-500"></i>
                    </div>
                    <div class="text-2xl font-bold text-slate-800 mt-2" id="statRawRowsStep2">--</div>
                    <div class="text-xs text-slate-500 mt-1" id="statRawRevenueStep2">Doanh thu thô: --</div>
                </div>

                <div class="bg-white rounded-xl p-4 border border-slate-200 shadow-sm">
                    <div class="flex justify-between items-center text-slate-500 text-xs">
                        <span>Đơn trùng & Lệch kỳ đã loại</span>
                        <i class="fa-solid fa-filter-circle-xmark text-amber-500"></i>
                    </div>
                    <div class="text-2xl font-bold text-amber-600 mt-2" id="statRemovedRows">--</div>
                    <div class="text-xs text-amber-700 mt-1" id="statRemovedValue">Giá trị loại trừ: --</div>
                </div>

                <div class="bg-white rounded-xl p-4 border border-slate-200 shadow-sm">
                    <div class="flex justify-between items-center text-slate-500 text-xs">
                        <span>Đơn Hủy & Đổi Trả đã xử lý</span>
                        <i class="fa-solid fa-arrow-rotate-left text-rose-500"></i>
                    </div>
                    <div class="text-2xl font-bold text-rose-600 mt-2" id="statCancelReturn">--</div>
                    <div class="text-xs text-rose-700 mt-1" id="statReturnImpact">Khấu trừ doanh thu: --</div>
                </div>

                <div class="bg-white rounded-xl p-4 border border-slate-200 shadow-sm">
                    <div class="flex justify-between items-center text-slate-500 text-xs">
                        <span>Dữ liệu sạch chốt (Sheet Sạch)</span>
                        <i class="fa-solid fa-circle-check text-emerald-500"></i>
                    </div>
                    <div class="text-2xl font-bold text-emerald-600 mt-2" id="statCleanedRows">--</div>
                    <div class="text-xs text-emerald-700 mt-1" id="statNetRevP1">Doanh thu thuần: --</div>
                </div>
            </div>

            <!-- Cleaning Audit Logs & Human Verification Panel -->
            <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
                <!-- Log chi tiết của Agent -->
                <div class="lg:col-span-2 bg-white rounded-xl border border-slate-200 shadow-sm p-5 space-y-4">
                    <div class="flex justify-between items-center border-b border-slate-100 pb-3">
                        <div class="flex items-center space-x-2">
                            <i class="fa-solid fa-microchip text-indigo-600"></i>
                            <h3 class="font-bold text-slate-800 text-sm">Nhật Ký Kiểm Toán Làm Sạch Dữ Liệu Của AI Agent</h3>
                        </div>
                        <span id="cleanTimestamp" class="text-xs text-slate-400">Chưa kích hoạt</span>
                    </div>

                    <div class="space-y-3" id="cleaningLogContainer">
                        <div class="p-4 rounded-lg bg-slate-50 border border-slate-200 text-center text-slate-500 text-xs py-8">
                            <i class="fa-solid fa-filter text-2xl text-slate-400 mb-2"></i>
                            <p>Nhấn nút <b>"AI Agent Làm Sạch Dữ Liệu"</b> để thực thi 4 quy tắc kế toán chuẩn hóa.</p>
                        </div>
                    </div>

                    <!-- Cleaned Data Export link -->
                    <div class="flex items-center justify-between pt-2">
                        <a href="/api/export-cleaned-csv" class="text-xs text-blue-600 hover:text-blue-800 font-semibold flex items-center space-x-1.5">
                            <i class="fa-solid fa-file-arrow-down"></i>
                            <span>Tải xuống Sheets Dữ Liệu Sạch (CSV)</span>
                        </a>
                        <span class="text-xs text-slate-400">Tuân thủ chuẩn kế toán bán lẻ: Net = Gross - Returns</span>
                    </div>
                </div>

                <!-- Human Verification Panel (Làn 1: Chuyên viên) -->
                <div class="bg-gradient-to-br from-slate-50 to-blue-50/50 rounded-xl border border-blue-200/80 shadow-sm p-5 flex flex-col justify-between">
                    <div>
                        <div class="flex items-center space-x-2 border-b border-blue-200 pb-3">
                            <div class="w-7 h-7 rounded-full bg-blue-600 text-white flex items-center justify-center text-xs font-bold">
                                <i class="fa-solid fa-user-check"></i>
                            </div>
                            <div>
                                <h3 class="font-bold text-slate-800 text-sm">Human Verification</h3>
                                <p class="text-[11px] text-slate-500">Chuyên viên Báo cáo kiểm tra & phê duyệt</p>
                            </div>
                        </div>

                        <div class="mt-4 space-y-3 text-xs">
                            <div class="p-3 bg-white rounded-lg border border-slate-200">
                                <span class="text-slate-500 block">Trạng thái xác thực:</span>
                                <div class="mt-1 font-bold text-sm" id="hvStatusDisplay">
                                    <span class="text-slate-400">Chờ dữ liệu làm sạch...</span>
                                </div>
                            </div>

                            <div class="space-y-1">
                                <label class="font-semibold text-slate-700">Ghi chú đối soát của Chuyên viên:</label>
                                <textarea id="hvNotes" rows="3" class="w-full text-xs p-2.5 rounded-lg border border-slate-300 focus:ring-2 focus:ring-blue-500 focus:outline-none" placeholder="Nhập nhận xét kiểm tra...">Đã kiểm tra đối chiếu các dòng loại trừ: Không phát hiện đơn giao thành công bị huỷ nhầm. Dữ liệu chuẩn xác để tiến hành Phân tích số liệu.</textarea>
                            </div>
                        </div>
                    </div>

                    <div class="mt-6 pt-4 border-t border-blue-200/60 space-y-2">
                        <button onclick="submitHumanVerification(true)" id="btnApproveHV" class="w-full bg-emerald-600 hover:bg-emerald-700 text-white font-semibold text-xs py-2.5 rounded-lg shadow-sm flex items-center justify-center space-x-2 transition opacity-50 cursor-not-allowed" disabled>
                            <i class="fa-solid fa-circle-check"></i>
                            <span>Con Người Xác Nhận: Dữ Liệu OK</span>
                        </button>
                        <button onclick="submitHumanVerification(false)" id="btnRejectHV" class="w-full bg-slate-200 hover:bg-slate-300 text-slate-700 font-semibold text-xs py-2 rounded-lg flex items-center justify-center space-x-2 transition opacity-50 cursor-not-allowed" disabled>
                            <i class="fa-solid fa-circle-xmark"></i>
                            <span>Dữ Liệu Chưa Đạt - Yêu Cầu Lọc Lại</span>
                        </button>
                    </div>
                </div>
            </div>

            <!-- Interactive Data Table (Bảng Dữ Liệu Chi Tiết: Sạch / Thô / Loại Trừ) -->
            <div class="bg-white rounded-xl border border-slate-200 shadow-sm p-5 space-y-4">
                <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-100 pb-3">
                    <div class="flex items-center space-x-2">
                        <i class="fa-solid fa-table-list text-indigo-600 text-base"></i>
                        <div>
                            <h3 class="font-bold text-slate-800 text-sm">Bảng Dữ Liệu Chi Tiết Sau Chuẩn Hóa</h3>
                            <p class="text-[11px] text-slate-500">Xem trực tiếp từng dòng giao dịch theo các chế độ lọc</p>
                        </div>
                    </div>
                    
                    <!-- View Mode Tabs -->
                    <div class="flex items-center space-x-1.5 bg-slate-100 p-1 rounded-lg">
                        <button onclick="loadDataPreview('cleaned', 1)" id="btnModeCleaned" class="px-3 py-1.5 rounded-lg text-xs font-bold bg-blue-600 text-white shadow-sm transition">
                            <i class="fa-solid fa-filter mr-1"></i> Dữ Liệu Đã Làm Sạch
                        </button>
                        <button onclick="loadDataPreview('raw', 1)" id="btnModeRaw" class="px-3 py-1.5 rounded-lg text-xs font-semibold text-slate-600 hover:bg-white transition">
                            <i class="fa-solid fa-database mr-1"></i> Dữ Liệu Thô Đầy Đủ
                        </button>
                        <button onclick="loadDataPreview('excluded', 1)" id="btnModeExcluded" class="px-3 py-1.5 rounded-lg text-xs font-semibold text-slate-600 hover:bg-white transition">
                            <i class="fa-solid fa-ban mr-1"></i> Các Dòng Bị Loại Trừ
                        </button>
                    </div>
                </div>

                <!-- Table Header with count and pagination -->
                <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 text-xs">
                    <span class="font-semibold text-slate-700" id="previewTotalCount">Đang tải dữ liệu...</span>
                    
                    <div class="flex items-center space-x-2">
                        <div class="flex items-center space-x-1">
                            <button onclick="prevPreviewPage()" id="btnPrevPreview" class="px-2.5 py-1 rounded border border-slate-300 text-slate-600 hover:bg-slate-100 disabled:opacity-40 disabled:cursor-not-allowed">
                                <i class="fa-solid fa-chevron-left"></i>
                            </button>
                            <span id="previewPageIndicator" class="px-2 py-1 text-slate-600 font-mono text-[11px]">Trang 1 / 1</span>
                            <button onclick="nextPreviewPage()" id="btnNextPreview" class="px-2.5 py-1 rounded border border-slate-300 text-slate-600 hover:bg-slate-100 disabled:opacity-40 disabled:cursor-not-allowed">
                                <i class="fa-solid fa-chevron-right"></i>
                            </button>
                        </div>
                    </div>
                </div>

                <div class="overflow-x-auto custom-scrollbar border border-slate-200 rounded-lg max-h-96">
                    <table class="w-full text-left text-xs text-slate-600">
                        <thead class="bg-slate-100 text-slate-700 font-bold uppercase tracking-wider sticky top-0 z-10">
                            <tr>
                                <th class="py-2.5 px-3">Mã Đơn</th>
                                <th class="py-2.5 px-3">Ngày GD</th>
                                <th class="py-2.5 px-3">Mã CH</th>
                                <th class="py-2.5 px-3">Tên Cửa Hàng</th>
                                <th class="py-2.5 px-3">Sản Phẩm</th>
                                <th class="py-2.5 px-3 text-center">SL</th>
                                <th class="py-2.5 px-3 text-right">Thành Tiền</th>
                                <th class="py-2.5 px-3 text-center">Trạng Thái</th>
                                <th class="py-2.5 px-3">Ghi Chú / Lý Do</th>
                            </tr>
                        </thead>
                        <tbody id="previewTableBody" class="divide-y divide-slate-200 font-mono">
                            <tr>
                                <td colspan="9" class="text-center py-6 text-slate-400 font-sans">
                                    <i class="fa-solid fa-spinner fa-spin mr-2"></i> Đang tải dữ liệu...
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>

                <!-- Next Step Action Card -->
                <div class="pt-2 flex justify-end">
                    <button onclick="switchTab('step3')" class="bg-gradient-to-r from-purple-600 to-indigo-600 hover:from-purple-700 hover:to-indigo-700 text-white font-bold text-xs px-6 py-3 rounded-xl shadow-md flex items-center space-x-2 transition">
                        <span>Tiếp Tục Sang Bước 3: Phân Tích (Số Liệu)</span>
                        <i class="fa-solid fa-arrow-right"></i>
                    </button>
                </div>
            </div>
        </div>

        <!-- ============================================================== -->
        <!-- BƯỚC 3: PHÂN TÍCH (SỐ LIỆU)                                    -->
        <!-- ============================================================== -->
        <div id="step3View" class="hidden space-y-6">
            <!-- Step Header Banner -->
            <div class="bg-white rounded-xl p-5 border border-slate-200 shadow-sm flex flex-col md:flex-row md:items-center justify-between gap-4">
                <div>
                    <div class="flex items-center space-x-2">
                        <span class="px-2.5 py-0.5 bg-purple-100 text-purple-800 text-xs font-bold rounded">BƯỚC 3: PHÂN TÍCH (SỐ LIỆU)</span>
                        <h2 class="text-lg font-bold text-slate-800">Phân Tích Số Liệu Quản Trị: Doanh Thu, Lợi Nhuận Gộp & Mục Tiêu 18 Cửa Hàng</h2>
                    </div>
                    <p class="text-xs text-slate-500 mt-1">
                        Tính toán chuẩn hóa theo ngày (Tháng 10: 31 ngày vs Tháng 09: 30 ngày), phân rã cơ cấu 4 nhóm ngành hàng mẹ & bé và đo lường ảnh hưởng của đổi trả.
                    </p>
                </div>
                <div class="flex flex-wrap items-center gap-2">
                    <button onclick="generateReport()" class="bg-purple-600 hover:bg-purple-700 text-white font-medium text-xs px-3.5 py-2.5 rounded-lg shadow-sm flex items-center space-x-1.5 transition">
                        <i class="fa-solid fa-arrows-rotate"></i>
                        <span>Cập Nhật Báo Cáo</span>
                    </button>
                    <button onclick="window.print()" class="bg-slate-100 hover:bg-slate-200 text-slate-700 font-medium text-xs px-3 py-2.5 rounded-lg border border-slate-300 shadow-sm flex items-center space-x-1.5 transition">
                        <i class="fa-solid fa-print"></i>
                        <span>In / Xuất Báo Cáo</span>
                    </button>
                    <button onclick="switchTab('step4')" class="bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-700 hover:to-teal-700 text-white font-semibold text-xs px-4 py-2.5 rounded-lg shadow-sm flex items-center space-x-1.5 transition">
                        <span>Sang Bước 4: Xuất Kết Quả</span>
                        <i class="fa-solid fa-arrow-right"></i>
                    </button>
                </div>
            </div>

            <!-- KPI Cards Toàn Hệ Thống -->
            <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-4">
                <div class="bg-white p-4 rounded-xl border border-slate-200 shadow-sm">
                    <span class="text-[11px] text-slate-500 block">Doanh Thu Thuần</span>
                    <div class="text-lg font-extrabold text-blue-700 mt-1" id="kpiNetRevenue">--</div>
                    <span class="text-[10px] text-slate-400 mt-1 block" id="kpiGrossAndReturn">Gross: --</span>
                </div>

                <div class="bg-white p-4 rounded-xl border border-slate-200 shadow-sm">
                    <span class="text-[11px] text-slate-500 block">Lợi Nhuận Gộp</span>
                    <div class="text-lg font-extrabold text-emerald-700 mt-1" id="kpiGrossProfit">--</div>
                    <span class="text-[10px] text-slate-400 mt-1 block" id="kpiMargin">Biên lãi: --</span>
                </div>

                <div class="bg-white p-4 rounded-xl border border-slate-200 shadow-sm">
                    <span class="text-[11px] text-slate-500 block">% Đạt Mục Tiêu DT</span>
                    <div class="text-lg font-extrabold text-indigo-700 mt-1" id="kpiRevTargetPct">--</div>
                    <div class="w-full bg-slate-100 rounded-full h-1.5 mt-2">
                        <div id="progRevTarget" class="bg-indigo-600 h-1.5 rounded-full" style="width: 0%"></div>
                    </div>
                </div>

                <div class="bg-white p-4 rounded-xl border border-slate-200 shadow-sm">
                    <span class="text-[11px] text-slate-500 block">% Đạt Mục Tiêu LN</span>
                    <div class="text-lg font-extrabold text-purple-700 mt-1" id="kpiGpTargetPct">--</div>
                    <div class="w-full bg-slate-100 rounded-full h-1.5 mt-2">
                        <div id="progGpTarget" class="bg-purple-600 h-1.5 rounded-full" style="width: 0%"></div>
                    </div>
                </div>

                <div class="bg-white p-4 rounded-xl border border-slate-200 shadow-sm">
                    <span class="text-[11px] text-slate-500 block">Tăng Trưởng MoM (DT)</span>
                    <div class="text-lg font-extrabold text-slate-700 mt-1" id="kpiRevMoM">--</div>
                    <span class="text-[10px] text-slate-400 mt-1 block">Chuẩn hoá 31 vs 30 ngày</span>
                </div>

                <div class="bg-white p-4 rounded-xl border border-slate-200 shadow-sm">
                    <span class="text-[11px] text-slate-500 block">Tỷ Lệ Đổi Trả Hệ Thống</span>
                    <div class="text-lg font-extrabold text-rose-600 mt-1" id="kpiReturnRate">--</div>
                    <span class="text-[10px] text-slate-400 mt-1 block" id="kpiTotalReturnVal">--</span>
                </div>
            </div>

            <!-- Charts Section (4 Biểu Đồ Phân Tích) -->
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
                <!-- Bar Chart: Doanh thu 18 Cửa hàng vs Target -->
                <div class="bg-white p-5 rounded-xl border border-slate-200 shadow-sm space-y-3">
                    <div class="flex justify-between items-center">
                        <h3 class="font-bold text-slate-800 text-sm flex items-center space-x-2">
                            <i class="fa-solid fa-chart-column text-blue-600"></i>
                            <span>So Sánh Doanh Thu Thực Tế vs Mục Tiêu (18 Cửa Hàng)</span>
                        </h3>
                        <span class="text-xs text-slate-400">Đơn vị: Triệu VNĐ</span>
                    </div>
                    <div class="h-64">
                        <canvas id="chartStoreRevenue"></canvas>
                    </div>
                </div>

                <!-- Bar Chart: Lợi nhuận gộp 18 Cửa hàng vs Target -->
                <div class="bg-white p-5 rounded-xl border border-slate-200 shadow-sm space-y-3">
                    <div class="flex justify-between items-center">
                        <h3 class="font-bold text-slate-800 text-sm flex items-center space-x-2">
                            <i class="fa-solid fa-chart-line text-emerald-600"></i>
                            <span>So Sánh Lợi Nhuận Gộp Thực Tế vs Mục Tiêu (18 Cửa Hàng)</span>
                        </h3>
                        <span class="text-xs text-slate-400">Đơn vị: Triệu VNĐ</span>
                    </div>
                    <div class="h-64">
                        <canvas id="chartStoreProfit"></canvas>
                    </div>
                </div>

                <!-- Donut Chart: Cơ cấu 4 ngành hàng mẹ & bé -->
                <div class="bg-white p-5 rounded-xl border border-slate-200 shadow-sm space-y-3">
                    <div class="flex justify-between items-center">
                        <h3 class="font-bold text-slate-800 text-sm flex items-center space-x-2">
                            <i class="fa-solid fa-pie-chart text-indigo-600"></i>
                            <span>Cơ Cấu Tỷ Trọng Doanh Thu Theo 4 Ngành Hàng Mẹ & Bé</span>
                        </h3>
                    </div>
                    <div class="h-64 flex justify-center">
                        <canvas id="chartCategoryShare"></canvas>
                    </div>
                </div>

                <!-- Bar Chart: Tỷ lệ đổi trả 18 Cửa hàng -->
                <div class="bg-white p-5 rounded-xl border border-slate-200 shadow-sm space-y-3">
                    <div class="flex justify-between items-center">
                        <h3 class="font-bold text-slate-800 text-sm flex items-center space-x-2">
                            <i class="fa-solid fa-triangle-exclamation text-rose-600"></i>
                            <span>Tỷ Lệ Đổi Trả (%) Của 18 Cửa Hàng (Ngưỡng cảnh báo: 8% & 12%)</span>
                        </h3>
                    </div>
                    <div class="h-64">
                        <canvas id="chartStoreReturns"></canvas>
                    </div>
                </div>
            </div>

            <!-- Detailed Stores Table (Bảng Thống Kê Phân Tích Số Liệu Chi Tiết) -->
            <div class="bg-white rounded-xl border border-slate-200 shadow-sm p-5 space-y-4">
                <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
                    <div>
                        <h3 class="font-bold text-slate-800 text-sm">Bảng Thống Kê Chi Tiết 18 Cửa Hàng Tháng 10/2026</h3>
                        <p class="text-xs text-slate-400">Dữ liệu đã khấu trừ hàng trả và chuẩn hóa kỳ thời gian (Net Revenue = Gross - Returns)</p>
                    </div>
                    <div class="flex items-center space-x-2">
                        <input type="text" id="tableFilterInput" onkeyup="filterStoreTable()" placeholder="Tìm tên cửa hàng, mã..." class="text-xs px-3 py-1.5 rounded-lg border border-slate-300 focus:outline-none focus:ring-1 focus:ring-blue-500">
                    </div>
                </div>

                <div class="overflow-x-auto custom-scrollbar border border-slate-200 rounded-lg">
                    <table class="w-full text-left text-xs text-slate-600" id="storesFullTable">
                        <thead class="bg-slate-100 text-slate-700 font-bold uppercase tracking-wider">
                            <tr>
                                <th class="py-2.5 px-3">Mã CH</th>
                                <th class="py-2.5 px-3">Tên Cửa Hàng</th>
                                <th class="py-2.5 px-3">Vùng</th>
                                <th class="py-2.5 px-3 text-right">Doanh Thu Thuần</th>
                                <th class="py-2.5 px-3 text-right">Lợi Nhuận Gộp</th>
                                <th class="py-2.5 px-3 text-center">Biên Lãi</th>
                                <th class="py-2.5 px-3 text-center">% Đạt DT</th>
                                <th class="py-2.5 px-3 text-center">% Đạt LN</th>
                                <th class="py-2.5 px-3 text-center">Tỷ Lệ Trả</th>
                                <th class="py-2.5 px-3 text-center">MoM (DT)</th>
                                <th class="py-2.5 px-3 text-center">MoM (LN)</th>
                            </tr>
                        </thead>
                        <tbody id="storesTableBody" class="divide-y divide-slate-200">
                            <tr>
                                <td colspan="11" class="text-center py-6 text-slate-400">Đang chuẩn bị báo cáo...</td>
                            </tr>
                        </tbody>
                    </table>
                </div>

                <!-- Next Step Action Card -->
                <div class="pt-2 flex justify-end">
                    <button onclick="switchTab('step4')" class="bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-700 hover:to-teal-700 text-white font-bold text-xs px-6 py-3 rounded-xl shadow-md flex items-center space-x-2 transition">
                        <span>Tiếp Tục Sang Bước 4: Xuất Kết Quả (Tải Dữ Liệu & Báo Cáo)</span>
                        <i class="fa-solid fa-arrow-right"></i>
                    </button>
                </div>
            </div>
        </div>

        <!-- ============================================================== -->
        <!-- BƯỚC 4: XUẤT KẾT QUẢ (TẢI DỮ LIỆU VÀ BÁO CÁO)                   -->
        <!-- ============================================================== -->
        <div id="step4View" class="hidden space-y-6">
            <!-- Step Header Banner -->
            <div class="bg-white rounded-xl p-5 border border-slate-200 shadow-sm flex flex-col md:flex-row md:items-center justify-between gap-4">
                <div>
                    <div class="flex items-center space-x-2">
                        <span class="px-2.5 py-0.5 bg-emerald-100 text-emerald-800 text-xs font-bold rounded">BƯỚC 4: XUẤT KẾT QUẢ</span>
                        <h2 class="text-lg font-bold text-slate-800">Xuất Kết Quả: Tải Dữ Liệu Sạch, Báo Cáo Quản Trị & Ký Duyệt Quyết Định</h2>
                    </div>
                    <p class="text-xs text-slate-500 mt-1">
                        Kiểm tra đối chiếu (Cross-check Audit) khớp 100%, phát hiện bất thường trọng yếu, xuất tệp dữ liệu sạch CSV, in báo cáo quản trị và ban hành quyết định can thiệp.
                    </p>
                </div>
                <div class="flex flex-wrap items-center gap-2">
                    <button onclick="runCrossCheckAudit()" class="bg-indigo-600 hover:bg-indigo-700 text-white font-medium text-xs px-3.5 py-2.5 rounded-lg shadow-sm flex items-center space-x-1.5 transition">
                        <i class="fa-solid fa-shield-halved"></i>
                        <span>Thực Thi Cross-check Audit</span>
                    </button>
                    <a href="/api/export-cleaned-csv" class="bg-emerald-600 hover:bg-emerald-700 text-white font-semibold text-xs px-4 py-2.5 rounded-lg shadow-sm flex items-center space-x-1.5 transition">
                        <i class="fa-solid fa-file-arrow-down"></i>
                        <span>Tải Sheets Sạch (CSV)</span>
                    </a>
                    <button onclick="window.print()" class="bg-slate-100 hover:bg-slate-200 text-slate-700 font-medium text-xs px-3.5 py-2.5 rounded-lg border border-slate-300 shadow-sm flex items-center space-x-1.5 transition">
                        <i class="fa-solid fa-print"></i>
                        <span>In / Xuất Báo Cáo</span>
                    </button>
                    <button onclick="openDecisionModal()" class="bg-gradient-to-r from-emerald-500 to-teal-600 hover:from-emerald-600 hover:to-teal-700 text-white font-semibold text-xs px-4 py-2.5 rounded-lg shadow-sm flex items-center space-x-1.5 transition">
                        <i class="fa-solid fa-stamp"></i>
                        <span>Ký Quyết Định Can Thiệp</span>
                    </button>
                </div>
            </div>

            <!-- Download & Export Hub Cards (Khu Vực Tải Dữ Liệu & Báo Cáo Nổi Bật) -->
            <div class="grid grid-cols-1 md:grid-cols-3 gap-5">
                <!-- Card 1: Tải dữ liệu sạch CSV -->
                <div class="bg-white rounded-xl border border-emerald-200 shadow-sm p-5 space-y-3 hover:shadow-md transition">
                    <div class="w-10 h-10 rounded-xl bg-emerald-100 text-emerald-700 flex items-center justify-center text-lg font-bold">
                        <i class="fa-solid fa-file-csv"></i>
                    </div>
                    <div>
                        <h4 class="font-bold text-sm text-slate-900">Tải Dữ Liệu Sạch (Sheets Sạch CSV)</h4>
                        <p class="text-xs text-slate-500 mt-1">Tệp dữ liệu đã khử trùng lặp, lọc đơn hủy, hoàn nhập đổi trả và đồng bộ kỳ kế toán.</p>
                    </div>
                    <a href="/api/export-cleaned-csv" class="w-full inline-flex items-center justify-center space-x-2 bg-emerald-600 hover:bg-emerald-700 text-white font-semibold text-xs py-2.5 rounded-lg shadow-sm transition">
                        <i class="fa-solid fa-cloud-arrow-down"></i>
                        <span>Tải Xuống Tệp CSV Ngay</span>
                    </a>
                </div>

                <!-- Card 2: Xuất Báo Cáo Quản Trị Toàn Diện -->
                <div class="bg-white rounded-xl border border-blue-200 shadow-sm p-5 space-y-3 hover:shadow-md transition">
                    <div class="w-10 h-10 rounded-xl bg-blue-100 text-blue-700 flex items-center justify-center text-lg font-bold">
                        <i class="fa-solid fa-file-invoice"></i>
                    </div>
                    <div>
                        <h4 class="font-bold text-sm text-slate-900">Xuất Báo Cáo Quản Trị (PDF / In)</h4>
                        <p class="text-xs text-slate-500 mt-1">Báo cáo đa chiều 18 cửa hàng, biểu đồ trực quan, phân tích cơ cấu & xếp hạng ưu tiên can thiệp.</p>
                    </div>
                    <button onclick="window.print()" class="w-full inline-flex items-center justify-center space-x-2 bg-blue-600 hover:bg-blue-700 text-white font-semibold text-xs py-2.5 rounded-lg shadow-sm transition">
                        <i class="fa-solid fa-print"></i>
                        <span>In Hoặc Lưu Báo Cáo PDF</span>
                    </button>
                </div>

                <!-- Card 3: Quyết Định Can Thiệp Của Giám Đốc -->
                <div class="bg-white rounded-xl border border-purple-200 shadow-sm p-5 space-y-3 hover:shadow-md transition">
                    <div class="w-10 h-10 rounded-xl bg-purple-100 text-purple-700 flex items-center justify-center text-lg font-bold">
                        <i class="fa-solid fa-signature"></i>
                    </div>
                    <div>
                        <h4 class="font-bold text-sm text-slate-900">Ban Hành Quyết Định Can Thiệp</h4>
                        <p class="text-xs text-slate-500 mt-1">Phê duyệt ngân sách, phân công cán bộ phụ trách và triển khai gói giải pháp hỗ trợ kịp thời.</p>
                    </div>
                    <button onclick="openDecisionModal()" class="w-full inline-flex items-center justify-center space-x-2 bg-gradient-to-r from-purple-600 to-indigo-600 hover:from-purple-700 hover:to-indigo-700 text-white font-semibold text-xs py-2.5 rounded-lg shadow-sm transition">
                        <i class="fa-solid fa-stamp"></i>
                        <span>Ký Quyết Định Hỗ Trợ</span>
                    </button>
                </div>
            </div>

            <!-- Cross-check Integrity Checklist (Đối soát 100% khớp) -->
            <div class="bg-white rounded-xl border border-slate-200 shadow-sm p-5 space-y-4">
                <div class="flex justify-between items-center border-b border-slate-100 pb-3">
                    <div class="flex items-center space-x-2">
                        <i class="fa-solid fa-check-double text-emerald-600 text-base"></i>
                        <h3 class="font-bold text-slate-800 text-sm">Kết Quả Đối Soát Toàn Vẹn Số Liệu (Cross-check Audit Trail)</h3>
                    </div>
                    <span class="px-2.5 py-1 bg-emerald-100 text-emerald-800 text-xs font-bold rounded-full">
                        <i class="fa-solid fa-circle-check mr-1"></i> 100% VERIFIED KHỚP TOÀN BỘ
                    </span>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-3 gap-4" id="integrityChecksContainer">
                    <!-- Populated by JS -->
                </div>
            </div>

            <!-- Executive Summary Alert Boxes (Phát hiện bất thường) -->
            <div class="bg-amber-50/70 border-l-4 border-amber-500 rounded-r-xl p-4 text-xs text-amber-900 space-y-2">
                <div class="font-bold text-sm flex items-center space-x-2">
                    <i class="fa-solid fa-triangle-exclamation text-amber-600"></i>
                    <span>Tóm Tắt Bất Thường Trọng Yếu Từ AI Agent Gửi Giám Đốc Kinh Doanh:</span>
                </div>
                <ul class="list-disc list-inside space-y-1 text-slate-700" id="executiveInsightsList">
                    <!-- Populated by JS -->
                </ul>
            </div>

            <!-- Priority Stores Grid (Ma Trận Xếp Hạng Cửa Hàng Cần Hỗ Trợ Trước) -->
            <div class="space-y-4">
                <div class="flex items-center justify-between">
                    <div>
                        <h3 class="font-extrabold text-slate-800 text-base flex items-center space-x-2">
                            <span class="w-2.5 h-6 bg-rose-600 rounded-full inline-block"></span>
                            <span>Ma Trận Xếp Hạng Ưu Tiên Can Thiệp (18 Cửa Hàng Phúc An)</span>
                        </h3>
                        <p class="text-xs text-slate-500">Được sắp xếp theo Điểm Khẩn Cấp (Urgency Score) từ cao xuống thấp để Giám đốc quyết định hỗ trợ trước</p>
                    </div>
                    <div class="flex items-center space-x-2 text-xs">
                        <span class="px-2 py-1 rounded bg-rose-600 text-white font-medium">P1: Khẩn Cấp</span>
                        <span class="px-2 py-1 rounded bg-amber-500 text-white font-medium">P2: Cần Hỗ Trợ</span>
                        <span class="px-2 py-1 rounded bg-blue-600 text-white font-medium">P3: Ổn Định</span>
                        <span class="px-2 py-1 rounded bg-emerald-600 text-white font-medium">P4: Xuất Sắc</span>
                    </div>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5" id="priorityStoresGrid">
                    <!-- Cards will be populated by JS -->
                </div>
            </div>

            <!-- Lịch Sử Các Quyết Định Đã Ký Duyệt -->
            <div class="bg-white rounded-xl border border-slate-200 shadow-sm p-5 space-y-4">
                <div class="flex justify-between items-center border-b border-slate-100 pb-3">
                    <div class="flex items-center space-x-2">
                        <i class="fa-solid fa-file-signature text-blue-600"></i>
                        <h3 class="font-bold text-slate-800 text-sm">Hồ Sơ Quyết Định Hỗ Trợ Kịp Thời Đã Ban Hành</h3>
                    </div>
                    <span class="text-xs text-slate-400" id="decisionsCountBadge">0 quyết định</span>
                </div>

                <div id="decisionsHistoryContainer" class="space-y-3">
                    <p class="text-center py-6 text-xs text-slate-400">Chưa có quyết định can thiệp nào được ký duyệt trong kỳ này.</p>
                </div>
            </div>
        </div>

        <!-- ============================================================== -->
        <!-- AI CO-PILOT CHATBOT VIEW                                       -->
        <!-- ============================================================== -->
        <div id="copilotView" class="hidden space-y-4">
            <div class="bg-white rounded-xl border border-slate-200 shadow-sm h-[680px] flex flex-col">
                <!-- Chat Header -->
                <div class="p-4 border-b border-slate-100 flex justify-between items-center bg-slate-50/50 rounded-t-xl">
                    <div class="flex items-center space-x-3">
                        <div class="w-9 h-9 rounded-xl bg-gradient-to-tr from-indigo-600 to-purple-600 text-white flex items-center justify-center font-bold shadow-sm">
                            <i class="fa-solid fa-robot"></i>
                        </div>
                        <div>
                            <h3 class="font-bold text-sm text-slate-800">Trợ Lý AI Phân Tích Quản Trị Bán Lẻ Phúc An</h3>
                            <p class="text-[11px] text-slate-500">Tra cứu số liệu 18 cửa hàng, phân tích nguyên nhân gốc rễ và đề xuất giải pháp</p>
                        </div>
                    </div>
                    <div class="flex items-center space-x-2 text-xs">
                        <button onclick="quickAsk('Cửa hàng nào cần hỗ trợ trước và lý do vì sao?')" class="hidden sm:inline-block bg-blue-50 hover:bg-blue-100 text-blue-700 px-2.5 py-1 rounded-full border border-blue-200">
                            Cửa hàng cần hỗ trợ?
                        </button>
                        <button onclick="quickAsk('Tại sao cửa hàng ST09 (Bắc Từ Liêm) bị cảnh báo đỏ đổi trả?')" class="hidden sm:inline-block bg-rose-50 hover:bg-rose-100 text-rose-700 px-2.5 py-1 rounded-full border border-rose-200">
                            Lỗi ST09 Bắc Từ Liêm?
                        </button>
                        <button onclick="quickAsk('Tại sao ST18 (Cần Thơ) sụt giảm mạnh MoM?')" class="hidden sm:inline-block bg-purple-50 hover:bg-purple-100 text-purple-700 px-2.5 py-1 rounded-full border border-purple-200">
                            Sụt giảm ST18?
                        </button>
                    </div>
                </div>

                <!-- Chat Messages Stream -->
                <div id="chatMessages" class="flex-1 p-5 overflow-y-auto space-y-4 custom-scrollbar text-xs">
                    <!-- Welcome msg -->
                    <div class="flex items-start space-x-3">
                        <div class="w-8 h-8 rounded-full bg-indigo-600 text-white flex items-center justify-center flex-shrink-0 text-xs">
                            <i class="fa-solid fa-robot"></i>
                        </div>
                        <div class="bg-indigo-50/80 border border-indigo-100 text-slate-800 p-3.5 rounded-2xl rounded-tl-none max-w-2xl leading-relaxed space-y-2">
                            <p class="font-bold text-indigo-900">Xin chào Giám đốc Kinh doanh và Quý chuyên viên!</p>
                            <p>Tôi là <b>AI Retail Copilot</b> của Phúc An Retail. Tôi đang phân tích trực tiếp trên tệp dữ liệu: <b>PhucAn_DuLieuBanHangTho_DaBoSungTruong.xlsx</b> (18 cửa hàng Mẹ & Bé toàn quốc) và sẵn sàng giải đáp mọi thắc mắc chuyên sâu.</p>
                            <p class="text-slate-600">Gợi ý một số câu hỏi:</p>
                            <ul class="list-disc list-inside text-slate-600 space-y-0.5">
                                <li><i>"Cửa hàng nào cần hỗ trợ trước và thứ tự ưu tiên là gì?"</i></li>
                                <li><i>"Tại sao cửa hàng ST09 (Bắc Từ Liêm) bị cảnh báo đỏ tỷ lệ đổi trả?"</i></li>
                                <li><i>"Tại sao cửa hàng ST18 (Cần Thơ) lại sụt giảm mạnh MoM (-46.6%)?"</i></li>
                                <li><i>"Kiểm toán đối soát dữ liệu có khớp 100% không?"</i></li>
                            </ul>
                        </div>
                    </div>
                </div>

                <!-- Chat Input Form -->
                <div class="p-4 border-t border-slate-100 bg-white rounded-b-xl">
                    <form onsubmit="handleChatSubmit(event)" class="flex items-center space-x-2">
                        <input type="text" id="chatInput" placeholder="Hỏi AI Agent về bất kỳ cửa hàng hoặc chỉ số nào..." class="flex-1 text-xs px-4 py-3 rounded-xl border border-slate-300 focus:outline-none focus:ring-2 focus:ring-indigo-500">
                        <button type="submit" id="btnSendChat" class="bg-indigo-600 hover:bg-indigo-700 text-white px-5 py-3 rounded-xl font-medium text-xs flex items-center space-x-1.5 transition">
                            <i class="fa-solid fa-paper-plane"></i>
                            <span>Gửi</span>
                        </button>
                    </form>
                </div>
            </div>
        </div>

    </main>

    <!-- ============================================================== -->
    <!-- MODAL: KÝ DUYỆT QUYẾT ĐỊNH CỦA GIÁM ĐỐC KINH DOANH            -->
    <!-- ============================================================== -->
    <div id="decisionModal" class="fixed inset-0 bg-slate-900/60 backdrop-blur-sm z-50 hidden flex items-center justify-center p-4">
        <div class="bg-white rounded-2xl shadow-2xl max-w-2xl w-full border border-slate-200 overflow-hidden flex flex-col max-h-[90vh]">
            <div class="bg-gradient-to-r from-blue-900 to-indigo-900 text-white p-5 flex justify-between items-center">
                <div class="flex items-center space-x-3">
                    <div class="w-9 h-9 rounded-lg bg-white/10 flex items-center justify-center text-emerald-400 font-bold">
                        <i class="fa-solid fa-stamp text-lg"></i>
                    </div>
                    <div>
                        <h3 class="font-bold text-base">Ban Hành Quyết Định Hỗ Trợ Cửa Hàng</h3>
                        <p class="text-xs text-blue-200">Làn 3: Giám Đốc Kinh Doanh - Phê duyệt kế hoạch can thiệp kịp thời</p>
                    </div>
                </div>
                <button onclick="closeDecisionModal()" class="text-slate-400 hover:text-white text-lg">
                    <i class="fa-solid fa-xmark"></i>
                </button>
            </div>

            <form onsubmit="submitExecutiveDecision(event)" class="p-6 overflow-y-auto space-y-4 text-xs flex-1">
                <div>
                    <label class="font-bold text-slate-700 block mb-1">1. Chọn Cửa Hàng Cần Can Thiệp Hỗ Trợ (Có thể chọn nhiều):</label>
                    <div class="grid grid-cols-2 sm:grid-cols-3 gap-2 border border-slate-200 p-3 rounded-lg max-h-40 overflow-y-auto" id="decisionStoreCheckboxes">
                        <!-- Populated by JS -->
                    </div>
                </div>

                <div>
                    <label class="font-bold text-slate-700 block mb-1">2. Gói Giải Pháp Can Thiệp & Kế Hoạch Hành Động:</label>
                    <select id="decActionPreset" onchange="applyDecisionPreset()" class="w-full text-xs p-2.5 rounded-lg border border-slate-300 mb-2">
                        <option value="custom">-- Chọn kịch bản mẫu từ AI hoặc tự soạn thảo --</option>
                        <option value="p1_combo">Kịch bản P1: Xử lý hàng lỗi hạn sử dụng (ST09) & Kích cầu chặn đà sụt giảm (ST18)</option>
                        <option value="sales_boost">Kịch bản Kích cầu: Hỗ trợ Marketing Local & Đào tạo Cross-sell (ST12, ST15, ST16)</option>
                        <option value="all_urgent">Kịch bản Tổng lực: Can thiệp toàn diện nhóm P1 (ST09, ST05, ST18, ST12)</option>
                    </select>
                    <textarea id="decActionPlan" rows="3" required class="w-full text-xs p-3 rounded-lg border border-slate-300 focus:ring-2 focus:ring-blue-500 focus:outline-none" placeholder="Chi tiết các biện pháp cụ thể..."></textarea>
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                    <div>
                        <label class="font-bold text-slate-700 block mb-1">3. Cán Bộ Phụ Trách Triển Khai:</label>
                        <input type="text" id="decAssignedLead" required value="Trưởng Ban Quản Lý Bán Lẻ Vùng - Vũ Đức Thịnh" class="w-full text-xs p-2.5 rounded-lg border border-slate-300 focus:outline-none focus:ring-2 focus:ring-blue-500">
                    </div>
                    <div>
                        <label class="font-bold text-slate-700 block mb-1">4. Ngân Sách Hỗ Trợ Dự Kiến (VNĐ):</label>
                        <input type="number" id="decBudget" required value="120000000" class="w-full text-xs p-2.5 rounded-lg border border-slate-300 focus:outline-none focus:ring-2 focus:ring-blue-500">
                    </div>
                </div>

                <div>
                    <label class="font-bold text-slate-700 block mb-1">5. Ghi Chú & Yêu Cầu Giám Sát Của Giám Đốc:</label>
                    <textarea id="decNotes" rows="2" class="w-full text-xs p-2.5 rounded-lg border border-slate-300" placeholder="Báo cáo tiến độ hàng tuần vào thứ Hai..."></textarea>
                </div>

                <div class="p-3 bg-blue-50 rounded-lg border border-blue-100 flex items-center space-x-2 text-blue-900">
                    <i class="fa-solid fa-signature text-blue-600 text-lg"></i>
                    <div>
                        <span class="font-bold block">Người Ký Duyệt Quyết Định:</span>
                        <span class="text-[11px] text-blue-700">Lê Thanh Tùng - Giám Đốc Kinh Doanh Toàn Quốc</span>
                    </div>
                </div>

                <div class="pt-3 border-t border-slate-200 flex justify-end space-x-3">
                    <button type="button" onclick="closeDecisionModal()" class="px-4 py-2 rounded-lg border border-slate-300 text-slate-600 hover:bg-slate-100 font-medium">Hủy bỏ</button>
                    <button type="submit" class="px-5 py-2 rounded-lg bg-emerald-600 hover:bg-emerald-700 text-white font-bold flex items-center space-x-1.5 shadow-md">
                        <i class="fa-solid fa-stamp"></i>
                        <span>Phê Duyệt & Ban Hành Quyết Định</span>
                    </button>
                </div>
            </form>
        </div>
    </div>

    <!-- Scripts Logic -->
    <script>
        // Global State Store
        let globalState = {
            rawLoaded: false,
            cleanedDone: false,
            humanVerified: false,
            reportDone: false,
            auditDone: false,
            reportData: null,
            auditData: null
        };

        // Charts references
        let chartRevInstance = null;
        let chartProfitInstance = null;
        let chartCategoryInstance = null;
        let chartReturnsInstance = null;

        // File Upload Handlers (Kéo thả & Chọn tệp tải lên trực tiếp trên Web)
        let selectedUploadFile = null;

        function triggerFileInput() {
            document.getElementById('fileUploadInput').click();
        }

        function handleDragOver(e) {
            e.preventDefault();
            e.stopPropagation();
            document.getElementById('dropZone').classList.add('border-blue-600', 'bg-blue-100/50');
        }

        function handleDragLeave(e) {
            e.preventDefault();
            e.stopPropagation();
            document.getElementById('dropZone').classList.remove('border-blue-600', 'bg-blue-100/50');
        }

        function handleFileDrop(e) {
            e.preventDefault();
            e.stopPropagation();
            document.getElementById('dropZone').classList.remove('border-blue-600', 'bg-blue-100/50');
            const files = e.dataTransfer.files;
            if (files && files.length > 0) {
                setUploadFile(files[0]);
            }
        }

        function handleFileSelected(e) {
            const files = e.target.files;
            if (files && files.length > 0) {
                setUploadFile(files[0]);
            }
        }

        function setUploadFile(file) {
            selectedUploadFile = file;
            const infoBox = document.getElementById('selectedFileInfo');
            const nameEl = document.getElementById('selectedFileName');
            const sizeEl = document.getElementById('selectedFileSize');
            const iconEl = document.getElementById('selectedFileIcon');
            const btnSubmit = document.getElementById('btnUploadSubmit');

            nameEl.innerText = file.name;
            const sizeInKb = (file.size / 1024).toFixed(1);
            sizeEl.innerText = `${sizeInKb > 1024 ? (sizeInKb / 1024).toFixed(2) + ' MB' : sizeInKb + ' KB'}`;

            if (file.name.endsWith('.csv')) {
                iconEl.className = "fa-solid fa-file-csv text-blue-600 text-base";
            } else {
                iconEl.className = "fa-solid fa-file-excel text-emerald-600 text-base";
            }

            infoBox.classList.remove('hidden');
            btnSubmit.classList.remove('opacity-50', 'cursor-not-allowed');
            btnSubmit.disabled = false;
        }

        function cancelSelectedFile(e) {
            if (e) e.stopPropagation();
            selectedUploadFile = null;
            document.getElementById('fileUploadInput').value = '';
            document.getElementById('selectedFileInfo').classList.add('hidden');
            const btnSubmit = document.getElementById('btnUploadSubmit');
            btnSubmit.classList.add('opacity-50', 'cursor-not-allowed');
            btnSubmit.disabled = true;
        }

        async function uploadSelectedFile() {
            if (!selectedUploadFile) {
                alert("Vui lòng chọn tệp Excel hoặc CSV trước!");
                return;
            }

            const btnSubmit = document.getElementById('btnUploadSubmit');
            btnSubmit.innerHTML = `<i class="fa-solid fa-spinner fa-spin"></i> <span>Đang tải lên và phân tích...</span>`;
            btnSubmit.disabled = true;

            const formData = new FormData();
            formData.append('file', selectedUploadFile);

            try {
                const res = await fetch('/api/upload-raw', {
                    method: 'POST',
                    body: formData
                });
                const json = await res.json();
                if (json.success) {
                    const d = json.data;
                    updateRawStatsDisplay(d);
                    document.getElementById('badgeStep1').innerText = "Tệp vừa tải lên";
                    document.getElementById('badgeStep1').className = "text-[10px] px-1.5 py-0.5 rounded-full bg-emerald-100 text-emerald-700 font-semibold ml-1";

                    confetti({ particleCount: 40, spread: 50, origin: { y: 0.4 } });

                    // Tự động kích hoạt làm sạch và chuyển tiếp
                    executeCleaning();
                } else {
                    alert("Lỗi tải tệp: " + json.error);
                }
            } catch (err) {
                alert("Lỗi kết nối máy chủ khi tải tệp: " + err);
            } finally {
                btnSubmit.innerHTML = `<i class="fa-solid fa-upload"></i> <span>Tải Lên & Kết Nối Nguồn Dữ Liệu</span>`;
                btnSubmit.disabled = false;
            }
        }

        // Navigation Switcher for 4 Steps + Copilot
        function switchTab(step) {
            // Map legacy phase names to steps if any
            if (step === 'phase1') step = 'step1';
            if (step === 'phase2') step = 'step3';
            if (step === 'phase3') step = 'step4';

            document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active', 'text-blue-600'));
            ['step1View', 'step2View', 'step3View', 'step4View', 'copilotView'].forEach(id => {
                const el = document.getElementById(id);
                if (el) el.classList.add('hidden');
            });

            // Update top roadmaps cards styles
            for (let i = 1; i <= 4; i++) {
                const card = document.getElementById(`cardNavStep${i}`);
                if (card) {
                    if (`step${i}` === step) {
                        card.className = "p-3 rounded-lg border-2 border-blue-600 bg-blue-50/80 cursor-pointer shadow-md transition flex items-start space-x-2.5";
                    } else {
                        card.className = "p-3 rounded-lg border border-slate-200 bg-slate-50 hover:bg-slate-100/70 cursor-pointer hover:shadow-sm transition flex items-start space-x-2.5";
                    }
                }
            }

            if (step === 'step1') {
                document.getElementById('tabBtnStep1').classList.add('active', 'text-blue-600');
                document.getElementById('step1View').classList.remove('hidden');
                loadDataPreview('raw', 1);
            } else if (step === 'step2') {
                document.getElementById('tabBtnStep2').classList.add('active', 'text-blue-600');
                document.getElementById('step2View').classList.remove('hidden');
                if (!globalState.cleanedDone) {
                    executeCleaning();
                } else {
                    loadDataPreview(currentPreviewMode, currentPreviewPage);
                }
            } else if (step === 'step3') {
                document.getElementById('tabBtnStep3').classList.add('active', 'text-blue-600');
                document.getElementById('step3View').classList.remove('hidden');
                if (!globalState.reportDone) {
                    generateReport();
                } else {
                    renderCharts();
                }
            } else if (step === 'step4') {
                document.getElementById('tabBtnStep4').classList.add('active', 'text-blue-600');
                document.getElementById('step4View').classList.remove('hidden');
                if (!globalState.auditDone) {
                    runCrossCheckAudit();
                }
            } else if (step === 'copilot') {
                document.getElementById('tabBtnCopilot').classList.add('active', 'text-blue-600');
                document.getElementById('copilotView').classList.remove('hidden');
            }
        }

        // Format Currency Helper
        function formatVND(amount) {
            if (amount === null || amount === undefined) return "--";
            return new Intl.NumberFormat('vi-VN', { style: 'currency', currency: 'VND' }).format(amount);
        }

        function formatNumber(num) {
            if (num === null || num === undefined) return "--";
            return new Intl.NumberFormat('vi-VN').format(num);
        }

        function updateRawStatsDisplay(d) {
            const rawRowsStr = `${formatNumber(d.total_rows)} dòng`;
            const rawRevStr = `Doanh thu thô: ${formatVND(d.raw_gross_sales)}`;

            document.getElementById('statRawRows').innerText = rawRowsStr;
            document.getElementById('statRawRevenue').innerText = rawRevStr;

            const elS2 = document.getElementById('statRawRowsStep2');
            if (elS2) elS2.innerText = rawRowsStr;
            const elRevS2 = document.getElementById('statRawRevenueStep2');
            if (elRevS2) elRevS2.innerText = rawRevStr;

            document.getElementById('activeFileNameBadge').innerText = d.file_name;
        }

        // 1. BƯỚC 1: Load Uploaded Data (Excel file)
        async function loadUploadedData() {
            const btn = document.getElementById('btnLoadUploaded');
            btn.innerHTML = `<i class="fa-solid fa-spinner fa-spin"></i> <span>Đang nạp file...</span>`;
            btn.disabled = true;

            try {
                const res = await fetch('/api/load-uploaded', { method: 'POST' });
                const json = await res.json();
                if (json.success) {
                    const d = json.data;
                    updateRawStatsDisplay(d);
                    document.getElementById('badgeStep1').innerText = "File .xlsx đã nạp";
                    document.getElementById('badgeStep1').className = "text-[10px] px-1.5 py-0.5 rounded-full bg-emerald-100 text-emerald-700 font-semibold ml-1";

                    const btnClean = document.getElementById('btnExecuteClean');
                    if (btnClean) {
                        btnClean.classList.remove('opacity-50', 'cursor-not-allowed');
                        btnClean.disabled = false;
                    }

                    // Tải xem trước dữ liệu thô
                    loadDataPreview('raw', 1);

                    // Làm sạch ngầm để sẵn sàng
                    executeCleaning();
                }
            } catch (err) {
                alert("Lỗi nạp file: " + err);
            } finally {
                btn.innerHTML = `<i class="fa-solid fa-file-circle-check"></i> <span>Nạp File Tải Lên (.xlsx)</span>`;
                btn.disabled = false;
            }
        }

        // Load 60k Sample Data
        async function loadSampleData() {
            const btn = document.getElementById('btnLoadSample');
            btn.innerHTML = `<i class="fa-solid fa-spinner fa-spin"></i> <span>Đang nạp file...</span>`;
            btn.disabled = true;

            try {
                const res = await fetch('/api/load-sample', { method: 'POST' });
                const json = await res.json();
                if (json.success) {
                    const d = json.data;
                    updateRawStatsDisplay(d);
                    document.getElementById('badgeStep1').innerText = "File mẫu 60k dòng";
                    document.getElementById('badgeStep1').className = "text-[10px] px-1.5 py-0.5 rounded-full bg-blue-100 text-blue-700 font-semibold ml-1";

                    const btnClean = document.getElementById('btnExecuteClean');
                    if (btnClean) {
                        btnClean.classList.remove('opacity-50', 'cursor-not-allowed');
                        btnClean.disabled = false;
                    }

                    loadDataPreview('raw', 1);
                    executeCleaning();
                }
            } catch (err) {
                alert("Lỗi nạp dữ liệu: " + err);
            } finally {
                btn.innerHTML = `<i class="fa-solid fa-database"></i> <span>Nạp File Mẫu 60k Dòng</span>`;
                btn.disabled = false;
            }
        }

        // 2. BƯỚC 2: Execute Cleaning (Làm Sạch & Chuẩn Hóa)
        async function executeCleaning() {
            const btn = document.getElementById('btnExecuteClean');
            if (btn) {
                btn.innerHTML = `<i class="fa-solid fa-spinner fa-spin"></i> <span>AI Agent đang làm sạch...</span>`;
                btn.disabled = true;
            }

            try {
                const res = await fetch('/api/execute-cleaning', { method: 'POST' });
                const json = await res.json();
                if (json.success) {
                    const d = json.data;
                    globalState.cleanedDone = true;

                    // Extract exact fields from engine response
                    const dedupRows = d.dedup ? d.dedup.removed_rows : 0;
                    const periodRows = d.period_sync ? d.period_sync.out_of_period_rows : 0;
                    const cancelRows = d.cancelled_filter ? d.cancelled_filter.cancelled_rows : 0;
                    const cancelAmount = d.cancelled_filter ? d.cancelled_filter.cancelled_amount : 0;
                    const returnRows = d.returns_handling ? d.returns_handling.returned_rows : 0;
                    const returnAmount = d.returns_handling ? d.returns_handling.returned_amount : 0;
                    const validRows = d.final_cleaned ? d.final_cleaned.valid_rows : 0;
                    const netRev = d.final_cleaned ? d.final_cleaned.net_revenue : 0;

                    // Update stats
                    document.getElementById('statRemovedRows').innerText = `${formatNumber(dedupRows + periodRows)} dòng`;
                    document.getElementById('statRemovedValue').innerText = `Lệch kỳ & trùng: đã bóc tách`;
                    
                    document.getElementById('statCancelReturn').innerText = `${formatNumber(cancelRows + returnRows)} đơn`;
                    document.getElementById('statReturnImpact').innerText = `Khấu trừ DT: -${formatVND(returnAmount)}`;

                    document.getElementById('statCleanedRows').innerText = `${formatNumber(validRows)} dòng`;
                    document.getElementById('statNetRevP1').innerText = `DT thuần: ${formatVND(netRev)}`;

                    document.getElementById('cleanTimestamp').innerText = `Hoàn tất: ${d.timestamp || ''}`;
                    document.getElementById('badgeStep2').innerText = "Đã làm sạch";
                    document.getElementById('badgeStep2').className = "text-[10px] px-1.5 py-0.5 rounded-full bg-emerald-100 text-emerald-700 font-semibold ml-1";

                    // Render Cleaning Log
                    const logContainer = document.getElementById('cleaningLogContainer');
                    logContainer.innerHTML = `
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
                            <div class="p-3 bg-emerald-50 border border-emerald-200 rounded-lg flex items-start space-x-2.5">
                                <i class="fa-solid fa-check-circle text-emerald-600 mt-0.5 text-sm"></i>
                                <div>
                                    <span class="font-bold text-emerald-900">1. Lọc đơn trùng lặp (RULE-DEDUP):</span>
                                    <p class="text-emerald-800">Đã phát hiện và loại bỏ <b>${formatNumber(dedupRows)}</b> dòng giao dịch bị ghi nhận lặp.</p>
                                </div>
                            </div>

                            <div class="p-3 bg-emerald-50 border border-emerald-200 rounded-lg flex items-start space-x-2.5">
                                <i class="fa-solid fa-check-circle text-emerald-600 mt-0.5 text-sm"></i>
                                <div>
                                    <span class="font-bold text-emerald-900">2. Đồng bộ kỳ thời gian (RULE-PERIOD-SYNC):</span>
                                    <p class="text-emerald-800">Tách riêng <b>${formatNumber(periodRows)}</b> dòng giao dịch kỳ trước để so sánh chính xác.</p>
                                </div>
                            </div>

                            <div class="p-3 bg-emerald-50 border border-emerald-200 rounded-lg flex items-start space-x-2.5">
                                <i class="fa-solid fa-check-circle text-emerald-600 mt-0.5 text-sm"></i>
                                <div>
                                    <span class="font-bold text-emerald-900">3. Loại bỏ đơn bị huỷ (RULE-CANCEL):</span>
                                    <p class="text-emerald-800">Tách rời <b>${formatNumber(cancelRows)}</b> đơn CANCELLED ra khỏi doanh thu (${formatVND(cancelAmount)}).</p>
                                </div>
                            </div>

                            <div class="p-3 bg-emerald-50 border border-emerald-200 rounded-lg flex items-start space-x-2.5">
                                <i class="fa-solid fa-check-circle text-emerald-600 mt-0.5 text-sm"></i>
                                <div>
                                    <span class="font-bold text-emerald-900">4. Xử lý hàng đổi trả (RULE-RETURN):</span>
                                    <p class="text-emerald-800">Khấu trừ <b>${formatNumber(returnRows)}</b> đơn RETURNED khỏi doanh thu gộp và hoàn nhập giá vốn kho.</p>
                                </div>
                            </div>
                        </div>
                    `;

                    // Enable Export button
                    const btnExp = document.getElementById('btnExportCleaned');
                    if (btnExp) {
                        btnExp.classList.remove('opacity-50', 'pointer-events-none');
                    }

                    // Update Human Verification Form
                    document.getElementById('hvStatusDisplay').innerHTML = `
                        <span class="text-amber-600 font-semibold flex items-center">
                            <i class="fa-solid fa-clock-rotate-left mr-1.5"></i> Chờ Chuyên viên bấm xác nhận
                        </span>
                    `;
                    document.getElementById('btnApproveHV').classList.remove('opacity-50', 'cursor-not-allowed');
                    document.getElementById('btnApproveHV').disabled = false;
                    document.getElementById('btnRejectHV').classList.remove('opacity-50', 'cursor-not-allowed');
                    document.getElementById('btnRejectHV').disabled = false;

                    // Load preview table
                    loadDataPreview('cleaned', 1);
                }
            } catch (err) {
                console.error("Lỗi làm sạch: " + err);
            } finally {
                if (btn) {
                    btn.innerHTML = `<i class="fa-solid fa-check"></i> <span>Đã Làm Sạch Xong</span>`;
                    btn.disabled = false;
                }
            }
        }

        // Interactive Data Preview with Pagination and Modes (Cleaned, Raw, Excluded)
        let currentPreviewMode = 'cleaned';
        let currentPreviewPage = 1;
        let currentPreviewTotal = 0;

        function prevPreviewPage() {
            if (currentPreviewPage > 1) {
                loadDataPreview(currentPreviewMode, currentPreviewPage - 1);
            }
        }

        function nextPreviewPage() {
            const totalPages = Math.ceil(currentPreviewTotal / 20) || 1;
            if (currentPreviewPage < totalPages) {
                loadDataPreview(currentPreviewMode, currentPreviewPage + 1);
            }
        }

        async function loadDataPreview(mode = null, page = 1) {
            if (mode) currentPreviewMode = mode;
            currentPreviewPage = page;

            // Highlight mode buttons in Step 2
            const btnCleaned = document.getElementById('btnModeCleaned');
            const btnRaw = document.getElementById('btnModeRaw');
            const btnExcluded = document.getElementById('btnModeExcluded');

            if (btnCleaned && btnRaw && btnExcluded) {
                btnCleaned.className = "px-3 py-1.5 rounded-lg text-xs font-semibold text-slate-600 hover:bg-white transition";
                btnRaw.className = "px-3 py-1.5 rounded-lg text-xs font-semibold text-slate-600 hover:bg-white transition";
                btnExcluded.className = "px-3 py-1.5 rounded-lg text-xs font-semibold text-slate-600 hover:bg-white transition";

                if (currentPreviewMode === 'cleaned') {
                    btnCleaned.className = "px-3 py-1.5 rounded-lg text-xs font-bold bg-blue-600 text-white shadow-sm transition";
                } else if (currentPreviewMode === 'raw') {
                    btnRaw.className = "px-3 py-1.5 rounded-lg text-xs font-bold bg-slate-800 text-white shadow-sm transition";
                } else if (currentPreviewMode === 'excluded') {
                    btnExcluded.className = "px-3 py-1.5 rounded-lg text-xs font-bold bg-amber-600 text-white shadow-sm transition";
                }
            }

            const tbodyStep1 = document.getElementById('previewTableBodyStep1');
            const tbodyStep2 = document.getElementById('previewTableBody');

            if (tbodyStep1) {
                tbodyStep1.innerHTML = `<tr><td colspan="9" class="text-center py-6 text-slate-400 font-sans"><i class="fa-solid fa-spinner fa-spin mr-2"></i> Đang tải dữ liệu...</td></tr>`;
            }
            if (tbodyStep2) {
                tbodyStep2.innerHTML = `<tr><td colspan="9" class="text-center py-6 text-slate-400 font-sans"><i class="fa-solid fa-spinner fa-spin mr-2"></i> Đang tải dữ liệu...</td></tr>`;
            }

            try {
                const res = await fetch(`/api/cleaned-data-preview?mode=${currentPreviewMode}&page=${currentPreviewPage}&limit=20`);
                const json = await res.json();
                if (json.success && json.records && json.records.length > 0) {
                    currentPreviewTotal = json.total;
                    const totalPages = Math.ceil(json.total / json.limit) || 1;
                    const modeLabel = currentPreviewMode === 'cleaned' ? 'dữ liệu sạch' : (currentPreviewMode === 'raw' ? 'dữ liệu thô' : 'dòng bị loại trừ');
                    
                    const countText = `Tổng cộng: ${formatNumber(json.total)} ${modeLabel} (Hiển thị 20 dòng/trang)`;
                    const pageText = `Trang ${json.page} / ${totalPages}`;

                    if (document.getElementById('previewTotalCount')) document.getElementById('previewTotalCount').innerText = countText;
                    if (document.getElementById('previewPageIndicator')) document.getElementById('previewPageIndicator').innerText = pageText;
                    if (document.getElementById('previewTotalCountStep1')) document.getElementById('previewTotalCountStep1').innerText = countText;
                    if (document.getElementById('previewPageIndicatorStep1')) document.getElementById('previewPageIndicatorStep1').innerText = pageText;

                    const btnPrev = document.getElementById('btnPrevPreview');
                    const btnNext = document.getElementById('btnNextPreview');
                    if (btnPrev) btnPrev.disabled = (json.page <= 1);
                    if (btnNext) btnNext.disabled = (json.page >= totalPages);

                    const rowsHtml = json.records.map(r => {
                        const isRet = r.status === 'RETURNED';
                        const isCanc = r.status === 'CANCELLED';
                        const badgeColor = isRet ? 'bg-rose-100 text-rose-700' : (isCanc ? 'bg-amber-100 text-amber-800' : 'bg-emerald-100 text-emerald-700');
                        return `
                            <tr class="hover:bg-slate-50 transition">
                                <td class="py-2.5 px-3 font-semibold text-slate-800">${r.transaction_id || '--'}</td>
                                <td class="py-2.5 px-3 text-slate-500">${r.transaction_date || '--'}</td>
                                <td class="py-2.5 px-3 font-bold">${r.store_id || '--'}</td>
                                <td class="py-2.5 px-3 font-sans">${r.store_name || '--'}</td>
                                <td class="py-2.5 px-3 font-sans">${r.product_name || '--'}</td>
                                <td class="py-2.5 px-3 text-center">${r.quantity || 1}</td>
                                <td class="py-2.5 px-3 text-right font-semibold ${isRet ? 'text-rose-600' : 'text-slate-800'}">${isRet ? '-' : ''}${formatVND(r.total_amount)}</td>
                                <td class="py-2.5 px-3 text-center">
                                    <span class="px-2 py-0.5 rounded text-[10px] font-bold ${badgeColor}">
                                        ${r.status || 'COMPLETED'}
                                    </span>
                                </td>
                                <td class="py-2.5 px-3 font-sans text-slate-400 text-[11px]">${r.note || '--'}</td>
                            </tr>
                        `;
                    }).join('');

                    if (tbodyStep1) tbodyStep1.innerHTML = rowsHtml;
                    if (tbodyStep2) tbodyStep2.innerHTML = rowsHtml;
                } else {
                    const emptyMsg = `<tr><td colspan="9" class="text-center py-6 text-slate-400 font-sans">Chưa có dữ liệu để hiển thị.</td></tr>`;
                    if (tbodyStep1) tbodyStep1.innerHTML = emptyMsg;
                    if (tbodyStep2) tbodyStep2.innerHTML = emptyMsg;
                }
            } catch (err) {
                const errMsg = `<tr><td colspan="9" class="text-center py-6 text-rose-500 font-sans">Lỗi tải dữ liệu: ${err}</td></tr>`;
                if (tbodyStep1) tbodyStep1.innerHTML = errMsg;
                if (tbodyStep2) tbodyStep2.innerHTML = errMsg;
            }
        }

        // Submit Human Verification (Khâu con người kiểm tra & phê duyệt theo BPMN)
        async function submitHumanVerification(approved) {
            const notes = document.getElementById('hvNotes').value;
            try {
                const res = await fetch('/api/human-verify', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({ approved, notes })
                });
                const json = await res.json();
                if (json.success) {
                    globalState.humanVerified = approved;
                    if (approved) {
                        document.getElementById('hvStatusDisplay').innerHTML = `
                            <span class="text-emerald-700 font-bold flex items-center">
                                <i class="fa-solid fa-circle-check mr-1.5"></i> ĐÃ XÁC NHẬN OK (Sẵn sàng sang Bước 3)
                            </span>
                        `;
                        document.getElementById('badgeStep2').innerText = "Đã xác thực OK";
                        document.getElementById('badgeStep2').className = "text-[10px] px-1.5 py-0.5 rounded-full bg-emerald-100 text-emerald-700 font-semibold ml-1";
                        
                        confetti({ particleCount: 50, spread: 60, origin: { y: 0.6 } });

                        // Transition to Step 3
                        setTimeout(() => {
                            switchTab('step3');
                        }, 800);
                    } else {
                        document.getElementById('hvStatusDisplay').innerHTML = `
                            <span class="text-rose-600 font-bold">
                                <i class="fa-solid fa-circle-xmark mr-1.5"></i> YÊU CẦU LỌC LẠI
                            </span>
                        `;
                    }
                }
            } catch (err) {
                alert("Lỗi xác thực: " + err);
            }
        }

        // 3. BƯỚC 3: Generate Management Report (Phân Tích Số Liệu)
        async function generateReport() {
            try {
                const res = await fetch('/api/generate-report', { method: 'POST' });
                const json = await res.json();
                if (json.success) {
                    const data = json.data;
                    globalState.reportData = data;
                    globalState.reportDone = true;

                    document.getElementById('badgeStep3').innerText = "Đã phân tích";
                    document.getElementById('badgeStep3').className = "text-[10px] px-1.5 py-0.5 rounded-full bg-emerald-100 text-emerald-700 font-semibold ml-1";

                    // Update System KPIs
                    const sum = data.system_summary;
                    document.getElementById('kpiNetRevenue').innerText = formatVND(sum.net_revenue);
                    document.getElementById('kpiGrossAndReturn').innerText = `Gross: ${formatVND(sum.gross_sales)} | Trả: ${formatVND(sum.return_amount)}`;
                    document.getElementById('kpiGrossProfit').innerText = formatVND(sum.gross_profit);
                    document.getElementById('kpiMargin').innerText = `Biên lãi gộp: ${sum.gross_margin}%`;

                    document.getElementById('kpiRevTargetPct').innerText = `${sum.rev_completion_pct}%`;
                    document.getElementById('progRevTarget').style.width = `${Math.min(sum.rev_completion_pct, 100)}%`;

                    document.getElementById('kpiGpTargetPct').innerText = `${sum.gp_completion_pct}%`;
                    document.getElementById('progGpTarget').style.width = `${Math.min(sum.gp_completion_pct, 100)}%`;

                    const momRevEl = document.getElementById('kpiRevMoM');
                    momRevEl.innerText = `${sum.rev_growth_mom > 0 ? '+' : ''}${sum.rev_growth_mom}%`;
                    momRevEl.className = `text-lg font-extrabold ${sum.rev_growth_mom >= 0 ? 'text-emerald-600' : 'text-rose-600'}`;

                    document.getElementById('kpiReturnRate').innerText = `${sum.return_rate}%`;
                    document.getElementById('kpiTotalReturnVal').innerText = `Giá trị trả: ${formatVND(sum.return_amount)}`;

                    // Render Store Table
                    renderStoresTable(data.store_reports);

                    // Render Charts
                    renderCharts();
                }
            } catch (err) {
                console.error("Lỗi tạo báo cáo: " + err);
            }
        }

        // Render Stores Table in Step 3
        function renderStoresTable(stores) {
            const tbody = document.getElementById('storesTableBody');
            tbody.innerHTML = '';

            stores.forEach(s => {
                const tr = document.createElement('tr');
                tr.className = "hover:bg-slate-50 transition text-xs";

                const isUrgent = s.store_id === 'ST09' || s.store_id === 'ST18' || s.store_id === 'ST05';
                const returnBadgeClass = s.return_rate >= 12 ? 'bg-rose-100 text-rose-700 font-bold' : (s.return_rate >= 8 ? 'bg-amber-100 text-amber-700' : 'text-slate-600');

                tr.innerHTML = `
                    <td class="py-2.5 px-3 font-mono font-bold ${isUrgent ? 'text-rose-600' : 'text-slate-800'}">${s.store_id}</td>
                    <td class="py-2.5 px-3 font-medium text-slate-800">${s.store_name}</td>
                    <td class="py-2.5 px-3 text-slate-500">${s.region}</td>
                    <td class="py-2.5 px-3 text-right font-semibold">${formatVND(s.net_revenue)}</td>
                    <td class="py-2.5 px-3 text-right font-semibold text-emerald-700">${formatVND(s.gross_profit)}</td>
                    <td class="py-2.5 px-3 text-center font-medium">${s.gross_margin}%</td>
                    <td class="py-2.5 px-3 text-center font-bold ${s.rev_completion_pct >= 95 ? 'text-blue-700' : 'text-slate-600'}">${s.rev_completion_pct}%</td>
                    <td class="py-2.5 px-3 text-center font-bold ${s.gp_completion_pct < 80 ? 'text-rose-600 bg-rose-50/50' : 'text-emerald-700'}">${s.gp_completion_pct}%</td>
                    <td class="py-2.5 px-3 text-center"><span class="px-2 py-0.5 rounded text-[11px] ${returnBadgeClass}">${s.return_rate}%</span></td>
                    <td class="py-2.5 px-3 text-center font-semibold ${s.rev_growth_mom < 0 ? 'text-rose-600' : 'text-slate-600'}">${s.rev_growth_mom > 0 ? '+' : ''}${s.rev_growth_mom}%</td>
                    <td class="py-2.5 px-3 text-center font-semibold ${s.gp_growth_mom < 0 ? 'text-rose-600' : 'text-emerald-700'}">${s.gp_growth_mom > 0 ? '+' : ''}${s.gp_growth_mom}%</td>
                `;
                tbody.appendChild(tr);
            });
        }

        function filterStoreTable() {
            const input = document.getElementById("tableFilterInput").value.toUpperCase();
            const rows = document.getElementById("storesTableBody").getElementsByTagName("tr");
            for (let i = 0; i < rows.length; i++) {
                const txt = rows[i].textContent || rows[i].innerText;
                rows[i].style.display = txt.toUpperCase().indexOf(input) > -1 ? "" : "none";
            }
        }

        // Render Charts using Chart.js in Step 3
        function renderCharts() {
            if (!globalState.reportData) return;
            const stores = globalState.reportData.store_reports;
            const labels = stores.map(s => s.store_id);

            // Chart 1: Doanh thu thực tế vs Mục tiêu
            const ctxRev = document.getElementById('chartStoreRevenue').getContext('2d');
            if (chartRevInstance) chartRevInstance.destroy();
            chartRevInstance = new Chart(ctxRev, {
                type: 'bar',
                data: {
                    labels: labels,
                    datasets: [
                        {
                            label: 'DT Thuần Thực Tế (Triệu)',
                            data: stores.map(s => Math.round(s.net_revenue / 1000000)),
                            backgroundColor: 'rgba(59, 130, 246, 0.85)',
                            borderRadius: 4
                        },
                        {
                            label: 'Mục Tiêu Doanh Thu (Triệu)',
                            data: stores.map(s => Math.round(s.target_revenue / 1000000)),
                            backgroundColor: 'rgba(203, 213, 225, 0.7)',
                            borderRadius: 4
                        }
                    ]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: { legend: { position: 'top', labels: { boxWidth: 12, font: { size: 10 } } } },
                    scales: { y: { beginAtZero: true } }
                }
            });

            // Chart 2: Lợi nhuận gộp vs Mục tiêu
            const ctxProfit = document.getElementById('chartStoreProfit').getContext('2d');
            if (chartProfitInstance) chartProfitInstance.destroy();
            chartProfitInstance = new Chart(ctxProfit, {
                type: 'bar',
                data: {
                    labels: labels,
                    datasets: [
                        {
                            label: 'Lợi Nhuận Gộp (Triệu)',
                            data: stores.map(s => Math.round(s.gross_profit / 1000000)),
                            backgroundColor: stores.map(s => s.gp_completion_pct < 80 ? 'rgba(225, 29, 72, 0.85)' : 'rgba(16, 185, 129, 0.85)'),
                            borderRadius: 4
                        },
                        {
                            label: 'Mục Tiêu LN Gộp (Triệu)',
                            data: stores.map(s => Math.round(s.target_gross_profit / 1000000)),
                            backgroundColor: 'rgba(203, 213, 225, 0.7)',
                            borderRadius: 4
                        }
                    ]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: { legend: { position: 'top', labels: { boxWidth: 12, font: { size: 10 } } } },
                    scales: { y: { beginAtZero: true } }
                }
            });

            // Chart 3: Donut cơ cấu ngành hàng
            const cats = globalState.reportData.category_summary;
            const ctxCat = document.getElementById('chartCategoryShare').getContext('2d');
            if (chartCategoryInstance) chartCategoryInstance.destroy();
            chartCategoryInstance = new Chart(ctxCat, {
                type: 'doughnut',
                data: {
                    labels: Object.keys(cats),
                    datasets: [{
                        data: Object.values(cats).map(c => c.revenue),
                        backgroundColor: [
                            '#3b82f6', // Ngành hàng 1
                            '#f59e0b', // Ngành hàng 2
                            '#10b981', // Ngành hàng 3
                            '#8b5cf6', // Ngành hàng 4
                            '#ec4899', // Ngành hàng 5
                            '#06b6d4'  // Ngành hàng 6
                        ]
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: { legend: { position: 'right', labels: { font: { size: 10 }, boxWidth: 12 } } }
                }
            });

            // Chart 4: Tỷ lệ đổi trả 18 cửa hàng
            const ctxRet = document.getElementById('chartStoreReturns').getContext('2d');
            if (chartReturnsInstance) chartReturnsInstance.destroy();
            chartReturnsInstance = new Chart(ctxRet, {
                type: 'bar',
                data: {
                    labels: labels,
                    datasets: [{
                        label: 'Tỷ Lệ Đổi Trả (%)',
                        data: stores.map(s => s.return_rate),
                        backgroundColor: stores.map(s => s.return_rate >= 12 ? '#e11d48' : (s.return_rate >= 8 ? '#f59e0b' : '#3b82f6')),
                        borderRadius: 4
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: { legend: { display: false } },
                    scales: { y: { beginAtZero: true, max: 20 } }
                }
            });
        }

        // 4. BƯỚC 4: Cross-check Audit & Xuất Kết Quả
        async function runCrossCheckAudit() {
            try {
                const res = await fetch('/api/cross-check-audit', { method: 'POST' });
                const json = await res.json();
                if (json.success) {
                    const audit = json.data;
                    globalState.auditData = audit;
                    globalState.auditDone = true;

                    document.getElementById('badgeStep4').innerText = "Đã đối soát";
                    document.getElementById('badgeStep4').className = "text-[10px] px-1.5 py-0.5 rounded-full bg-emerald-100 text-emerald-700 font-semibold ml-1";

                    // 1. Render Integrity Checks
                    const chkContainer = document.getElementById('integrityChecksContainer');
                    chkContainer.innerHTML = '';
                    audit.integrity_checks.forEach(c => {
                        const div = document.createElement('div');
                        div.className = "p-3 rounded-lg bg-emerald-50/70 border border-emerald-200 text-xs";
                        div.innerHTML = `
                            <div class="flex items-center justify-between font-bold text-emerald-900">
                                <span>${c.check_name}</span>
                                <span class="text-[10px] bg-emerald-200 text-emerald-900 px-1.5 py-0.5 rounded font-bold">MATCHED</span>
                            </div>
                            <div class="mt-2 space-y-1 text-slate-600 font-mono">
                                <div>Sheet sạch: <b>${typeof c.sheet_value === 'number' && c.sheet_value > 1000 ? formatVND(c.sheet_value) : formatNumber(c.sheet_value)}</b></div>
                                <div>Báo cáo: <b>${typeof c.report_value === 'number' && c.report_value > 1000 ? formatVND(c.report_value) : formatNumber(c.report_value)}</b></div>
                                <div class="text-emerald-700 font-sans text-[11px] pt-1 border-t border-emerald-200/50">
                                    <i class="fa-solid fa-check mr-1"></i> ${c.message}
                                </div>
                            </div>
                        `;
                        chkContainer.appendChild(div);
                    });

                    // 2. Render Executive Insights List
                    const insList = document.getElementById('executiveInsightsList');
                    insList.innerHTML = '';
                    audit.executive_summary_insights.forEach(ins => {
                        const li = document.createElement('li');
                        li.innerText = ins;
                        insList.appendChild(li);
                    });

                    // 3. Render Priority Stores Grid
                    const grid = document.getElementById('priorityStoresGrid');
                    grid.innerHTML = '';

                    audit.priority_stores.forEach(p => {
                        const card = document.createElement('div');
                        const isP1 = p.priority_level === 'P1_URGENT';
                        const isP2 = p.priority_level === 'P2_SUPPORT';
                        const borderClass = isP1 ? 'border-rose-400 ring-2 ring-rose-200 bg-white' : (isP2 ? 'border-amber-300 bg-white' : 'border-slate-200 bg-white');

                        let issuesHtml = '';
                        p.issues.forEach(iss => {
                            issuesHtml += `
                                <div class="p-2 rounded bg-rose-50 border border-rose-200 text-[11px] text-rose-900">
                                    <span class="font-bold flex items-center"><i class="fa-solid fa-triangle-exclamation mr-1 text-rose-600"></i> ${iss.title}</span>
                                    <p class="mt-0.5 text-slate-700">${iss.detail}</p>
                                </div>
                            `;
                        });

                        let recsHtml = '';
                        p.ai_recommendations.forEach(r => {
                            recsHtml += `<li class="text-[11px] text-slate-700">${r}</li>`;
                        });

                        card.className = `rounded-xl border ${borderClass} shadow-sm p-4 space-y-3 transition hover:shadow-md`;
                        card.innerHTML = `
                            <div class="flex justify-between items-start border-b border-slate-100 pb-2.5">
                                <div>
                                    <div class="flex items-center space-x-2">
                                        <span class="font-bold text-sm text-slate-900">${p.store_name}</span>
                                        <span class="font-mono text-xs text-slate-400 font-bold">(${p.store_id})</span>
                                    </div>
                                    <p class="text-[11px] text-slate-500">${p.region} • Quản lý: ${p.manager}</p>
                                </div>
                                <span class="px-2 py-0.5 rounded text-[10px] font-bold ${p.priority_badge}">
                                    ${p.priority_label}
                                </span>
                            </div>

                            <div class="grid grid-cols-2 gap-2 text-xs">
                                <div class="bg-slate-50 p-2 rounded">
                                    <span class="text-slate-500 text-[10px] block">Doanh Thu Thuần</span>
                                    <span class="font-bold text-slate-800">${formatVND(p.net_revenue)}</span>
                                    <span class="text-[10px] text-blue-600 font-semibold block">Đạt ${p.rev_completion_pct}%</span>
                                </div>
                                <div class="bg-slate-50 p-2 rounded">
                                    <span class="text-slate-500 text-[10px] block">Lợi Nhuận Gộp</span>
                                    <span class="font-bold text-emerald-700">${formatVND(p.gross_profit)}</span>
                                    <span class="text-[10px] ${p.gp_completion_pct < 80 ? 'text-rose-600 font-bold' : 'text-emerald-700 font-semibold'} block">Đạt ${p.gp_completion_pct}%</span>
                                </div>
                            </div>

                            <div class="flex justify-between items-center text-xs px-1">
                                <span class="text-slate-500">Tỷ lệ đổi trả:</span>
                                <span class="font-bold ${p.return_rate >= 12 ? 'text-rose-600' : (p.return_rate >= 8 ? 'text-amber-600' : 'text-slate-700')}">${p.return_rate}%</span>
                            </div>

                            ${p.issues.length > 0 ? `<div class="space-y-1.5">${issuesHtml}</div>` : ''}

                            <div class="pt-2 border-t border-slate-100">
                                <span class="font-bold text-[11px] text-indigo-900 flex items-center mb-1">
                                    <i class="fa-solid fa-wand-magic-sparkles mr-1 text-indigo-600"></i> Khuyến Nghị AI Cho Giám Đốc:
                                </span>
                                <ul class="list-disc list-inside space-y-1">
                                    ${recsHtml}
                                </ul>
                            </div>

                            <button onclick="openDecisionModal('${p.store_id}')" class="w-full mt-2 py-1.5 rounded-lg border border-emerald-500 text-emerald-700 hover:bg-emerald-50 font-semibold text-xs transition flex items-center justify-center space-x-1">
                                <i class="fa-solid fa-file-signature"></i>
                                <span>Ký Quyết Định Hỗ Trợ Riêng Cửa Hàng Này</span>
                            </button>
                        `;
                        grid.appendChild(card);
                    });

                    // Populate Checkboxes in Decision Modal
                    populateDecisionModalCheckboxes(audit.priority_stores);

                    // Load past decisions
                    loadDecisionsList();
                }
            } catch (err) {
                console.error("Lỗi đối soát: " + err);
            }
        }

        // Decision Modal Helpers
        function populateDecisionModalCheckboxes(stores) {
            const container = document.getElementById('decisionStoreCheckboxes');
            container.innerHTML = '';

            stores.forEach(s => {
                const isUrgent = s.priority_level === 'P1_URGENT';
                const label = document.createElement('label');
                label.className = `flex items-center space-x-1.5 text-xs p-1 rounded hover:bg-slate-50 cursor-pointer ${isUrgent ? 'font-bold text-rose-700' : 'text-slate-700'}`;
                label.innerHTML = `
                    <input type="checkbox" name="selectedStores" value="${s.store_id}" ${isUrgent ? 'checked' : ''} class="rounded text-blue-600">
                    <span>${s.store_id} - ${s.store_name}</span>
                `;
                container.appendChild(label);
            });
        }

        function openDecisionModal(preselectedStoreId = null) {
            document.getElementById('decisionModal').classList.remove('hidden');
            if (preselectedStoreId) {
                const checkboxes = document.querySelectorAll('input[name="selectedStores"]');
                checkboxes.forEach(cb => {
                    cb.checked = (cb.value === preselectedStoreId);
                });
            }
            applyDecisionPreset();
        }

        function closeDecisionModal() {
            document.getElementById('decisionModal').classList.add('hidden');
        }

        function applyDecisionPreset() {
            const val = document.getElementById('decActionPreset').value;
            const planEl = document.getElementById('decActionPlan');

            if (val === 'p1_combo') {
                planEl.value = "1. Đối với ST09 (Bắc Từ Liêm): Rà soát ngay hạn sử dụng và quy trình kiểm định hàng nhập (lý do đổi trả: Hết hạn, Hư bao bì); đào tạo kỹ năng tư vấn chuẩn xác.\\n2. Đối với ST18 (Cần Thơ): Cử Chuyên viên Bán lẻ Vùng Miền Nam trực tiếp hỗ trợ thị trường; giải ngân 30 triệu VNĐ gói khuyến mại Combo Bỉm Sữa kích cầu để chặn đà sụt giảm MoM (-46.6%).";
            } else if (val === 'sales_boost') {
                planEl.value = "Hỗ trợ gói Marketing Local và huấn luyện kỹ năng Cross-sell/Upsell các mặt hàng biên lãi cao (Thời trang, Đồ chơi) cho ST12 (Bắc Ninh), ST15 (Nha Trang) và ST16 (Quận 1).";
            } else if (val === 'all_urgent') {
                planEl.value = "Kế hoạch can thiệp toàn diện cho nhóm P1 (ST09, ST05, ST18, ST12): Rà soát tồn kho cận date, hỗ trợ ngân sách truyền thông và điều chỉnh cơ cấu trưng bày quầy kệ.";
            }
        }

        async function submitExecutiveDecision(e) {
            e.preventDefault();
            const selectedStores = Array.from(document.querySelectorAll('input[name="selectedStores"]:checked')).map(cb => cb.value);
            if (selectedStores.length === 0) {
                alert("Vui lòng chọn ít nhất một cửa hàng!");
                return;
            }

            const payload = {
                store_ids: selectedStores,
                action_plan: document.getElementById('decActionPlan').value,
                assigned_lead: document.getElementById('decAssignedLead').value,
                budget: document.getElementById('decBudget').value,
                notes: document.getElementById('decNotes').value
            };

            try {
                const res = await fetch('/api/executive-decision', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify(payload)
                });
                const json = await res.json();
                if (json.success) {
                    alert(`✅ ${json.message}`);
                    closeDecisionModal();
                    confetti({ particleCount: 70, spread: 80, origin: { y: 0.5 } });
                    loadDecisionsList();
                } else {
                    alert("Lỗi: " + json.error);
                }
            } catch (err) {
                alert("Lỗi kết nối: " + err);
            }
        }

        async function loadDecisionsList() {
            try {
                const res = await fetch('/api/decisions-list');
                const json = await res.json();
                if (json.success && json.data.length > 0) {
                    document.getElementById('decisionsCountBadge').innerText = `${json.data.length} quyết định`;
                    const container = document.getElementById('decisionsHistoryContainer');
                    container.innerHTML = '';

                    json.data.forEach(d => {
                        const div = document.createElement('div');
                        div.className = "p-4 rounded-xl border border-blue-200 bg-blue-50/40 text-xs space-y-2";
                        const storeList = d.stores.map(s => `<span class="px-2 py-0.5 rounded bg-blue-100 text-blue-800 font-semibold mr-1">${s.store_id}: ${s.store_name}</span>`).join(' ');

                        div.innerHTML = `
                            <div class="flex justify-between items-center border-b border-blue-100 pb-2">
                                <div class="flex items-center space-x-2">
                                    <i class="fa-solid fa-stamp text-blue-600 text-base"></i>
                                    <span class="font-bold text-sm text-blue-950">${d.decision_id}</span>
                                    <span class="px-2 py-0.5 rounded-full bg-emerald-100 text-emerald-800 font-bold text-[10px]">ĐANG TRIỂN KHAI</span>
                                </div>
                                <span class="text-slate-400 text-[11px]">${d.decision_date}</span>
                            </div>
                            <div>
                                <span class="font-semibold text-slate-700">Cửa hàng thụ hưởng hỗ trợ:</span>
                                <div class="mt-1 flex flex-wrap gap-1">${storeList}</div>
                            </div>
                            <div class="text-slate-700 bg-white p-2.5 rounded border border-slate-200 leading-relaxed font-mono whitespace-pre-line">${d.action_plan}</div>
                            <div class="flex justify-between items-center text-slate-500 pt-1 text-[11px]">
                                <span>Phụ trách: <b>${d.assigned_lead}</b></span>
                                <span>Ngân sách: <b class="text-emerald-700 font-semibold">${formatVND(d.allocated_budget)}</b></span>
                            </div>
                        `;
                        container.appendChild(div);
                    });
                }
            } catch (err) {
                console.error(err);
            }
        }

        // 5. AI Copilot Chatbot Handler
        async function handleChatSubmit(e) {
            e.preventDefault();
            const input = document.getElementById('chatInput');
            const msg = input.value.trim();
            if (!msg) return;

            appendChatMessage('user', msg);
            input.value = '';

            try {
                const res = await fetch('/api/chat', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({ message: msg })
                });
                const json = await res.json();
                if (json.success) {
                    appendChatMessage('agent', json.reply);
                } else {
                    appendChatMessage('agent', 'Xin lỗi, đã xảy ra lỗi trong quá trình xử lý câu hỏi.');
                }
            } catch (err) {
                appendChatMessage('agent', 'Lỗi kết nối máy chủ: ' + err);
            }
        }

        function quickAsk(question) {
            document.getElementById('chatInput').value = question;
            switchTab('copilot');
            setTimeout(() => {
                document.getElementById('btnSendChat').click();
            }, 300);
        }

        function appendChatMessage(sender, text) {
            const container = document.getElementById('chatMessages');
            const div = document.createElement('div');
            div.className = `flex items-start space-x-3 ${sender === 'user' ? 'justify-end' : ''}`;

            if (sender === 'user') {
                div.innerHTML = `
                    <div class="bg-blue-600 text-white p-3 rounded-2xl rounded-tr-none max-w-lg leading-relaxed shadow-sm">
                        ${text}
                    </div>
                    <div class="w-8 h-8 rounded-full bg-slate-200 text-slate-600 flex items-center justify-center flex-shrink-0 text-xs font-bold">
                        Tôi
                    </div>
                `;
            } else {
                let formatted = text
                    .replace(/### (.*?)\\n/g, '<h4 class="font-bold text-sm text-indigo-950 mb-1">$1</h4>')
                    .replace(/#### (.*?)\\n/g, '<h5 class="font-bold text-xs text-indigo-900 mt-2 mb-0.5">$1</h5>')
                    .replace(/\\*\\*(.*?)\\*\\*/g, '<b>$1</b>')
                    .replace(/`(.*?)`/g, '<code class="bg-slate-100 text-indigo-800 px-1 py-0.5 rounded font-mono text-[11px]">$1</code>')
                    .replace(/\\n\\n/g, '<br><br>')
                    .replace(/\\n/g, '<br>');

                div.innerHTML = `
                    <div class="w-8 h-8 rounded-full bg-indigo-600 text-white flex items-center justify-center flex-shrink-0 text-xs">
                        <i class="fa-solid fa-robot"></i>
                    </div>
                    <div class="bg-white border border-slate-200 text-slate-800 p-3.5 rounded-2xl rounded-tl-none max-w-2xl leading-relaxed shadow-sm">
                        ${formatted}
                    </div>
                `;
            }

            container.appendChild(div);
            container.scrollTop = container.scrollHeight;
        }

        // On Page Load: initialize state with uploaded data by default
        window.addEventListener('DOMContentLoaded', () => {
            // Automatically load uploaded data on startup
            loadUploadedData();
        });
    </script>
</body>
</html>
'''

with open('app/templates/index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("SUCCESS: index.html has been updated with the 4 operational steps!")
