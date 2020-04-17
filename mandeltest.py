import mandel4pil as mandel

m = mandel.Mandelbild(-0.71+0.305j, 1e-2, 1000)
m.iterate(126)
im = m.show_image(palette=mandel.palette_bm())

