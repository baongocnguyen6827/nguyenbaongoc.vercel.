# -*- coding: utf-8 -*-
"""
Script to update app/templates/index.html with correct keys for executeCleaning.
"""

with open('update_template.py', 'r', encoding='utf-8') as f:
    content = f.read()

target_cleaning = '''        // 2. BƯỚC 2: Execute Cleaning (Làm Sạch & Chuẩn Hóa)
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

                    // Update stats
                    document.getElementById('statRemovedRows').innerText = `${formatNumber(d.cleaning_summary.duplicates_removed + d.cleaning_summary.out_of_period_removed)} dòng`;
                    document.getElementById('statRemovedValue').innerText = `Lệch kỳ & trùng: đã bóc tách`;
                    
                    document.getElementById('statCancelReturn').innerText = `${formatNumber(d.cleaning_summary.cancelled_removed + d.cleaning_summary.returns_handled)} đơn`;
                    document.getElementById('statReturnImpact').innerText = `Khấu trừ DT: -${formatVND(d.cleaning_summary.return_amount_deducted)}`;

                    document.getElementById('statCleanedRows').innerText = `${formatNumber(d.cleaning_summary.final_cleaned_rows)} dòng`;
                    document.getElementById('statNetRevP1').innerText = `DT thuần: ${formatVND(d.cleaning_summary.net_revenue)}`;

                    document.getElementById('cleanTimestamp').innerText = `Hoàn tất: ${d.cleaned_timestamp}`;
                    document.getElementById('badgeStep2').innerText = "Đã làm sạch";
                    document.getElementById('badgeStep2').className = "text-[10px] px-1.5 py-0.5 rounded-full bg-emerald-100 text-emerald-700 font-semibold ml-1";

                    // Render Cleaning Log
                    const logContainer = document.getElementById('cleaningLogContainer');
                    const log = d.cleaning_log;
                    logContainer.innerHTML = `
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
                            <div class="p-3 bg-emerald-50 border border-emerald-200 rounded-lg flex items-start space-x-2.5">
                                <i class="fa-solid fa-check-circle text-emerald-600 mt-0.5 text-sm"></i>
                                <div>
                                    <span class="font-bold text-emerald-900">1. Lọc đơn trùng lặp (RULE-DEDUP):</span>
                                    <p class="text-emerald-800">Đã phát hiện và loại bỏ <b>${formatNumber(log.deduplication.duplicates_removed)}</b> dòng giao dịch bị ghi nhận lặp.</p>
                                </div>
                            </div>

                            <div class="p-3 bg-emerald-50 border border-emerald-200 rounded-lg flex items-start space-x-2.5">
                                <i class="fa-solid fa-check-circle text-emerald-600 mt-0.5 text-sm"></i>
                                <div>
                                    <span class="font-bold text-emerald-900">2. Đồng bộ kỳ thời gian (RULE-PERIOD-SYNC):</span>
                                    <p class="text-emerald-800">Tách riêng <b>${formatNumber(log.period_sync.out_of_period_rows)}</b> dòng giao dịch kỳ trước để so sánh chính xác.</p>
                                </div>
                            </div>

                            <div class="p-3 bg-emerald-50 border border-emerald-200 rounded-lg flex items-start space-x-2.5">
                                <i class="fa-solid fa-check-circle text-emerald-600 mt-0.5 text-sm"></i>
                                <div>
                                    <span class="font-bold text-emerald-900">3. Loại bỏ đơn bị huỷ (RULE-CANCEL):</span>
                                    <p class="text-emerald-800">Tách rời <b>${formatNumber(log.cancelled_filter.cancelled_rows)}</b> đơn CANCELLED ra khỏi doanh thu (${formatVND(log.cancelled_filter.cancelled_amount)}).</p>
                                </div>
                            </div>

                            <div class="p-3 bg-emerald-50 border border-emerald-200 rounded-lg flex items-start space-x-2.5">
                                <i class="fa-solid fa-check-circle text-emerald-600 mt-0.5 text-sm"></i>
                                <div>
                                    <span class="font-bold text-emerald-900">4. Xử lý hàng đổi trả (RULE-RETURN):</span>
                                    <p class="text-emerald-800">Khấu trừ <b>${formatNumber(log.returns_handling.returned_rows)}</b> đơn RETURNED khỏi doanh thu gộp và hoàn nhập giá vốn kho.</p>
                                </div>
                            </div>
                        </div>
                    `;'''

replacement_cleaning = '''        // 2. BƯỚC 2: Execute Cleaning (Làm Sạch & Chuẩn Hóa)
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
                    `;'''

if target_cleaning in content:
    content = content.replace(target_cleaning, replacement_cleaning)
    with open('update_template.py', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated update_template.py successfully")
else:
    print("Could not find target_cleaning in update_template.py")

