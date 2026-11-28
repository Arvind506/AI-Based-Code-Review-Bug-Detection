import os
from reportlab.platypus import Paragraph, Spacer, PageBreak, Table, TableStyle, HRFlowable, Image
from reportlab.lib import colors

def get_preliminary_flowables(styles):
    story = []
    assets_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "report_assets")
    logo_path = os.path.join(assets_dir, "spdt_college_logo_clean.png")

    # =========================================================================
    # PAGE 1: COVER PAGE
    # =========================================================================
    story.append(Spacer(1, 15))
    story.append(Paragraph("A", styles["CoverMeta"]))
    story.append(Paragraph("<b>Research Project</b>", styles["CoverMetaBold14"]))
    story.append(Paragraph("on", styles["CoverMeta"]))
    story.append(Spacer(1, 15))
    story.append(Paragraph("<b>“AI Code Review &amp; Bug Detection”</b>", styles["CoverTitle30"]))
    story.append(Paragraph("<i>A Hybrid Static AST &amp; Generative LLM Quality Assurance Framework for Modern Polyglot Software Engineering</i>", styles["CoverSubtitle12"]))
    story.append(Spacer(1, 15))
    
    story.append(Paragraph("Submitted to", styles["CoverMeta"]))
    story.append(Paragraph("<b>Department of Information Technology</b>", styles["CoverMetaBold14"]))
    story.append(Paragraph("Of", styles["CoverMeta"]))
    story.append(Spacer(1, 10))

    if os.path.exists(logo_path):
        img_logo1 = Image(logo_path, width=105, height=105)
        img_logo1.hAlign = 'CENTER'
        story.append(img_logo1)
        story.append(Spacer(1, 12))

    story.append(Paragraph("<b>SHRI RAJASTHANI SEVA SANGH’S</b>", styles["CoverMetaBold14"]))
    story.append(Paragraph("<b>SMT. PARMESHWARIDEVI DURGADUTT TIBREWALA LIONS JUHU<br/>COLLEGE OF ARTS, COMMERCE &amp; SCIENCE (AUTONOMOUS)</b>", styles["CoverMetaBold13"]))
    story.append(Paragraph("<b>J.B. NAGAR, ANDHERI (EAST), MUMBAI - 400059</b>", styles["CoverMetaBold14"]))
    story.append(Spacer(1, 16))

    story.append(Paragraph("Submitted by", styles["CoverMeta"]))
    story.append(Paragraph("<b>Kushwaha Arvind Rambadan</b>", styles["CoverMetaBold14"]))
    story.append(Spacer(1, 16))

    story.append(Paragraph("For Partial Fulfillment for Degree of", styles["CoverMeta"]))
    story.append(Paragraph("<b>Master of Science (Information Technology) in 2026-2027</b>", styles["CoverMetaBold14"]))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 2: CERTIFICATE OF APPROVAL
    # =========================================================================
    story.append(Spacer(1, 15))
    story.append(Paragraph(
        "<b>SHRI RAJASTHANI SEVA SANGH’S SMT. PARMESHWARIDEVI<br/>"
        "DURGADUTT TIBREWALA LIONS JUHU COLLEGE OF ARTS, COMMERCE<br/>"
        "&amp; SCIENCE (AUTONOMOUS), J.B. NAGAR, ANDHERI (EAST), MUMBAI - 400059</b>", styles["CertHeader13"]))
    story.append(Spacer(1, 18))

    if os.path.exists(logo_path):
        img_logo2 = Image(logo_path, width=105, height=105)
        img_logo2.hAlign = 'CENTER'
        story.append(img_logo2)
        story.append(Spacer(1, 18))

    story.append(Paragraph("<u><b>CERTIFICATE</b></u>", styles["CertTitle26"]))
    story.append(Spacer(1, 20))

    cert_text = (
        "This is to certify that the Project entitled, <b>“AI Code Review &amp; Bug Detection”</b>, is a Bonafide "
        "work of <b>Kushwaha Arvind Rambadan</b> bearing Seat No. ______________ Submitted in Partial "
        "Fulfilment of the requirements for the award of degree of <b>Master of Science in Information "
        "Technology</b> during the academic year 2026-27 from the University of Mumbai."
    )
    story.append(Paragraph(cert_text, styles["CertBody12"]))
    story.append(Spacer(1, 75))

    sig_table_data = [
        [Paragraph("____________________<br/><b>Internal Guide</b>", styles["SigCellBold12"]),
         Paragraph("____________________<br/><b>Principal</b>", styles["SigCellBold12"]),
         Paragraph("____________________<br/><b>External Examiner</b>", styles["SigCellBold12"])]
    ]
    t_sig = Table(sig_table_data, colWidths=[160, 160, 160])
    t_sig.setStyle(TableStyle([
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(t_sig)
    story.append(Spacer(1, 70))

    bottom_table_data = [
        [Paragraph("<b>Date :</b> ______________", styles["BottomLeftBold12"]),
         Paragraph("<b>College Seal</b>", styles["BottomRightBold12"])]
    ]
    t_bottom = Table(bottom_table_data, colWidths=[240, 240])
    t_bottom.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(t_bottom)
    story.append(PageBreak())

    # =========================================================================
    # PAGE 3: DECLARATION OF AUTHENTICITY
    # =========================================================================
    story.append(Spacer(1, 15))
    story.append(Paragraph("DECLARATION", styles["ChapterHeader"]))
    story.append(Spacer(1, 20))
    
    decl_p1 = (
        "I hereby declare that the research project titled <b>“AI Code Review &amp; "
        "Bug Detection”</b> submitted by me to the Department of Information Technology, Shri Rajasthani Seva Sangh’s "
        "Smt. Parmeshwaridevi Durgadutt Tibrewala Lions Juhu College of Arts, Commerce &amp; Science (Autonomous), "
        "J.B. Nagar, Andheri (East), Mumbai - 400059, is a record of original work done by me under the supervision "
        "and guidance of <b>____________________</b>."
    )
    decl_p2 = (
        "I further declare that the content embodied in this thesis report has not been submitted previously to any other "
        "institution, university, or examining body for the award of any diploma, degree, fellowship, or other similar title. "
        "All scholarly contributions, references, published algorithms, third-party libraries (including Python ast, Tree-sitter, "
        "Streamlit, Groq API, and ReportLab), and external research papers cited within this report have been properly "
        "referenced in accordance with IEEE academic ethics and non-plagiarism conventions."
    )
    decl_p3 = (
        "I acknowledge that any algorithmic defect, architectural oversight, or experimental limitation documented herein "
        "is solely my academic responsibility."
    )
    story.append(Paragraph(decl_p1, styles["BodyJustified"]))
    story.append(Spacer(1, 10))
    story.append(Paragraph(decl_p2, styles["BodyJustified"]))
    story.append(Spacer(1, 10))
    story.append(Paragraph(decl_p3, styles["BodyJustified"]))
    story.append(Spacer(1, 50))
    
    cand_sig = [
        [Paragraph("<b>Date:</b> ____________________<br/><b>Place:</b> Mumbai, India", styles["TableCellBold"]),
         Paragraph("<b>Candidate Name:</b> Kushwaha Arvind Rambadan<br/><b>Signature:</b> ___________________________<br/><b>Roll / Seat No:</b> _______________", styles["TableCellBold"])]
    ]
    story.append(Table(cand_sig, colWidths=[230, 235]))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 4: ABSTRACT
    # =========================================================================
    story.append(Spacer(1, 10))
    story.append(Paragraph("ABSTRACT", styles["ChapterHeader"]))
    story.append(Spacer(1, 12))
    
    abs_text1 = (
        "Modern software engineering teams face relentless pressure to deliver rapid releases while maintaining uncompromising "
        "standards of code reliability, maintainability, and security. Traditional manual peer review processes, although indispensable, "
        "are inherently bottlenecked by human reviewer availability, cognitive fatigue, and high commercial costs. Conversely, conventional "
        "static analysis and linting tools rely strictly on rigid syntax matching and heuristic pattern libraries; they frequently inundate "
        "developers with false-positive warnings while remaining entirely blind to high-level architectural context, semantic intent, "
        "and algorithmic bottlenecks."
    )
    abs_text2 = (
        "This research project presents the design, architectural formalization, empirical evaluation, and production deployment of the "
        "<b>AI Code Review & Bug Detection</b>—an intelligent, hybrid software quality assurance "
        "platform. The system unifies deterministic Abstract Syntax Tree (AST) static analysis with state-of-the-art Large Language Models "
        "(Groq-accelerated Llama 3.3 / GPT-OSS inference) within an interactive, zero-configuration reactive web architecture."
    )
    abs_text3 = (
        "To achieve comprehensive polyglot coverage, the platform introduces a dual-engine parsing pipeline: native Python standard-library "
        "<code>ast</code> parsing for rapid deterministic introspection, paired with universal <b>Tree-sitter concrete syntax tree (CST) "
        "grammars</b> spanning eight additional industry-standard programming languages: Java, C, C++, JavaScript, TypeScript, Go, Rust, "
        "and Kotlin. Over these structural syntax representations, the platform executes three concurrent analytical engines: "
        "(1) a <b>Heuristic Bug Detection Engine</b> capable of detecting infinite loops, literal division by zero, dead/unreachable code, "
        "and duplicated logic blocks; (2) an <b>OWASP-Aligned Security Vulnerability Scanner</b> that audits codebases against SQL injection, "
        "hardcoded credentials, unsafe arbitrary code execution (<code>eval</code>/<code>exec</code>), command injection, and insecure "
        "deserialization; and (3) an <b>Asymptotic Complexity Estimator</b> that evaluates Big-O time complexity via recursive traversal "
        "and maximum loop nesting depth."
    )
    abs_text4 = (
        "Complementing the static verification layer, the system integrates a contextual Large Language Model orchestrator via Groq’s "
        "ultra-low-latency LPU inference infrastructure. Rather than querying ungrounded generative models, static AST and security findings "
        "are dynamically injected as contextual anchors into specialized system prompts, producing holistic code reviews, automated "
        "behavior-preserving refactoring suggestions, and conversational Q&amp;A without hallucination risks. Empirical validation over 16 "
        "automated test suites, 9 language benchmarks, and known vulnerable testbeds confirms sub-50ms static parse latency, robust zero-breakage "
        "execution, and executive PDF audit reporting."
    )
    story.append(Paragraph(abs_text1, styles["BodyJustified"]))
    story.append(Spacer(1, 8))
    story.append(Paragraph(abs_text2, styles["BodyJustified"]))
    story.append(Spacer(1, 8))
    story.append(Paragraph(abs_text3, styles["BodyJustified"]))
    story.append(Spacer(1, 8))
    story.append(Paragraph(abs_text4, styles["BodyJustified"]))
    story.append(Spacer(1, 14))
    story.append(Paragraph("<b>Keywords:</b> Static Code Analysis, Abstract Syntax Tree (AST), Concrete Syntax Tree (CST), Tree-sitter, Large Language Models (LLMs), Groq LPU, Automated Bug Detection, OWASP Top 10, Code Refactoring, Big-O Complexity, Streamlit.", styles["BodyJustified"]))
    story.append(PageBreak())

    # =========================================================================
    # PAGE 5: ACKNOWLEDGEMENTS
    # =========================================================================
    story.append(Spacer(1, 10))
    story.append(Paragraph("ACKNOWLEDGEMENTS", styles["ChapterHeader"]))
    story.append(Spacer(1, 12))
    
    ack_p1 = (
        "The completion of this Master's dissertation represents a monumental milestone in my academic journey. "
        "I express my profound gratitude to the Almighty for granting me the intellectual perseverance, discipline, "
        "and resilience needed to overcome complex theoretical and software engineering hurdles throughout this investigation."
    )
    ack_p2 = (
        "I express my deepest academic gratitude and respect to my project guide, <b>____________________</b>, for his "
        "invaluable scholarly mentorship, incisive technical critique, and unwavering encouragement. His rigorous standards "
        "of algorithmic correctness and architectural elegance continuously challenged me to elevate this work from a simple "
        "academic project into an enterprise-grade software intelligence platform."
    )
    ack_p3 = (
        "I extend my sincere thanks to <b>____________________</b>, Head of the Department of Information Technology, and our "
        "respected Principal, for providing state-of-the-art computational facilities, high-performance computing hardware, "
        "and an inspiring autonomous academic environment that fosters innovation."
    )
    ack_p4 = (
        "I cannot overlook the profound sacrifices made by my family. My parents and my brother provided unconditional moral support, "
        "patience, and understanding during the countless sleepless nights and intensive debugging sessions required to complete this thesis. "
        "Their faith in my capabilities has been my greatest source of strength."
    )
    ack_p5 = (
        "Finally, I extend my heartfelt appreciation to my classmates, technical peers, and the open-source software engineering community "
        "whose libraries, compilers, and research publications formed the bedrock of this investigation."
    )
    story.append(Paragraph(ack_p1, styles["BodyJustified"]))
    story.append(Paragraph(ack_p2, styles["BodyJustified"]))
    story.append(Paragraph(ack_p3, styles["BodyJustified"]))
    story.append(Paragraph(ack_p4, styles["BodyJustified"]))
    story.append(Paragraph(ack_p5, styles["BodyJustified"]))
    story.append(Spacer(1, 20))
    story.append(Paragraph("<b>Kushwaha Arvind Rambadan</b><br/>M.Sc. (Information Technology)<br/>Mumbai, India", styles["BodyJustified"]))
    story.append(PageBreak())

    # =========================================================================
    # PAGES 6 to 8: TABLE OF CONTENTS (STRUCTURED 3-PART MATRIX)
    # =========================================================================
    story.append(Spacer(1, 10))
    story.append(Paragraph("TABLE OF CONTENTS (PART I: CHAPTERS 1 - 3)", styles["ChapterHeader"]))
    story.append(Spacer(1, 10))
    
    toc_entries_p1 = [
        ("Certificate of Approval", "ii"),
        ("Declaration of Authenticity", "iii"),
        ("Abstract", "iv"),
        ("Acknowledgements", "v"),
        ("Table of Contents", "vi"),
        ("List of Figures", "xi"),
        ("List of Tables", "xi"),
        ("Chapter 1: Introduction", "1"),
        ("&nbsp;&nbsp;1.1 Background & Context of Software Quality Assurance", "1"),
        ("&nbsp;&nbsp;1.2 Evolution of Program Analysis: Linters to Generative AI", "1"),
        ("&nbsp;&nbsp;1.3 Motivation & Research Problem Statement", "2"),
        ("&nbsp;&nbsp;1.4 Core Objectives of the Proposed System", "2"),
        ("&nbsp;&nbsp;1.5 Purpose, Scope and Enterprise Applicability", "3"),
        ("&nbsp;&nbsp;1.6 Need for the Proposed Hybrid Architecture", "3"),
        ("&nbsp;&nbsp;1.7 Technology Toolchain & Architectural Rationale", "3"),
        ("&nbsp;&nbsp;1.8 Ethical, Privacy & Intellectual Property Considerations", "4"),
        ("&nbsp;&nbsp;1.9 Summary and Organization of the Thesis Report", "4"),
        ("Chapter 2: Review of Literature", "5"),
        ("&nbsp;&nbsp;2.1 Theoretical Foundations of Static Program Analysis", "5"),
        ("&nbsp;&nbsp;2.2 Survey of Classical Rule-Based Linters (SonarQube, Bandit, ESLint)", "6"),
        ("&nbsp;&nbsp;2.3 Concrete Syntax Trees & Incremental Tree-sitter Grammars", "6"),
        ("&nbsp;&nbsp;2.4 Large Language Models in Automated Software Engineering", "6"),
        ("&nbsp;&nbsp;2.5 Security Vulnerability Taxonomies (OWASP Top 10 & CWE)", "7"),
        ("&nbsp;&nbsp;2.6 Comparative Analysis of Existing Code Review Paradigms", "7"),
        ("&nbsp;&nbsp;2.7 Identification of Research Gaps", "8"),
        ("&nbsp;&nbsp;2.8 Research Contributions of This Project", "8"),
        ("&nbsp;&nbsp;2.9 Summary of the Literature Review", "8"),
        ("Chapter 3: Requirement Specification & Feasibility Study", "9"),
        ("&nbsp;&nbsp;3.1 System Requirement Analysis & Developer Personas", "9"),
        ("&nbsp;&nbsp;3.2 Functional Requirements Specification (FR-01 to FR-18)", "10"),
        ("&nbsp;&nbsp;3.3 Non-Functional Requirements Specification (NFR-01 to NFR-10)", "11"),
        ("&nbsp;&nbsp;3.4 Software and Hardware Specification Matrix", "12"),
        ("&nbsp;&nbsp;3.5 Multi-Dimensional Feasibility Study", "13"),
        ("&nbsp;&nbsp;3.6 Validation and Quality Acceptance Criteria", "13"),
        ("&nbsp;&nbsp;3.7 Work Breakdown Structure (WBS) & 16-Week Project Schedule", "14"),
        ("&nbsp;&nbsp;3.8 Requirements Traceability Matrix (RTM)", "15"),
    ]

    toc_table_data = []
    for title, pg in toc_entries_p1:
        st_style = styles["TOC_Chapter"] if not title.startswith("&nbsp;") else styles["TOC_Line"]
        p_title = Paragraph(title, st_style)
        p_dots = Paragraph(". . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .", styles["TableCell"])
        p_pg = Paragraph(f"<b>{pg}</b>", styles["TableCellBold"] if not title.startswith("&nbsp;") else styles["TableCell"])
        toc_table_data.append([p_title, p_dots, p_pg])

    t_toc1 = Table(toc_table_data, colWidths=[240, 185, 40])
    t_toc1.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.2),
        ('TOPPADDING', (0,0), (-1,-1), 1.2),
    ]))
    story.append(t_toc1)
    story.append(PageBreak())

    # TOC Page 2
    story.append(Spacer(1, 10))
    story.append(Paragraph("TABLE OF CONTENTS (PART II: CHAPTERS 4 - 5)", styles["ChapterHeader"]))
    story.append(Spacer(1, 10))

    toc_entries_p2 = [
        ("Chapter 4: System Architecture and Detailed Design", "16"),
        ("&nbsp;&nbsp;4.1 Three-Tier Layered Architecture Formalization", "16"),
        ("&nbsp;&nbsp;4.2 Modular Decomposition & Engine Responsibilities", "17"),
        ("&nbsp;&nbsp;4.3 Data Flow Modeling (DFD Level 0 Context & Level 1 Overview)", "18"),
        ("&nbsp;&nbsp;4.4 UML Behavioral Modeling: Use Case Diagram & Actor Specifications", "19"),
        ("&nbsp;&nbsp;4.5 Pipeline & Workflow Modeling (Activity Flowchart)", "20"),
        ("&nbsp;&nbsp;4.6 Sequence Diagram (Multi-Engine Orchestration Sequence)", "21"),
        ("&nbsp;&nbsp;4.7 Database Design: Relational Schema & ER Diagram", "22"),
        ("&nbsp;&nbsp;4.8 Human-Computer Interaction (HCI) & Reactive UI Principles", "23"),
        ("&nbsp;&nbsp;4.9 Object-Oriented Class Design & Component Interface Specifications", "24"),
        ("&nbsp;&nbsp;4.10 State Machine Modeling: Source File Analysis Lifecycle", "24"),
        ("Chapter 5: Implementation Details & Code Construction", "25"),
        ("&nbsp;&nbsp;5.1 Implementation Environment & Directory Organization", "25"),
        ("&nbsp;&nbsp;5.2 Step-by-Step Implementation Lifecycle", "26"),
        ("&nbsp;&nbsp;5.3 Comprehensive Algorithmic & Code Details", "27"),
        ("&nbsp;&nbsp;&nbsp;&nbsp;5.3.1 Python Native AST Parsing Engine (backend/parser.py)", "27"),
        ("&nbsp;&nbsp;&nbsp;&nbsp;5.3.2 Multi-Language Tree-sitter Grammar Parser (backend/tree_parser.py)", "27"),
        ("&nbsp;&nbsp;&nbsp;&nbsp;5.3.3 Algorithmic Bug Detection Engine (backend/bug_detector.py)", "28"),
        ("&nbsp;&nbsp;&nbsp;&nbsp;5.3.4 OWASP Security Vulnerability Engine (backend/security_scanner.py)", "28"),
        ("&nbsp;&nbsp;&nbsp;&nbsp;5.3.5 Big-O Asymptotic Complexity Estimator (backend/complexity.py)", "29"),
        ("&nbsp;&nbsp;&nbsp;&nbsp;5.3.6 Logic Similarity & Plagiarism Checker (backend/similarity.py)", "29"),
        ("&nbsp;&nbsp;&nbsp;&nbsp;5.3.7 Groq LLM Inference & Prompt Engineering", "29"),
        ("&nbsp;&nbsp;&nbsp;&nbsp;5.3.8 Reactive User Interface & Dashboard Logic (app.py)", "30"),
        ("&nbsp;&nbsp;&nbsp;&nbsp;5.3.9 Executive PDF Audit Report Generation Engine", "30"),
        ("&nbsp;&nbsp;5.4 Computational Efficiency & Memory Optimization Techniques", "31"),
        ("&nbsp;&nbsp;5.5 Packaging, Containerization & Local Deployment Strategy", "31"),
    ]

    toc_table_data2 = []
    for title, pg in toc_entries_p2:
        st_style = styles["TOC_Chapter"] if not title.startswith("&nbsp;") else styles["TOC_Line"]
        p_title = Paragraph(title, st_style)
        p_dots = Paragraph(". . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .", styles["TableCell"])
        p_pg = Paragraph(f"<b>{pg}</b>", styles["TableCellBold"] if not title.startswith("&nbsp;") else styles["TableCell"])
        toc_table_data2.append([p_title, p_dots, p_pg])

    t_toc2 = Table(toc_table_data2, colWidths=[240, 185, 40])
    t_toc2.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.5),
        ('TOPPADDING', (0,0), (-1,-1), 1.5),
    ]))
    story.append(t_toc2)
    story.append(PageBreak())

    # TOC Page 3
    story.append(Spacer(1, 10))
    story.append(Paragraph("TABLE OF CONTENTS (PART III: CHAPTERS 6 - 8 & APPENDICES)", styles["ChapterHeader"]))
    story.append(Spacer(1, 10))

    toc_entries_p3 = [
        ("Chapter 6: Verification, Testing and Quality Assurance", "32"),
        ("&nbsp;&nbsp;6.1 Comprehensive Testing Philosophy & Test Strategy", "32"),
        ("&nbsp;&nbsp;6.2 Executed Logic & Data Test Cases (TC-01 to TC-20 Table)", "32"),
        ("&nbsp;&nbsp;6.3 Security Benchmark Validation Against Real Vulnerable Code", "34"),
        ("&nbsp;&nbsp;6.4 Manual User Interface & Accessibility Test Suite (UI-01 to UI-10)", "34"),
        ("&nbsp;&nbsp;6.5 Edge-Case Handling & Boundary Stress Testing", "35"),
        ("&nbsp;&nbsp;6.6 Architectural Refinements Made During Testing", "35"),
        ("&nbsp;&nbsp;6.7 Performance & Scalability Stress Test Suite (PS-01 to PS-10)", "35"),
        ("&nbsp;&nbsp;6.8 Edge-Case & Operational Fault Recovery Matrix (EC-01 to EC-10)", "36"),
        ("Chapter 7: Experimental Results, Performance & User Walkthrough", "37"),
        ("&nbsp;&nbsp;7.1 Empirical Performance Results Across 9 Languages (Latency)", "37"),
        ("&nbsp;&nbsp;7.2 Bug Detection Accuracy & Security Severity Distribution", "38"),
        ("&nbsp;&nbsp;7.3 Comparative Evaluation Against Industry-Standard Linters", "38"),
        ("&nbsp;&nbsp;7.4 User Interface Walkthrough & Annotated Screenshots", "39"),
        ("&nbsp;&nbsp;7.5 User Documentation & Operational Runbook", "40"),
        ("&nbsp;&nbsp;7.6 Empirical Discussion & Threats to Validity", "40"),
        ("&nbsp;&nbsp;7.7 Quantitative Developer Productivity Impact Assessment", "41"),
        ("&nbsp;&nbsp;7.8 Empirical Case Study: Refactoring Receiptiframe.js (420 LOC)", "41"),
        ("Chapter 8: Conclusion, Limitations and Future Scope", "42"),
        ("&nbsp;&nbsp;8.1 Summary of Project Contributions & Achievements", "42"),
        ("&nbsp;&nbsp;8.2 Critical Analysis of Current System Limitations", "42"),
        ("&nbsp;&nbsp;8.3 Future Scope & Long-Term Technological Roadmap", "43"),
        ("&nbsp;&nbsp;8.4 Concluding Remarks", "43"),
        ("References (IEEE Citation Format)", "44"),
        ("Appendices", "46"),
        ("&nbsp;&nbsp;Appendix A: Multi-Language Grammar Node Type Reference", "46"),
        ("&nbsp;&nbsp;Appendix B: Security Vulnerability Regex Rules & CWE Mapping", "47"),
        ("&nbsp;&nbsp;Appendix C: Installation & Quick-Start Guide", "47"),
        ("&nbsp;&nbsp;Appendix D: Project File Manifest & Module Index", "48"),
        ("&nbsp;&nbsp;Appendix E: Comprehensive Technical Glossary", "48"),
        ("&nbsp;&nbsp;Appendix F: Benchmark Vulnerable vs. AI-Refactored Code", "49"),
        ("&nbsp;&nbsp;Appendix G: Complete Environment & Dependency Manifest", "51"),
    ]

    toc_table_data3 = []
    for title, pg in toc_entries_p3:
        st_style = styles["TOC_Chapter"] if not title.startswith("&nbsp;") else styles["TOC_Line"]
        p_title = Paragraph(title, st_style)
        p_dots = Paragraph(". . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .", styles["TableCell"])
        p_pg = Paragraph(f"<b>{pg}</b>", styles["TableCellBold"] if not title.startswith("&nbsp;") else styles["TableCell"])
        toc_table_data3.append([p_title, p_dots, p_pg])

    t_toc3 = Table(toc_table_data3, colWidths=[240, 185, 40])
    t_toc3.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.5),
        ('TOPPADDING', (0,0), (-1,-1), 1.5),
    ]))
    story.append(t_toc3)
    story.append(PageBreak())

    # =========================================================================
    # PAGE 9: LIST OF FIGURES & LIST OF TABLES
    # =========================================================================
    story.append(Spacer(1, 10))
    story.append(Paragraph("LIST OF FIGURES", styles["ChapterHeader"]))
    story.append(Spacer(1, 10))

    figures = [
        ("Figure 3.1", "Project schedule (Gantt chart)", "14"),
        ("Figure 4.1", "Three-Tier Layered System Architecture Diagram", "17"),
        ("Figure 4.2", "Data Flow Diagram (DFD Level 0 Context & Level 1 Process)", "18"),
        ("Figure 4.3", "UML Use Case Diagram for Code Review Platform", "19"),
        ("Figure 4.4", "Complete Dual-Engine AST & Heuristic Processing Pipeline", "20"),
        ("Figure 4.5", "Entity-Relationship & Relational Data Schema (SQLite3)", "22"),
        ("Figure 7.1", "Measured End-to-End Static Analysis Latency Across 9 Languages", "37"),
        ("Figure 7.2", "Distribution of Detected Bug Categories Across Test Repositories", "38"),
        ("Figure 7.3", "Security Vulnerabilities by OWASP Severity Breakdown", "38"),
        ("Figure 7.4", "System Overview Dashboard with Real-Time Metrics & Charts", "39"),
        ("Figure 7.5", "Security Vulnerability Scan & Heuristic Bug Detection Interface", "40"),
    ]
    f_data = []
    for num, desc, pg in figures:
        p_num = Paragraph(f"<b>{num}</b>", styles["TableCellBold"])
        p_desc = Paragraph(desc, styles["TableCell"])
        p_pg = Paragraph(f"<b>{pg}</b>", styles["TableCellBold"])
        f_data.append([p_num, p_desc, p_pg])

    t_fig = Table(f_data, colWidths=[65, 360, 40])
    t_fig.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
    ]))
    story.append(t_fig)

    story.append(Spacer(1, 15))
    story.append(Paragraph("LIST OF TABLES", styles["ChapterHeader"]))
    story.append(Spacer(1, 10))

    tables_list = [
        ("Table 2.1", "Comparative Analysis Matrix of Existing Code Review Paradigms", "7"),
        ("Table 3.1", "Functional Requirements Specification (FR-01 to FR-18)", "10"),
        ("Table 3.2", "Non-Functional Quality Attributes and Acceptance Criteria", "11"),
        ("Table 3.3", "Hardware and Software Operating Environment Specifications", "12"),
        ("Table 3.4", "Requirements Traceability Matrix (RTM)", "15"),
        ("Table 4.1", "Module Decomposition and Architectural Responsibilities", "17"),
        ("Table 5.1", "Language Grammar and Tree-sitter AST Node Mapping", "27"),
        ("Table 6.1", "Executed Logic & Data Integrity Test Cases (TC-01 to TC-10)", "32"),
        ("Table 6.2", "Executed Advanced Security & Heuristic Test Cases (TC-11 to TC-20)", "33"),
        ("Table 6.3", "Manual User Interface & Usability Test Suite (UI-01 to UI-10)", "34"),
        ("Table 6.4", "Performance & Scalability Stress Test Suite (PS-01 to PS-10)", "35"),
        ("Table 6.5", "Edge-Case & Operational Fault Recovery Matrix (EC-01 to EC-10)", "36"),
        ("Table 7.1", "Comparative Evaluation: Proposed System vs Conventional Linters", "38"),
        ("Table A.1", "Universal Tree-sitter Grammar Node Identifiers Across 9 Languages", "46"),
        ("Table B.1", "OWASP Security Vulnerability Regex Rules and CWE Mappings", "47"),
        ("Table G.1", "Production Dependency Package Manifest & License Compliance", "51"),
    ]
    t_data = []
    for num, desc, pg in tables_list:
        p_num = Paragraph(f"<b>{num}</b>", styles["TableCellBold"])
        p_desc = Paragraph(desc, styles["TableCell"])
        p_pg = Paragraph(f"<b>{pg}</b>", styles["TableCellBold"])
        t_data.append([p_num, p_desc, p_pg])

    t_tab = Table(t_data, colWidths=[65, 360, 40])
    t_tab.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
    ]))
    story.append(t_tab)
    story.append(PageBreak())

    return story
