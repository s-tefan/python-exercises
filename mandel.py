#from graphics import *
import math
import cmath
import random
#win=GraphWin("apa",1750,1000)
win=GraphWin("apa",875,500)


cramp=["red","yellow","green","blue","purple"]
nmax=100
#center=-0.2+0.8*1j; width=0.1
center=-0.24+0.86*1j; width=0.02
#center=0
#width=3.5
height=4*width/7
a=center-width/2-height/2*1j
win.setCoords(a.real,a.imag,a.real+width,a.imag+height)

clist=[]
for n in range(4):
    for m in range(7):
        c=center+width*(-3/7+m/7)+height*(3/8-n/4)*1j
        clist.append(c)

import rutskapare
w=width/7
h=height/4
rutskapare.rutrit(clist,w,h,nmax,cramp,win)

for apa in range(6):
    nlist=rutskapare.refine(clist,w,h)
    w=w/3
    h=h/3
    rutskapare.rutrit(nlist,w,h,nmax,cramp,win)
    clist=nlist+clist
