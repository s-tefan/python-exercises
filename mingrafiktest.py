#import numpy as np
import math as m
import graphics as g
from time import sleep 
def rotzmatrix(th):
    return np.array([[m.cos(th),-m.sin(th),0,0],
                     [m.sin(th),m.cos(th),0,0],
                     [0,0,1,0],
                     [0,0,0,1]])

def rotztransf(th):
#    return lambda p : (rotzmatrix(th)).dot(hom(p))
    return lambda p : (m.cos(th)*p[0]-m.sin(th)*p[1],
                     m.sin(th)*p[0]+m.cos(th)*p[1],
                     p[2])

def rotxtransf(th):
#    return lambda p : (rotxmatrix(th)).dot(hom(p))
    return lambda p : (p[0],
                       m.cos(th)*p[1]-m.sin(th)*p[2],
                     m.sin(th)*p[1]+m.cos(th)*p[2])


def projz(pt):
    return (pt[0],pt[1])

def hom(x,y,z):
    return np.array([[x],[y],[z],[1]])

class Figur:
    points=[] # list of 3-tuples
    lines=[]    # list of 2-tuples of indices in points
    scale=100
    def __init__(self,pts,lns):
        self.points=pts
        self.lines=lns
    def grlines(self):
        grl=[]
        for line in self.lines:
            p0=projz(self.points[line[0]])
            p1=projz(self.points[line[1]])
            grl.append(g.Line(g.Point(*p0),g.Point(*p1)))
        return grl
    def grpoints(self):
        grp=[]
        for pt in self.points:
            p=projz(pt)
            grp.append(g.Point(*p))
        return grp
    def draw(self,win):
        for ln in self.grlines():
            ln.draw(win)
        for pt in self.grpoints():
            pt.draw(win)
    def undraw(self):
        for ln in self.grlines():
            ln.undraw()
        for pt in self.grpoints():
            pt.undraw()
    def apply(self,transf):
        ps=[]
        for p in self.points:
            ps.append(transf(p))
        self.points=ps
        

win=g.GraphWin('ap',400,400)
win.setCoords(-3,-3,3,3)
fig=Figur([(0,0,0),(0,2,0),(0,1,0),(1,2,0),(0.8,1,0)],
          [(0,1),(1,3),(2,4)])
print(fig.grpoints())
print(fig.grlines())
for n in range(24):
    fig.draw(win)
    sleep(1)
    fig.undraw()
#    fig.apply(rotztransf(m.pi/6))
    fig.apply(rotxtransf(m.pi/6))


        
