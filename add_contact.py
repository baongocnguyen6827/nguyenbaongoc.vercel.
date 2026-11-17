# add_contact.py
import re

html_path = r"c:\Users\ADMIN\OneDrive\Attachments\Thi cuối môn AI301\app\templates\index.html"
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Add "Liên Hệ" button in Top Header
target_theme_btn = """                    <!-- Theme Switcher Button (Light / Dark) -->
                    <button id="themeToggleBtn" """

contact_header_btn = """                    <!-- Contact Quick Button -->
                    <button onclick="openContactModal()" class="flex items-center gap-1.5 px-3 py-2 rounded-2xl border border-slate-200 dark:border-slate-700 bg-slate-50 dark:bg-slate-800 hover:bg-rose-50 dark:hover:bg-slate-700 text-slate-700 dark:text-slate-200 hover:text-rose-600 font-bold text-xs transition cursor-pointer shadow-xs" title="Thông tin liên hệ / Contact Info">
                        <i class="fa-solid fa-headset text-rose-500"></i>
                        <span class="hidden sm:inline" data-i18n="contact_btn">Liên Hệ</span>
                    </button>

                    <!-- Theme Switcher Button (Light / Dark) -->
                    <button id="themeToggleBtn" """

if target_theme_btn in content:
    content = content.replace(target_theme_btn, contact_header_btn, 1)
    print("Header Contact Button added successfully")
else:
    print("Warning: target_theme_btn not found")

# 2. Add modern Frosted Glass Footer right after </main>
target_main_end = "</main>\n    </div>"

