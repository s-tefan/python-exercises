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
    def __init__(self, cmid, cwidth, width, height=0):
        self.cmid = cmid
        self.cwidth = cwidth
        # If cwidth is complex use it, if real use it in both dimensions
        if isinstance(cwidth,complex) and cwidth.imag!=0:
            self.xwidth = cwidth.real
            self.ywidth = cwidth.imag
        else:
            self.xwidth = cwidth
            self.ywidth = cwidth
        self.width = width
        if height != 0:
            self.height = height
        else:
            self.height = int(self.width*(self.ywidth/self.xwidth))
        print(self.width, self.height, self.xwidth, self.ywidth)
        self.xdelta = self.xwidth/self.width
        self.ydelta = self.ywidth/self.height
        self.rundict = {}
        self.iters = 1
        for m in range(self.height):
            for n in range(self.width):
                c = cmid + (n-self.width//2)*self.xdelta + (self.height//2-m)*self.ydelta*1j
                p = Mandelpunkt(c)
                self.rundict[(m,n)] = p
                ''' 
                if not(p.runaway):
                    self.rundict[(m,n)] = p
                '''
    def old__init__(self, cstart, cstop, delta):
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
                ''' 
                if not(p.runaway):
                    self.rundict[(m,n)] = p
                '''
    
    def iterate(self, n=1):
        for coords in self.rundict:
            p = self.rundict[coords]
            if not(p.runaway):
                p.iterate(n)
        self.iters += n

    def make_image(self):
        imlist = []
        for co in self.rundict:
            val = self.rundict[co].iters
            if val >=  self.iters: # sholdn't be >self.iters
                palval = 255 
            else:
                palval = 254*val//self.iters
            imlist.append(palval)
        im = PIL.Image.frombytes('L',(self.width,self.height),bytes(imlist))
        return im

    def save_image( self, 
                    name = None, 
                    path = '', 
                    suffix = '', 
                    palette = palette2()
                    ) :
        if name==None:
            name = path + \
                'mandel_{cm}_{cw}_{i}_{w}.png'.format(
                cm = self.cmid,
                cw = self.cwidth,
                i = self.iters,
                w = self.width )
        im = self.make_image()
        im.putpalette(palette)
        im.save(name)
        return im

    def show_image(self):
        im = self.make_image()
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

def palette_binary():
    pal = []
    for k in range(256):
        if k%2 : 
            pal += [0,0,0]
        else :
            pal += [255,255,255]
    return pal

def palette_trinary():
    pal = []
    for k in range(255):
        if k%2 : 
            pal += [255,0,0]
        else :
            pal += [255,255,255]
    pal += [0,0,0]
    return pal


def test():
    #test = Mandelbild(-1.19+0.175j, -1.18+0.185j, 1e-5)
    test = Mandelbild(-1.185+0.18j, 0.01, 1000)
    for k in range(254):
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

def newshow(cmid, cwidth, width, its):
    m = Mandelbild(cmid, cwidth, width)
    m.iterate(its)
    im = m.show_image()
    return im
