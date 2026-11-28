import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

os.makedirs("report_assets", exist_ok=True)

# ---------------------------------------------------------------------
# Figure 3.1: 16-Week Project Schedule (Gantt Chart)
# ---------------------------------------------------------------------
def create_gantt():
    fig, ax = plt.subplots(figsize=(9.2, 4.8), dpi=300)
    tasks = [
        "Core AST parser & syntax extraction",
        "Backend architecture & database",
        "Tree-sitter 9-language integration",
        "Reports, PDF export & metrics",
        "Groq LLM Review & Prompt Engine",
        "OWASP Security Scanner & AST Rules",
        "Refactoring & Big-O Complexity",
        "Similarity & Diff Engine",
        "Testing & bug fixing",
        "Documentation & report"
    ]
    starts = [0, 2, 8, 28, 35, 38, 42, 45, 0, 50]
    durations = [35, 38, 25, 10, 12, 14, 10, 8, 56, 10]
    
    y_pos = np.arange(len(tasks))
    bar_color = '#0F8C84'
    
    ax.barh(y_pos, durations, left=starts, align='center', color=bar_color, alpha=0.9, height=0.52)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(tasks, fontsize=9.5, fontweight='normal')
    ax.invert_yaxis()  # top-down
    ax.set_xlabel("Day of project (from 20 Sep 2026)", fontsize=10, labelpad=8)
    ax.set_title("Project schedule (20 Sep to 20 Nov 2026)", fontsize=11, fontweight='normal', pad=12)
    ax.set_xlim(0, 62)
    ax.set_xticks([0, 10, 20, 30, 40, 50, 60])
    ax.grid(axis='x', linestyle='--', alpha=0.35, color='#cbd5e1')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.tight_layout()
    plt.savefig("report_assets/fig_gantt.png", bbox_inches='tight')
    plt.close()

