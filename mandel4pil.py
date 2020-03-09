import PIL.Image
import math

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


def palette1():
    pal = []
    for k in range(256):
        rg = (255-k)//2
        rg *= (rg<128)
        b = (255-k)*2-255
        b *= (b>=0)
        pal += [rg,rg,b]
    return pal

def palette2():
    pal = []
    for k in range(256):
        if k == 255 : 
            pal += [0,0,0]
        else :
            r = (255-k//2)
            g = (255-k)
            b = 255-k
            pal += [r,g,b]
    return pal

def test():
    test = Mandelbild(-1.19+0.175j, -1.18+0.185j, 1e-5)
    for k in range(255):
        print(k)
        test.iterate()

    imlist = []
    for co in test.rundict:
        #print(test.rundict[co].c, test.rundict[co].iters)
        imlist.append(test.rundict[co].iters)
    return test,imlist

def showim(test, imlist):
    im = PIL.Image.frombytes('L',(test.width,test.height),bytes(imlist))
    im.putpalette(palette2())
    im.show()
    return im