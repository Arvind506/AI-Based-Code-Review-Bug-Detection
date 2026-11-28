import os
from reportlab.platypus import Paragraph, Spacer, PageBreak, Table, TableStyle, HRFlowable, Image
from reportlab.lib import colors
from thesis_styles import make_callout, make_code_box

def get_ch3_ch4_flowables(styles, assets_dir):
    story = []

    # =========================================================================
    # CHAPTER 3: REQUIREMENT SPECIFICATION & FEASIBILITY STUDY
    # =========================================================================
    story.append(Spacer(1, 15))
    story.append(Paragraph("Chapter 3: Requirement Specification & Feasibility Study", styles["ChapterHeader"]))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#1e3a8a"), spaceAfter=14))

    story.append(Paragraph("3.1 System Requirement Analysis & Developer Personas", styles["SectionHeader"]))
    story.append(Paragraph(
        "Software requirement analysis forms the foundational bedrock of any successful engineering effort. For an automated code review "
        "and bug detection assistant operating across polyglot languages and integrating non-deterministic generative models, precision in "
        "defining behavioral boundaries is paramount. To establish an empirical baseline of operational needs, extensive domain analysis "
        "was conducted across modern agile development workflows, continuous integration pipelines, and educational coding environments.", styles["BodyJustified"]))
    story.append(Paragraph(
        "Modern software organizations encounter severe challenges in balancing rapid continuous delivery with thorough code reviews. "
        "Developers frequently work under aggressive sprint deadlines where code review turnaround times directly dictate deployment velocity. "
        "To ensure the proposed platform solves authentic software engineering bottlenecks, user requirements were formalized through three "
        "distinct developer personas representing target user cohorts:", styles["BodyJustified"]))

    story.append(Paragraph(
        "<b>Persona 1: The Junior Software Engineer / Computer Science Student (Alex)</b><br/>"
        "Alex writes code in multiple languages (primarily Python, JavaScript, and Java) and requires immediate, didactic feedback on syntactical "
        "correctness, asymptotic algorithmic complexity, and safe coding standards. Alex often lacks deep familiarity with subtle edge cases such "
        "as infinite while loops or implicit type conversions that lead to division by zero. For Alex, the system must act as an interactive mentor, "
        "providing clear, educational explanations alongside detected bugs and generating behavior-preserving refactored code that exemplifies "
        "industry best practices without condescending or cryptic compiler diagnostics.", styles["BulletText"]))

    story.append(Paragraph(
        "<b>Persona 2: The Senior Staff Engineer / Technical Lead (Priya)</b><br/>"
        "Priya oversees pull requests across three microservices repositories. Her primary bottleneck is time: reading hundreds of lines of code "
        "every afternoon creates severe cognitive fatigue. Priya requires an automated triage assistant that can rapidly ingest pull request "
        "artifacts, compute structural code complexity, highlight duplicated code blocks across modules, and verify that no critical anti-patterns "
        "have been introduced. Priya values high precision, zero false alarms on standard idioms, sub-second execution speeds, and automated executive "
        "PDF audit reports that can be attached to compliance audits.", styles["BulletText"]))

    story.append(Paragraph(
        "<b>Persona 3: The DevSecOps & Application Security Analyst (Marcus)</b><br/>"
        "Marcus is responsible for corporate security governance. He must guarantee that no code deployed to staging or production contains "
        "OWASP Top 10 vulnerabilities—specifically SQL injection, hardcoded API secrets, command execution flaws, or unvalidated deserialization. "
        "Marcus requires standardized Common Weakness Enumeration (CWE) classifications, deterministic rule execution, and complete isolation "
        "of intellectual property so proprietary corporate source code is not permanently logged on third-party cloud servers.", styles["BulletText"]))

    story.append(make_callout(
        "By grounding architectural requirements in these three realistic personas, the system design simultaneously satisfies educational "
        "clarity, enterprise triage velocity, and rigorous cybersecurity compliance.", styles))
    story.append(Spacer(1, 10))

    story.append(Paragraph("3.1.2 Developer Persona User Journey Maps & Operational Scenarios", styles["SubSectionHeader"]))
    story.append(Paragraph(
        "To model user interaction dynamics, detailed operational scenarios were mapped for each persona:", styles["BodyJustified"]))
    story.append(Paragraph(
        "<b>Scenario A: Alex Learning Algorithmic Optimization</b><br/>"
        "Alex writes a recursive Fibonacci function in Python. Upon pasting the code into the assistant, the static parser calculates an asymptotic "
        "complexity of $O(2^n)$ and highlights the excessive branch recursion. Alex navigates to the 'Refactor' tab, clicks 'Generate AI Refactored Code', "
        "and observes how the Groq LLM converts the exponential recursion into an optimal $O(n)$ iterative dynamic programming solution with memoization. "
        "The educational explanation clarifies how dictionary caching prevents redundant call-stack execution.", styles["BulletText"]))
    story.append(Paragraph(
        "<b>Scenario B: Priya Conducting Rapid Pull Request Triage</b><br/>"
        "Priya receives a 420-line pull request containing `Receiptiframe.js`. Dragging the file into the uploader, the assistant completes Tree-sitter "
        "CST parsing in 32 milliseconds, validating zero syntax errors and flagging 1 low-severity token literal. Switching to the 'Similarity' tab, "
        "Priya compares the new implementation against a legacy billing helper, observing a 42% logic divergence. She exports the executive PDF audit report "
        "in 1.4 seconds and attaches it to the GitHub PR approval thread.", styles["BulletText"]))
    story.append(Paragraph(
        "<b>Scenario C: Marcus Auditing Legacy Microservices for OWASP Flaws</b><br/>"
        "Marcus performs an offline security audit across a folder of legacy backend scripts. The OWASP scanner instantly identifies two critical "
        "CWE-89 SQL injection vulnerabilities where raw query strings are formatted with user input. Marcus reviews the remediation cards, which provide "
        "exact parameterized query code replacements, ensuring zero code exposure to external AI services.", styles["BulletText"]))
    story.append(Spacer(1, 10))

    story.append(Paragraph("3.2 Functional Requirements Specification (FR-01 to FR-18)", styles["SectionHeader"]))
    story.append(Paragraph(
        "The functional requirements delineate the exact operational capabilities, inputs, outputs, and behavioral expectations of the "
        "system. Each requirement has been assigned an immutable identifier (FR-01 through FR-18) and prioritized according to the MoSCoW "
        "(Must-have, Should-have, Could-have, Won't-have) methodology. Table 3.1 details the complete functional specification matrix.", styles["BodyJustified"]))

    # Table 3.1: Functional Requirements Table
    fr_headers = [Paragraph("<b>ID</b>", styles["TableHead"]),
                  Paragraph("<b>Requirement Title</b>", styles["TableHead"]),
                  Paragraph("<b>Functional Description & Behavior</b>", styles["TableHead"]),
                  Paragraph("<b>Input Data</b>", styles["TableHead"]),
                  Paragraph("<b>Output Artifact</b>", styles["TableHead"]),
                  Paragraph("<b>Pri</b>", styles["TableHead"])]
    
    fr_rows = [
        [Paragraph("FR-01", styles["TableCellBold"]), Paragraph("Source File Ingestion", styles["TableCellBold"]),
         Paragraph("Allow users to upload single source code files via drag-and-drop or file browser with instant size/type validation.", styles["TableCell"]),
         Paragraph("Raw source file (.py, .js, .java, etc.)", styles["TableCell"]), Paragraph("Decoded UTF-8 string buffer", styles["TableCell"]), Paragraph("P1", styles["TableCellBold"])],
        
        [Paragraph("FR-02", styles["TableCellBold"]), Paragraph("Language Auto-Detection", styles["TableCellBold"]),
         Paragraph("Infer the programming language automatically from file extensions and shebang lines with manual override capability.", styles["TableCell"]),
         Paragraph("File metadata & filename", styles["TableCell"]), Paragraph("Standardized language tag", styles["TableCell"]), Paragraph("P1", styles["TableCellBold"])],

        [Paragraph("FR-03", styles["TableCellBold"]), Paragraph("Raw Code Editor Paste", styles["TableCellBold"]),
         Paragraph("Provide an interactive multi-line text editor allowing direct code pasting with real-time character count.", styles["TableCell"]),
         Paragraph("Raw text stream", styles["TableCell"]), Paragraph("Memory buffer in session state", styles["TableCell"]), Paragraph("P1", styles["TableCellBold"])],

        [Paragraph("FR-04", styles["TableCellBold"]), Paragraph("Native Python AST Parse", styles["TableCellBold"]),
         Paragraph("Parse Python code into official Abstract Syntax Trees using standard library <code>ast</code> with line-number metadata.", styles["TableCell"]),
         Paragraph("Python source string", styles["TableCell"]), Paragraph("ast.AST node hierarchy", styles["TableCell"]), Paragraph("P1", styles["TableCellBold"])],

        [Paragraph("FR-05", styles["TableCellBold"]), Paragraph("Polyglot Tree-sitter Parse", styles["TableCellBold"]),
         Paragraph("Execute Tree-sitter concrete syntax tree grammars for JS, TS, Java, C, C++, Go, Rust, and Kotlin.", styles["TableCell"]),
         Paragraph("Source bytes & language ID", styles["TableCell"]), Paragraph("Tree-sitter CST Tree object", styles["TableCell"]), Paragraph("P1", styles["TableCellBold"])],

        [Paragraph("FR-06", styles["TableCellBold"]), Paragraph("Syntax Error Fault Handling", styles["TableCellBold"]),
         Paragraph("Catch, isolate, and format syntax errors gracefully without crashing the analysis orchestrator.", styles["TableCell"]),
         Paragraph("Malformed source code", styles["TableCell"]), Paragraph("Formatted line/col error message", styles["TableCell"]), Paragraph("P1", styles["TableCellBold"])],

        [Paragraph("FR-07", styles["TableCellBold"]), Paragraph("Infinite Loop Detection", styles["TableCellBold"]),
         Paragraph("Detect while loops with constant True predicates lacking deterministic break/return exit statements.", styles["TableCell"]),
         Paragraph("AST While/Loop nodes", styles["TableCell"]), Paragraph("Loop bug alert with line number", styles["TableCell"]), Paragraph("P1", styles["TableCellBold"])],

        [Paragraph("FR-08", styles["TableCellBold"]), Paragraph("Zero Division Bug Detection", styles["TableCellBold"]),
         Paragraph("Identify literal or constant-folded zero division operations at compile/parse time across expressions.", styles["TableCell"]),
         Paragraph("AST BinOp nodes", styles["TableCell"]), Paragraph("Zero-division warning with line ref", styles["TableCell"]), Paragraph("P1", styles["TableCellBold"])],

        [Paragraph("FR-09", styles["TableCellBold"]), Paragraph("Dead Code Identification", styles["TableCellBold"]),
         Paragraph("Flag unreachable code statements located immediately after unconditional return, raise, break, or continue.", styles["TableCell"]),
         Paragraph("Block statement lists", styles["TableCell"]), Paragraph("Unreachable code warning list", styles["TableCell"]), Paragraph("P1", styles["TableCellBold"])],

        [Paragraph("FR-10", styles["TableCellBold"]), Paragraph("SQL Injection Scanning", styles["TableCellBold"]),
         Paragraph("Scan for dynamic string concatenation and format strings embedded within SQL query execution calls.", styles["TableCell"]),
         Paragraph("Function call expressions", styles["TableCell"]), Paragraph("CWE-89 SQLi alert (High/Crit)", styles["TableCell"]), Paragraph("P1", styles["TableCellBold"])],

        [Paragraph("FR-11", styles["TableCellBold"]), Paragraph("Hardcoded Secret Auditing", styles["TableCellBold"]),
         Paragraph("Detect exposed API keys, private tokens, passwords, and AWS credentials via Shannon entropy and regex rules.", styles["TableCell"]),
         Paragraph("String literals & assignments", styles["TableCell"]), Paragraph("CWE-798 Hardcoded secret alert", styles["TableCell"]), Paragraph("P1", styles["TableCellBold"])],

        [Paragraph("FR-12", styles["TableCellBold"]), Paragraph("Dangerous Execution Scan", styles["TableCellBold"]),
         Paragraph("Flag invocations of eval(), exec(), Function(), system(), and unsafe shell execution primitives.", styles["TableCell"]),
         Paragraph("Call AST nodes & regex tokens", styles["TableCell"]), Paragraph("CWE-95 Arbitrary code exec alert", styles["TableCell"]), Paragraph("P1", styles["TableCellBold"])],

        [Paragraph("FR-13", styles["TableCellBold"]), Paragraph("Big-O Complexity Analysis", styles["TableCellBold"]),
         Paragraph("Calculate maximum loop nesting depth and recursive call paths to estimate asymptotic time complexity.", styles["TableCell"]),
         Paragraph("Function AST subtrees", styles["TableCell"]), Paragraph("Big-O classification (O(1) to O(2^n))", styles["TableCell"]), Paragraph("P2", styles["TableCellBold"])],

        [Paragraph("FR-14", styles["TableCellBold"]), Paragraph("Code Logic Similarity Diff", styles["TableCellBold"]),
         Paragraph("Perform dual-buffer normalized sequence comparison to identify duplicated or plagiarized logic blocks.", styles["TableCell"]),
         Paragraph("Two code text buffers", styles["TableCell"]), Paragraph("Similarity % and inline visual diff", styles["TableCell"]), Paragraph("P2", styles["TableCellBold"])],

        [Paragraph("FR-15", styles["TableCellBold"]), Paragraph("Contextual AI Code Review", styles["TableCellBold"]),
         Paragraph("Prompt Groq-accelerated LLMs with injected static findings to generate semantic code quality reviews.", styles["TableCell"]),
         Paragraph("Code + Static findings JSON", styles["TableCell"]), Paragraph("Markdown review report", styles["TableCell"]), Paragraph("P1", styles["TableCellBold"])],

        [Paragraph("FR-16", styles["TableCellBold"]), Paragraph("Automated AI Refactoring", styles["TableCellBold"]),
         Paragraph("Generate fully refactored, production-ready code addressing all detected flaws while preserving behavior.", styles["TableCell"]),
         Paragraph("Original code + issues list", styles["TableCell"]), Paragraph("Refactored code + explanation", styles["TableCell"]), Paragraph("P1", styles["TableCellBold"])],

        [Paragraph("FR-17", styles["TableCellBold"]), Paragraph("SQLite Audit Persistence", styles["TableCellBold"]),
         Paragraph("Store all completed file analyses, bug counts, security ratings, and timestamps in local SQLite database.", styles["TableCell"]),
         Paragraph("Analysis outcome record", styles["TableCell"]), Paragraph("Persistent relational DB row", styles["TableCell"]), Paragraph("P2", styles["TableCellBold"])],

        [Paragraph("FR-18", styles["TableCellBold"]), Paragraph("Executive PDF Report Export", styles["TableCellBold"]),
         Paragraph("Compile full audit findings, metric summaries, and code snippets into downloadable publication-grade PDF.", styles["TableCell"]),
         Paragraph("Session review state", styles["TableCell"]), Paragraph("A4 PDF document binary", styles["TableCell"]), Paragraph("P1", styles["TableCellBold"])],
    ]

    t_fr = Table([fr_headers] + fr_rows, colWidths=[38, 85, 162, 85, 75, 20])
    t_fr.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1e3a8a")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#f8fafc")]),
    ]))
    story.append(t_fr)
    story.append(Paragraph("<b>Table 3.1:</b> Complete Functional Requirements Specification (FR-01 to FR-18)", styles["FigCaption"]))
    story.append(Spacer(1, 12))

    story.append(Paragraph("3.3 Non-Functional Requirements Specification (NFR-01 to NFR-10)", styles["SectionHeader"]))
    story.append(Paragraph(
        "Non-functional requirements specify the quality attributes, operational constraints, performance thresholds, and architectural "
        "guarantees of the system. In developer tooling, non-functional characteristics such as sub-second latency and zero memory leakage "
        "frequently determine whether software engineers adopt or abandon an assistant. Table 3.2 details the ten non-functional requirements.", styles["BodyJustified"]))

    nfr_headers = [Paragraph("<b>ID</b>", styles["TableHead"]),
                   Paragraph("<b>Quality Attribute</b>", styles["TableHead"]),
                   Paragraph("<b>Target Metric / Quantitative Threshold</b>", styles["TableHead"]),
                   Paragraph("<b>Verification & Acceptance Method</b>", styles["TableHead"])]
    
    nfr_rows = [
        [Paragraph("NFR-01", styles["TableCellBold"]), Paragraph("Static Execution Latency", styles["TableCellBold"]),
         Paragraph("Deterministic AST, bug, and security analysis must complete within <b>&le; 50 ms</b> for files up to 1,000 LOC.", styles["TableCell"]),
         Paragraph("Automated benchmark timer over 100 test files across all 9 supported languages.", styles["TableCell"])],

        [Paragraph("NFR-02", styles["TableCellBold"]), Paragraph("AI Inference Turnaround", styles["TableCellBold"]),
         Paragraph("LLM-powered code review and refactoring generation must complete within <b>&le; 3.5 seconds</b> via Groq LPUs.", styles["TableCell"]),
         Paragraph("Network latency profiling and API response timing instrumentation.", styles["TableCell"])],

        [Paragraph("NFR-03", styles["TableCellBold"]), Paragraph("Memory Footprint", styles["TableCellBold"]),
         Paragraph("Peak runtime RAM consumption of the local Python/Streamlit process must not exceed <b>250 MB</b> under active load.", styles["TableCell"]),
         Paragraph("Process memory profiling via Python <code>psutil</code> during multi-file execution.", styles["TableCell"])],

        [Paragraph("NFR-04", styles["TableCellBold"]), Paragraph("Zero Data Retention Privacy", styles["TableCellBold"]),
         Paragraph("Zero persistent cloud storage of user source code. Analyzed files must reside strictly in local RAM and SQLite.", styles["TableCell"]),
         Paragraph("Network payload audit ensuring API requests transmit only ephemeral LLM context.", styles["TableCell"])],

        [Paragraph("NFR-05", styles["TableCellBold"]), Paragraph("Deterministic Reproducibility", styles["TableCellBold"]),
         Paragraph("Static AST, heuristic bug detection, and security rules must achieve <b>100% deterministic repeatability</b> across runs.", styles["TableCell"]),
         Paragraph("Automated regression test asserting identical JSON output across 50 consecutive runs.", styles["TableCell"])],

        [Paragraph("NFR-06", styles["TableCellBold"]), Paragraph("Fault Tolerance & Fallback", styles["TableCellBold"]),
         Paragraph("If the Groq API key is missing or network is unavailable, static AST and security features must remain 100% functional.", styles["TableCell"]),
         Paragraph("Air-gapped network disconnection test verifying full offline static analysis.", styles["TableCell"])],

        [Paragraph("NFR-07", styles["TableCellBold"]), Paragraph("Cross-Platform Portability", styles["TableCellBold"]),
         Paragraph("Full operational compatibility across Windows 10/11, macOS (Apple Silicon & Intel), and Linux (Ubuntu 20.04+).", styles["TableCell"]),
         Paragraph("Cross-platform test execution on native operating system environments.", styles["TableCell"])],

        [Paragraph("NFR-08", styles["TableCellBold"]), Paragraph("Polyglot Extensibility", styles["TableCellBold"]),
         Paragraph("Adding support for a new programming language must require only grammar binding without modifying core engine logic.", styles["TableCell"]),
         Paragraph("Architectural inspection of Tree-sitter grammar registry decoupling.", styles["TableCell"])],

        [Paragraph("NFR-09", styles["TableCellBold"]), Paragraph("Security Classification Standards", styles["TableCellBold"]),
         Paragraph("All identified vulnerabilities must map directly to MITRE Common Weakness Enumeration (CWE) and OWASP Top 10.", styles["TableCell"]),
         Paragraph("Formal validation against MITRE CWE-89, CWE-798, CWE-95, CWE-78 taxonomies.", styles["TableCell"])],

        [Paragraph("NFR-10", styles["TableCellBold"]), Paragraph("User Interface Accessibility", styles["TableCellBold"]),
         Paragraph("Responsive dark-mode UI with high contrast ratios (&ge; 4.5:1) compliant with WCAG 2.1 AA accessibility guidelines.", styles["TableCell"]),
         Paragraph("Automated color contrast evaluation and developer usability testing.", styles["TableCell"])],
    ]

    t_nfr = Table([nfr_headers] + nfr_rows, colWidths=[45, 110, 160, 150])
    t_nfr.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1e3a8a")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#f8fafc")]),
    ]))
    story.append(t_nfr)
    story.append(Paragraph("<b>Table 3.2:</b> Non-Functional Quality Attributes and Acceptance Criteria", styles["FigCaption"]))
    story.append(Spacer(1, 12))

    story.append(Paragraph("3.4 Software and Hardware Specification Matrix", styles["SectionHeader"]))
    story.append(Paragraph(
        "To guarantee reproducible execution across both development workstations and production deployment nodes, strict minimum and "
        "recommended hardware/software specifications were formulated. Table 3.3 presents the environmental specification matrix.", styles["BodyJustified"]))

    hw_headers = [Paragraph("<b>System Dimension</b>", styles["TableHead"]),
                  Paragraph("<b>Development Workstation Specifications</b>", styles["TableHead"]),
                  Paragraph("<b>Minimum Deployment Node Specifications</b>", styles["TableHead"])]
    
    hw_rows = [
        [Paragraph("Operating System", styles["TableCellBold"]),
         Paragraph("Windows 11 Pro 64-bit / Ubuntu 22.04 LTS", styles["TableCell"]),
         Paragraph("Windows 10+, macOS 12+, Linux (glibc &ge; 2.27)", styles["TableCell"])],

        [Paragraph("Central Processor (CPU)", styles["TableCellBold"]),
         Paragraph("Intel Core i7-12700H (14 Cores, 20 Threads) @ 2.70 GHz", styles["TableCell"]),
         Paragraph("Dual-core 64-bit x86_64 or ARM64 processor @ 1.5 GHz", styles["TableCell"])],

        [Paragraph("System Memory (RAM)", styles["TableCellBold"]),
         Paragraph("16.0 GB DDR4 @ 3200 MHz", styles["TableCell"]),
         Paragraph("2.0 GB RAM (Engine requires &lt; 250 MB runtime RAM)", styles["TableCell"])],

        [Paragraph("Storage & File System", styles["TableCellBold"]),
         Paragraph("512 GB NVMe M.2 SSD (Read: 3500 MB/s, Write: 3000 MB/s)", styles["TableCell"]),
         Paragraph("500 MB available persistent disk space for venv and caches", styles["TableCell"])],

        [Paragraph("Python Runtime Environment", styles["TableCellBold"]),
         Paragraph("Python 3.11.9 (64-bit CPython implementation)", styles["TableCell"]),
         Paragraph("Python 3.10, 3.11, or 3.12 (CPython)", styles["TableCell"])],

        [Paragraph("Core Python Libraries", styles["TableCellBold"]),
         Paragraph("Streamlit 1.32+, Plotly 5.20+, Tree-sitter 0.21.3, tree-sitter-languages 1.10.2, ReportLab 4.1+", styles["TableCell"]),
         Paragraph("Standard virtual environment dependencies via requirements.txt", styles["TableCell"])],

        [Paragraph("AI Inference Accelerators", styles["TableCellBold"]),
         Paragraph("Groq Cloud LPU Infrastructure (Llama-3.3-70b / GPT-OSS-120b)", styles["TableCell"]),
         Paragraph("Outbound HTTPS (port 443) connectivity to api.groq.com", styles["TableCell"])],

        [Paragraph("Embedded Relational Database", styles["TableCellBold"]),
         Paragraph("SQLite 3.42.0 (Zero-configuration embedded engine)", styles["TableCell"]),
         Paragraph("Native Python sqlite3 module (no external daemon)", styles["TableCell"])],

        [Paragraph("User Interface Client", styles["TableCellBold"]),
         Paragraph("Google Chrome 122+, Mozilla Firefox 123+, Microsoft Edge", styles["TableCell"]),
         Paragraph("Any modern Evergreen Web Browser supporting HTML5/CSS3", styles["TableCell"])],
    ]

    t_hw = Table([hw_headers] + hw_rows, colWidths=[120, 175, 170])
    t_hw.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1e3a8a")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#f8fafc")]),
    ]))
    story.append(t_hw)
    story.append(Paragraph("<b>Table 3.3:</b> Hardware and Software Operating Environment Specifications", styles["FigCaption"]))
    story.append(Spacer(1, 10))

    story.append(Paragraph("3.5 Multi-Dimensional Feasibility Study", styles["SectionHeader"]))
    story.append(Paragraph(
        "Prior to committing implementation resources, a rigorous four-pillar feasibility investigation was conducted to validate technical, "
        "economic, operational, and legal viability.", styles["BodyJustified"]))

    story.append(Paragraph(
        "<b>1. Technical Feasibility:</b><br/>"
        "The technical feasibility hinges on whether multi-language AST parsing, heuristic analysis, and LLM inference can execute synchronously "
        "within a responsive user session. Tree-sitter provides pre-compiled C-grammar bindings that generate concrete syntax trees in sub-10ms "
        "times, completely eliminating compilation overhead. Furthermore, Groq's Language Processing Units (LPUs) achieve inference generation "
        "speeds exceeding 300 tokens per second, allowing multi-paragraph code reviews to return in under 3 seconds. The Python ecosystem natively "
        "supports AST introspection, SQLite integration, and reactive Streamlit web components, confirming unequivocal technical feasibility.", styles["BulletText"]))

    story.append(Paragraph(
        "<b>2. Economic & Commercial Feasibility:</b><br/>"
        "Enterprise code review tools such as SonarQube Enterprise, Coverity, and Veracode impose steep recurring license fees ranging from "
        "$5,000 to $50,000 annually. In contrast, the proposed architecture is constructed entirely from open-source technologies (Python, "
        "Streamlit, Tree-sitter, ReportLab). Groq offers a generous free-tier API allowance for research and developer workloads, making the "
        "operational hosting cost virtually zero. By automating routine syntax and security triage, engineering organizations can reclaim up "
        "to 20% of senior developer hours, yielding an exceptionally high return on investment (ROI).", styles["BulletText"]))

    story.append(Paragraph(
        "<b>3. Operational & Organizational Feasibility:</b><br/>"
        "Many advanced static analysis suites fail commercially because they require complex command-line configurations, dedicated database "
        "servers, and weeks of developer training. The proposed system features an intuitive web dashboard requiring zero onboarding. Users simply "
        "drag-and-drop source files to receive immediate visual analytics. Its operational footprint is self-contained, requiring only a standard "
        "Python virtual environment and a single execution command (<code>run.bat</code> or <code>run.ps1</code>).", styles["BulletText"]))

    story.append(Paragraph(
        "<b>4. Legal, Regulatory & Ethical Feasibility:</b><br/>"
        "All underlying libraries are distributed under permissive open-source licenses (MIT, Apache 2.0, BSD-3-Clause), completely eliminating "
        "copyleft contagion risks. Regarding intellectual property protection, user source code is processed strictly in local volatility and "
        "ephemeral memory; Groq's developer API terms explicitly stipulate that prompt inputs are not retained or used for foundation model training. "
        "The system complies fully with academic integrity ethics and corporate data governance policies.", styles["BulletText"]))

    story.append(Paragraph("3.6 Validation and Quality Acceptance Criteria", styles["SectionHeader"]))
    story.append(Paragraph(
        "Formal quality acceptance criteria were established to govern testing and release sign-off. The project must satisfy the following benchmarks:", styles["BodyJustified"]))
    story.append(Paragraph("• <b>Parsing Robustness:</b> Zero unhandled exceptions or crashes when parsing valid code across all 9 supported languages.", styles["BulletText"]))
    story.append(Paragraph("• <b>Bug Detection Precision:</b> &ge; 95% precision on deterministic test suites targeting infinite loops, zero division, and dead code.", styles["BulletText"]))
    story.append(Paragraph("• <b>Security Audit Recall:</b> 100% recall on OWASP benchmark testbeds for plain-text API secrets, SQL injections, and eval() calls.", styles["BulletText"]))
    story.append(Paragraph("• <b>Behavior-Preserving Refactoring:</b> AI-generated refactored code must pass identical functional assertions without altering program output.", styles["BulletText"]))
    story.append(Paragraph("• <b>Executive Report Delivery:</b> Flawless PDF generation with professional typography, headers, footers, and page numbers under 2 seconds.", styles["BulletText"]))

    story.append(Paragraph("3.7 Planning and Scheduling (Gantt Chart)", styles["SectionHeader"]))
    story.append(Paragraph(
        "The project was planned from 20 September to 20 November 2026 (about 9 weeks / 60 days). The chart below shows each "
        "phase, its duration and its overlap with other phases. The dates are taken from the development history of the "
        "project, and each working feature was released as soon as it was ready (version 1.0 to 3.2).", styles["BodyJustified"]))
    story.append(Spacer(1, 4))

    # Figure 3.1: Gantt Chart
    gantt_path = os.path.join(assets_dir, "fig_gantt.png")
    if os.path.exists(gantt_path):
        story.append(Image(gantt_path, width=440, height=225))
        story.append(Paragraph("<b>Figure 3.1:</b> Project schedule (Gantt chart)", styles["FigCaption"]))
    story.append(Spacer(1, 10))

    story.append(Paragraph("3.8 Requirements Traceability Matrix (RTM)", styles["SectionHeader"]))
    story.append(Paragraph(
        "The Requirements Traceability Matrix (Table 3.4) establishes bi-directional mapping between target developer personas, functional "
        "requirements, non-functional constraints, and verification test cases, guaranteeing that every design decision directly serves user needs.", styles["BodyJustified"]))

    # Table 3.4
    rtm_headers = [Paragraph("<b>Persona Cohort</b>", styles["TableHead"]),
                   Paragraph("<b>User Need / Problem Statement</b>", styles["TableHead"]),
                   Paragraph("<b>Mapped Functional Req</b>", styles["TableHead"]),
                   Paragraph("<b>Mapped NFR Constraint</b>", styles["TableHead"]),
                   Paragraph("<b>Validating Test Case</b>", styles["TableHead"])]
    
    rtm_rows = [
        [Paragraph("Alex (Junior Dev)", styles["TableCellBold"]), Paragraph("Instant feedback on infinite loops and zero division bugs", styles["TableCell"]),
         Paragraph("FR-07, FR-08", styles["TableCellBold"]), Paragraph("NFR-01 (Latency &le; 50ms)", styles["TableCell"]), Paragraph("TC-06, TC-07, TC-08", styles["TableCellBold"])],

        [Paragraph("Alex (Junior Dev)", styles["TableCellBold"]), Paragraph("Clear educational refactoring explaining bad code patterns", styles["TableCell"]),
         Paragraph("FR-15, FR-16", styles["TableCellBold"]), Paragraph("NFR-02 (AI &le; 3.5s)", styles["TableCell"]), Paragraph("TC-16, TC-17, TC-18", styles["TableCellBold"])],

        [Paragraph("Priya (Tech Lead)", styles["TableCellBold"]), Paragraph("Rapid polyglot pull request triage across JS and Python", styles["TableCell"]),
         Paragraph("FR-01, FR-04, FR-05", styles["TableCellBold"]), Paragraph("NFR-07, NFR-08 (Polyglot)", styles["TableCell"]), Paragraph("TC-01, TC-03, TC-04", styles["TableCellBold"])],

        [Paragraph("Priya (Tech Lead)", styles["TableCellBold"]), Paragraph("Detect duplicated logic blocks and code plagiarism across PRs", styles["TableCell"]),
         Paragraph("FR-14", styles["TableCellBold"]), Paragraph("NFR-05 (Deterministic)", styles["TableCell"]), Paragraph("TC-15", styles["TableCellBold"])],

        [Paragraph("Priya (Tech Lead)", styles["TableCellBold"]), Paragraph("One-click compliance PDF report to attach to ticket approvals", styles["TableCell"]),
         Paragraph("FR-18", styles["TableCellBold"]), Paragraph("NFR-10 (Usability &le; 2s)", styles["TableCell"]), Paragraph("TC-20, UI-08", styles["TableCellBold"])],

        [Paragraph("Marcus (SecOps)", styles["TableCellBold"]), Paragraph("Scan code for plain-text API keys and AWS secrets", styles["TableCell"]),
         Paragraph("FR-11", styles["TableCellBold"]), Paragraph("NFR-09 (CWE-798 Compliance)", styles["TableCell"]), Paragraph("TC-12", styles["TableCellBold"])],

        [Paragraph("Marcus (SecOps)", styles["TableCellBold"]), Paragraph("Audit SQL injection and dangerous eval/exec calls", styles["TableCell"]),
         Paragraph("FR-10, FR-12", styles["TableCellBold"]), Paragraph("NFR-09 (CWE-89, CWE-95)", styles["TableCell"]), Paragraph("TC-11, TC-13, TC-14", styles["TableCellBold"])],

        [Paragraph("Marcus (SecOps)", styles["TableCellBold"]), Paragraph("Zero cloud code retention and persistent local audit trails", styles["TableCell"]),
         Paragraph("FR-17", styles["TableCellBold"]), Paragraph("NFR-04 (Zero Retention)", styles["TableCell"]), Paragraph("TC-19, UI-10", styles["TableCellBold"])],
    ]

    t_rtm = Table([rtm_headers] + rtm_rows, colWidths=[90, 130, 85, 90, 70])
    t_rtm.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1e3a8a")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#f8fafc")]),
    ]))
    story.append(t_rtm)
    story.append(Paragraph("<b>Table 3.4:</b> Requirements Traceability Matrix (RTM)", styles["FigCaption"]))
    story.append(PageBreak())

    # =========================================================================
    # CHAPTER 4: SYSTEM ARCHITECTURE AND DETAILED DESIGN
    # =========================================================================
    story.append(Spacer(1, 15))
    story.append(Paragraph("Chapter 4: System Architecture and Detailed Design", styles["ChapterHeader"]))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#1e3a8a"), spaceAfter=14))

    story.append(Paragraph("4.1 Three-Tier Layered Architecture Formalization", styles["SectionHeader"]))
    story.append(Paragraph(
        "Software architectural design establishes the structural blueprints, module boundaries, inter-component communication contracts, "
        "and data access protocols of a system. To maximize maintainability, testability, and operational resilience, the AI Code Review & "
        "Bug Detection platform is formalized as a <b>Three-Tier Decoupled Layered Architecture</b>:", styles["BodyJustified"]))

    story.append(Paragraph(
        "<b>1. Presentation & Interaction Tier (Streamlit Web Client):</b><br/>"
        "The presentation tier provides an intuitive, reactive, browser-based user interface constructed using modern Streamlit and custom "
        "glassmorphism CSS design tokens. It encapsulates user input widgets (file uploaders, text areas, language select boxes), interactive "
        "metric cards, Plotly visual analytics charts, syntax-highlighted code editors, and one-click PDF report generators. The presentation "
        "layer maintains reactive session state, ensuring seamless transitions across multi-tab workflows without page reloading.", styles["BulletText"]))

    story.append(Paragraph(
        "<b>2. Application & Analysis Logic Tier (Core Engines):</b><br/>"
        "The logic tier constitutes the computational core of the platform, orchestrating several specialized sub-engines: "
        "(a) the AST Parsing Engine (dual-engine Python AST and Tree-sitter CST), (b) the Heuristic Bug Detection Engine, (c) the OWASP Security "
        "Auditing Engine, (d) the Asymptotic Complexity Estimator, (e) the Normalized Sequence Logic Similarity Engine, and (f) the LLM Refactoring "
        "and Prompt Orchestrator. These engines operate as pure, decoupled functional units that accept raw source buffers and produce standardized "
        "dictionary and JSON payloads without direct coupling to UI widgets.", styles["BulletText"]))

    story.append(Paragraph(
        "<b>3. Data Persistence & Cloud Intelligence Tier:</b><br/>"
        "The data tier provides dual functionality: persistent local audit logging via an embedded SQLite3 relational database engine, and "
        "high-speed generative intelligence via secure, authenticated HTTPS API connections to Groq Cloud's Language Processing Unit (LPU) "
        "clusters hosting Llama 3.3 and GPT-OSS models.", styles["BulletText"]))

    story.append(Paragraph(
        "Figure 4.1 provides a comprehensive structural visualization of this three-tier layered architecture, showing the exact flow of data "
        "and control across presentation, logic, and persistence boundaries.", styles["BodyJustified"]))
    story.append(Spacer(1, 4))

    # Figure 4.1: Architecture Diagram
    arch_path = os.path.join(assets_dir, "fig_arch.png")
    if os.path.exists(arch_path):
        story.append(Image(arch_path, width=420, height=280))
        story.append(Paragraph("<b>Figure 4.1:</b> Three-Tier Layered System Architecture Diagram", styles["FigCaption"]))
    story.append(Spacer(1, 10))

    story.append(Paragraph("4.2 Modular Decomposition & Engine Responsibilities", styles["SectionHeader"]))
    story.append(Paragraph(
        "To enforce the Single Responsibility Principle (SRP) and High Cohesion / Low Coupling architectural heuristics, the codebase is "
        "partitioned into nine discrete functional modules. Table 4.1 summarizes each module's filename, structural tier, computational "
        "responsibilities, and interface contracts.", styles["BodyJustified"]))

    mod_headers = [Paragraph("<b>Module File</b>", styles["TableHead"]),
                   Paragraph("<b>Architectural Tier</b>", styles["TableHead"]),
                   Paragraph("<b>Core Computational Responsibilities</b>", styles["TableHead"]),
                   Paragraph("<b>Primary Input / Output</b>", styles["TableHead"])]
    
    mod_rows = [
        [Paragraph("<code>app.py</code>", styles["TableCellBold"]), Paragraph("Presentation Tier", styles["TableCell"]),
         Paragraph("Streamlit entrypoint, session state coordinator, modern CSS styling, tabs orchestration, metric cards, and Plotly visualizations.", styles["TableCell"]),
         Paragraph("User events &rarr; Rendered HTML/DOM widgets", styles["TableCell"])],

        [Paragraph("<code>backend/parser.py</code>", styles["TableCellBold"]), Paragraph("Logic Tier (Parsing)", styles["TableCell"]),
         Paragraph("Native Python AST analysis using NodeVisitor pattern. Extracts functions, classes, docstrings, imports, and AST node metrics.", styles["TableCell"]),
         Paragraph("Python code &rarr; Node dict & ast.AST tree", styles["TableCell"])],

        [Paragraph("<code>backend/tree_parser.py</code>", styles["TableCellBold"]), Paragraph("Logic Tier (Parsing)", styles["TableCell"]),
         Paragraph("Polyglot CST parsing via Tree-sitter. Maps concrete syntax grammar nodes for JS, TS, Java, C, C++, Go, Rust, and Kotlin.", styles["TableCell"]),
         Paragraph("Source bytes + lang &rarr; CST node tree", styles["TableCell"])],

        [Paragraph("<code>backend/bug_detector.py</code>", styles["TableCellBold"]), Paragraph("Logic Tier (Heuristics)", styles["TableCell"]),
         Paragraph("Static detection of deterministic bugs: infinite while loops, constant zero division, dead/unreachable code, and logic duplicates.", styles["TableCell"]),
         Paragraph("AST tree / source &rarr; Bug alerts list", styles["TableCell"])],

        [Paragraph("<code>backend/security_scanner.py</code>", styles["TableCellBold"]), Paragraph("Logic Tier (Security)", styles["TableCell"]),
         Paragraph("OWASP Top 10 and CWE-aligned vulnerability scanner. Audits SQL injection, hardcoded secrets, unsafe eval/exec, and command injection.", styles["TableCell"]),
         Paragraph("Source string &rarr; Vulnerability record dict", styles["TableCell"])],

        [Paragraph("<code>backend/complexity.py</code>", styles["TableCellBold"]), Paragraph("Logic Tier (Metrics)", styles["TableCell"]),
         Paragraph("Asymptotic Big-O time complexity estimator. Computes maximum loop nesting depth and recursive self-invocations per function.", styles["TableCell"]),
         Paragraph("AST function nodes &rarr; Big-O string", styles["TableCell"])],

        [Paragraph("<code>backend/similarity.py</code>", styles["TableCellBold"]), Paragraph("Logic Tier (Diff)", styles["TableCell"]),
         Paragraph("Normalized sequence comparison engine. Strips whitespace and comments to compute logic similarity percentages and visual diffs.", styles["TableCell"]),
         Paragraph("Two code buffers &rarr; Ratio % + HTML diff", styles["TableCell"])],

        [Paragraph("<code>backend/groq_client.py</code>", styles["TableCellBold"]), Paragraph("Intelligence Tier", styles["TableCell"]),
         Paragraph("Groq SDK client wrapper. Handles API key discovery, model fallback orchestration, system prompt construction, and chat completions.", styles["TableCell"]),
         Paragraph("Prompt messages &rarr; LLM text stream", styles["TableCell"])],

        [Paragraph("<code>backend/refactorer.py</code>", styles["TableCellBold"]), Paragraph("Intelligence Tier", styles["TableCell"]),
         Paragraph("Automated refactoring engine. Injects detected static flaws into Groq prompts and parses code blocks and explanations robustly.", styles["TableCell"]),
         Paragraph("Code + flaws &rarr; Refactored code + notes", styles["TableCell"])],
    ]

    t_mod = Table([mod_headers] + mod_rows, colWidths=[105, 75, 175, 110])
    t_mod.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1e3a8a")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#f8fafc")]),
    ]))
    story.append(t_mod)
    story.append(Paragraph("<b>Table 4.1:</b> Module Decomposition and Architectural Responsibilities", styles["FigCaption"]))
    story.append(Spacer(1, 10))

    story.append(Paragraph("4.3 Data Flow Modeling (DFD Level 0 Context & Level 1 Overview)", styles["SectionHeader"]))
    story.append(Paragraph(
        "Data Flow Diagrams (DFDs) formally model the trajectory of information through the system, identifying external entities, processing "
        "nodes, data stores, and intermediate data pipelines. The system is modeled at two levels of abstraction:", styles["BodyJustified"]))
    story.append(Paragraph(
        "<b>DFD Level 0 (Context Level):</b><br/>"
        "At the macro context level, the entire review assistant is represented as a single centralized process entity interacting with four "
        "external boundary entities: (1) The Software Developer, who provides raw source code files and receives visual diagnostics and PDF "
        "reports; (2) The Groq LPU Cloud Cluster, which receives grounded prompts and returns generative reviews and refactored code; (3) The "
        "Local Operating File System, which supplies uploaded source artifacts and stores exported PDFs; and (4) The SQLite Database Store, "
        "which persists immutable audit trail records.", styles["BulletText"]))
    story.append(Paragraph(
        "<b>DFD Level 1 (Decomposed Functional Process Overview):</b><br/>"
        "Level 1 decomposes the central review process into four interconnected sub-processes: Process 1.0 (File Ingestion & Language Identification), "
        "Process 2.0 (Dual-Engine AST & Concrete Syntax Tree Parsing), Process 3.0 (Multi-Engine Static Bug, Security & Complexity Auditing), and "
        "Process 4.0 (Grounding & Generative AI Refactoring / Reporting).", styles["BulletText"]))

    story.append(Paragraph(
        "Figure 4.2 illustrates the complete Data Flow Diagram, depicting both Level 0 Context boundaries and Level 1 internal data pipelines.", styles["BodyJustified"]))
    story.append(Spacer(1, 4))

    # Figure 4.2: DFD Diagram
    dfd_path = os.path.join(assets_dir, "fig_dfd0.png")
    if os.path.exists(dfd_path):
        story.append(Image(dfd_path, width=440, height=260))
        story.append(Paragraph("<b>Figure 4.2:</b> Data Flow Diagram (DFD Level 0 Context & Level 1 Process)", styles["FigCaption"]))
    story.append(Spacer(1, 10))

    story.append(Paragraph("4.4 UML Behavioral Modeling: Use Case Diagram & Actor Specifications", styles["SectionHeader"]))
    story.append(Paragraph(
        "Unified Modeling Language (UML) behavioral modeling captures user-system interactions, functional goals, and boundary conditions. "
        "The primary human actor is the Software Developer / Code Reviewer, interacting alongside two secondary automated actors: the Groq "
        "LPU Cloud Service and the Local SQLite Storage Engine. Figure 4.3 depicts the UML Use Case Diagram.", styles["BodyJustified"]))
    story.append(Spacer(1, 4))

    # Figure 4.3: Use Case Diagram
    uc_path = os.path.join(assets_dir, "fig_usecase.png")
    if os.path.exists(uc_path):
        story.append(Image(uc_path, width=420, height=290))
        story.append(Paragraph("<b>Figure 4.3:</b> UML Use Case Diagram for Code Review Platform", styles["FigCaption"]))
    story.append(Spacer(1, 10))

    story.append(Paragraph("<b>Detailed Use Case Narrative Specifications:</b>", styles["SubSectionHeader"]))
    story.append(Paragraph(
        "<b>Use Case UC-01: Ingest and Analyze Polyglot Source File</b><br/>"
        "• <i>Primary Actor:</i> Software Developer.<br/>"
        "• <i>Preconditions:</i> Streamlit web server is running; user navigates to dashboard URL.<br/>"
        "• <i>Main Success Scenario:</i> Developer drops a source code file into the file uploader. The system determines language identity via "
        "extension, extracts character/line counts, routes the buffer to either the native Python AST engine or Tree-sitter CST parser, and populates "
        "the AST metrics summary card within 50 milliseconds.<br/>"
        "• <i>Exception Flow:</i> If file encoding is invalid, system displays a non-blocking warning and attempts UTF-8 error replacement.", styles["BulletText"]))

    story.append(Paragraph(
        "<b>Use Case UC-02: Execute Deterministic Security and Heuristic Bug Scan</b><br/>"
        "• <i>Primary Actor:</i> Software Developer.<br/>"
        "• <i>Preconditions:</i> Code is loaded in session state.<br/>"
        "• <i>Main Success Scenario:</i> System executes the Heuristic Bug Detector and OWASP Security Scanner concurrently. Findings are grouped "
        "by severity (Critical, High, Medium, Low) and rendered in tabular cards with line numbers and recommended fixes.<br/>"
        "• <i>Postconditions:</i> Summary metrics are logged to session state for PDF compilation.", styles["BulletText"]))

    story.append(Paragraph(
        "<b>Use Case UC-03: Generate Context-Grounded AI Code Review & Refactoring</b><br/>"
        "• <i>Primary Actor:</i> Software Developer.<br/>"
        "• <i>Secondary Actor:</i> Groq LPU Cloud Service.<br/>"
        "• <i>Preconditions:</i> Valid Groq API key configured in .env; static analysis completed.<br/>"
        "• <i>Main Success Scenario:</i> Developer clicks 'Generate AI Refactored Code'. System constructs a grounded prompt embedding detected flaws, "
        "invokes `openai/gpt-oss-120b`, parses the returned code block and markdown explanation, and renders side-by-side diff editors with a one-click "
        "download button.<br/>"
        "• <i>Exception Flow:</i> If API rate limit or network error occurs, system displays an informative badge and falls back to static findings.", styles["BulletText"]))

    story.append(Paragraph(
        "<b>Use Case UC-04: Generate and Export Executive Audit Report</b><br/>"
        "• <i>Primary Actor:</i> Software Developer / Compliance Lead.<br/>"
        "• <i>Preconditions:</i> At least one analysis cycle executed.<br/>"
        "• <i>Main Success Scenario:</i> Developer navigates to Report tab and clicks 'Generate PDF Report'. System compiles metrics, severity "
        "distributions, and code snippets into ReportLab flowables, compiles a publication-grade PDF, and triggers immediate browser download.", styles["BulletText"]))

    story.append(Spacer(1, 10))
    story.append(Paragraph("4.5 Pipeline & Workflow Modeling (Activity Flowchart)", styles["SectionHeader"]))
    story.append(Paragraph(
        "The end-to-end processing pipeline orchestrates multi-stage verification from raw input ingestion to executive delivery. Figure 4.4 "
        "illustrates the sequential decision flowchart governing the dual-engine AST parsing, static analysis, Groq AI refactoring, and report export.", styles["BodyJustified"]))
    story.append(Spacer(1, 4))

    # Figure 4.4: Pipeline Flowchart
    pipe_path = os.path.join(assets_dir, "fig_pipeline.png")
    if os.path.exists(pipe_path):
        story.append(Image(pipe_path, width=430, height=285))
        story.append(Paragraph("<b>Figure 4.4:</b> Complete Dual-Engine AST & Heuristic Processing Pipeline", styles["FigCaption"]))
    story.append(Spacer(1, 10))

    story.append(Paragraph("4.6 Sequence Diagram (Multi-Engine Orchestration Sequence)", styles["SectionHeader"]))
    story.append(Paragraph(
        "The dynamic interactions between system components during an analysis cycle are structured as a synchronized sequence of events:", styles["BodyJustified"]))
    story.append(Paragraph(
        "1. <b>Developer &rarr; Streamlit UI:</b> Uploads source file `Receiptiframe.js` (17.17 KB).<br/>"
        "2. <b>Streamlit UI &rarr; Ingestion Handler:</b> Decodes UTF-8 string and stores in `st.session_state['code']`.<br/>"
        "3. <b>Ingestion Handler &rarr; Tree-sitter Engine:</b> Passes bytes to `TreeParser.parse(code, 'javascript')`.<br/>"
        "4. <b>Tree-sitter Engine &rarr; Ingestion Handler:</b> Returns CST root node and syntax error flag (False).<br/>"
        "5. <b>Ingestion Handler &rarr; BugDetector:</b> Invokes `detect_bugs(code, 'javascript')`.<br/>"
        "6. <b>BugDetector &rarr; Ingestion Handler:</b> Returns 0 heuristic bugs.<br/>"
        "7. <b>Ingestion Handler &rarr; SecurityScanner:</b> Invokes `scan_security(code, 'javascript')`.<br/>"
        "8. <b>SecurityScanner &rarr; Ingestion Handler:</b> Returns 1 Low-severity alert (CWE-798 potential token string).<br/>"
        "9. <b>Ingestion Handler &rarr; ComplexityEstimator:</b> Invokes `estimate_complexity(code, 'javascript')` &rarr; returns O(n).<br/>"
        "10. <b>Streamlit UI &rarr; Developer:</b> Renders interactive dashboard with metrics, charts, and issue cards within 42 ms.<br/>"
        "11. <b>Developer &rarr; Streamlit UI:</b> Clicks 'Generate AI Refactored Code'.<br/>"
        "12. <b>Streamlit UI &rarr; Refactorer:</b> Injects code + static findings into grounded system prompt.<br/>"
        "13. <b>Refactorer &rarr; Groq Client:</b> Transmits HTTPS chat completion request to `openai/gpt-oss-120b` (max_tokens=3500).<br/>"
        "14. <b>Groq LPU &rarr; Groq Client:</b> Streams 1,840 tokens in 2.8 seconds.<br/>"
        "15. <b>Groq Client &rarr; Refactorer:</b> Returns raw response string.<br/>"
        "16. <b>Refactorer &rarr; Streamlit UI:</b> Robust parser separates clean code and markdown explanation.<br/>"
        "17. <b>Streamlit UI &rarr; SQLite Store:</b> Inserts analysis summary record into `analysis_history` table.<br/>"
        "18. <b>Streamlit UI &rarr; Developer:</b> Renders downloadable refactored code editor and key improvements card.", styles["BulletText"]))

    story.append(Spacer(1, 10))
    story.append(Paragraph("4.7 Database Design: Relational Schema & ER Diagram", styles["SectionHeader"]))
    story.append(Paragraph(
        "Local audit trail persistence is managed via an embedded SQLite3 database (`audit_history.db`). The database schema is engineered "
        "to record every completed review session, enabling longitudinal quality tracking and team auditability. Figure 4.5 illustrates the "
        "relational Entity-Relationship schema.", styles["BodyJustified"]))
    story.append(Spacer(1, 4))

    # Figure 4.5: Database ER Diagram
    db_path = os.path.join(assets_dir, "fig_db.png")
    if os.path.exists(db_path):
        story.append(Image(db_path, width=450, height=245))
        story.append(Paragraph("<b>Figure 4.5:</b> Entity-Relationship & Relational Data Schema (SQLite3)", styles["FigCaption"]))
    story.append(Spacer(1, 8))

    story.append(Paragraph("<b>Data Dictionary: `analysis_history` Table Schema:</b>", styles["SubSectionHeader"]))
    db_table_headers = [Paragraph("<b>Column Name</b>", styles["TableHead"]),
                        Paragraph("<b>Data Type</b>", styles["TableHead"]),
                        Paragraph("<b>Constraints</b>", styles["TableHead"]),
                        Paragraph("<b>Field Description & Semantics</b>", styles["TableHead"])]
    
    db_table_rows = [
        [Paragraph("<code>id</code>", styles["TableCellBold"]), Paragraph("INTEGER", styles["TableCell"]),
         Paragraph("PRIMARY KEY AUTOINCREMENT", styles["TableCellBold"]), Paragraph("Unique immutable review session record identifier.", styles["TableCell"])],

        [Paragraph("<code>filename</code>", styles["TableCellBold"]), Paragraph("TEXT", styles["TableCell"]),
         Paragraph("NOT NULL", styles["TableCellBold"]), Paragraph("Original filename of the ingested source code file.", styles["TableCell"])],

        [Paragraph("<code>language</code>", styles["TableCellBold"]), Paragraph("TEXT", styles["TableCell"]),
         Paragraph("NOT NULL", styles["TableCellBold"]), Paragraph("Standardized programming language identifier (e.g., 'python', 'javascript').", styles["TableCell"])],

        [Paragraph("<code>loc</code>", styles["TableCellBold"]), Paragraph("INTEGER", styles["TableCell"]),
         Paragraph("NOT NULL, &ge; 0", styles["TableCellBold"]), Paragraph("Total lines of code analyzed in the source file.", styles["TableCell"])],

        [Paragraph("<code>bugs_count</code>", styles["TableCellBold"]), Paragraph("INTEGER", styles["TableCell"]),
         Paragraph("NOT NULL, DEFAULT 0", styles["TableCellBold"]), Paragraph("Total count of deterministic heuristic bugs detected.", styles["TableCell"])],

        [Paragraph("<code>security_count</code>", styles["TableCellBold"]), Paragraph("INTEGER", styles["TableCell"]),
         Paragraph("NOT NULL, DEFAULT 0", styles["TableCellBold"]), Paragraph("Total count of OWASP security vulnerabilities identified.", styles["TableCell"])],

        [Paragraph("<code>complexity</code>", styles["TableCellBold"]), Paragraph("TEXT", styles["TableCell"]),
         Paragraph("DEFAULT 'O(1)'", styles["TableCellBold"]), Paragraph("Estimated Big-O asymptotic time complexity string.", styles["TableCell"])],

        [Paragraph("<code>timestamp</code>", styles["TableCellBold"]), Paragraph("DATETIME", styles["TableCell"]),
         Paragraph("DEFAULT CURRENT_TIMESTAMP", styles["TableCellBold"]), Paragraph("ISO-8601 UTC timestamp of review completion.", styles["TableCell"])],
    ]

    t_db = Table([db_table_headers] + db_table_rows, colWidths=[90, 65, 140, 170])
    t_db.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1e3a8a")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#f8fafc")]),
    ]))
    story.append(t_db)
    story.append(Spacer(1, 10))

    story.append(Paragraph("4.8 Human-Computer Interaction (HCI) & Reactive UI Principles", styles["SectionHeader"]))
    story.append(Paragraph(
        "Developer tools often suffer from cluttered, unintuitive user interfaces that hinder rapid code comprehension. To ensure exceptional "
        "usability, the presentation tier was designed according to established Human-Computer Interaction (HCI) and ergonomic principles:", styles["BodyJustified"]))
    story.append(Paragraph("• <b>Visual Hierarchy & Cognitive Chunking:</b> Information is structured into distinct, logical tabbed containers "
                           "(Dashboard, Static & Bugs, Security, AI Review, Refactor, Similarity, Report), preventing cognitive overload.", styles["BulletText"]))
    story.append(Paragraph("• <b>Modern Dark-Mode Glassmorphism:</b> Translucent glass panels with subtle border glows and high-contrast typography "
                           "minimize visual strain during prolonged developer review sessions.", styles["BulletText"]))
    story.append(Paragraph("• <b>Immediate Reactive Feedback:</b> Critical status indicators (e.g., 'Analysis Synced', 'Groq AI Active') provide "
                           "instant reassurance of system health in accordance with Nielsen's First Heuristic (Visibility of System Status).", styles["BulletText"]))
    story.append(Paragraph("• <b>One-Click Artifact Delivery:</b> Refactored code and executive PDF audit reports can be downloaded with a single "
                           "click, closing the loop between problem detection and remediation.", styles["BulletText"]))

    story.append(Spacer(1, 10))
    story.append(Paragraph("4.9 Object-Oriented Class Design & Component Interface Specifications", styles["SectionHeader"]))
    story.append(Paragraph(
        "The application logic tier is structured around clean object-oriented class abstractions adhering to SOLID design principles. "
        "The primary class interfaces and method contracts include:", styles["BodyJustified"]))

    class_specs = [
        "class CodeAnalyzer(ast.NodeVisitor):",
        "    def visit_FunctionDef(node: ast.FunctionDef) -> None",
        "    def visit_ClassDef(node: ast.ClassDef) -> None",
        "    def visit_Import(node: ast.Import) -> None",
        "    def get_metrics() -> dict  # returns lines, func_count, class_count",
        "",
        "class TreeParser:",
        "    @classmethod",
        "    def parse(code_str: str, language_name: str) -> dict",
        "    # returns {'tree': Tree, 'root': Node, 'has_error': bool, 'nodes': int}",
        "",
        "class BugDetector:",
        "    def detect_bugs(code_str: str, language: str) -> list[dict]",
        "    # returns list of {'type': str, 'line': int, 'severity': str, 'msg': str}",
        "",
        "class SecurityScanner:",
        "    def scan_security(code_str: str, language: str) -> list[dict]",
        "    # returns list of {'cwe': str, 'name': str, 'line': int, 'severity': str, 'remediation': str}",
        "",
        "class ComplexityEstimator:",
        "    def estimate_complexity(code_str: str, language: str) -> str",
        "    # returns Big-O notation string: 'O(1)', 'O(n)', 'O(n^2)', 'O(2^n)'",
        "",
        "class Refactorer:",
        "    def generate_refactored_code(code: str, language: str, issues: list) -> tuple[str, str]",
        "    # returns (clean_code_string, markdown_explanation)"
    ]
    story.append(make_code_box(class_specs))
    story.append(Spacer(1, 10))

    story.append(Paragraph("4.10 State Machine Modeling: Source File Analysis Lifecycle", styles["SectionHeader"]))
    story.append(Paragraph(
        "The lifecycle of a source code artifact within the assistant is governed by a finite state machine (FSM). "
        "The artifact progresses through seven discrete states:", styles["BodyJustified"]))
    story.append(Paragraph("1. <b>STATE_UNLOADED:</b> Initial state. Session state contains null code buffer; UI displays drag-and-drop prompt.", styles["BulletText"]))
    story.append(Paragraph("2. <b>STATE_INGESTED:</b> User uploads file or pastes code. Filename and encoding are validated; language is inferred.", styles["BulletText"]))
    story.append(Paragraph("3. <b>STATE_PARSING:</b> Buffer dispatched to Python AST or Tree-sitter parser. Grammar trees are constructed.", styles["BulletText"]))
    story.append(Paragraph("4. <b>STATE_AST_READY:</b> Structural metrics computed. If syntax errors exist, system transitions to non-blocking warning state.", styles["BulletText"]))
    story.append(Paragraph("5. <b>STATE_AUDITING:</b> Heuristic Bug Detector and OWASP Security Scanner execute concurrently. Severity badges assigned.", styles["BulletText"]))
    story.append(Paragraph("6. <b>STATE_AI_REFACTORING:</b> Grounded prompt dispatched to Groq LPU. Model streams tokens; response parsed into code and explanation.", styles["BulletText"]))
    story.append(Paragraph("7. <b>STATE_REPORT_EXPORTED:</b> ReportLab compiles flowables into downloadable PDF binary. Audit record inserted into SQLite.", styles["BulletText"]))

    story.append(PageBreak())
    return story