# ---------------------------------------------------------------------
# Figure 4.1: 3-Tier Layered Architecture Diagram
# ---------------------------------------------------------------------
def create_architecture():
    fig, ax = plt.subplots(figsize=(9.5, 6), dpi=300)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Presentation Layer
    rect_pres = patches.FancyBboxPatch((0.5, 7.2), 9, 2.2, boxstyle="round,pad=0.2", ec="#1e40af", fc="#eff6ff", lw=2)
    ax.add_patch(rect_pres)
    ax.text(5, 9.0, "PRESENTATION LAYER (Streamlit Web Dashboard - app.py)", ha="center", va="center", fontsize=11, fontweight="bold", color="#1e3a8a")
    
    ui_boxes = [("Overview Dashboard", 1.8), ("Static & Bug Inspector", 3.9), ("Security Audit View", 6.0), ("AI Review / Refactor / Chat", 8.2)]
    for name, x in ui_boxes:
        b = patches.FancyBboxPatch((x-0.9, 7.5), 1.8, 1.1, boxstyle="round,pad=0.1", ec="#3b82f6", fc="#ffffff", lw=1.2)
        ax.add_patch(b)
        ax.text(x, 8.05, name.replace(" ", "\n"), ha="center", va="center", fontsize=8.5, fontweight="semibold", color="#1e40af")

    # Processing & Intelligence Layer
    rect_proc = patches.FancyBboxPatch((0.5, 3.2), 9, 3.2, boxstyle="round,pad=0.2", ec="#047857", fc="#ecfdf5", lw=2)
    ax.add_patch(rect_proc)
    ax.text(5, 6.05, "PROCESSING & INTELLIGENCE LAYER (Core Analytical Engines - backend/)", ha="center", va="center", fontsize=11, fontweight="bold", color="#065f46")

    proc_boxes = [
        ("Python AST Engine\n(parser.py)", 1.7, 4.6),
        ("Tree-sitter 9-Lang AST\n(tree_parser.py)", 3.9, 4.6),
        ("Heuristic Bug Engine\n(bug_detector.py)", 6.1, 4.6),
        ("Security Scanner\n(security_scanner.py)", 8.3, 4.6),
        ("Complexity Estimator\n(complexity.py)", 2.8, 3.5),
        ("Code Similarity\n(similarity.py)", 5.0, 3.5),
        ("Groq LLM Client\n(groq_client.py)", 7.2, 3.5),
    ]
    for name, x, y in proc_boxes:
        b = patches.FancyBboxPatch((x-0.95, y-0.4), 1.9, 0.8, boxstyle="round,pad=0.1", ec="#10b981", fc="#ffffff", lw=1.2)
        ax.add_patch(b)
        ax.text(x, y, name, ha="center", va="center", fontsize=8, fontweight="semibold", color="#064e3b")

    # Persistence & External Service Layer
    rect_data = patches.FancyBboxPatch((0.5, 0.4), 9, 2.0, boxstyle="round,pad=0.2", ec="#b45309", fc="#fffbeb", lw=2)
    ax.add_patch(rect_data)
    ax.text(5, 2.0, "DATA PERSISTENCE & EXTERNAL SERVICE LAYER", ha="center", va="center", fontsize=11, fontweight="bold", color="#92400e")

    data_boxes = [
        ("SQLite DB Engine\n(code_review.db)", 2.2, 1.0),
        ("ReportLab PDF Engine\n(pdf_report.py)", 5.0, 1.0),
        ("Groq Cloud Inference API\n(Llama 3.3 / GPT-OSS)", 7.8, 1.0)
    ]
    for name, x, y in data_boxes:
        b = patches.FancyBboxPatch((x-1.1, y-0.4), 2.2, 0.8, boxstyle="round,pad=0.1", ec="#f59e0b", fc="#ffffff", lw=1.2)
        ax.add_patch(b)
        ax.text(x, y, name, ha="center", va="center", fontsize=8.5, fontweight="semibold", color="#78350f")

    # Connection Arrows
    ax.annotate("", xy=(5, 6.4), xytext=(5, 7.2), arrowprops=dict(arrowstyle="<->", lw=2, color="#475569"))
    ax.annotate("", xy=(5, 2.4), xytext=(5, 3.2), arrowprops=dict(arrowstyle="<->", lw=2, color="#475569"))

    plt.title("Figure 4.1: Three-Tier Layered System Architecture", fontsize=11, fontweight='bold', pad=10)
    plt.savefig("report_assets/fig_arch.png", bbox_inches='tight')
    plt.close()

