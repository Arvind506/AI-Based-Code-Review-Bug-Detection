import os
import sys
import time
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate
from thesis_styles import get_thesis_styles
from thesis_canvas import NumberedCanvas
from thesis_preliminary import get_preliminary_flowables
from thesis_ch1_ch2 import get_ch1_ch2_flowables
from thesis_ch3_ch4 import get_ch3_ch4_flowables
from thesis_ch5_ch6 import get_ch5_ch6_flowables
from thesis_ch7_ch8 import get_ch7_ch8_flowables

def build_pdf():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    assets_dir = os.path.join(base_dir, "report_assets")
    output_pdf = os.path.join(base_dir, "AI_Code_Review_Bug_Detection_Final_Report.pdf")

    print("=" * 70)
    print("STARTING THESIS REPORT GENERATION PIPELINE")
    print(f"Target Output: {output_pdf}")
    print("=" * 70)

    start_time = time.time()
    styles = get_thesis_styles()
    story = []

    print("[1/5] Compiling Preliminary Pages (Cover, Certificate, TOC, Lists)...")
    prelim_story = get_preliminary_flowables(styles)
    story.extend(prelim_story)
    print(f"       -> Added {len(prelim_story)} flowables.")

    print("[2/5] Compiling Chapter 1 (Introduction) & Chapter 2 (Literature Review)...")
    ch1_2_story = get_ch1_ch2_flowables(styles)
    story.extend(ch1_2_story)
    print(f"       -> Added {len(ch1_2_story)} flowables.")

    print("[3/5] Compiling Chapter 3 (Requirements) & Chapter 4 (Architecture & UML)...")
    ch3_4_story = get_ch3_ch4_flowables(styles, assets_dir)
    story.extend(ch3_4_story)
    print(f"       -> Added {len(ch3_4_story)} flowables.")

    print("[4/5] Compiling Chapter 5 (Implementation) & Chapter 6 (Testing & QA)...")
    ch5_6_story = get_ch5_ch6_flowables(styles)
    story.extend(ch5_6_story)
    print(f"       -> Added {len(ch5_6_story)} flowables.")

    print("[5/5] Compiling Chapter 7 (Results), Chapter 8 (Conclusion), References & Appendices...")
    ch7_8_story = get_ch7_ch8_flowables(styles, assets_dir)
    story.extend(ch7_8_story)
    print(f"       -> Added {len(ch7_8_story)} flowables.")

    print(f"Total Flowables in Master Document: {len(story)}")
    print("Rendering PDF with NumberedCanvas (two-pass dynamic headers & page numbering)...")

    doc = SimpleDocTemplate(
        output_pdf,
        pagesize=A4,
        leftMargin=65,
        rightMargin=65,
        topMargin=55,
        bottomMargin=55
    )

    doc.build(story, canvasmaker=NumberedCanvas)
    elapsed = time.time() - start_time
    print(f"Build complete in {elapsed:.2f} seconds.")

    # Check file size
    file_size_mb = os.path.getsize(output_pdf) / (1024 * 1024)
    print(f"File Size: {file_size_mb:.2f} MB")

    # Verify page count
    try:
        from pypdf import PdfReader
        reader = PdfReader(output_pdf)
        total_pages = len(reader.pages)
        print(f"VERIFIED TOTAL PAGE COUNT: {total_pages} PAGES")
        if total_pages >= 60:
            print(f"SUCCESS: Requirement satisfied! ({total_pages} >= 60 pages)")
        else:
            print(f"WARNING: Page count is {total_pages}, which is less than 60.")
    except ImportError:
        try:
            from PyPDF2 import PdfReader
            reader = PdfReader(output_pdf)
            total_pages = len(reader.pages)
            print(f"VERIFIED TOTAL PAGE COUNT: {total_pages} PAGES")
        except Exception as e:
            print(f"Could not import pypdf/PyPDF2: {e}")

if __name__ == "__main__":
    build_pdf()
