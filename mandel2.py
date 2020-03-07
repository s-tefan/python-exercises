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

    
def greja(c):
    z=0
    for k in range(nmax):
        if abs(z)>2: break
        z = z**2 + c
    p = graphics.Point(c.real, c.imag)
    #blobb = graphics.Circle(p, r)
    '''
    p1 = p.clone()
    p1.move(-r,-r)
    p2 = p.clone()
    p2.move(r,r)
    blobb = graphics.Rectangle(p1,p2)
    '''
    blobb = p
    intens = int(255/(1+k/20))
    col = graphics.color_rgb(intens,intens,intens)
    blobb.setFill(col)
    #blobb.setWidth(0)
    blobb.draw(win)



#xmin, xmax, ymin, ymax = -2,0.5,0,1
xmin, xmax, ymin, ymax = -1.75,-1.7,0,0.02
cstart = xmin + ymin*1j
cstop = xmax + ymax*1j
delta = (xmax-xmin)/400*(1+1j)
nmax = 100
win = graphingwin(xmin,xmax,ymin,ymax,xres=800,yres=800,equal=True)
r = abs(delta)/2
for c in iterc(cstart, cstop, 16*delta):
    #print(c)
    greja(c)
for c in iterc(cstart, cstop, 8*delta):
    #print(c)
    greja(c)
for c in iterc(cstart, cstop, 4*delta):
    #print(c)
    greja(c)
for c in iterc(cstart+2*delta, cstop, 4*delta):
    #print(c)
    greja(c)
for c in iterc(cstart+2*delta.real, cstop, 4*delta):
    #print(c)
    greja(c)
for c in iterc(cstart+2*delta.imag*1j, cstop, 4*delta):
    #print(c)
    greja(c)
for c in iterc(cstart+delta, cstop, 2*delta):
    #print(c)
    greja(c)
for c in iterc(cstart+delta.real, cstop, 2*delta):
    #print(c)
    greja(c)
for c in iterc(cstart+delta.imag*1j, cstop, 2*delta):
    #print(c)
    greja(c)
win.getMouse()