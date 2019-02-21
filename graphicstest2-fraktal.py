from graphics import *
import math


class MyPolygon(Polygon):
    def rotate(self,x0,y0,th):
        for p in self.points:
            x=p.x
            y=p.y
            rx=x-x0
            ry=y-y0
            c=math.cos(th)
            s=math.sin(th)
            dx=(c-1)*rx-s*ry
            dy=s*rx+(c-1)*ry
            p.move(dx,dy)
            print(x,y,rx,ry,c,s,dx,dy)
        if self.canvas:
            try:
                self.draw(self.canvas)
            except GraphicsError:
                w=self.canvas
                self.undraw()
                self.draw(w)

    def scale(self,x0,y0,sf):
        for p in self.points:
            x=p.x
            y=p.y
            rx=x-x0
            ry=y-y0
            dx=(sf-1)*rx
            dy=(sf-1)*ry
            p.move(dx,dy)
        if self.canvas:
            try:
                self.draw(self.canvas)
            except GraphicsError:
                w=self.canvas
                self.undraw()
                self.draw(w)

    def clone(self):
        other = MyPolygon(*self.points)
        other.config = self.config.copy()
        return other

class MyTrinaryFractal:
    a=0.62

    def pointOnLineBetween(p1,p2,t):
        '''Returns a point p1+t(p2-p1).'''
        q=p1.clone()
        q.x+=t*(p2.x-p1.x)
        q.y+=t*(p2.y-p1.y)
        return q

    def expandTriangleByCorner(p0,p1,p2):
        '''This should take a triangle and expand a corners with another triangle,
        scaled by a factor a.'''
        ## fixa till punkter
        a=MyTrinaryFractal.a
        q1=MyTrinaryFractal.pointOnLineBetween(p0,p1,-a)
        q2=MyTrinaryFractal.pointOnLineBetween(p0,p2,-a)
        return (p0,q1,q2)
        
        
        
   
win=GraphWin("apa",800,800)
win.setCoords(-4,-4,4,4)


a=0.8
b=math.sqrt(3)/2

r=1
points=[Point(0,r),Point(b*r,-0.5*r),Point(-b*r,-0.5*r)]
t=MyPolygon(points)
t.setFill('red')
t.draw(win)
tcenter=(0,0)

for k in [0,1,2]:
    Text(t.points[k],'{}'.format(k)).draw(win)

'''
tl=[t.clone(),t.clone(),t.clone()]
tlcolors=['blue','green','yellow']


for k in range(len(tl)):
    tl[k].setFill(tlcolors[k])
    rot=math.pi+k*2*math.pi/3
    tl[k].rotate(*tcenter,rot)
    tl[k].scale(*tcenter,a)
    tl[k].move(r*(1+a)*math.sin(rot),-r*(1+a)*math.cos(rot))
    tl[k].draw(win)
'''

tlist=[]
for k in range(3):
    plist=t.points[k:]+t.points[:k]
    tt=MyPolygon(*MyTrinaryFractal.expandTriangleByCorner(*plist))
    tt.setFill('black')
    tt.draw(win)
    tlist.append(tt)
    for m in [1,2]:
        Text(tt.points[m],'{}{}'.format(m,k)).draw(win)

    

for n in range(10):
    tlist2=[]
    for t in tlist:
        for k in [1,2]:
            plist=t.points[k:]+t.points[:k]
            tt=MyPolygon(*MyTrinaryFractal.expandTriangleByCorner(*plist))
            tt.setFill('yellow')
            tt.draw(win)
            tlist2.append(tt)
    tlist=tlist2


        




####n=100
####for k in range(n):
##
##print("Klicka i fönstret för att fortsätta.")
##win.getMouse() # Pause to view result
##
##t.move(0,1)
##
##print("Klicka i fönstret för att fortsätta.")
##win.getMouse() # Pause to view result
##
##t.rotate(0,1,math.pi/6)
##
#### t uppdateras inte men det funkar om man släcker och tänder
###t.undraw()
###t.draw(win)
####klonen blir roterad
####t2=t.clone()
####t2.setFill('green')
####t2.draw(win)
##
##print("Klicka i fönstret för att fortsätta.")
##win.getMouse() # Pause to view result
##
##t.scale(0,1,0.8)
##
##print("Klicka i fönstret för att fortsätta.")
##win.getMouse() # Pause to view result
##
##t.move(-1,0)
##
##
##
##print("Klicka i fönstret för att fortsätta.")
##win.getMouse() # Pause to view result
##
##t.move(-1,0)
##
##


print("Klicka i fönstret för att avsluta.")
win.getMouse() # Pause to view result
win.close()    # Close window when done
