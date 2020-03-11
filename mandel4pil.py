import PIL.Image
import math

class Mandelpunkt:
    def __init__(self, c):
        self.c = c
        self.z = c
        self.iters = 1
        self.runaway = abs(self.z)>2
    
    def iterate(self, n = 1):
        for k in range(n):
            if self.runaway:
                break
            else:
                self.z = self.z**2 + self.c
                self.runaway = abs(self.z)>2
                if not self.runaway:
                    self.iters += 1
    

class Mandelbild:
    def __init__(self, cstart, cstop, delta):
        self.cstart = cstart
        self.cstop = cstop
        self.delta = delta
        self.rundict = {}
        self.width = int(((cstop-cstart)/delta).real)
        self.height = int(((cstop-cstart)/delta).imag)
        self.iters = 1
        for m in range(self.height):
            for n in range(self.width):
                c = cstart + n*delta + (self.height-m)*delta*1j
                p = Mandelpunkt(c)
                self.rundict[(m,n)] = p 
                if not(p.runaway):
                    self.rundict[(m,n)] = p
    
    def iterate(self, n=1):
        for coords in self.rundict:
            p = self.rundict[coords]
            if not(p.runaway):
                p.iterate(n)
        self.iters += n

    def show_image(self):
        imlist = []
        for co in self.rundict:
            #print(self.rundict[co].iters, self.iters)
            imlist.append((255*self.rundict[co].iters)//self.iters)
        im = PIL.Image.frombytes('L',(self.width,self.height),bytes(imlist))
        im.putpalette(palette2())
        im.show()
        return im


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

def newshow(cstart, delta, width, height, its):
    cstop = cstart + delta * (width+height*1j)
    print(cstart, cstop)
    m = Mandelbild(cstart, cstop, delta)
    m.iterate(its)
    im = m.show_image()
    return im
