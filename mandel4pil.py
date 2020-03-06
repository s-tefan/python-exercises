#import PIL.ImageDraw 

class Mandelpunkt:
    def __init__(self, c):
        self.c = c
        self.z = c
        self.iters = 0
        self.runaway = abs(self.z)>2
    
    def iterate(self):
        self.z = self.z**2 + self.c
        self.iters += 1
        self.runaway = abs(self.z)>2


class Mandelbild:
    def __init__(self,cstart, cstop, delta):
        self.mandeldict = {}
        self.rundict = {}
        width = int(((cstop-cstart)/delta).real)
        height = int(((cstop-cstart)/delta).imag)
        for m in range(height):
            for n in range(width):
                c = cstart + n*delta.real + m*delta.imag*1j
                p = Mandelpunkt(c)
                self.mandeldict[(m,n)] = p 
                if not(p.runaway):
                    self.rundict[(m,n)] = p
    
    def iterate(self):
        for coords in self.rundict:
            p = self.rundict[coords]
            p.iterate()
            if p.runaway:
                self.rundict.pop(coords, False)


test = Mandelbild(-3+0j, 1+2j, 0.5)
for k in range(30):
    test.iterate()

for co in test.mandeldict:
    print(test.mandeldict[co].c, test.mandeldict[co].iters)