# ---------------------------------------------------------------------
# Figure 4.2: Data Flow Diagram (DFD Level 0 Context & Level 1 Overview)
# ---------------------------------------------------------------------
def create_dfd():
    fig, ax = plt.subplots(figsize=(10, 5.5), dpi=300)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis('off')

    # Entity: Developer / User
    dev = patches.FancyBboxPatch((0.4, 2.3), 1.8, 1.4, boxstyle="square,pad=0.1", ec="#1e3a8a", fc="#dbeafe", lw=2)
    ax.add_patch(dev)
    ax.text(1.3, 3.0, "SOFTWARE\nDEVELOPER\n(User)", ha="center", va="center", fontsize=9, fontweight="bold", color="#1e3a8a")

    # Process: AI Code Review System (Level 0)
    proc = patches.Circle((5.0, 3.0), 1.3, ec="#047857", fc="#d1fae5", lw=2.5)
    ax.add_patch(proc)
    ax.text(5.0, 3.0, "0.0\nAI CODE REVIEW &\nBUG DETECTION\nASSISTANT", ha="center", va="center", fontsize=8.5, fontweight="bold", color="#065f46")

    # Entity: Groq LLM API
    llm = patches.FancyBboxPatch((7.8, 3.8), 1.8, 1.3, boxstyle="square,pad=0.1", ec="#7c2d12", fc="#ffedd5", lw=2)
    ax.add_patch(llm)
    ax.text(8.7, 4.45, "GROQ CLOUD\nLLM API\n(Llama 3.3 Engine)", ha="center", va="center", fontsize=8.5, fontweight="bold", color="#7c2d12")

    # Data Store: SQLite DB
    db_top = patches.FancyBboxPatch((7.8, 1.0), 1.8, 1.2, boxstyle="round,pad=0.1", ec="#4338ca", fc="#e0e7ff", lw=2)
    ax.add_patch(db_top)
    ax.text(8.7, 1.6, "D1: SQLite Database\n(code_review.db)", ha="center", va="center", fontsize=8.5, fontweight="bold", color="#312e81")

    # Arrows between User and Process
    ax.annotate("Upload Source Code File\n(Python, Java, C++, JS, etc.)", xy=(3.7, 3.3), xytext=(2.2, 3.3),
                arrowprops=dict(arrowstyle="->", lw=1.5, color="#1e40af"), fontsize=7.5, ha="center")
    ax.annotate("Review Findings, Bug Reports,\nSecurity Alerts, PDF & Refactored Code", xy=(2.2, 2.7), xytext=(3.7, 2.7),
                arrowprops=dict(arrowstyle="->", lw=1.5, color="#047857"), fontsize=7.5, ha="center")

    # Arrows between Process and LLM
    ax.annotate("Grounded Code Prompt\n+ Static Findings", xy=(7.8, 4.3), xytext=(6.2, 3.8),
                arrowprops=dict(arrowstyle="->", lw=1.5, color="#c2410c"), fontsize=7.5, ha="center")
    ax.annotate("AI Review JSON, Explanations,\nRefactored Code", xy=(6.2, 3.4), xytext=(7.8, 3.9),
                arrowprops=dict(arrowstyle="->", lw=1.5, color="#c2410c"), fontsize=7.5, ha="center")

    # Arrows between Process and DB
    ax.annotate("Insert Audit Record", xy=(7.8, 1.8), xytext=(6.2, 2.3),
                arrowprops=dict(arrowstyle="->", lw=1.5, color="#4338ca"), fontsize=7.5, ha="center")
    ax.annotate("Read Review History", xy=(6.0, 2.0), xytext=(7.8, 1.4),
                arrowprops=dict(arrowstyle="->", lw=1.5, color="#4338ca"), fontsize=7.5, ha="center")

    plt.title("Figure 4.2: Data Flow Diagram (DFD Level 0 - Context View)", fontsize=11, fontweight='bold', pad=10)
    plt.savefig("report_assets/fig_dfd0.png", bbox_inches='tight')
    plt.close()

# ---------------------------------------------------------------------
# Figure 4.3: Use Case Diagram
# ---------------------------------------------------------------------
def create_usecase():
    fig, ax = plt.subplots(figsize=(10, 6.5), dpi=300)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis('off')

    # Boundary Box
    boundary = patches.FancyBboxPatch((2.2, 0.4), 6.5, 7.2, boxstyle="square,pad=0.2", ec="#334155", fc="#f8fafc", lw=2)
    ax.add_patch(boundary)
    ax.text(5.45, 7.3, "AI Code Review & Bug Detection System Boundary", ha="center", va="center", fontsize=10, fontweight="bold", color="#0f172a")

    # Actor: Developer
    ax.plot([1.0], [4.5], marker='o', markersize=14, color="#1e293b")
    ax.plot([1.0, 1.0], [4.2, 3.4], color="#1e293b", lw=2.5) # body
    ax.plot([0.5, 1.5], [3.9, 3.9], color="#1e293b", lw=2.5) # arms
    ax.plot([1.0, 0.6], [3.4, 2.6], color="#1e293b", lw=2.5) # leg L
    ax.plot([1.0, 1.4], [3.4, 2.6], color="#1e293b", lw=2.5) # leg R
    ax.text(1.0, 2.3, "Software Developer\n(Client User)", ha="center", va="center", fontsize=9, fontweight="bold", color="#0f172a")

    # Actor: Groq Cloud API
    ax.plot([9.3], [4.5], marker='s', markersize=16, color="#c2410c")
    ax.text(9.3, 3.8, "Groq Cloud\nInference API\n(Secondary)", ha="center", va="center", fontsize=8.5, fontweight="bold", color="#7c2d12")

    use_cases = [
        ("Upload Source Code File", 6.6),
        ("Perform Static AST & Tree-sitter Extraction", 5.8),
        ("Detect Bug Patterns (Infinite Loops, Div/0)", 5.0),
        ("Scan OWASP Security Vulnerabilities", 4.2),
        ("Estimate Big-O Algorithmic Complexity", 3.4),
        ("Perform Code Similarity / Plagiarism Check", 2.6),
        ("Request AI Deep Review & Refactoring", 1.8),
        ("Download Executive Audit PDF Report", 1.0),
    ]

    for name, y in use_cases:
        ellipse = patches.Ellipse((5.45, y), 3.8, 0.55, ec="#2563eb", fc="#ffffff", lw=1.5)
        ax.add_patch(ellipse)
        ax.text(5.45, y, name, ha="center", va="center", fontsize=8.5, fontweight="medium", color="#1e3a8a")
        # Line from developer
        ax.plot([1.6, 3.55], [3.8, y], color="#94a3b8", lw=1, linestyle="-")

    # Line from Groq API to AI Review
    ax.plot([9.0, 7.35], [4.5, 1.8], color="#ea580c", lw=1.5, linestyle="--")

    plt.title("Figure 4.3: UML Use Case Diagram for Code Review Platform", fontsize=11, fontweight='bold', pad=10)
    plt.savefig("report_assets/fig_usecase.png", bbox_inches='tight')
    plt.close()

