import graphics,math


def plotta(x,y,c,win):
#    prick=graphics.Circle(graphics.Point(x,y),0.002)
    (dx,dy)=(5,5e-5)
    prick=graphics.Oval(graphics.Point(x-dx,y-dy),graphics.Point(x+dx,y+dy))
    prick.setFill(c)
    prick.setOutline(c)
    prick.draw(win)

def sgdEuklides(a,b):
    if type(b)!=int:
        raise TypeError
    if b==0:
        return a
    if a==0:
        return b
    if b<0:
        a=-a
        b=-b
    while b>0:
        rr=b
        q=a//b
        r=a%b
        a=b
        b=r
    return rr

def forkorta(a,b):
    sgd=sgdEuklides(a,b)
    return a//sgd,b//sgd

def kvadratrotRat(a,p,q):
    p1=p2=p
    q1=q2=q
    while q1<last or q2<last:
        (p1,q1)=forkorta(p1**2+a*q1**2,2*p1*q1)
        (p2,q2)=forkorta(p2+a*q2,p2+q2)
        r1=p1//q1+(p1%q1)/q1
        r2=p2//q2+(p2%q2)/q2
        print('{}/{} \u2248 {}; {}/{} \u2248 {}'.format(p1,q1,r1,p2,q2,r2))
        if q2<last: plotta(q2,r2,'red',win)
        if q1<last: plotta(q1,r1,'blue',win)


a=4
r=math.sqrt(a)

win=graphics.GraphWin('',1000,600)
last=3000
win.setCoords(0,r-1e-2,last,r+1e-2)


for q in range(1,last):
    p=int(r*q)
    if r-p/q>(p+1)/q-r:
        p=p+1
    print('{}/{} \u2248 {}, {}'.format(p,q,p/q, p/q-r))
    plotta(q,p/q,'black',win)
kvadratrotRat(a,5,2)

l=graphics.Line(graphics.Point(0,r),graphics.Point(last,r))
l.setOutline('green')
l.draw(win)
