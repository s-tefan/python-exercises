import cmath

def kubikrot(a,x,d):
    while True:
        x=(2*x+a/x**2)/3
        if abs(x**3-1)<d:
            return x


from graphics import *
xp,yp=600,200
d=1/xp

win=GraphWin("apa",xp,yp)
c=['red','green','blue']


for n in range(yp):
    for m in range (xp):
        x=-0.01-m*d+1.0j*n*d
        x=kubikrot(1,x,0.01)
        a=round(cmath.phase(x)*3/(2*cmath.pi))
#        print(a,end=',')
        win.plotPixel(xp-m,yp-n,c[a])
    print()