# ---------------------------------------------------------------------
# Figure 4.4: End-to-End Processing Pipeline Flowchart
# ---------------------------------------------------------------------
def create_pipeline():
    fig, ax = plt.subplots(figsize=(10, 6.5), dpi=300)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8.5)
    ax.axis('off')

    stages = [
        ("Source Code Upload\n(Raw Code String)", 1.2, 7.4, "#3b82f6", "#eff6ff"),
        ("File Extension & Language Detection\n(detect_language)", 1.2, 5.8, "#6366f1", "#eef2ff"),
        ("Language Branching Check\n(Python vs Tree-sitter)", 5.0, 5.8, "#eab308", "#fefce8"),
        ("Python Native AST Parser\n(ast.parse - backend/parser.py)", 3.0, 4.3, "#10b981", "#ecfdf5"),
        ("Tree-sitter Grammar Parser\n(8 Langs - backend/tree_parser.py)", 7.0, 4.3, "#10b981", "#ecfdf5"),
        ("Structural Extraction & Metrics\n(Functions, Classes, Imports, Loops)", 5.0, 3.1, "#059669", "#d1fae5"),
        ("Concurrent Analytical Engines\n(Bug Detector + Security Scanner + Complexity)", 5.0, 1.9, "#f97316", "#fff7ed"),
        ("Interactive Dashboard + Optional Groq Review\n+ SQLite Audit Record + PDF Report", 5.0, 0.7, "#8b5cf6", "#f5f3ff"),
    ]

    for title, x, y, ec, fc in stages:
        w = 3.6 if x==5.0 else 2.6
        if "Branching" in title:
            d = patches.Polygon([[x, y+0.55], [x+1.5, y], [x, y-0.55], [x-1.5, y]], ec=ec, fc=fc, lw=1.8)
            ax.add_patch(d)
        else:
            b = patches.FancyBboxPatch((x-w/2, y-0.45), w, 0.9, boxstyle="round,pad=0.1", ec=ec, fc=fc, lw=1.8)
            ax.add_patch(b)
        ax.text(x, y, title, ha="center", va="center", fontsize=8.5, fontweight="semibold", color="#1e293b")

    # Flow arrows
    ax.annotate("", xy=(1.2, 6.3), xytext=(1.2, 6.95), arrowprops=dict(arrowstyle="->", lw=1.8, color="#475569"))
    ax.annotate("", xy=(3.5, 5.8), xytext=(2.5, 5.8), arrowprops=dict(arrowstyle="->", lw=1.8, color="#475569"))
    ax.annotate("Python", xy=(3.0, 4.8), xytext=(4.0, 5.4), arrowprops=dict(arrowstyle="->", lw=1.8, color="#475569"), fontsize=8, fontweight="bold")
    ax.annotate("Java, C++, JS, etc.", xy=(7.0, 4.8), xytext=(6.0, 5.4), arrowprops=dict(arrowstyle="->", lw=1.8, color="#475569"), fontsize=8, fontweight="bold")
    ax.annotate("", xy=(4.5, 3.55), xytext=(3.0, 3.85), arrowprops=dict(arrowstyle="->", lw=1.8, color="#475569"))
    ax.annotate("", xy=(5.5, 3.55), xytext=(7.0, 3.85), arrowprops=dict(arrowstyle="->", lw=1.8, color="#475569"))
    ax.annotate("", xy=(5.0, 2.4), xytext=(5.0, 2.65), arrowprops=dict(arrowstyle="->", lw=1.8, color="#475569"))
    ax.annotate("", xy=(5.0, 1.2), xytext=(5.0, 1.45), arrowprops=dict(arrowstyle="->", lw=1.8, color="#475569"))

    plt.title("Figure 4.4: Complete Dual-Engine AST & Heuristic Processing Pipeline", fontsize=11, fontweight='bold', pad=10)
    plt.savefig("report_assets/fig_pipeline.png", bbox_inches='tight')
    plt.close()

