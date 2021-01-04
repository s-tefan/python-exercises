# simple_demo.py
from fpdf import FPDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Welcome to Python!", ln=1, align="C")
pdf.cell(300, 10, txt="För faen!", ln=1, align="C")
pdf.line(10, 10, 10, 100)
pdf.set_line_width(1)
pdf.set_draw_color(255, 255, 0)
pdf.line(20, 20, 100, 20)

pdf.output("simple_demo.pdf")
