import os
from dotenv import load_dotenv

load_dotenv(override=True)
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

from backend.parser import CodeParser
from backend.tree_parser import TreeParser, detect_language, is_tree_sitter_language
from backend.analyzer import CodeAnalyzer
from backend.multi_analyzer import MultiLanguageAnalyzer
from backend.complexity import ComplexityAnalyzer, estimate_complexity_generic
from backend.bug_detector import BugDetector
from backend.security_scanner import SecurityScanner
from backend.ai_reviewer import AIReviewer
from backend.refactorer import CodeRefactorer
from backend.similarity import SimilarityChecker
from backend.explainer import CodeExplainer
from backend.chatbot import CodeChatBot
from backend.pdf_report import PDFReport
from backend import groq_client

from database.database import (
    create_table,
    insert_analysis,
    get_history,
    clear_history,
)

# --------------------------------------------------
# Setup & Page Configuration
# --------------------------------------------------

create_table()

st.set_page_config(
    page_title="AI Code Review & Bug Detection",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

SUPPORTED_TYPES = ["py", "java", "c", "h", "cpp", "cc", "hpp", "js", "jsx", "ts", "tsx", "go", "rs", "kt", "kts"]

# --------------------------------------------------
# Premium Custom Styling (Light & Dark Theme Adaptive)
# --------------------------------------------------

CUSTOM_CSS = """
<style>
/* Modern fonts and general layout */
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
}

code, pre {
    font-family: 'JetBrains Mono', monospace !important;
}

/* Glassmorphism Hero Header */
.hero-banner {
    background: linear-gradient(135deg, rgba(79, 70, 229, 0.12) 0%, rgba(147, 51, 234, 0.10) 50%, rgba(236, 72, 153, 0.08) 100%);
    border: 1px solid rgba(99, 102, 241, 0.25);
    border-radius: 18px;
    padding: 28px 32px;
    margin-bottom: 24px;
    backdrop-filter: blur(10px);
    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.08);
}

.hero-title {
    font-size: 2.2rem;
    font-weight: 800;
    letter-spacing: -0.02em;
    background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 50%, #db2777 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin: 0 0 10px 0;
    display: flex;
    align-items: center;
    gap: 12px;
}

.hero-subtitle {
    font-size: 1.05rem;
    color: var(--text-color);
    opacity: 0.85;
    margin-bottom: 16px;
    line-height: 1.5;
}

.lang-pills-container {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-top: 12px;
}

.lang-pill {
    display: inline-flex;
    align-items: center;
    padding: 4px 12px;
    border-radius: 9999px;
    font-size: 0.78rem;
    font-weight: 600;
    letter-spacing: 0.02em;
    background: rgba(99, 102, 241, 0.15);
    color: #4f46e5;
    border: 1px solid rgba(99, 102, 241, 0.3);
}

/* Styled Metric Cards */
.metric-card {
    background: rgba(128, 128, 128, 0.05);
    border: 1px solid rgba(128, 128, 128, 0.18);
    border-radius: 14px;
    padding: 18px 20px;
    text-align: left;
    transition: all 0.25s ease;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.04);
}

.metric-card:hover {
    transform: translateY(-2px);
    border-color: rgba(99, 102, 241, 0.45);
    box-shadow: 0 8px 24px rgba(99, 102, 241, 0.12);
}

.metric-label {
    font-size: 0.82rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    opacity: 0.7;
    margin-bottom: 6px;
}

.metric-val {
    font-size: 1.9rem;
    font-weight: 800;
    letter-spacing: -0.02em;
    line-height: 1.2;
}

.metric-val.blue { color: #3b82f6; }
.metric-val.purple { color: #8b5cf6; }
.metric-val.emerald { color: #10b981; }
.metric-val.amber { color: #f59e0b; }
.metric-val.rose { color: #ef4444; }

/* Status Badges */
.badge-pill {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 5px 14px;
    border-radius: 9999px;
    font-size: 0.85rem;
    font-weight: 600;
}

.badge-online {
    background: rgba(16, 185, 129, 0.15);
    color: #10b981;
    border: 1px solid rgba(16, 185, 129, 0.35);
}

.badge-warning {
    background: rgba(245, 158, 11, 0.15);
    color: #f59e0b;
    border: 1px solid rgba(245, 158, 11, 0.35);
}

/* Capability Cards for Empty State */
.cap-card {
    background: rgba(128, 128, 128, 0.05);
    border: 1px solid rgba(128, 128, 128, 0.15);
    border-radius: 14px;
    padding: 22px;
    height: 100%;
    transition: all 0.3s ease;
}

.cap-card:hover {
    border-color: rgba(99, 102, 241, 0.4);
    transform: translateY(-3px);
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.06);
}

.cap-icon {
    font-size: 1.8rem;
    margin-bottom: 12px;
    display: inline-block;
}

.cap-title {
    font-size: 1.1rem;
    font-weight: 700;
    margin-bottom: 8px;
    color: var(--text-color);
}

.cap-desc {
    font-size: 0.9rem;
    opacity: 0.75;
    line-height: 1.5;
}

/* Sidebar Branding */
.sidebar-brand {
    padding: 12px 4px 18px 4px;
    border-bottom: 1px solid rgba(128, 128, 128, 0.15);
    margin-bottom: 18px;
}

.sidebar-title {
    font-size: 1.35rem;
    font-weight: 800;
    background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin: 0;
}

.feature-item {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 7px 10px;
    border-radius: 8px;
    font-size: 0.88rem;
    margin-bottom: 4px;
    background: rgba(128, 128, 128, 0.03);
    border: 1px solid rgba(128, 128, 128, 0.08);
}

/* Streamlit Tabs Customization */
.stTabs [data-baseweb="tab-list"] {
    gap: 8px;
    border-bottom: 1px solid rgba(128, 128, 128, 0.2);
    padding-bottom: 4px;
}

.stTabs [data-baseweb="tab"] {
    border-radius: 10px 10px 0 0;
    padding: 10px 18px;
    font-weight: 600;
    font-size: 0.92rem;
    border: none;
    transition: all 0.2s ease;
}

.stTabs [aria-selected="true"] {
    background: rgba(99, 102, 241, 0.12) !important;
    border-bottom: 2px solid #6366f1 !important;
    color: #4f46e5 !important;
}

/* File upload container */
.uploaded-banner {
    background: rgba(16, 185, 129, 0.08);
    border: 1px solid rgba(16, 185, 129, 0.25);
    border-radius: 12px;
    padding: 14px 20px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin: 16px 0;
}

/* Code block highlight card */
.code-stat-card {
    background: rgba(128, 128, 128, 0.04);
    border: 1px solid rgba(128, 128, 128, 0.14);
    border-radius: 12px;
    padding: 16px;
    margin-bottom: 14px;
}

.code-stat-title {
    font-weight: 700;
    font-size: 0.95rem;
    margin-bottom: 8px;
    display: flex;
    align-items: center;
    gap: 8px;
}
</style>
"""

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# --------------------------------------------------
# Sidebar Design
# --------------------------------------------------

with st.sidebar:
    st.markdown("""
    <div class="sidebar-brand">
        <h2 class="sidebar-title">⚡ AI Code Review & Bug Detection</h2>
        <p style="font-size: 0.82rem; opacity: 0.7; margin: 4px 0 0 0;">Multi-language Static + AI Code Intelligence</p>
    </div>
    """, unsafe_allow_html=True)

    if groq_client.is_configured():
        st.markdown("""
        <div class="badge-pill badge-online" style="width: 100%; justify-content: center; margin-bottom: 12px;">
            <span style="font-size: 0.7rem;">●</span> Groq AI Engine: Active
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="badge-pill badge-warning" style="width: 100%; justify-content: center; margin-bottom: 12px;">
            <span style="font-size: 0.7rem;">○</span> Groq AI Engine: Offline
        </div>
        """, unsafe_allow_html=True)

    with st.expander("🔑 Configure Groq API Key", expanded=not groq_client.is_configured()):
        current_key = os.getenv("GROQ_API_KEY", "")
        entered_key = st.text_input(
            "Groq API Key",
            value=current_key,
            type="password",
            placeholder="gsk_...",
            help="Get a free key from https://console.groq.com/keys",
        )
        if st.button("Save API Key", use_container_width=True, type="primary"):
            if entered_key.strip():
                os.environ["GROQ_API_KEY"] = entered_key.strip()
                try:
                    with open(".env", "w", encoding="utf-8") as f:
                        f.write(f"GROQ_API_KEY={entered_key.strip()}\n")
                except Exception:
                    pass
                st.success("API Key saved! AI features unlocked.")
                st.rerun()
            else:
                st.warning("Please enter a valid key.")
        st.markdown("[Get free key (console.groq.com)](https://console.groq.com/keys)", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("""
    <div style="font-size: 0.8rem; opacity: 0.6; text-align: center;">
        Engine v3.2 • Python & Tree-sitter Core<br>
        Local Execution • 100% Privacy Preserved
    </div>
    """, unsafe_allow_html=True)


# --------------------------------------------------
# Core Pipeline Logic (100% Preserved & Untouched)
# --------------------------------------------------

def analyze_file(filepath, language):
    """Run the full analysis pipeline for a single file and return a
    dict with every result the UI needs."""

    if language == "python":
        parsed_result = CodeParser(filepath).parse()
        warnings = CodeAnalyzer(filepath).analyze()
        complexity_result = ComplexityAnalyzer(filepath).analyze()
        tree = None
    else:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            code = f.read()
        tp = TreeParser(language)
        extracted = tp.extract(code)
        tree = extracted.pop("tree")
        parsed_result = extracted
        warnings = MultiLanguageAnalyzer(filepath, language).analyze()
        complexity_result = estimate_complexity_generic(parsed_result.get("loops", 0))

    explanation = CodeExplainer(parsed_result, language).explain()
    bugs = BugDetector(filepath, language).detect()
    security_issues = SecurityScanner(filepath).scan()

    return {
        "parsed_result": parsed_result,
        "warnings": warnings,
        "complexity_result": complexity_result,
        "explanation": explanation,
        "bugs": bugs,
        "security_issues": security_issues,
        "tree": tree,
    }


# --------------------------------------------------
# Hero Header Banner
# --------------------------------------------------

st.markdown("""
<div class="hero-banner">
    <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 12px;">
        <div>
            <h1 class="hero-title">⚡ AI Code Review & Bug Detection</h1>
            <div class="hero-subtitle">
                Automated static analysis, Tree-sitter syntax extraction, vulnerability audits, and LLM-powered review in one place.
            </div>
        </div>
        <div style="display: flex; gap: 8px; align-items: center;">
            <span class="badge-pill" style="background: rgba(99,102,241,0.15); color: #6366f1; border: 1px solid rgba(99,102,241,0.3);">
                v3.2 Production
            </span>
            <span class="badge-pill" style="background: rgba(16,185,129,0.15); color: #10b981; border: 1px solid rgba(16,185,129,0.3);">
                9 Languages Supported
            </span>
        </div>
    </div>
    <div class="lang-pills-container">
        <span class="lang-pill">🐍 Python</span>
        <span class="lang-pill">☕ Java</span>
        <span class="lang-pill">⚡ C / C++</span>
        <span class="lang-pill">🌐 JavaScript</span>
        <span class="lang-pill">📘 TypeScript</span>
        <span class="lang-pill">🐹 Go</span>
        <span class="lang-pill">🦀 Rust</span>
        <span class="lang-pill">📱 Kotlin</span>
    </div>
</div>
""", unsafe_allow_html=True)


# --------------------------------------------------
# File Upload & Quick Test Samples Section
# --------------------------------------------------

upload_col1, upload_col2 = st.columns([2.3, 1.2])
with upload_col1:
    uploaded_file = st.file_uploader(
        "Upload source code file for deep analysis",
        type=SUPPORTED_TYPES,
        help="Select any source code file (.py, .js, .ts, .java, .cpp, .c, .go, .rs, .kt)",
    )
with upload_col2:
    st.markdown("""
    <div style="padding: 8px 12px 6px 12px; border-radius: 12px; background: rgba(128,128,128,0.05); border: 1px dashed rgba(128,128,128,0.25); margin-top: 10px; margin-bottom: 8px;">
        <span style="font-weight: 700; font-size: 0.85rem;">📁 Quick Test Samples:</span><br>
        <span style="font-size: 0.76rem; opacity: 0.8;">Click any sample to load & analyze instantly:</span>
    </div>
    """, unsafe_allow_html=True)

    sc1, sc2 = st.columns(2)
    with sc1:
        if st.button("🐞 buggy.py", use_container_width=True, help="Test heuristic bugs (zero div, infinite loop)"):
            st.session_state["selected_sample"] = "buggy.py"
            st.rerun()
        if st.button("🌐 sample.js", use_container_width=True, help="Test JavaScript Tree-sitter AST & Refactoring"):
            st.session_state["selected_sample"] = "sample.js"
            st.rerun()
    with sc2:
        if st.button("🔒 insecure.py", use_container_width=True, help="Test OWASP SQLi, secrets, eval"):
            st.session_state["selected_sample"] = "insecure.py"
            st.rerun()
        if st.button("🐹 sample.go", use_container_width=True, help="Test Go language syntax & complexity"):
            st.session_state["selected_sample"] = "sample.go"
            st.rerun()

    if os.path.exists("samples"):
        sample_files = [f for f in sorted(os.listdir("samples")) if os.path.isfile(os.path.join("samples", f))]
        selected_sample_dd = st.selectbox(
            "Or choose another sample file:",
            ["-- Select from all samples --"] + sample_files,
            index=0,
            label_visibility="collapsed"
        )
        if selected_sample_dd != "-- Select from all samples --":
            if st.session_state.get("selected_sample") != selected_sample_dd:
                st.session_state["selected_sample"] = selected_sample_dd
                st.rerun()

# --------------------------------------------------
# Main View: Uploaded File vs Sample vs Onboarding Showcase
# --------------------------------------------------

active_filename = None
filepath = None
filesize_kb = 0.0
is_sample_mode = False

if uploaded_file is not None:
    st.session_state["selected_sample"] = None
    os.makedirs("uploads", exist_ok=True)
    filepath = os.path.join("uploads", uploaded_file.name)
    with open(filepath, "wb") as f:
        f.write(uploaded_file.getbuffer())
    active_filename = uploaded_file.name
    filesize_kb = uploaded_file.size / 1024
    is_sample_mode = False
elif st.session_state.get("selected_sample"):
    sample_name = st.session_state["selected_sample"]
    sample_src = os.path.join("samples", sample_name)
    if os.path.exists(sample_src):
        os.makedirs("uploads", exist_ok=True)
        filepath = os.path.join("uploads", sample_name)
        with open(sample_src, "rb") as sf:
            content_bytes = sf.read()
        with open(filepath, "wb") as df:
            df.write(content_bytes)
        active_filename = sample_name
        filesize_kb = len(content_bytes) / 1024
        is_sample_mode = True

if active_filename and filepath and os.path.exists(filepath):
    language = detect_language(active_filename)

    if "last_uploaded_file" not in st.session_state or st.session_state["last_uploaded_file"] != active_filename:
        st.session_state["last_uploaded_file"] = active_filename
        st.session_state["refactor_result"] = None
        st.session_state["ai_review_result"] = None

    # Success & Quick Status Bar with Reset button
    b_col1, b_col2 = st.columns([4, 1])
    with b_col1:
        source_label = "Sample File" if is_sample_mode else "Uploaded File"
        st.markdown(f"""
        <div class="uploaded-banner" style="margin: 8px 0;">
            <div>
                <span style="font-size: 1.1rem; font-weight: 700; color: #10b981;">✅ {source_label} Ready for Review</span>
                <div style="font-size: 0.85rem; opacity: 0.8; margin-top: 2px;">
                    <strong>{active_filename}</strong> ({filesize_kb:.2f} KB) &nbsp;•&nbsp; Detected Language: <strong>{language.capitalize()}</strong>
                </div>
            </div>
            <div>
                <span class="badge-pill badge-online">Analysis Synced</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    with b_col2:
        st.write("")
        if st.button("✕ Reset / Clear File", use_container_width=True):
            st.session_state["selected_sample"] = None
            st.session_state["last_uploaded_file"] = None
            st.session_state["refactor_result"] = None
            st.session_state["ai_review_result"] = None
            st.rerun()

    with st.spinner("⚡ Running static parsers, security engines & bug heuristics..."):
        result = analyze_file(filepath, language)

    parsed_result = result["parsed_result"]
    warnings = result["warnings"]
    complexity_result = result["complexity_result"]
    explanation = result["explanation"]
    bugs = result["bugs"]
    security_issues = result["security_issues"]
    tree = result["tree"]

    insert_analysis(
        active_filename,
        len(parsed_result["functions"]),
        len(parsed_result["classes"]),
        len(parsed_result["imports"]),
        len(warnings),
        complexity_result["complexity"],
        language=language,
        bugs=len(bugs),
        security_issues=len(security_issues),
    )

    tabs = st.tabs([
        "📊 Dashboard",
        "⚠ Static & Bugs",
        "🔒 Security",
        "🤖 AI Review & Chat",
        "🛠 Refactor",
        "🧬 Similarity",
        "📄 Report",
    ])

    # ==================================================
    # TAB 1 — Dashboard
    # ==================================================
    with tabs[0]:
        st.markdown("### 📊 Executive Metrics Overview")

        # 5 Custom Visual Metric Cards
        col_m1, col_m2, col_m3, col_m4, col_m5 = st.columns(5)
        with col_m1:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">Functions</div>
                <div class="metric-val blue">{len(parsed_result["functions"])}</div>
            </div>
            """, unsafe_allow_html=True)
        with col_m2:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">Classes</div>
                <div class="metric-val purple">{len(parsed_result["classes"])}</div>
            </div>
            """, unsafe_allow_html=True)
        with col_m3:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">Imports</div>
                <div class="metric-val emerald">{len(parsed_result["imports"])}</div>
            </div>
            """, unsafe_allow_html=True)
        with col_m4:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">Warnings</div>
                <div class="metric-val amber">{len(warnings)}</div>
            </div>
            """, unsafe_allow_html=True)
        with col_m5:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">Bugs Found</div>
                <div class="metric-val rose">{len(bugs)}</div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # Visual Analytics Section
        chart_col1, chart_col2 = st.columns(2)
        df = pd.DataFrame({
            "Category": ["Functions", "Classes", "Imports", "Warnings", "Bugs"],
            "Count": [
                len(parsed_result["functions"]),
                len(parsed_result["classes"]),
                len(parsed_result["imports"]),
                len(warnings),
                len(bugs),
            ],
        })

        with chart_col1:
            fig_pie = px.pie(
                df,
                names="Category",
                values="Count",
                hole=0.45,
                title="Code Component Composition",
                color="Category",
                color_discrete_map={
                    "Functions": "#3b82f6",
                    "Classes": "#8b5cf6",
                    "Imports": "#10b981",
                    "Warnings": "#f59e0b",
                    "Bugs": "#ef4444",
                }
            )
            fig_pie.update_layout(
                margin=dict(t=50, b=20, l=20, r=20),
                legend=dict(orientation="h", yanchor="bottom", y=-0.2),
            )
            st.plotly_chart(fig_pie, use_container_width=True)

        with chart_col2:
            fig_bar = px.bar(
                df,
                x="Category",
                y="Count",
                text="Count",
                title="Structural Quantities",
                color="Category",
                color_discrete_map={
                    "Functions": "#3b82f6",
                    "Classes": "#8b5cf6",
                    "Imports": "#10b981",
                    "Warnings": "#f59e0b",
                    "Bugs": "#ef4444",
                }
            )
            fig_bar.update_traces(textposition="outside")
            fig_bar.update_layout(
                margin=dict(t=50, b=20, l=20, r=20),
                showlegend=False,
            )
            st.plotly_chart(fig_bar, use_container_width=True)

        st.markdown("### 📋 Code Structure Breakdown")
        cs1, cs2, cs3 = st.columns(3)
        with cs1:
            st.markdown("""
            <div class="code-stat-card">
                <div class="code-stat-title">⚡ Functions Identified</div>
            </div>
            """, unsafe_allow_html=True)
            if parsed_result["functions"]:
                st.write(parsed_result["functions"])
            else:
                st.caption("No top-level functions found.")
        with cs2:
            st.markdown("""
            <div class="code-stat-card">
                <div class="code-stat-title">📦 Classes & Types</div>
            </div>
            """, unsafe_allow_html=True)
            if parsed_result["classes"]:
                st.write(parsed_result["classes"])
            else:
                st.caption("No classes detected.")
        with cs3:
            st.markdown("""
            <div class="code-stat-card">
                <div class="code-stat-title">🔗 Modules & Imports</div>
            </div>
            """, unsafe_allow_html=True)
            if parsed_result["imports"]:
                st.write(parsed_result["imports"])
            else:
                st.caption("No import statements detected.")

        if tree is not None:
            with st.expander("🌳 Syntax Tree Visualizer (Tree-sitter AST)"):
                st.code(str(tree.root_node)[:5000], language="text")

        with st.expander("📄 Full Source Code View"):
            with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                st.code(f.read(), language=language if language != "csharp" else "text")

    # ==================================================
    # TAB 2 — Static Review + Bug Detection
    # ==================================================
    with tabs[1]:
        col_st1, col_st2 = st.columns([1.2, 1])

        with col_st1:
            st.markdown("### 🐞 Detected Bugs & Anti-Patterns")
            st.caption("Automated detection: infinite loops, division by zero, dead code, logic duplicates, unused variables")
            if bugs:
                for b in bugs:
                    st.error(b)
            else:
                st.success("🎉 No bugs or code defects detected in this file!")

            st.markdown("### ⚠ Static Code Warnings")
            if warnings:
                for w in warnings:
                    if "Dangerous" in w or "unreachable" in w.lower():
                        st.error(w)
                    elif "Unused" in w or "unused" in w:
                        st.warning(w)
                    else:
                        st.info(w)
            else:
                st.success("🎉 Clean code! No static warnings raised.")

        with col_st2:
            st.markdown("### ⏱ Algorithmic Complexity")
            st.markdown(f"""
            <div style="background: rgba(99, 102, 241, 0.08); border: 1px solid rgba(99, 102, 241, 0.25); border-radius: 14px; padding: 20px; margin-bottom: 20px;">
                <span style="font-size: 0.85rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; color: #6366f1;">Estimated Big-O Time Complexity</span>
                <div style="font-size: 2.2rem; font-weight: 800; color: #4f46e5; margin: 8px 0;">{complexity_result['complexity']}</div>
                <div style="font-size: 0.92rem; opacity: 0.85;">{complexity_result['reason']}</div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("### 💡 Code Structure Explainer")
            st.markdown(explanation)

    # ==================================================
    # TAB 3 — Security Scanner
    # ==================================================
    with tabs[2]:
        st.markdown("### 🔒 Security Audit & Vulnerability Scanner")
        st.caption("Checks for SQL injection, hardcoded credentials, unsafe eval/exec, weak crypto, and command injection")

        if security_issues:
            summary = SecurityScanner.summarize(security_issues)
            s1, s2, s3 = st.columns(3)
            with s1:
                st.markdown(f"""
                <div class="metric-card" style="border-left: 4px solid #ef4444;">
                    <div class="metric-label">High Severity</div>
                    <div class="metric-val rose">{summary.get("High", 0)}</div>
                </div>
                """, unsafe_allow_html=True)
            with s2:
                st.markdown(f"""
                <div class="metric-card" style="border-left: 4px solid #f59e0b;">
                    <div class="metric-label">Medium Severity</div>
                    <div class="metric-val amber">{summary.get("Medium", 0)}</div>
                </div>
                """, unsafe_allow_html=True)
            with s3:
                st.markdown(f"""
                <div class="metric-card" style="border-left: 4px solid #3b82f6;">
                    <div class="metric-label">Low Severity</div>
                    <div class="metric-val blue">{summary.get("Low", 0)}</div>
                </div>
                """, unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)

            for issue in security_issues:
                severity_icon = {"High": "🔴", "Medium": "🟠", "Low": "🟡"}.get(issue["severity"], "⚪")
                with st.expander(f"{severity_icon} [{issue['severity']}] Line {issue['line']} — {issue['type']}"):
                    st.write(issue["message"])
                    st.code(issue["code"], language=language)
        else:
            st.success("🎉 Security clean! No known vulnerability patterns found in this file.")

    # ==================================================
    # TAB 4 — AI Review & Chatbot
    # ==================================================
    with tabs[3]:
        st.markdown("### 🤖 Groq LLM AI Code Reviewer")
        st.caption("Holistic code review: bug detection, code smells, security analysis, performance & improvements")

        if st.button("🚀 Run AI Deep Review", key="run_ai_review", type="primary"):
            with st.spinner("Querying Groq Llama 3.3 model..."):
                ai_result = AIReviewer(filepath, language).review(
                    static_bugs=bugs, static_security=security_issues
                )
            st.session_state["ai_review_result"] = ai_result

        ai_result = st.session_state.get("ai_review_result")

        if ai_result:
            if not ai_result["available"]:
                st.warning(ai_result["message"])
            else:
                sections = [
                    ("bugs", "🐞 Critical Bugs & Logic Flaws"),
                    ("code_smells", "👃 Code Smells & Architectural Issues"),
                    ("security_issues", "🔒 Security Vulnerabilities"),
                    ("performance_suggestions", "⚡ Performance & Optimization Tips"),
                    ("improvements", "💡 Best Practice Improvements"),
                ]
                for key, label in sections:
                    st.subheader(label)
                    values = ai_result.get(key) or []
                    if values:
                        for v in values:
                            st.write(f"- {v}")
                    else:
                        st.caption("No specific items identified in this category.")

        st.markdown("---")
        st.markdown("### 💬 Interactive Code Assistant")
        st.caption("Ask questions about the uploaded file's logic, edge cases, or architecture")
        question = st.text_input("Ask a question about the uploaded code", placeholder="e.g. How does the calculation handle null inputs?")

        if question:
            if not groq_client.is_configured():
                st.warning("Chat is disabled because GROQ_API_KEY is not configured in .env.")
            else:
                with st.spinner("🤖 Thinking..."):
                    try:
                        answer = CodeChatBot(filepath, language).ask(question)
                        st.markdown("#### 🤖 Assistant Response")
                        st.markdown(f"""
                        <div style="background: rgba(99, 102, 241, 0.06); border: 1px solid rgba(99, 102, 241, 0.2); border-radius: 12px; padding: 18px;">
                            {answer}
                        </div>
                        """, unsafe_allow_html=True)
                    except Exception as e:
                        st.error(f"Error: {e}")

    # ==================================================
    # TAB 5 — Refactor
    # ==================================================
    with tabs[4]:
        st.markdown("### 🛠 AI-Powered Intelligent Refactoring")
        st.caption("Improves code readability, maintainability and structure while keeping functional behavior identical")

        if st.button("✨ Generate AI Refactored Code", key="run_refactor", type="primary"):
            with st.spinner("Generating refactored version..."):
                refactor_result = CodeRefactorer(filepath, language).refactor()
            st.session_state["refactor_result"] = refactor_result

        refactor_result = st.session_state.get("refactor_result")

        if refactor_result:
            if not refactor_result["available"]:
                st.warning(refactor_result["message"])
            elif not refactor_result.get("refactored_code"):
                st.warning("⚠️ No refactored code was generated. Please click 'Generate AI Refactored Code' again.")
            else:
                col_rf1, col_rf2 = st.columns([1.4, 1])
                with col_rf1:
                    st.subheader("Refactored Code")
                    st.code(refactor_result["refactored_code"], language=language)
                    st.download_button(
                        "⬇ Download Refactored Code",
                        data=refactor_result["refactored_code"],
                        file_name=f"refactored_{active_filename}",
                        type="primary",
                        mime="text/plain",
                    )
                with col_rf2:
                    st.subheader("Key Improvements")
                    st.markdown(refactor_result["explanation"])

    # ==================================================
    # TAB 6 — Similarity Checker
    # ==================================================
    with tabs[5]:
        st.markdown("### 🧬 Plagiarism & Code Similarity Checker")
        st.caption("Compare your active file against a second source file to detect duplicate logic or code reuse")

        second_file = st.file_uploader(
            "Upload a second file to compare against",
            type=SUPPORTED_TYPES,
            key="second_file"
        )

        if second_file:
            second_path = os.path.join("uploads", f"compare_{second_file.name}")
            with open(second_path, "wb") as f:
                f.write(second_file.getbuffer())

            checker = SimilarityChecker(filepath, second_path)
            comparison = checker.compare()

            sim_pct = comparison["similarity_percent"]
            st.markdown(f"""
            <div style="background: rgba(128,128,128,0.05); border: 1px solid rgba(128,128,128,0.18); border-radius: 14px; padding: 20px; margin-bottom: 20px;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div>
                        <span style="font-size: 0.85rem; font-weight: 700; opacity: 0.7;">SIMILARITY SCORE</span>
                        <div style="font-size: 2.2rem; font-weight: 800; color: #4f46e5;">{sim_pct}%</div>
                    </div>
                    <div>
                        <span style="font-size: 1.1rem; font-weight: 700;">{SimilarityChecker.verdict(sim_pct)}</span>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

            st.progress(min(int(sim_pct), 100))

            second_language = detect_language(second_file.name)
            if second_language == "python":
                second_parsed = CodeParser(second_path).parse()
            else:
                with open(second_path, "r", encoding="utf-8", errors="ignore") as f:
                    second_parsed = TreeParser(second_language).extract(f.read())
                    second_parsed.pop("tree", None)

            structure_overlap = SimilarityChecker.compare_structures(parsed_result, second_parsed)

            st.subheader("Shared Constructs")
            oc1, oc2 = st.columns(2)
            with oc1:
                st.write("**Shared functions:**", structure_overlap["shared_functions"] or "None")
            with oc2:
                st.write("**Shared classes:**", structure_overlap["shared_classes"] or "None")

            if comparison["matching_blocks"]:
                with st.expander(f"🔍 {len(comparison['matching_blocks'])} matching code block(s) detected"):
                    for block in comparison["matching_blocks"][:10]:
                        st.caption(
                            f"{active_filename} line {block['a_start']} ↔ "
                            f"{second_file.name} line {block['b_start']} "
                            f"({block['size']} lines)"
                        )
                        st.code("\n".join(block["lines"]), language="text")
        else:
            st.info("Upload a second source file above to compute the similarity metrics.")

    # ==================================================
    # TAB 7 — Report
    # ==================================================
    with tabs[6]:
        st.markdown("### 📄 Export Executive PDF Review Report")
        st.caption("Generate a formatted PDF summary containing all metrics, detected bugs, security scan, and AI review")

        pdf = PDFReport()
        pdf_path = pdf.generate(
            active_filename,
            parsed_result,
            warnings,
            complexity_result,
            explanation,
            language=language,
            bugs=bugs,
            security_issues=security_issues,
            ai_review=st.session_state.get("ai_review_result"),
        )

        with open(pdf_path, "rb") as pdf_file:
            st.download_button(
                label="⬇ Download Complete PDF Report",
                data=pdf_file,
                file_name=f"{active_filename}_review_report.pdf",
                mime="application/pdf",
                type="primary",
            )

else:
    # --------------------------------------------------
    # Modern Empty State: Platform Feature Showcase
    # --------------------------------------------------
    st.markdown("""
    <div style="margin: 20px 0 24px 0;">
        <h3 style="margin-bottom: 6px;">✨ What This Platform Does</h3>
        <p style="opacity: 0.75; font-size: 0.95rem;">Upload any source code file above or click any sample to immediately test these 4 core pillars of analysis:</p>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown("""
        <div class="cap-card">
            <span class="cap-icon">🌳</span>
            <div class="cap-title">Multi-AST Parsing</div>
            <div class="cap-desc">
                High-performance Tree-sitter & AST engines extract functions, classes, loops, and constructs across 9 languages.
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🚀 Test JS AST (sample.js)", key="pillar_js", use_container_width=True):
            st.session_state["selected_sample"] = "sample.js"
            st.rerun()

    with c2:
        st.markdown("""
        <div class="cap-card">
            <span class="cap-icon">🐞</span>
            <div class="cap-title">Bug Detection</div>
            <div class="cap-desc">
                Zero-config heuristic detection for division by zero, infinite loops, dead code, and complexity estimates.
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🚀 Test Bugs (buggy.py)", key="pillar_buggy", use_container_width=True):
            st.session_state["selected_sample"] = "buggy.py"
            st.rerun()

    with c3:
        st.markdown("""
        <div class="cap-card">
            <span class="cap-icon">🔒</span>
            <div class="cap-title">Security Scanner</div>
            <div class="cap-desc">
                OWASP-aligned rules flag SQL injection, hardcoded credentials, command execution, and unsafe deserialization.
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🚀 Test Security (insecure.py)", key="pillar_sec", use_container_width=True):
            st.session_state["selected_sample"] = "insecure.py"
            st.rerun()

    with c4:
        st.markdown("""
        <div class="cap-card">
            <span class="cap-icon">🤖</span>
            <div class="cap-title">Groq LLM Review</div>
            <div class="cap-desc">
                Grounded AI code reviews, automated refactoring suggestions, interactive code Q&A, and PDF summaries.
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🚀 Test Go Review (sample.go)", key="pillar_go", use_container_width=True):
            st.session_state["selected_sample"] = "sample.go"
            st.rerun()

# --------------------------------------------------
# Analysis History & Audit Trail (Bottom Section)
# --------------------------------------------------

st.markdown("<br><hr style='border: none; border-top: 1px solid rgba(128,128,128,0.15); margin: 36px 0 24px 0;'>", unsafe_allow_html=True)
st.markdown("### 🗄 Analysis History & Audit Trail")

hist_col1, hist_col2 = st.columns([3, 1])
with hist_col1:
    search = st.text_input("🔍 Search history by filename", placeholder="Type a filename to filter...")
with hist_col2:
    st.write("")
    if st.button("🗑 Clear Audit History"):
        clear_history()
        st.success("History cleared successfully!")
        st.rerun()

history = get_history()

columns = ["id", "filename", "language", "functions", "classes", "imports", "warnings", "bugs", "security_issues", "complexity", "created_at"]

filtered_history = [row for row in history if search.lower() in row[1].lower()] if search else history

if filtered_history:
    for row in filtered_history[:50]:
        record = dict(zip(columns, row))
        with st.expander(f"📄 {record['filename']} ({record['language'].capitalize()}) — {record['created_at']}"):
            c1, c2, c3, c4, c5 = st.columns(5)
            c1.metric("Functions", record["functions"])
            c2.metric("Classes", record["classes"])
            c3.metric("Warnings", record["warnings"])
            c4.metric("Bugs", record["bugs"])
            c5.metric("Security", record["security_issues"])
            st.write(f"**Estimated Complexity:** `{record['complexity']}`")

    st.markdown("#### 📈 Defect Trends Across Audited Files")
    trend_df = pd.DataFrame(filtered_history, columns=columns)
    fig_trend = px.line(
        trend_df.iloc[::-1],
        x="filename",
        y="warnings",
        markers=True,
        title="Warnings Detected per File",
        color_discrete_sequence=["#6366f1"]
    )
    fig_trend.update_layout(margin=dict(t=40, b=20, l=20, r=20))
    st.plotly_chart(fig_trend, use_container_width=True)
else:
    st.info("No audit history found yet. Upload a source file above to begin tracking analyses.")
