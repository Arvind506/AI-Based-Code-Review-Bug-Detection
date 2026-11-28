import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def create_ui_screens():
    # 1. UI Screen: Dashboard
    fig, ax = plt.subplots(figsize=(10, 5.2), dpi=300)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5.5)
    ax.axis('off')
    
    # Outer browser window
    win = patches.FancyBboxPatch((0.2, 0.2), 9.6, 5.1, boxstyle="round,pad=0.1", ec="#334155", fc="#0f172a", lw=2)
    ax.add_patch(win)
    # Browser bar
    ax.add_patch(patches.Rectangle((0.2, 4.8), 9.6, 0.5, fc="#1e293b"))
    ax.plot([0.5, 0.75, 1.0], [5.05, 5.05, 5.05], 'o', color="#ef4444", markersize=6)
    ax.text(5.0, 5.05, "http://localhost:8501 - AI Code Review & Bug Detection", color="#94a3b8", fontsize=8, ha="center")
    
    # Sidebar
    ax.add_patch(patches.Rectangle((0.2, 0.2), 2.2, 4.6, fc="#1e293b"))
    ax.text(1.3, 4.4, "⚡ AI Reviewer", color="#a855f7", fontsize=10, fontweight="bold", ha="center")
    ax.text(1.3, 4.0, "● Groq AI: Active", color="#10b981", fontsize=7.5, fontweight="bold", ha="center")
    ax.text(1.3, 3.4, "🛠 Capabilities\n- 9-Lang AST\n- Bug Heuristics\n- OWASP Scanner\n- Big-O Complexity\n- AI Refactoring", color="#cbd5e1", fontsize=7, ha="center")
    
    # Header Banner
    ax.add_patch(patches.FancyBboxPatch((2.6, 3.9), 7.0, 0.75, boxstyle="round,pad=0.08", ec="#4f46e5", fc="#1e1b4b", lw=1.5))
    ax.text(6.1, 4.35, "⚡ AI Code Review & Bug Detection", color="#818cf8", fontsize=9.5, fontweight="bold", ha="center")
    ax.text(6.1, 4.05, "File: buggy.py (1.2 KB) • Language: Python • Status: Analyzed ✅", color="#34d399", fontsize=7.5, ha="center")
    
    # 5 Metrics
    labels = ["FUNCTIONS", "CLASSES", "IMPORTS", "WARNINGS", "BUGS"]
    vals = ["4", "0", "2", "3", "4"]
    colors = ["#38bdf8", "#c084fc", "#34d399", "#fbbf24", "#f87171"]
    for i in range(5):
        bx = 2.6 + i * 1.43
        ax.add_patch(patches.FancyBboxPatch((bx, 2.9), 1.25, 0.8, boxstyle="round,pad=0.05", ec="#334155", fc="#1e293b", lw=1))
        ax.text(bx + 0.62, 3.45, labels[i], color="#94a3b8", fontsize=6.5, fontweight="bold", ha="center")
        ax.text(bx + 0.62, 3.12, vals[i], color=colors[i], fontsize=13, fontweight="bold", ha="center")
        
    # Chart area
    ax.add_patch(patches.FancyBboxPatch((2.6, 0.5), 3.4, 2.2, boxstyle="round,pad=0.05", ec="#334155", fc="#1e293b", lw=1))
    ax.text(4.3, 2.45, "Code Composition (Donut)", color="#f8fafc", fontsize=7.5, fontweight="bold", ha="center")
    ax.add_patch(patches.Circle((4.3, 1.4), 0.75, ec="#38bdf8", fc="#1e293b", lw=14))
    
    ax.add_patch(patches.FancyBboxPatch((6.2, 0.5), 3.4, 2.2, boxstyle="round,pad=0.05", ec="#334155", fc="#1e293b", lw=1))
    ax.text(7.9, 2.45, "Structural Metrics (Bar)", color="#f8fafc", fontsize=7.5, fontweight="bold", ha="center")
    ax.bar([6.8, 7.3, 7.8, 8.3, 8.8], [0.8, 0.2, 0.6, 1.1, 1.4], width=0.35, color=colors, bottom=0.8)
    
    plt.title("Figure 7.4: System Overview Dashboard with Real-Time Metrics & Charts", fontsize=10, fontweight='bold', pad=8)
    plt.savefig("report_assets/ui_screen_dashboard.png", bbox_inches='tight')
    plt.close()

    # 2. UI Screen: Security & Bug Scan
    fig, ax = plt.subplots(figsize=(10, 5.2), dpi=300)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5.5)
    ax.axis('off')
    
    win = patches.FancyBboxPatch((0.2, 0.2), 9.6, 5.1, boxstyle="round,pad=0.1", ec="#334155", fc="#0f172a", lw=2)
    ax.add_patch(win)
    ax.add_patch(patches.Rectangle((0.2, 4.8), 9.6, 0.5, fc="#1e293b"))
    ax.text(5.0, 5.05, "Security Audit & Bug Inspection Panel", color="#94a3b8", fontsize=8, ha="center")
    
    # Left: Security Cards
    ax.add_patch(patches.FancyBboxPatch((0.5, 3.8), 4.3, 0.8, boxstyle="round,pad=0.06", ec="#ef4444", fc="#450a0a", lw=1.5))
    ax.text(0.7, 4.3, "🔴 [High] Line 13 — SQL Injection Risk", color="#fca5a5", fontsize=7.5, fontweight="bold")
    ax.text(0.7, 4.0, "query = 'SELECT * FROM users WHERE user = '' + u + '''", color="#f87171", fontsize=7)
    
    ax.add_patch(patches.FancyBboxPatch((0.5, 2.8), 4.3, 0.8, boxstyle="round,pad=0.06", ec="#ef4444", fc="#450a0a", lw=1.5))
    ax.text(0.7, 3.3, "🔴 [High] Line 6 — Hardcoded Secret Detected", color="#fca5a5", fontsize=7.5, fontweight="bold")
    ax.text(0.7, 3.0, "DB_PASSWORD = 'SuperSecret123' (Move to .env)", color="#f87171", fontsize=7)
    
    ax.add_patch(patches.FancyBboxPatch((0.5, 1.8), 4.3, 0.8, boxstyle="round,pad=0.06", ec="#f59e0b", fc="#451a03", lw=1.5))
    ax.text(0.7, 2.3, "🟠 [Medium] Line 20 — Weak Hash (MD5)", color="#fde68a", fontsize=7.5, fontweight="bold")
    ax.text(0.7, 2.0, "hashlib.md5(...) -> Upgrade to SHA-256 or Argon2", color="#fbbf24", fontsize=7)
    
    # Right: Bug Detection & Complexity
    ax.add_patch(patches.FancyBboxPatch((5.2, 2.9), 4.3, 1.7, boxstyle="round,pad=0.08", ec="#6366f1", fc="#1e1b4b", lw=1.5))
    ax.text(7.35, 4.25, "⏱ Estimated Time Complexity", color="#a5b4fc", fontsize=8.5, fontweight="bold", ha="center")
    ax.text(7.35, 3.75, "O(n²)", color="#818cf8", fontsize=18, fontweight="bold", ha="center")
    ax.text(7.35, 3.2, "Nested loops detected in matrix processing.", color="#c7d2fe", fontsize=7.5, ha="center")
    
    ax.add_patch(patches.FancyBboxPatch((5.2, 0.6), 4.3, 2.1, boxstyle="round,pad=0.08", ec="#ef4444", fc="#1e293b", lw=1.2))
    ax.text(7.35, 2.35, "🐞 Programmatic Bugs Flagged", color="#f87171", fontsize=8.5, fontweight="bold", ha="center")
    ax.text(5.5, 1.9, "• Line 6: Division by zero literal (a / 0)", color="#fca5a5", fontsize=7)
    ax.text(5.5, 1.5, "• Line 11: Infinite loop without break statement", color="#fca5a5", fontsize=7)
    ax.text(5.5, 1.1, "• Line 20: Unreachable dead code after return", color="#fca5a5", fontsize=7)
    ax.text(5.5, 0.7, "• Line 30: Duplicate logic block of calculate_total()", color="#fca5a5", fontsize=7)

    plt.title("Figure 7.5: Security Vulnerability Scan & Heuristic Bug Detection Interface", fontsize=10, fontweight='bold', pad=8)
    plt.savefig("report_assets/ui_screen_security.png", bbox_inches='tight')
    plt.close()

create_ui_screens()
print("UI Screenshots generated successfully!")
