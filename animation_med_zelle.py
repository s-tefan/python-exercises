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


def wait(win):
    pass
    win.getMouse() # pause for click in window


def main1():
    win = graphingwin(0,1,0,1)
    p1, p2 = graphics.Point(0.1,0.1), graphics.Point(0.8,0.7)
    r1 = graphics.Rectangle(p1, p2)
    r1.setFill('red')
    r1.draw(win)
    wait(win)
    r2 = graphics.Rectangle(graphics.Point(0.2,0.2), graphics.Point(0.7,0.8))
    r2.setFill('green')
    r2.draw(win)
    wait(win)
    r1.undraw()
    wait(win)
    p1 = graphics.Point(0.3,0.4)
    r1.draw(win)
    wait(win)
    win.close()

def main2():
    colors = ['red','green','blue']
    win = graphingwin(0,1,0,1)
    c = 0
    p1, p2 = graphics.Point(random.random(),random.random()), graphics.Point(random.random(),random.random())
    r1 = graphics.Rectangle(p1, p2)
    r1.setFill(colors[c])
    r1.draw(win)
    while True:
        p1, p2 = graphics.Point(random.random(),random.random()), graphics.Point(random.random(),random.random())
        r1.undraw()
        r1 = graphics.Rectangle(p1, p2)
        r1.setFill(colors[c])
        r1.draw(win)
        wait(win)
        c = (c+1)%3

def main3():
    win = graphingwin(0,1,0,1)
    p1, p2 = graphics.Point(random.random(),random.random()), graphics.Point(random.random(),random.random())
    r1 = graphics.Rectangle(p1, p2)
    r1.setFill('red')
    r1.draw(win)
    while True:
        r1.move(0.01*(random.random()-0.5),0.01*(random.random()-0.5))
        time.sleep(0.1)

def main4():
    def getr(start,stop,delta):
        val = start
        while val <= stop:
            yield val
            val += delta

    rmin, rmax = 1, 4
    delta = 1.0e-2
    win = graphingwin(rmin, rmax, 0, 1)
    for r in getr(rmin, rmax, delta):
        x = 0.5
        for k in range(40):
            x = r*x*(1-x)
        for k in range(64):
            x = r*x*(1-x)
            p = graphics.Point(r,x)
            p.draw(win)
    wait(win)

main4()