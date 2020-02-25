import graphics # Kräver John Zelles modul graphics.py
# http://mcsp.wartburg.edu/zelle/python/graphics.py
import time
import random

def graphingwin(xmin,xmax,ymin,ymax,xres=800,yres=800,equal=False):
    if equal==True:
        yres=int((ymax-ymin)/(xmax-xmin)*yres)
    win=graphics.GraphWin("apa",xres,yres)
    win.setCoords(xmin,ymin,xmax,ymax)
    return win


def iterc(start,stop,delta):
    val = start
    while val.imag <= stop.imag:
        while val.real <= stop.real:
            yield val
            val += delta.real
        val = start.real + (val.imag + delta.imag)*1j





xmin, xmax, ymin, ymax = -2,0.5,0,1
#xmin, xmax, ymin, ymax = -1.75,-1.7,0,0.02
cstart = xmin + ymin*1j
cstop = xmax + ymax*1j
delta = (xmax-xmin)/200*(1+1j)
nmax = 100
win = graphingwin(xmin,xmax,ymin,ymax,xres=800,yres=800,equal=True)
r = abs(delta)/2

cdict = {}
n = 0
for c in iterc(cstart, cstop, delta):
    c1=c-delta
    c2=c+delta
    #blobb = graphics.Point(c.real, c.imag)
    blobb = graphics.Rectangle(graphics.Point(c1.real, c1.imag), graphics.Point(c2.real, c2.imag))
    intens = 255
    col = graphics.color_rgb(intens,intens,intens)
    blobb.setFill(col)
    blobb.setWidth(0)
    blobb.draw(win)
    cdict[c]=[c,0,blobb]
while True:
    n+=1
    print(n)
    for c in cdict:
        z = cdict[c][0]
        if abs(z)<2:
            z = z**2 + c
            cdict[c][0] = z
            cdict[c][1]+=1
        if n%20 == 0:
            intens = int(255/(1 + cdict[c][1]/20))
            col = graphics.color_rgb(intens,intens,intens)
            cdict[c][2].setFill(col)



win.getMouse()