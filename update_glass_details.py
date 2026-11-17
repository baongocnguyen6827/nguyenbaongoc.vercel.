# update_glass_details.py

html_path = r"c:\Users\ADMIN\OneDrive\Attachments\Thi cuối môn AI301\app\templates\index.html"
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

target_str = "        /* LUXURY CRYSTAL GLASSMORPHISM CARDS (.os-card) */"
addition = """        /* Frosted Glass Utilities for Inner Containers */
        .bg-white {
            background-color: rgba(255, 255, 255, 0.72) !important;
            backdrop-filter: blur(16px) saturate(170%);
            -webkit-backdrop-filter: blur(16px) saturate(170%);
        }
        body.dark .bg-white {
            background-color: rgba(30, 41, 59, 0.68) !important;
            backdrop-filter: blur(16px) saturate(170%);
            -webkit-backdrop-filter: blur(16px) saturate(170%);
        }
        .bg-slate-50, .bg-slate-50\\/90 {
            background-color: rgba(255, 255, 255, 0.58) !important;
            backdrop-filter: blur(14px);
            -webkit-backdrop-filter: blur(14px);
        }
        body.dark .bg-slate-50, body.dark .bg-slate-50\\/90 {
            background-color: rgba(15, 23, 42, 0.6) !important;
        }

        /* LUXURY CRYSTAL GLASSMORPHISM CARDS (.os-card) */"""

if target_str in content:
    content = content.replace(target_str, addition, 1)
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Glass utilities added successfully")
else:
    print("Warning: target_str not found")

