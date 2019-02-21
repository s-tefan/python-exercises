from turtle import *

def koch(t,x,minx):
    if x>minx:
        koch(t,x/3,minx)
        t.left(60)
        koch(t,x/3,minx)
        t.right(120)
        koch(t,x/3,minx)
        t.left(60)
        koch(t,x/3,minx)
    else:
        t.fd(x)

t=Turtle()
tracer(2)
#t.speed(0)
#ts=t.getscreen()
#ts=Screen()
(ww,hh)=(3**6,int(3**5.5/2))
(ww,hh)=(3**6.5,int(3**6/2))
#screensize(ww,hh)
setup(width=ww,height=hh,startx=0,starty=0) # Den här fixar, men...
#print(screensize()) # Fattar inte riktigt hur fönsterstorlek funkar.

setworldcoordinates(0,0,ww,hh)

print(screensize())
#setup(width=ww,height=hh,startx=0,starty=0)
#t.home()
print(t.pos())
koch(t,ww,1)
