import os
from reportlab.platypus import Paragraph, Spacer, PageBreak, Table, TableStyle, HRFlowable
from reportlab.lib import colors
from thesis_styles import make_callout, make_code_box

def get_ch1_ch2_flowables(styles):
    story = []

    # =========================================================================
    # CHAPTER 1: INTRODUCTION
    # =========================================================================
    story.append(Spacer(1, 15))
    story.append(Paragraph("Chapter 1: Introduction", styles["ChapterHeader"]))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#1e3a8a"), spaceAfter=14))

    story.append(Paragraph("1.1 Background & Context of Software Quality Assurance", styles["SectionHeader"]))
    story.append(Paragraph(
        "Software engineering has evolved into one of the most critical backbones of modern society, underpinning global financial systems, "
        "healthcare devices, telecommunications, and cloud infrastructures. As software systems grow exponentially in architectural complexity, "
        "the cost of undetected defects, security vulnerabilities, and code debt rises precipitously. Studies consistently indicate that "
        "defects discovered during production or post-deployment cost organizations up to thirty times more to remediate compared to those "
        "caught early during the authoring and code review phases. Consequently, modern software development lifecycles (SDLC) place paramount "
        "emphasis on early defect detection, static code analysis, and continuous peer review.", styles["BodyJustified"]))
    story.append(Paragraph(
        "Despite its ubiquity, traditional peer code review remains an intensely manual, time-consuming, and cognitively exhausting process. "
        "Senior software engineers frequently spend between 15% and 25% of their working hours manually reading pull requests, verifying style "
        "consistency, searching for anti-patterns, and checking for common security oversights. Under the pressure of tight release deadlines, "
        "human reviewers inevitably suffer from reviewer fatigue, leading to superficial reviews where subtle memory leaks, injection vulnerabilities, "
        "or algorithmic inefficiencies pass unnoticed into production codebases.", styles["BodyJustified"]))

    story.append(Paragraph("1.2 Evolution of Program Analysis: Linters to Generative AI", styles["SectionHeader"]))
    story.append(Paragraph(
        "To mitigate human limitations, the software engineering discipline developed automated program analysis tools, which historically "
        "progressed through three distinct evolutionary generations:", styles["BodyJustified"]))
    story.append(Paragraph(
        "<b>1. First-Generation Lexical Linters (Regex & Token-Based):</b> Early tools such as original Unix <code>lint</code> and basic grep-style "
        "scanners operated on raw text tokens. While fast, they lacked structural comprehension, generating rampant false alarms on comments "
        "or string literals that coincidentally matched warning keywords.", styles["BulletText"]))
    story.append(Paragraph(
        "<b>2. Second-Generation Abstract Syntax Tree (AST) Analyzers:</b> Tools such as ESLint, Bandit, Checkstyle, and SonarQube compile source "
        "code into syntactic tree representations, allowing deterministic validation of scope, unused variables, and dangerous function calls. "
        "However, AST linters are fundamentally rule-bound: they cannot understand semantic developer intent, cannot suggest contextual "
        "refactorings, and require entirely separate parser implementations for every distinct programming language.", styles["BulletText"]))
    story.append(Paragraph(
        "<b>3. Third-Generation Large Language Models (LLMs):</b> Modern foundation models trained on trillions of code tokens exhibit remarkable "
        "natural language reasoning, multi-language fluency, and contextual comprehension. However, ungrounded LLMs suffer from non-deterministic "
        "hallucinations, invent non-existent APIs, and impose massive computational latency and economic costs when processing raw code repositories.", styles["BulletText"]))

    story.append(Paragraph("1.3 Motivation & Research Problem Statement", styles["SectionHeader"]))
    story.append(Paragraph(
        "The core motivation of this research is to resolve the fundamental trade-off between deterministic precision and contextual intelligence. "
        "Traditional AST static analyzers provide guaranteed reproducibility, offline execution, and lightning speed, but lack semantic depth "
        "and cannot generate automated, behavior-preserving refactorings. Conversely, Large Language Models excel at understanding high-level intent "
        "and generating refactored code, but suffer from hallucinations, non-deterministic outputs, and privacy/latency concerns. "
        "This project investigates whether a <b>hybrid static-generative architecture</b> can unify the mathematical rigor of Abstract Syntax "
        "Trees with the contextual power of Groq-accelerated LLMs to create an automated code review assistant that is fast, accurate, "
        "polyglot, and hallucination-free.", styles["BodyJustified"]))

    story.append(Paragraph("1.4 Core Objectives of the Proposed System", styles["SectionHeader"]))
    story.append(Paragraph(
        "To address this problem statement, the project was executed against six concrete, quantifiable research objectives:", styles["BodyJustified"]))
    story.append(Paragraph("1. <b>Dual-Engine Parsing Pipeline:</b> Implement standard library Python <code>ast</code> alongside universal "
                           "Tree-sitter CST grammars to establish structural analysis across 9 programming languages (Python, JS, TS, Java, C, C++, Go, Rust, Kotlin).", styles["BulletText"]))
    story.append(Paragraph("2. <b>Deterministic Heuristic Bug Detection:</b> Formulate offline static algorithms to detect infinite while loops, "
                           "literal division by zero, unreachable dead code, and duplicated statement blocks without dynamic code execution.", styles["BulletText"]))
    story.append(Paragraph("3. <b>OWASP Top 10 & CWE Security Auditing:</b> Construct a multi-pattern regex and AST security engine targeting "
                           "SQL injection, hardcoded credentials, unsafe execution (<code>eval</code>, <code>exec</code>), and command injection.", styles["BulletText"]))
    story.append(Paragraph("4. <b>Asymptotic Complexity & Plagiarism Diffing:</b> Compute Big-O time complexity via recursive loop depth traversal "
                           "and perform normalized sequence comparison using Ratcliff/Obershelp gestalt pattern matching.", styles["BulletText"]))
    story.append(Paragraph("5. <b>Context-Grounded LLM Refactoring:</b> Engineer a resilient prompting orchestrator interfacing with Groq LPU "
                           "clusters (<code>openai/gpt-oss-120b</code>) that injects verified static findings to produce behavior-preserving refactored code.", styles["BulletText"]))
    story.append(Paragraph("6. <b>Zero-Cost Production Delivery:</b> Package the complete solution into an intuitive dark-mode Streamlit dashboard "
                           "with local SQLite audit logging and executive ReportLab PDF report generation.", styles["BulletText"]))

    story.append(Paragraph("1.5 Purpose, Scope and Enterprise Applicability", styles["SectionHeader"]))
    story.append(Paragraph(
        "The primary purpose of this assistant is to democratize elite-grade software quality assurance for individual developers, university "
        "laboratories, and enterprise engineering teams. By providing instant, offline static verification combined with on-demand AI refactoring, "
        "the tool eliminates reviewer fatigue, accelerates pull request triage, and prevents costly security regressions before code reaches staging.", styles["BodyJustified"]))
    story.append(Paragraph(
        "The scope of this project encompasses single-file and modular polyglot source analysis up to 5,000 lines of code per file across nine "
        "major languages. It deliberately focuses on source code quality, security posture, and asymptotic efficiency, while deferring dynamic "
        "runtime profiling and whole-repo symbolic execution to future work.", styles["BodyJustified"]))

    story.append(Paragraph("1.6 Need for the Proposed Hybrid Architecture", styles["SectionHeader"]))
    story.append(Paragraph(
        "In modern DevOps and CI/CD pipelines, latency and reliability are paramount. Pure cloud LLM reviewers are too slow and expensive "
        "to run on every local code save, while pure linters miss high-level architectural flaws. The proposed hybrid architecture provides a "
        "two-tiered execution model: instant, sub-50ms static feedback running entirely locally, coupled with asynchronous, grounded LLM "
        "refactorings returning in under 3 seconds via Groq LPUs.", styles["BodyJustified"]))

    story.append(Paragraph("1.7 Technology Toolchain & Architectural Rationale", styles["SectionHeader"]))
    story.append(Paragraph(
        "The technology stack was chosen based on performance, portability, and zero commercial licensing overhead:", styles["BodyJustified"]))
    story.append(Paragraph("• <b>Python 3.11 Runtime:</b> Delivers robust CPython optimizations, native <code>ast</code> introspection, and seamless integration with C-extensions.", styles["BulletText"]))
    story.append(Paragraph("• <b>Tree-sitter 0.21:</b> Industry-standard incremental parser utilized by GitHub and modern IDEs for robust, grammar-based syntax tree generation.", styles["BulletText"]))
    story.append(Paragraph("• <b>Streamlit & Plotly:</b> Reactive, stateful web presentation framework enabling high-performance dark-mode UI without JavaScript frontend overhead.", styles["BulletText"]))
    story.append(Paragraph("• <b>Groq LPU Inference:</b> Ultra-low latency tensor streaming architecture capable of generating over 300 tokens/sec, unlocking real-time AI code reviews.", styles["BulletText"]))
    story.append(Paragraph("• <b>SQLite3 & ReportLab:</b> Serverless, embedded ACID relational persistence paired with publication-grade programmatic PDF document compilation.", styles["BulletText"]))

    story.append(Paragraph("1.7.2 Comparative Architectural Trade-offs in Modern Developer Toolchains", styles["SubSectionHeader"]))
    story.append(Paragraph(
        "When engineering developer-facing productivity tooling, architects must evaluate the delivery form factor. "
        "Four primary deployment paradigms exist in the modern software engineering landscape:<br/>"
        "• <b>Command-Line Interface (CLI):</b> Exceptional for headless CI/CD automation, but presents a steep learning curve and lacks rich visual diff exploration.<br/>"
        "• <b>IDE Extension (e.g. VS Code Plugin):</b> Deeply integrated into the typing loop, but heavily tightly coupled to specific proprietary editor APIs and language servers.<br/>"
        "• <b>Dedicated Web Dashboard (Streamlit):</b> Combines zero-installation access, universal cross-platform browser support, interactive rich charts, "
        "and side-by-side visual diff editors without requiring local Node.js or Electron runtimes.<br/>"
        "• <b>Automated Git Webhook / Bot:</b> Executes on remote servers during PR creation, but incurs severe turnaround latency (minutes) compared to local interactive review.", styles["BodyJustified"]))

    story.append(Paragraph("1.8 Ethical, Privacy & Intellectual Property Considerations", styles["SectionHeader"]))
    story.append(Paragraph(
        "Modern developer tooling must adhere to stringent intellectual property and privacy standards. In conventional cloud AI tools, "
        "proprietary code is frequently stored, analyzed, or utilized for foundation model training without developer consent. "
        "The proposed platform establishes a zero-retention privacy policy: all Abstract Syntax Tree generation, heuristic bug detection, "
        "and security scanning execute entirely within local volatile memory. When the user explicitly requests generative AI refactoring, "
        "code is transmitted over encrypted TLS connections to Groq Cloud under strict commercial privacy terms that prohibit data retention "
        "or secondary model training.", styles["BodyJustified"]))

    story.append(Paragraph("1.9 Summary and Organization of the Thesis Report", styles["SectionHeader"]))
    story.append(Paragraph(
        "This thesis report is structured into eight comprehensive chapters and seven technical appendices:<br/>"
        "• <b>Chapter 1:</b> Establishes background, motivation, research objectives, and architectural rationale.<br/>"
        "• <b>Chapter 2:</b> Reviews foundational static analysis literature, AST parsers, LLM code models, and research gaps.<br/>"
        "• <b>Chapter 3:</b> Details developer personas, functional specifications (FR-01 to FR-18), non-functional requirements, and feasibility.<br/>"
        "• <b>Chapter 4:</b> Presents three-tier architecture, module decomposition, DFDs, UML use cases, activity pipeline, and database schema.<br/>"
        "• <b>Chapter 5:</b> Walks through complete code construction, algorithms, Tree-sitter bindings, and Groq prompting implementations.<br/>"
        "• <b>Chapter 6:</b> Formulates testing methodology, 20 executed test cases (TC-01 to TC-20), security benchmarks, and usability suites.<br/>"
        "• <b>Chapter 7:</b> Analyzes multi-language latency benchmarks, bug distributions, comparative evaluations, and annotated UI screenshots.<br/>"
        "• <b>Chapter 8:</b> Concludes with key findings, system limitations, future research roadmap, followed by References and Appendices A through G.", styles["BodyJustified"]))

    story.append(PageBreak())

    # =========================================================================
    # CHAPTER 2: REVIEW OF LITERATURE
    # =========================================================================
    story.append(Spacer(1, 15))
    story.append(Paragraph("Chapter 2: Review of Literature", styles["ChapterHeader"]))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#1e3a8a"), spaceAfter=14))

    story.append(Paragraph("2.1 Theoretical Foundations of Static Program Analysis", styles["SectionHeader"]))
    story.append(Paragraph(
        "Static program analysis is the mathematical evaluation of software properties performed without executing the program on physical "
        "or virtual hardware. The theoretical foundation traces back to the seminal work of Patrick and Radhia Cousot on <b>Abstract Interpretation</b> (1977). "
        "Abstract interpretation formalizes the approximation of program semantics: given a concrete state space $\\mathcal{S}$ and a concrete transfer "
        "function $\\tau: \\mathcal{S} \\to \\mathcal{S}$, static analyzers construct an abstract domain $\\mathcal{A}$ via a Galois connection "
        "$(\\alpha, \\gamma)$ where $\\alpha: \\mathcal{P}(\\mathcal{S}) \\to \\mathcal{A}$ abstracts states and $\\gamma: \\mathcal{A} \\to \\mathcal{P}(\\mathcal{S})$ "
        "concretizes them.", styles["BodyJustified"]))
    story.append(Paragraph(
        "By Rice's Theorem (1953), any non-trivial semantic property of a universal Turing machine is undecidable. Consequently, static analysis "
        "engines must make principled compromises between soundness (guaranteeing all true defects are flagged) and completeness (guaranteeing "
        "zero false alarms). Traditional industrial linters deliberately sacrifice completeness to maintain practical tractability, relying on "
        "Abstract Syntax Trees (ASTs) and Control Flow Graphs (CFGs) to detect localized anti-patterns.", styles["BodyJustified"]))

    story.append(Paragraph("2.1.2 Formal Mathematical Semantics of Syntax Trees and Control Flow", styles["SubSectionHeader"]))
    story.append(Paragraph(
        "Mathematically, an Abstract Syntax Tree is a rooted, directed tree $T = (V_T, E_T, r, \\lambda)$ where $V_T$ is a finite set of syntactic nodes, "
        "$E_T \\subset V_T \\times V_T$ defines parent-child containment relationships, $r \\in V_T$ is the root compilation unit, and "
        "$\\lambda: V_T \\to \\Sigma$ maps each node to a production rule in the underlying formal grammar $\\mathcal{G} = (V_N, V_T, P, S)$. "
        "Control Flow Graphs (CFG) augment the syntactic tree into a directed graph $\\mathcal{G}_{CFG} = (B, E_{CFG}, b_{entry}, b_{exit})$ "
        "where each vertex $b \\in B$ represents a basic block of linear instructions, and directed edges $(b_i, b_j) \\in E_{CFG}$ represent "
        "runtime branching paths. In this research, heuristic bug detection is formulated as an reachability evaluation over $\\mathcal{G}_{CFG}$.", styles["BodyJustified"]))

    story.append(Paragraph("2.2 Survey of Classical Rule-Based Linters (SonarQube, Bandit, ESLint)", styles["SectionHeader"]))
    story.append(Paragraph(
        "Over the past two decades, rule-based static linters have become mandatory components of enterprise software pipelines. "
        "<b>SonarQube</b> utilizes proprietary AST parsers to calculate technical debt, cyclomatic complexity, and code duplication across "
        "monolithic codebases. However, SonarQube requires dedicated database servers, complex build toolchain integration, and expensive "
        "commercial licenses for advanced security features.", styles["BodyJustified"]))
    story.append(Paragraph(
        "In the Python ecosystem, <b>Bandit</b> processes the standard library <code>ast</code> to find common security flaws such as hardcoded "
        "passwords or insecure cryptographic hashes. In JavaScript, <b>ESLint</b> constructs ESTree-compliant ASTs to enforce coding style and "
        "catch scope errors. While these tools excel within their respective single-language boundaries, they cannot cross language borders, "
        "lack holistic semantic reasoning, and offer no integrated automated refactoring capabilities.", styles["BodyJustified"]))

    story.append(Paragraph("2.3 Concrete Syntax Trees & Incremental Tree-sitter Grammars", styles["SectionHeader"]))
    story.append(Paragraph(
        "A major breakthrough in polyglot program analysis occurred with the development of <b>Tree-sitter</b> by Max Brunsfeld and the GitHub "
        "Atom team. Unlike traditional batch compilers that discard whitespace, comments, and delimiters into Abstract Syntax Trees, Tree-sitter "
        "generates a <b>Concrete Syntax Tree (CST)</b> that retains 100% of source tokens.", styles["BodyJustified"]))
    story.append(Paragraph(
        "Tree-sitter employs an optimized GLR (Generalized Left-to-right Rightmost derivation) parsing algorithm implemented in portable C. "
        "It achieves three foundational properties essential for interactive developer tooling: (1) <b>High Speed:</b> parsing thousands of lines "
        "in single-digit milliseconds; (2) <b>Robust Error Recovery:</b> generating valid syntax subtrees even when code contains active syntax "
        "errors or unclosed blocks; and (3) <b>Universal Grammar Specifications:</b> providing uniform node query interfaces across dozens of "
        "programming languages.", styles["BodyJustified"]))

    story.append(Paragraph("2.4 Large Language Models in Automated Software Engineering", styles["SectionHeader"]))
    story.append(Paragraph(
        "The application of transformer architectures to source code has revolutionized automated software engineering. Models such as "
        "OpenAI Codex (Chen et al., 2021), StarCoder (Li et al., 2023), CodeLlama (Roziere et al., 2023), and DeepSeek-Coder (Guo et al., 2024) "
        "are pre-trained on hundreds of billions of code tokens across dozens of programming languages. These models learn complex semantic "
        "relationships, API idioms, and algorithmic patterns.", styles["BodyJustified"]))
    story.append(Paragraph(
        "Despite their fluency, recent empirical studies by Beller et al. and Sarsa et al. reveal that unconstrained generative models suffer "
        "from significant reliability issues: up to 30% of generated code snippets contain subtle logic bugs, introduce deprecated library calls, "
        "or hallucinate non-existent parameters. Grounding generative models with deterministic static analysis outputs (injecting verified AST "
        "flaws into prompts) represents the frontier of reliable AI-assisted software engineering.", styles["BodyJustified"]))

    story.append(Paragraph("2.4.2 Prompt Engineering & In-Context Learning for Code Intelligence", styles["SubSectionHeader"]))
    story.append(Paragraph(
        "In-Context Learning (ICL) enables foundation models to perform sophisticated transformation tasks without parameter fine-tuning. "
        "In software refactoring, raw 'zero-shot' prompts frequently yield generic, hallucinated, or incomplete solutions. "
        "To achieve production-grade code synthesis, this research formalizes an <b>AST-Grounded Dynamic Prompting Pipeline</b>. "
        "The orchestrator constructs a structured contextual envelope containing: (1) Role and behavioral constraints, (2) Target language grammar constraints, "
        "(3) Concrete AST metrics (functions, classes, loop depth), (4) Deterministically verified bug and security vulnerability alerts, and "
        "(5) Strict output format schemas enforcing separation between refactored source code and explanatory technical commentary.", styles["BodyJustified"]))

    story.append(Paragraph("2.5 Security Vulnerability Taxonomies (OWASP Top 10 & CWE)", styles["SectionHeader"]))
    story.append(Paragraph(
        "Standardized vulnerability categorization is essential for actionable remediation. The <b>Open Web Application Security Project (OWASP)</b> "
        "publishes the definitive Top 10 web application security risks, highlighting injection flaws, broken access control, cryptographic "
        "failures, and insecure design. Concurrently, the MITRE Corporation maintains the <b>Common Weakness Enumeration (CWE)</b> dictionary, "
        "providing formal numerical identifiers (e.g., CWE-89 for SQL Injection, CWE-798 for Hardcoded Credentials, CWE-95 for Eval Injection). "
        "Mapping static analysis findings directly to CWE identifiers ensures enterprise audit compliance and interoperability.", styles["BodyJustified"]))

    story.append(Paragraph("2.6 Comparative Analysis of Existing Code Review Paradigms", styles["SectionHeader"]))
    story.append(Paragraph(
        "Table 2.1 presents a comprehensive comparative analysis of existing code review paradigms against the proposed hybrid architecture.", styles["BodyJustified"]))

    # Table 2.1
    t2_headers = [Paragraph("<b>Review Paradigm</b>", styles["TableHead"]),
                  Paragraph("<b>Polyglot AST Support</b>", styles["TableHead"]),
                  Paragraph("<b>Analysis Speed</b>", styles["TableHead"]),
                  Paragraph("<b>Semantic Intent</b>", styles["TableHead"]),
                  Paragraph("<b>Auto-Refactoring</b>", styles["TableHead"]),
                  Paragraph("<b>Operational Cost</b>", styles["TableHead"])]
    
    t2_rows = [
        [Paragraph("Manual Peer Review", styles["TableCellBold"]), Paragraph("Human dependent", styles["TableCell"]),
         Paragraph("Hours to Days", styles["TableCellBold"]), Paragraph("High (Human)", styles["TableCell"]),
         Paragraph("Manual authoring", styles["TableCell"]), Paragraph("High ($50-$100/hr)", styles["TableCellBold"])],

        [Paragraph("Traditional Linters (ESLint/Bandit)", styles["TableCellBold"]), Paragraph("Single-Language Silo", styles["TableCell"]),
         Paragraph("&lt; 500 ms", styles["TableCell"]), Paragraph("None (Rigid rules)", styles["TableCell"]),
         Paragraph("Style fixes only", styles["TableCell"]), Paragraph("Free / Open-Source", styles["TableCell"])],

        [Paragraph("Enterprise Static Suites (SonarQube)", styles["TableCellBold"]), Paragraph("Multi-plugin required", styles["TableCell"]),
         Paragraph("10s - 5 mins", styles["TableCell"]), Paragraph("None (AST metrics)", styles["TableCell"]),
         Paragraph("Remediation advice only", styles["TableCell"]), Paragraph("Commercial ($5k-$50k/yr)", styles["TableCellBold"])],

        [Paragraph("Raw Generative LLM (ChatGPT / Claude)", styles["TableCellBold"]), Paragraph("Token-based (No AST)", styles["TableCell"]),
         Paragraph("2s - 15s", styles["TableCell"]), Paragraph("High (Contextual)", styles["TableCellBold"]),
         Paragraph("Generates code (Hallucinations)", styles["TableCell"]), Paragraph("Per-token API fees", styles["TableCell"])],

        [Paragraph("<b>Proposed Hybrid Assistant</b>", styles["TableCellBold"]), Paragraph("<b>9 Languages (Tree-sitter)</b>", styles["TableCellBold"]),
         Paragraph("<b>&lt; 50 ms (Static) / 2.8s (AI)</b>", styles["TableCellBold"]), Paragraph("<b>High (AST-Grounded LLM)</b>", styles["TableCellBold"]),
         Paragraph("<b>Behavior-Preserving Code</b>", styles["TableCellBold"]), Paragraph("<b>Zero Licensing Cost</b>", styles["TableCellBold"])],
    ]

    t2 = Table([t2_headers] + t2_rows, colWidths=[90, 85, 75, 75, 75, 65])
    t2.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1e3a8a")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor("#f8fafc")]),
    ]))
    story.append(t2)
    story.append(Paragraph("<b>Table 2.1:</b> Comparative Analysis Matrix of Existing Code Review Paradigms", styles["FigCaption"]))
    story.append(Spacer(1, 10))

    story.append(Paragraph("2.7 Identification of Research Gaps", styles["SectionHeader"]))
    story.append(Paragraph(
        "The survey reveals four glaring research gaps in automated code quality engineering:", styles["BodyJustified"]))
    story.append(Paragraph("1. <b>The Context Blindness Gap:</b> Conventional linters flag syntax anomalies without understanding developer intent, "
                           "causing high false-positive rates that trigger developer alert fatigue.", styles["BulletText"]))
    story.append(Paragraph("2. <b>The Hallucination & Trust Gap:</b> Ungrounded LLMs invent non-existent APIs and generate syntactically plausible "
                           "but logically broken refactorings.", styles["BulletText"]))
    story.append(Paragraph("3. <b>The Language Fragmentation Overhead:</b> Polyglot microservices teams must maintain disparate linter configurations "
                           "across Python, JavaScript, Java, and C++, creating inconsistent quality bars.", styles["BulletText"]))
    story.append(Paragraph("4. <b>The Remediation Disconnect:</b> Almost all existing static tools stop at defect detection, offering no integrated "
                           "mechanism to synthesize and download verified, production-ready refactored code.", styles["BulletText"]))

    story.append(Paragraph("2.8 Research Contributions of This Project", styles["SectionHeader"]))
    story.append(Paragraph(
        "To overcome these gaps, this thesis delivers four concrete technical contributions:", styles["BodyJustified"]))
    story.append(Paragraph("• <i>Hybrid Dual-Engine Architecture:</i> Unifies Python native AST with Tree-sitter CST grammars, establishing structural "
                           "feature parity across 9 major programming languages.", styles["BulletText"]))
    story.append(Paragraph("• <i>Deterministic Heuristic Bug & Complexity Engines:</i> Fast, offline algorithms for detecting infinite loops, division by "
                           "zero, dead code, and Big-O asymptotic complexity without requiring runtime execution.", styles["BulletText"]))
    story.append(Paragraph("• <i>Context-Grounded LLM Orchestration:</i> A prompt-engineering pipeline that feeds verified static findings into Groq "
                           "LPUs, producing verifiable refactorings and code explanations with zero hallucination.", styles["BulletText"]))
    story.append(Paragraph("• <i>Zero-Configuration Accessible Delivery:</i> A responsive Streamlit dashboard with local SQLite persistence and "
                           "one-click ReportLab PDF audit report exports.", styles["BulletText"]))

    story.append(Paragraph("2.9 Summary of the Literature Review", styles["SectionHeader"]))
    story.append(Paragraph(
        "In summary, the literature demonstrates that while static program analysis and generative artificial intelligence developed as "
        "separate disciplines, their intersection represents the future of software quality engineering. By grounding generative LLMs "
        "in deterministic syntax trees, the weaknesses of each approach are neutralized while their respective strengths are fully realized.", styles["BodyJustified"]))

    story.append(PageBreak())
    return story
