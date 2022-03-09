import cairo
width, height = 210*72/25.4, 297*72/25.4
with open("test.pdf", 'wb') as of:
    s = cairo.PDFSurface(of, width, height)
    c = cairo.Context(s)
    c.move_to(72,72)
    c.show_text('apa')