footer_html = """</main>

        <!-- ===================================================================== -->
        <!-- 3. FOOTER: THÔNG TIN LIÊN HỆ & BẢN QUYỀN HỆ THỐNG                     -->
        <!-- ===================================================================== -->
        <footer class="w-full mt-12 border-t border-white/80 dark:border-white/10 bg-white/60 dark:bg-slate-900/60 backdrop-blur-2xl transition-colors">
            <div class="max-w-[1700px] mx-auto px-4 sm:px-7 py-8">
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
                    
                    <!-- Col 1: System Info & Brand -->
                    <div class="space-y-3">
                        <div class="flex items-center gap-3">
                            <div class="w-10 h-10 rounded-2xl btn-pink-pill flex items-center justify-center text-lg shadow-md">
                                <i class="fa-solid fa-cubes"></i>
                            </div>
                            <div>
                                <div class="flex items-center gap-1.5">
                                    <span class="font-extrabold text-[17px] text-slate-900 dark:text-white tracking-tight">Bảo Ngọc</span>
                                    <span class="px-2 py-0.5 text-[10px] font-extrabold rounded-full bg-rose-100 text-rose-600 uppercase">AI</span>
                                </div>
                                <p class="text-[11px] font-medium text-slate-400">Retail Agent OS</p>
                            </div>
                        </div>
                        <p class="text-xs text-slate-500 dark:text-slate-400 leading-relaxed" data-i18n="footer_about">
                            Hệ thống AI Agent tự động hóa phân tích chuỗi bán lẻ, đối soát dữ liệu doanh thu, bóc tách đơn hủy &amp; đổi trả, đo lường CSAT khách hàng và đề xuất kịch bản tăng trưởng thông minh.
                        </p>
                        <div class="flex items-center gap-2 pt-1">
                            <span class="w-2.5 h-2.5 rounded-full bg-emerald-500 live-dot"></span>
                            <span class="text-[11px] font-extrabold text-emerald-600 dark:text-emerald-400">Hệ Thống Trực Tuyến 24/7 (Live v2.6.4)</span>
                        </div>
                    </div>

                    <!-- Col 2: Contact Information (User Requested) -->
                    <div class="space-y-3">
                        <h4 class="text-xs font-black uppercase tracking-wider text-rose-600 dark:text-rose-400 flex items-center gap-2">
                            <i class="fa-solid fa-address-book"></i>
                            <span data-i18n="contact_title">Thông Tin Liên Hệ</span>
                        </h4>
                        <ul class="space-y-2.5 text-xs">
                            <!-- Phone -->
                            <li class="flex items-start gap-2.5">
                                <span class="w-7 h-7 rounded-xl bg-rose-100 text-rose-600 dark:bg-rose-950/60 dark:text-rose-400 flex items-center justify-center flex-shrink-0 mt-0.5">
                                    <i class="fa-solid fa-phone text-[11px]"></i>
                                </span>
                                <div>
                                    <span class="text-slate-400 font-medium text-[10px] block" data-i18n="contact_phone_lbl">Số điện thoại:</span>
                                    <a href="tel:0362848956" class="font-extrabold text-slate-800 dark:text-slate-100 hover:text-rose-600 transition tracking-wide text-[13px]">
                                        0362848956
                                    </a>
                                </div>
                            </li>

                            <!-- Email -->
                            <li class="flex items-start gap-2.5">
                                <span class="w-7 h-7 rounded-xl bg-amber-100 text-amber-600 dark:bg-amber-950/60 dark:text-amber-400 flex items-center justify-center flex-shrink-0 mt-0.5">
                                    <i class="fa-solid fa-envelope text-[11px]"></i>
                                </span>
                                <div>
                                    <span class="text-slate-400 font-medium text-[10px] block" data-i18n="contact_email_lbl">Email:</span>
                                    <a href="mailto:baongocnguyen686827@gmail.com" class="font-bold text-slate-800 dark:text-slate-100 hover:text-rose-600 transition break-all text-xs">
                                        baongocnguyen686827@gmail.com
                                    </a>
                                </div>
                            </li>

                            <!-- Address -->
                            <li class="flex items-start gap-2.5">
                                <span class="w-7 h-7 rounded-xl bg-emerald-100 text-emerald-600 dark:bg-emerald-950/60 dark:text-emerald-400 flex items-center justify-center flex-shrink-0 mt-0.5">
                                    <i class="fa-solid fa-location-dot text-[11px]"></i>
                                </span>
                                <div>
                                    <span class="text-slate-400 font-medium text-[10px] block" data-i18n="contact_address_lbl">Địa chỉ:</span>
                                    <span class="font-extrabold text-slate-800 dark:text-slate-100" data-i18n="contact_address_val">
                                        Hà Nội, Việt Nam
                                    </span>
                                </div>
                            </li>
                        </ul>
                    </div>

                    <!-- Col 3: Lead Administrator -->
                    <div class="space-y-3">
                        <h4 class="text-xs font-black uppercase tracking-wider text-rose-600 dark:text-rose-400 flex items-center gap-2">
                            <i class="fa-solid fa-user-shield"></i>
                            <span data-i18n="contact_manager_title">Nhân Sự Phụ Trách</span>
                        </h4>
                        <div class="p-3.5 rounded-2xl os-card border border-rose-200/80 dark:border-slate-700 space-y-2">
                            <div class="flex items-center gap-3">
                                <div class="w-10 h-10 rounded-full bg-rose-100 text-rose-600 font-black text-xs flex items-center justify-center border border-rose-200 flex-shrink-0">
                                    BN
                                </div>
                                <div class="leading-tight">
                                    <p class="font-extrabold text-xs text-slate-900 dark:text-white">Nguyễn Bảo Ngọc</p>
                                    <p class="text-[10px] text-rose-600 dark:text-rose-400 font-bold mt-0.5">Bảo Ngọc Retail</p>
                                </div>
                            </div>
                            <p class="text-[11px] text-slate-500 dark:text-slate-400 leading-tight">
                                Quản trị Vận hành Hệ thống AI &amp; Kiểm soát Dữ liệu Chuỗi Bán lẻ.
                            </p>
                            <div class="pt-1 flex items-center gap-2">
                                <a href="tel:0362848956" class="px-2.5 py-1.5 rounded-xl bg-rose-50 hover:bg-rose-100 text-rose-600 font-bold text-[10px] transition flex items-center gap-1 cursor-pointer">
                                    <i class="fa-solid fa-phone"></i>
                                    <span>Gọi Ngay</span>
                                </a>
                                <a href="mailto:baongocnguyen686827@gmail.com" class="px-2.5 py-1.5 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold text-[10px] transition flex items-center gap-1 cursor-pointer">
                                    <i class="fa-solid fa-envelope"></i>
                                    <span>Gửi Mail</span>
                                </a>
                            </div>
                        </div>
                    </div>

                    <!-- Col 4: Quick Action & Support Hours -->
                    <div class="space-y-3">
                        <h4 class="text-xs font-black uppercase tracking-wider text-rose-600 dark:text-rose-400 flex items-center gap-2">
                            <i class="fa-solid fa-clock"></i>
                            <span data-i18n="contact_hours_title">Khung Giờ Hỗ Trợ</span>
                        </h4>
                        <div class="text-xs space-y-2 text-slate-600 dark:text-slate-300">
                            <p class="flex items-center justify-between">
                                <span class="text-slate-400 font-medium">Thứ Hai - Thứ Sáu:</span>
                                <b class="font-bold">08:00 - 22:00</b>
                            </p>
                            <p class="flex items-center justify-between">
                                <span class="text-slate-400 font-medium">Thứ Bảy - Chủ Nhật:</span>
                                <b class="font-bold">08:30 - 21:00</b>
                            </p>
                            <p class="flex items-center justify-between border-t border-pink-100 dark:border-slate-800 pt-1.5">
                                <span class="text-slate-400 font-medium">Hỗ trợ khẩn cấp:</span>
                                <b class="text-rose-600 font-extrabold">24/7 Hotline</b>
                            </p>
                        </div>
                        <button onclick="openContactModal()" class="w-full mt-2 py-2 px-3 rounded-xl btn-pink-pill text-xs font-bold flex items-center justify-center gap-2 cursor-pointer shadow-md">
                            <i class="fa-solid fa-paper-plane"></i>
                            <span>Liên Hệ Trực Tiếp Với Bảo Ngọc</span>
                        </button>
                    </div>

                </div>

                <!-- Bottom Copyright Line -->
                <div class="mt-8 pt-5 border-t border-pink-100/80 dark:border-slate-800 flex flex-col sm:flex-row items-center justify-between gap-3 text-xs text-slate-400 font-medium">
                    <p>© 2026 Bảo Ngọc Retail AI. Tất cả quyền được bảo lưu.</p>
                    <div class="flex items-center gap-4">
                        <span class="flex items-center gap-1.5">
                            <i class="fa-solid fa-location-dot text-rose-500"></i>
                            <span class="font-bold text-slate-600 dark:text-slate-300">Hà Nội</span>
                        </span>
                        <span>•</span>
                        <a href="tel:0362848956" class="hover:text-rose-600 transition font-bold text-slate-600 dark:text-slate-300">0362848956</a>
                        <span>•</span>
                        <a href="mailto:baongocnguyen686827@gmail.com" class="hover:text-rose-600 transition font-bold text-slate-600 dark:text-slate-300">baongocnguyen686827@gmail.com</a>
                    </div>
                </div>
            </div>
        </footer>
    </div>"""