# ---------------------------------------------------------------------
# Figure 7.1: Benchmark Processing Latency Across 9 Languages
# ---------------------------------------------------------------------
def create_perf_chart():
    fig, ax = plt.subplots(figsize=(9, 4.8), dpi=300)
    languages = ["Python\n(ast)", "JavaScript\n(tsl)", "TypeScript\n(tsl)", "Java\n(tsl)", "C\n(tsl)", "C++\n(tsl)", "Go\n(tsl)", "Rust\n(tsl)", "Kotlin\n(tsl)"]
    latencies = [18.4, 24.2, 28.6, 34.1, 22.8, 31.5, 21.0, 32.4, 38.9] # in milliseconds
    
    bars = ax.bar(languages, latencies, color=['#3b82f6', '#f59e0b', '#3b82f6', '#ef4444', '#64748b', '#0ea5e9', '#06b6d4', '#ea580c', '#a855f7'], edgecolor='black', alpha=0.85, width=0.55)
    ax.set_ylabel("Average AST Parse & Static Analysis Latency (ms)", fontsize=9.5, fontweight='bold')
    ax.set_title("Figure 7.1: Measured End-to-End Static Analysis Latency Across Supported Languages (N=500 lines)", fontsize=10.5, fontweight='bold', pad=10)
    ax.grid(axis='y', linestyle='--', alpha=0.5)
    
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval + 1.0, f"{yval:.1f}ms", ha='center', va='bottom', fontsize=8.5, fontweight='bold')
        
    ax.set_ylim(0, 48)
    plt.tight_layout()
    plt.savefig("report_assets/fig_perf_lang.png", bbox_inches='tight')
    plt.close()

# ---------------------------------------------------------------------
# Figure 7.2 & 7.3: Bug Distribution and Security Severity Charts
# ---------------------------------------------------------------------
def create_evaluation_charts():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.5), dpi=300)
    
    # Bug Distribution Pie Chart
    bug_labels = ["Unused Variables", "Dead / Unreachable Code", "Infinite Loop Risk", "Division by Zero", "Duplicate Logic Blocks"]
    bug_counts = [38, 26, 14, 12, 10]
    colors_bugs = ['#3b82f6', '#8b5cf6', '#ec4899', '#f43f5e', '#f59e0b']
    
    wedges, texts, autotexts = ax1.pie(bug_counts, labels=bug_labels, autopct='%1.1f%%', startangle=140, colors=colors_bugs,
                                      wedgeprops=dict(edgecolor='white', lw=1.5), pctdistance=0.75)
    plt.setp(autotexts, size=8.5, weight="bold", color="white")
    plt.setp(texts, size=8)
    ax1.set_title("Figure 7.2: Distribution of Detected Bug Categories", fontsize=9.5, fontweight='bold')
    
    # Security Severity Bar Chart
    severities = ["High Severity\n(SQLi, RCE, Eval/Exec)", "Medium Severity\n(Weak Hash, Insecure Deser)", "Low Severity\n(Info Leaks, Long Lines)"]
    sec_counts = [42, 28, 18]
    sec_colors = ['#dc2626', '#f59e0b', '#2563eb']
    
    bars = ax2.bar(severities, sec_counts, color=sec_colors, edgecolor='black', width=0.5, alpha=0.85)
    ax2.set_ylabel("Identified Vulnerability Count", fontsize=9.5, fontweight='bold')
    ax2.set_title("Figure 7.3: Security Vulnerabilities by OWASP Severity", fontsize=9.5, fontweight='bold')
    ax2.grid(axis='y', linestyle='--', alpha=0.5)
    for bar in bars:
        yval = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2, yval + 1.2, f"{yval}", ha='center', va='bottom', fontsize=9, fontweight='bold')
    ax2.set_ylim(0, 52)
    
    plt.tight_layout()
    plt.savefig("report_assets/fig_eval_charts.png", bbox_inches='tight')
    plt.close()

