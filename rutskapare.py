from graphics import *
import math
import cmath
import random

def refine(clist,w,h):
    grid=[-w/3+h/3*1j,h/3*1j,w/3+h/3*1j, \
          -w/3,w/3, \
          -w/3-h/3*1j,-h/3*1j,w/3-h/3*1j]
    rlist=[]      
    for c in clist:
          for d in grid:
              rlist.append(c+d)
    return rlist
        
    
    
def rutrit(list,w,h,nmax,cramp,win):
    for c in list:
        z=c
        n=0
        while abs(z)<2 and n<nmax:
            z=z**2+c
            n+=1
        pt=Point(c.real,c.imag)
        r=Rectangle(Point(c.real-w/2,c.imag-h/2),Point(c.real+w/2,c.imag+h/2))
        m=len(cramp)
        if n<nmax:
            nn=int(10*math.log(n))%m
            #pt.setOutline(cramp[nn])
            r.setFill(cramp[nn])
            r.setOutline(cramp[nn])
        else:
            r.setFill("black")
        r.draw(win)
        #pt.draw(win)
	