if target_main_end in content:
    content = content.replace(target_main_end, footer_html, 1)
    print("Footer with Contact Details added successfully")
else:
    print("Warning: target_main_end not found")

# 3. Add Contact Modal (#contactModal) right before </body>
modal_html = """    <!-- ===================================================================== -->
    <!-- MODAL: THÔNG TIN LIÊN HỆ CHI TIẾT (CONTACT MODAL)                     -->
    <!-- ===================================================================== -->
    <div id="contactModal" class="fixed inset-0 z-50 hidden items-center justify-center p-4 bg-slate-900/40 backdrop-blur-md">
        <div class="os-card rounded-3xl shadow-2xl border border-white/90 dark:border-slate-700 max-w-lg w-full overflow-hidden flex flex-col view-fade">
            <!-- Header -->
            <div class="p-5 bg-gradient-to-r from-rose-500 via-pink-500 to-rose-600 text-white flex items-center justify-between">
                <div class="flex items-center gap-3">
                    <div class="w-10 h-10 rounded-2xl bg-white/20 flex items-center justify-center text-lg">
                        <i class="fa-solid fa-address-card"></i>
                    </div>
                    <div>
                        <h3 class="font-black text-base" data-i18n="contact_title">Thông Tin Liên Hệ</h3>
                        <p class="text-xs text-rose-100 font-medium">Bảo Ngọc AI — Retail Agent OS</p>
                    </div>
                </div>
                <button onclick="closeContactModal()" class="w-8 h-8 rounded-full bg-white/20 hover:bg-white/30 flex items-center justify-center transition cursor-pointer">
                    <i class="fa-solid fa-xmark text-sm"></i>
                </button>
            </div>

            <!-- Body -->
            <div class="p-6 space-y-5">
                <!-- User Profile Card -->
                <div class="flex items-center gap-3.5 p-3.5 rounded-2xl bg-rose-50/60 dark:bg-slate-800/60 border border-rose-100 dark:border-slate-700">
                    <div class="w-12 h-12 rounded-full bg-rose-200 text-rose-700 font-black text-base flex items-center justify-center border-2 border-white shadow-xs">
                        BN
                    </div>
                    <div>
                        <h4 class="font-extrabold text-sm text-slate-900 dark:text-white">Nguyễn Bảo Ngọc</h4>
                        <p class="text-xs text-rose-600 dark:text-rose-400 font-bold">Bảo Ngọc Retail</p>
                        <p class="text-[11px] text-slate-400 font-medium">Khu vực: Hà Nội, Việt Nam</p>
                    </div>
                </div>

                <!-- Detail List -->
                <div class="space-y-3 text-xs">
                    <!-- Phone -->
                    <div class="flex items-center justify-between p-3.5 rounded-2xl bg-white/80 dark:bg-slate-800/80 border border-slate-200/80 dark:border-slate-700">
                        <div class="flex items-center gap-3">
                            <span class="w-9 h-9 rounded-xl bg-rose-100 text-rose-600 dark:bg-rose-950/60 dark:text-rose-400 flex items-center justify-center text-sm">
                                <i class="fa-solid fa-phone"></i>
                            </span>
                            <div>
                                <span class="text-[10px] text-slate-400 font-bold uppercase block" data-i18n="contact_phone_lbl">Số điện thoại</span>
                                <a href="tel:0362848956" class="font-black text-slate-900 dark:text-white text-sm hover:text-rose-600 transition">
                                    0362848956
                                </a>
                            </div>
                        </div>
                        <a href="tel:0362848956" class="px-3 py-1.5 rounded-xl bg-rose-500 hover:bg-rose-600 text-white font-bold text-xs transition flex items-center gap-1.5 shadow-sm">
                            <i class="fa-solid fa-phone-volume text-[11px]"></i>
                            <span>Gọi Ngay</span>
                        </a>
                    </div>

                    <!-- Email -->
                    <div class="flex items-center justify-between p-3.5 rounded-2xl bg-white/80 dark:bg-slate-800/80 border border-slate-200/80 dark:border-slate-700">
                        <div class="flex items-center gap-3 min-w-0 pr-2">
                            <span class="w-9 h-9 rounded-xl bg-amber-100 text-amber-600 dark:bg-amber-950/60 dark:text-amber-400 flex items-center justify-center text-sm flex-shrink-0">
                                <i class="fa-solid fa-envelope"></i>
                            </span>
                            <div class="min-w-0">
                                <span class="text-[10px] text-slate-400 font-bold uppercase block" data-i18n="contact_email_lbl">Email hỗ trợ</span>
                                <a href="mailto:baongocnguyen686827@gmail.com" class="font-extrabold text-slate-900 dark:text-white text-xs hover:text-rose-600 transition truncate block">
                                    baongocnguyen686827@gmail.com
                                </a>
                            </div>
                        </div>
                        <div class="flex items-center gap-1.5 flex-shrink-0">
                            <button onclick="copyContactEmail()" title="Sao chép email" class="px-2.5 py-1.5 rounded-xl border border-slate-200 hover:bg-slate-100 text-slate-700 dark:text-slate-200 font-bold text-xs transition cursor-pointer">
                                <i class="fa-regular fa-copy"></i>
                            </button>
                            <a href="mailto:baongocnguyen686827@gmail.com" class="px-3 py-1.5 rounded-xl bg-amber-500 hover:bg-amber-600 text-white font-bold text-xs transition flex items-center gap-1.5 shadow-sm">
                                <i class="fa-solid fa-paper-plane text-[11px]"></i>
                                <span>Gửi Mail</span>
                            </a>
                        </div>
                    </div>

                    <!-- Address -->
                    <div class="flex items-center gap-3 p-3.5 rounded-2xl bg-white/80 dark:bg-slate-800/80 border border-slate-200/80 dark:border-slate-700">
                        <span class="w-9 h-9 rounded-xl bg-emerald-100 text-emerald-600 dark:bg-emerald-950/60 dark:text-emerald-400 flex items-center justify-center text-sm flex-shrink-0">
                            <i class="fa-solid fa-location-dot"></i>
                        </span>
                        <div>
                            <span class="text-[10px] text-slate-400 font-bold uppercase block" data-i18n="contact_address_lbl">Địa chỉ hoạt động</span>
                            <span class="font-black text-slate-900 dark:text-white text-xs block" data-i18n="contact_address_val">
                                Hà Nội, Việt Nam
                            </span>
                            <span class="text-[10px] text-slate-400 font-medium">Trung tâm Điều hành &amp; Quản trị Chuỗi Bán lẻ</span>
                        </div>
                    </div>
                </div>

                <!-- Footer Action -->
                <div class="pt-2 flex items-center justify-end gap-2.5">
                    <button onclick="closeContactModal()" class="px-4 py-2 rounded-xl border border-slate-200 dark:border-slate-700 hover:bg-slate-100 text-slate-700 dark:text-slate-200 font-bold text-xs transition cursor-pointer">
                        Đóng
                    </button>
                    <a href="tel:0362848956" class="px-4 py-2 rounded-xl btn-pink-pill text-xs font-bold flex items-center gap-1.5 shadow-md">
                        <i class="fa-solid fa-phone"></i>
                        <span>Kết Nối Ngay: 0362848956</span>
                    </a>
                </div>
            </div>
        </div>
    </div>
"""

