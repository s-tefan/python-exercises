from graphics import *
import math
import cmath
import random
win=GraphWin("apa",800,800)
win.setCoords(-2,-2,2,2)




def iterate(z):
    return z-(z**3-1)/z**2/3



z=-1+0.1*1j

#alist=[-0.1-0.02*n for n in range(100)]
#for a in alist:
#    n=10
#zlist=[-2+4*random.random()+(2*random.random()-1)*1j for n in range(100)]

    #z0=a+0.1*1j
#for z0 in zlist:
for n in range(100000):
    z0=-2+3*random.random()+(2*random.random()-1)*1j

    z=z0
##    for k in range(n):
    while abs(z**3-1)>0.1:
        z1=iterate(z)
#        pt0=Point(z.real,z.imag)
#        pt1=Point(z1.real,z1.imag)
#        pt0.draw(win)
#        pt1.draw(win)
#        l=Line(pt0,pt1)
#        l.setArrow("last")
#        l.draw(win)
        z=z1

#    l=Line(Point(z0.real,z0.imag),Point(z1.real,z1.imag))
#    l.draw(win)
    pt=Point(z0.real,z0.imag)
    phi=cmath.phase(z)
    if abs(phi)<math.pi/3:
        pt.setOutline("blue")
    elif phi>math.pi/3:
        pt.setOutline("red")
    elif phi<math.pi/3:
        pt.setOutline("green")
    pt.draw(win)
        
         
    
