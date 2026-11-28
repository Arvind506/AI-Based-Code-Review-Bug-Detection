import os
import sys
import re
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
        self.drawRightString(A4[0] - 57.6, A4[1] - 42, "M.Sc. (Information Technology) | Research Project")
        self.setStrokeColor(colors.HexColor("#cbd5e1"))
        self.setLineWidth(0.6)
        self.line(72, A4[1] - 46, A4[0] - 57.6, A4[1] - 46)

        # Running Footer
        self.line(72, 48, A4[0] - 57.6, 48)
        self.drawString(72, 36, "Department of Information Technology | Research Project")
        
        # Roman numerals for preliminary pages (3 to 12), Arabic for main body (13+)
        if self._pageNumber <= 12:
            romans = ["i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x", "xi", "xii", "xiii"]
            idx = self._pageNumber - 1 # Page 3 is index 2 -> iii
            p_str = romans[idx] if 0 <= idx < len(romans) else str(self._pageNumber)
            self.drawRightString(A4[0] - 57.6, 36, p_str)
        else:
            arabic_page = self._pageNumber - 12
            total_arabic = page_count - 12
            self.drawRightString(A4[0] - 57.6, 36, f"Page {arabic_page} of {total_arabic}")

        self.restoreState()

print("NumberedCanvas ready.")