body_end_tag = "</body>"
if body_end_tag in content:
    content = content.replace(body_end_tag, modal_html + "\n" + body_end_tag, 1)
    print("Contact Modal HTML added successfully")
else:
    print("Warning: body_end_tag not found")

# 4. Add JS functions for contact modal & update I18N dictionary
contact_js = """
        // =====================================================================
        // CONTACT MODAL FUNCTIONS
        // =====================================================================
        function openContactModal() {
            const modal = document.getElementById('contactModal');
            if (modal) {
                modal.classList.remove('hidden');
                modal.classList.add('flex');
            }
        }

        function closeContactModal() {
            const modal = document.getElementById('contactModal');
            if (modal) {
                modal.classList.add('hidden');
                modal.classList.remove('flex');
            }
        }

        function copyContactEmail() {
            navigator.clipboard.writeText('baongocnguyen686827@gmail.com').then(() => {
                showToast('Đã sao chép email: baongocnguyen686827@gmail.com', 'success');
            }).catch(() => {
                showToast('Email: baongocnguyen686827@gmail.com', 'info');
            });
        }
"""

# Insert contact_js right before "function initLanguage()"
init_lang_target = "        function initLanguage()"
if init_lang_target in content:
    content = content.replace(init_lang_target, contact_js + "\n" + init_lang_target, 1)
    print("Contact JS functions added successfully")