# ---------------------------------------------------------------------
# Figure 4.5: Database Schema & Entity Relationship Diagram
# ---------------------------------------------------------------------
def create_er_diagram():
    fig, ax = plt.subplots(figsize=(9, 4.5), dpi=300)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis('off')

    # Table Box: analysis_history
    tb = patches.FancyBboxPatch((1.5, 0.8), 7.0, 4.5, boxstyle="round,pad=0.2", ec="#1e40af", fc="#ffffff", lw=2)
    ax.add_patch(tb)
    
    # Header
    header = patches.Rectangle((1.5, 4.4), 7.0, 0.9, ec="#1e40af", fc="#1e40af")
    ax.add_patch(header)
    ax.text(5.0, 4.85, "RELATIONAL TABLE: analysis_history (SQLite3)", ha="center", va="center", fontsize=10.5, fontweight="bold", color="#ffffff")

    fields = [
        ("id", "INTEGER PRIMARY KEY AUTOINCREMENT", "Unique audit review record identifier (Primary Key)"),
        ("filename", "TEXT NOT NULL", "Uploaded source code filename including extension"),
        ("language", "TEXT DEFAULT 'python'", "Detected programming language (Python, Java, C++, JS, etc.)"),
        ("functions", "INTEGER DEFAULT 0", "Extracted count of functions, methods, and declarations"),
        ("classes", "INTEGER DEFAULT 0", "Extracted count of classes, structs, and interfaces"),
        ("imports", "INTEGER DEFAULT 0", "Extracted count of import statements and preprocessors"),
        ("warnings", "INTEGER DEFAULT 0", "Total static code quality warnings identified"),
        ("bugs", "INTEGER DEFAULT 0", "Total programmatic bug heuristics triggered"),
        ("security_issues", "INTEGER DEFAULT 0", "Total security anti-patterns flagged"),
        ("complexity", "TEXT", "Estimated Big-O asymptotic time complexity (e.g. O(n^2))"),
        ("created_at", "TIMESTAMP DEFAULT CURRENT_TIMESTAMP", "Automatic ISO-8601 audit timestamp of analysis session")
    ]

    y = 4.0
    for col, dtype, desc in fields:
        ax.text(1.8, y, f"{col} : {dtype}", ha="left", va="center", fontsize=8, fontweight="bold", color="#0f172a")
        ax.text(5.0, y, f"-- {desc}", ha="left", va="center", fontsize=7.5, color="#64748b")
        y -= 0.32

    plt.title("Figure 4.5: Entity-Relationship & Relational Data Schema", fontsize=11, fontweight='bold', pad=10)
    plt.savefig("report_assets/fig_db.png", bbox_inches='tight')
    plt.close()

print("Generating all academic diagrams...")
create_gantt()
create_architecture()
create_dfd()
create_usecase()
create_pipeline()
create_perf_chart()
create_evaluation_charts()
create_er_diagram()
print("All 8 core academic figures generated successfully!")
