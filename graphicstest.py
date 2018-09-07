from graphics import *
import math
win=GraphWin("apa",800,800)
win.setCoords(0,0,1,1)
pt=Point(0.5,0.5)
pt.draw(win)

n=100
for k in range(n):
    x=k/n
    y=0.5+0.5*math.sin(2*math.pi*x)
    Point(x,y).draw(win)