else:
    print("Warning: init_lang_target not found")

# 5. Add I18N entries for contact section across all 4 languages
# vi additions
content = content.replace(
    "toast_switched: 'Đã chuyển đổi sang Tiếng Việt!'",
    """toast_switched: 'Đã chuyển đổi sang Tiếng Việt!',
                contact_btn: 'Liên Hệ',
                contact_title: 'Thông Tin Liên Hệ',
                contact_phone_lbl: 'Số điện thoại:',
                contact_email_lbl: 'Email:',
                contact_address_lbl: 'Địa chỉ:',
                contact_address_val: 'Hà Nội, Việt Nam',
                contact_manager_title: 'Nhân Sự Phụ Trách',
                contact_hours_title: 'Khung Giờ Hỗ Trợ',
                footer_about: 'Hệ thống AI Agent tự động hóa phân tích chuỗi bán lẻ, đối soát dữ liệu doanh thu, bóc tách đơn hủy & đổi trả, đo lường CSAT khách hàng và đề xuất kịch bản tăng trưởng thông minh.'"""
)

# en additions
content = content.replace(
    "toast_switched: 'Switched to English successfully!'",
    """toast_switched: 'Switched to English successfully!',
                contact_btn: 'Contact',
                contact_title: 'Contact Information',
                contact_phone_lbl: 'Phone Number:',
                contact_email_lbl: 'Support Email:',
                contact_address_lbl: 'Address:',
                contact_address_val: 'Hanoi, Vietnam',
                contact_manager_title: 'Lead Administrator',
                contact_hours_title: 'Support Hours',
                footer_about: 'Autonomous Retail AI Agent OS for multi-store data reconciliation, returns deduction, CSAT measurement, and automated growth decision intelligence.'"""
)

# ja additions
content = content.replace(
    "toast_switched: '日本語に切り替えました！'",
    """toast_switched: '日本語に切り替えました！',
                contact_btn: 'お問い合わせ',
                contact_title: 'お問い合わせ先情報',
                contact_phone_lbl: '電話番号:',
                contact_email_lbl: 'サポートメール:',
                contact_address_lbl: '所在地:',
                contact_address_val: 'ハノイ、ベトナム',
                contact_manager_title: '担当管理者',
                contact_hours_title: 'サポート受付時間',
                footer_about: '小売チェーン向けAIエージェントOS：売上照合の自動化、返品・キャンセル分析、CSAT顧客満足度測定、成長戦略の試算。'"""
)

# zh additions
content = content.replace(
    "toast_switched: '已成功切换至中文！'",
    """toast_switched: '已成功切换至中文！',
                contact_btn: '联系方式',
                contact_title: '直接联系信息',
                contact_phone_lbl: '联系电话:',
                contact_email_lbl: '支持邮箱:',
                contact_address_lbl: '办公地址:',
                contact_address_val: '越南河内',
                contact_manager_title: '负责人信息',
                contact_hours_title: '服务支持时间',
                footer_about: '面向零售连锁门店的智能体操作系统：自动化对账、退换货剔除、CSAT客户满意度洞察及智能经营决策建议。'"""
)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Contact section and modal fully integrated!")

