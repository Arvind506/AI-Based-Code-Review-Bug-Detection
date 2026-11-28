import os
import sys
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, KeepTogether, PageBreak, HRFlowable
)
from reportlab.pdfgen import canvas

# ----------------------------------------------------------------------
# NumberedCanvas for Two-Pass Dynamic Page Numbering & Running Headers
# ----------------------------------------------------------------------
class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        # Do not draw headers/footers on Cover (page 1) and Certificate (page 2)
        if self._pageNumber <= 2:
            return

        self.saveState()
        self.setFont("Helvetica", 8.5)
        self.setFillColor(colors.HexColor("#475569"))

        # Running Header
        self.drawString(72, A4[1] - 42, "AI Code Review & Bug Detection")
        self.drawRightString(A4[0] - 57.6, A4[1] - 42, "Final Year Project Report")
        self.setStrokeColor(colors.HexColor("#cbd5e1"))
        self.setLineWidth(0.6)
        self.line(72, A4[1] - 46, A4[0] - 57.6, A4[1] - 46)

        # Running Footer
        self.line(72, 48, A4[0] - 57.6, 48)
        self.drawString(72, 36, "Department of Information Technology | Research Project")
        
        # Roman numerals for preliminary pages (3 to 6), Arabic for main body (7+)
        if self._pageNumber <= 6:
            romans = ["i", "ii", "iii", "iv", "v", "vi", "vii"]
            p_str = romans[self._pageNumber - 3] if (self._pageNumber - 3) < len(romans) else str(self._pageNumber)
            self.drawRightString(A4[0] - 57.6, 36, p_str)
        else:
            arabic_page = self._pageNumber - 6
            total_arabic = page_count - 6
            self.drawRightString(A4[0] - 57.6, 36, f"Page {arabic_page} of {total_arabic}")

        self.restoreState()

print("NumberedCanvas initialized successfully.")
