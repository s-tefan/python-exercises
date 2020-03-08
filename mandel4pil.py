import PIL.Image

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
        self.cstart = cstart
        self.cstop = cstop
        self.delta = delta
        self.rundict = {}
        self.width = int(((cstop-cstart)/delta).real)
        self.height = int(((cstop-cstart)/delta).imag)
        for m in range(self.height):
            for n in range(self.width):
                c = cstart + n*delta + (self.height-m)*delta*1j
                p = Mandelpunkt(c)
                self.rundict[(m,n)] = p 
                if not(p.runaway):
                    self.rundict[(m,n)] = p
    
    def iterate(self):
        for coords in self.rundict:
            p = self.rundict[coords]
            if not(p.runaway):
                p.iterate()


test = Mandelbild(-1.2+0.175j, -1.175+0.2j, 2e-5)
for k in range(255):
    test.iterate()

imlist = []
for co in test.rundict:
    print(test.rundict[co].c, test.rundict[co].iters)
    imlist.append(test.rundict[co].iters)

im = PIL.Image.frombytes('L',(test.width,test.height),bytes(imlist))
im.show()
