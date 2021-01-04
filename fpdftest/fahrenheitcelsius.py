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

pdf.set_line_width(10)
start = 1000
for k in range(30):
    f = 20*k
    if k % 2 :
        pdf.set_draw_color(255,0, 0)
    else:
        pdf.set_draw_color(0, 0, 0)
    pdf.line(10, start-f, 10, start-(f+1))
    pdf.text(5, start-f, txt=str(f))

for j in range(30):
    cstep = 20
    fstep = cstep*9/5
    c = cstep*(j-1)
    f = c/5*9 + 32
    if k % 2 :
        pdf.set_draw_color(0,255,255)
    else:
        pdf.set_draw_color(0, 0, 0)
    pdf.line(110, start-f, 110, start-(f+fstep/2))
    pdf.text(105, start-f, txt=str(c))
        

pdf.output("simple_demo.pdf")
