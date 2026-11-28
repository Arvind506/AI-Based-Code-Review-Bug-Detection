import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, HRFlowable

def get_thesis_styles():
    base = getSampleStyleSheet()

    styles = {
        "CoverTitle": ParagraphStyle(
            "CoverTitle",
            parent=base["Normal"],
            fontName="Helvetica-Bold",
            fontSize=22,
            leading=28,
            alignment=1, # Center
            textColor=colors.HexColor("#0f172a"),
            spaceAfter=14
        ),
        "CoverSubtitle": ParagraphStyle(
            "CoverSubtitle",
            parent=base["Normal"],
            fontName="Helvetica-Oblique",
            fontSize=11,
            leading=16,
            alignment=1,
            textColor=colors.HexColor("#334155"),
            spaceAfter=24
        ),
        "CoverMeta": ParagraphStyle(
            "CoverMeta",
            parent=base["Normal"],
            fontName="Times-Roman",
            fontSize=11,
            leading=15,
            alignment=1,
            textColor=colors.HexColor("#0f172a")
        ),
        "CoverMetaBold": ParagraphStyle(
            "CoverMetaBold",
            parent=base["Normal"],
            fontName="Times-Bold",
            fontSize=11,
            leading=16,
            alignment=1,
            textColor=colors.HexColor("#0f172a")
        ),
        "CoverMetaBold14": ParagraphStyle(
            "CoverMetaBold14",
            parent=base["Normal"],
            fontName="Times-Bold",
            fontSize=14,
            leading=18,
            alignment=1,
            textColor=colors.HexColor("#0f172a")
        ),
        "CoverMetaBold13": ParagraphStyle(
            "CoverMetaBold13",
            parent=base["Normal"],
            fontName="Times-Bold",
            fontSize=13,
            leading=17,
            alignment=1,
            textColor=colors.HexColor("#0f172a")
        ),
        "CoverTitle30": ParagraphStyle(
            "CoverTitle30",
            parent=base["Normal"],
            fontName="Times-Bold",
            fontSize=28,
            leading=34,
            alignment=1,
            textColor=colors.HexColor("#0f172a")
        ),
        "CoverSubtitle12": ParagraphStyle(
            "CoverSubtitle12",
            parent=base["Normal"],
            fontName="Times-Italic",
            fontSize=12,
            leading=16,
            alignment=1,
            textColor=colors.HexColor("#0f172a")
        ),
        "CertHeader13": ParagraphStyle(
            "CertHeader13",
            parent=base["Normal"],
            fontName="Times-Bold",
            fontSize=13,
            leading=17,
            alignment=1,
            textColor=colors.HexColor("#0f172a")
        ),
        "CertTitle26": ParagraphStyle(
            "CertTitle26",
            parent=base["Normal"],
            fontName="Times-Bold",
            fontSize=26,
            leading=30,
            alignment=1,
            textColor=colors.HexColor("#0f172a")
        ),
        "CertBody12": ParagraphStyle(
            "CertBody12",
            parent=base["Normal"],
            fontName="Times-Roman",
            fontSize=12,
            leading=20,
            alignment=4,
            textColor=colors.HexColor("#0f172a")
        ),
        "SigCellBold12": ParagraphStyle(
            "SigCellBold12",
            parent=base["Normal"],
            fontName="Times-Bold",
            fontSize=12,
            leading=16,
            alignment=1,
            textColor=colors.HexColor("#0f172a")
        ),
        "BottomLeftBold12": ParagraphStyle(
            "BottomLeftBold12",
            parent=base["Normal"],
            fontName="Times-Bold",
            fontSize=12,
            leading=16,
            alignment=0,
            textColor=colors.HexColor("#0f172a")
        ),
        "BottomRightBold12": ParagraphStyle(
            "BottomRightBold12",
            parent=base["Normal"],
            fontName="Times-Bold",
            fontSize=12,
            leading=16,
            alignment=2,
            textColor=colors.HexColor("#0f172a")
        ),
        "TableSigCell": ParagraphStyle(
            "TableSigCell",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=10,
            leading=16,
            alignment=1,
            textColor=colors.HexColor("#0f172a")
        ),
        "TableLeftCell": ParagraphStyle(
            "TableLeftCell",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=10.5,
            leading=16,
            alignment=0,
            textColor=colors.HexColor("#0f172a")
        ),
        "TableRightCell": ParagraphStyle(
            "TableRightCell",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=10.5,
            leading=16,
            alignment=2,
            textColor=colors.HexColor("#0f172a")
        ),
        "ChapterHeader": ParagraphStyle(
            "ChapterHeader",
            parent=base["Normal"],
            fontName="Helvetica-Bold",
            fontSize=19,
            leading=24,
            alignment=1, # Center
            textColor=colors.HexColor("#0f172a"),
            spaceBefore=10,
            spaceAfter=18,
            keepWithNext=True
        ),
        "SectionHeader": ParagraphStyle(
            "SectionHeader",
            parent=base["Normal"],
            fontName="Helvetica-Bold",
            fontSize=13,
            leading=17,
            alignment=0, # Left
            textColor=colors.HexColor("#1e3a8a"),
            spaceBefore=14,
            spaceAfter=6,
            keepWithNext=True
        ),
        "SubSectionHeader": ParagraphStyle(
            "SubSectionHeader",
            parent=base["Normal"],
            fontName="Helvetica-Bold",
            fontSize=11,
            leading=15,
            alignment=0,
            textColor=colors.HexColor("#0f172a"),
            spaceBefore=10,
            spaceAfter=4,
            keepWithNext=True
        ),
        "BodyJustified": ParagraphStyle(
            "BodyJustified",
            parent=base["Normal"],
            fontName="Times-Roman",
            fontSize=10.5,
            leading=15,
            alignment=4, # Justify
            textColor=colors.HexColor("#0f172a"),
            spaceAfter=7
        ),
        "BulletText": ParagraphStyle(
            "BulletText",
            parent=base["Normal"],
            fontName="Times-Roman",
            fontSize=10,
            leading=14,
            alignment=4,
            leftIndent=18,
            spaceAfter=4
        ),
        "FigCaption": ParagraphStyle(
            "FigCaption",
            parent=base["Normal"],
            fontName="Helvetica-Bold",
            fontSize=8.5,
            leading=12,
            alignment=1, # Center
            textColor=colors.HexColor("#334155"),
            spaceBefore=6,
            spaceAfter=12
        ),
        "TableHead": ParagraphStyle(
            "TableHead",
            parent=base["Normal"],
            fontName="Helvetica-Bold",
            fontSize=8,
            leading=11,
            alignment=0,
            textColor=colors.white
        ),
        "TableCell": ParagraphStyle(
            "TableCell",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=8,
            leading=11,
            alignment=0,
            textColor=colors.HexColor("#0f172a")
        ),
        "TableCellBold": ParagraphStyle(
            "TableCellBold",
            parent=base["Normal"],
            fontName="Helvetica-Bold",
            fontSize=8,
            leading=11,
            alignment=0,
            textColor=colors.HexColor("#0f172a")
        ),
        "CodeListing": ParagraphStyle(
            "CodeListing",
            parent=base["Normal"],
            fontName="Courier",
            fontSize=7.5,
            leading=10,
            alignment=0,
            textColor=colors.HexColor("#0f172a"),
            leftIndent=10,
            spaceBefore=2,
            spaceAfter=2
        ),
        "CalloutBox": ParagraphStyle(
            "CalloutBox",
            parent=base["Normal"],
            fontName="Times-Italic",
            fontSize=9.5,
            leading=13.5,
            alignment=4,
            textColor=colors.HexColor("#1e3a8a"),
            leftIndent=12,
            rightIndent=12,
            spaceBefore=6,
            spaceAfter=6
        ),
        "TOC_Line": ParagraphStyle(
            "TOC_Line",
            parent=base["Normal"],
            fontName="Times-Roman",
            fontSize=9.5,
            leading=13.5,
            alignment=0,
            textColor=colors.HexColor("#0f172a")
        ),
        "TOC_Chapter": ParagraphStyle(
            "TOC_Chapter",
            parent=base["Normal"],
            fontName="Helvetica-Bold",
            fontSize=10,
            leading=14.5,
            alignment=0,
            textColor=colors.HexColor("#1e3a8a"),
            spaceBefore=4
        )
    }
    return styles

def make_callout(text, styles, width=465):
    p = Paragraph(f"<b>Key Design Note:</b> {text}", styles["CalloutBox"])
    t = Table([[p]], colWidths=[width])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#f8fafc")),
        ('BOX', (0,0), (-1,-1), 1.0, colors.HexColor("#cbd5e1")),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ]))
    return t

def make_code_box(code_lines, width=465):
    p_lines = [Paragraph(line.replace(" ", "&nbsp;"), ParagraphStyle("cb", fontName="Courier", fontSize=7.2, leading=9.8, textColor=colors.HexColor("#0f172a"))) for line in code_lines]
    t = Table([[p_lines]], colWidths=[width])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#f1f5f9")),
        ('BOX', (0,0), (-1,-1), 0.8, colors.HexColor("#94a3b8")),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ]))
    return t
