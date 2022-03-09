import cairo
import math
'''
width, height = 210*72/25.4, 297*72/25.4
with open("test.pdf", 'wb') as of:
    s = cairo.PDFSurface(of, width, height)
    c = cairo.Context(s)
    c.select_font_face('PT Mono')
    c.set_font_size(12)
    c.set_source_rgba(0, 0, 0, 0.6)
    c.move_to(72,72)
    c.show_text('apa')
    s.flush()
    s.show_page()
    s.finish()
'''
s = cairo.ImageSurface(cairo.FORMAT_ARGB32, 200, 200)
c = cairo.Context(s)
c.set_source_rgb(1, 1, 0)  # Solid color
c.rectangle(10, 10, 110, 110)  # Rectangle(x0, y0, x1, y1)
c.fill()


ctx = c # för att slippa ändra koden ...
ctx.save()
ctx.scale(200, 200)  # Normalizing the canvas
ctx.move_to(0, 0)
# Arc(cx, cy, radius, start_angle, stop_angle)
ctx.arc(0.2, 0.1, 0.1, -math.pi / 2, 0)
ctx.line_to(0.5, 0.1)  # Line to (x,y)
# Curve(x1, y1, x2, y2, x3, y3)
ctx.curve_to(0.5, 0.2, 0.5, 0.4, 0.2, 0.8)
ctx.close_path()

ctx.set_source_rgb(0.3, 0.2, 0.5)  # Solid color
ctx.set_line_width(0.02)
ctx.stroke()
ctx.restore()
pat = cairo.LinearGradient(0.0, 0.0, 0.0, 1.0)
pat.add_color_stop_rgba(1, 0.7, 0, 0, 0.5)  # First stop, 50% opacity
pat.add_color_stop_rgba(0, 0.9, 0.7, 0.2, 1)  # Last stop, 100% opacity
c.rectangle(0, 0, 100, 100)  # Rectangle(x0, y0, x1, y1)
c.set_source(pat)
c.fill()
c.select_font_face('PT Mono')
c.set_font_size(36)
c.set_source_rgba(0, 0, 0, 0.6)
c.move_to(72,72)
c.show_text('apa')
s.write_to_png("example.png")
