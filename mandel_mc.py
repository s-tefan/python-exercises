from graphics import *
import math
import cmath
import random
win=GraphWin("apa",1750,1000)
#win.setCoords(-2,-1,1.5,1)


cramp=["red","yellow","green","blue","purple"]
nmax=100
center=-0.2+0.8*1j
width=0.1
height=4*width/7
a=center-width/2-height/2
win.setCoords(a.real,a.imag,(a+width).real,(a+height*1j).imag)

for n in range(1000000):
    c=a+width*random.random()+height*random.random()*1j    
#    c=-2+3*random.random()+(2*random.random()-1)*1j
    z=c
    n=0
    while abs(z)<2 and n<nmax:
        z=z**2+c
        n+=1
    pt=Point(c.real,c.imag)
    if n<nmax:
        pt.setOutline(cramp[n%5])
    pt.draw(win)
    
