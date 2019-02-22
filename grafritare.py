import graphics # Kräver John Zelles modul graphics.py
# http://mcsp.wartburg.edu/zelle/python/graphics.py


def graphingwin(xmin,xmax,ymin,ymax,xres=800,yres=800,equal=False):
    if equal==True:
        yres=int((ymax-ymin)/(xmax-xmin)*yres)
    win=graphics.GraphWin("apa",xres,yres)
    win.setCoords(xmin,ymin,xmax,ymax)
    return win

def graphingwin2(xrange,yrange,**kwargs):
    return graphingwin(xrange[0],yrange[1],yr[0],yr[1],**kwargs)

def drawline(win,px,py,qx,qy,color='black'):
    linje=graphics.Line(graphics.Point(px,py),graphics.Point(qx,qy))
    linje.setOutline(color)
    linje.draw(win)

def plotpointlist(win,plist,color='black'):
    firstpoint=True
    for p in plist:
        if firstpoint:
            p0=p
            firstpoint=False
        else:
            drawline(win,p0[0],p0[1],p[0],p[1],color=color)
            p0=p

def plotcoordlists(win,xlist,ylist,**kwargs):
    plist=[]
    for k in range(len(xlist)):
        plist.append((xlist[k],ylist[k]))
    plotpointlist(win,plist,**kwargs)

def xaxis(win,y=0,color='grey',ticks=1):
    xlow=win.trans.xbase
    xhigh=xlow+win.trans.xscale*win.width
    linje=graphics.Line(graphics.Point(xlow,y),graphics.Point(xhigh,y))
    linje.setOutline(color)
    linje.draw(win)
    tickx=xlow+ticks-xlow%ticks 
    while tickx<xhigh:
        tick=graphics.Line(\
            graphics.Point(tickx,y-2*win.trans.yscale),\
            graphics.Point(tickx,y+2*win.trans.yscale))
        tick.setOutline(color)
        tick.draw(win)
        tickx+=ticks

def yaxis(win,x=0,color='grey',ticks=1):
    yhigh=win.trans.ybase
    ylow=yhigh-win.trans.yscale*win.height
    print(ylow,yhigh)
    linje=graphics.Line(graphics.Point(x,ylow),graphics.Point(x,yhigh))
    linje.setOutline(color)
    print(linje)
    linje.draw(win)
    ticky=ylow+ticks-ylow%ticks 
    print(ticky)
    while ticky<yhigh:
        tick=graphics.Line(\
            graphics.Point(x-2*win.trans.xscale,ticky),\
            graphics.Point(x+2*win.trans.xscale,ticky))
        tick.setOutline(color)
        tick.draw(win)
        print(ticky)
        ticky+=ticks

def grid(win,color='grey',xdist=1,ydist=1):
    xlow=win.trans.xbase
    xhigh=xlow+win.trans.xscale*win.width
    yhigh=win.trans.ybase
    ylow=yhigh-win.trans.yscale*win.height
    ticky=ylow+ydist-ylow%ydist
    tickx=xlow+xdist-xlow%xdist
    while tickx<xhigh:
        tick=graphics.Line(\
            graphics.Point(tickx,ylow),\
            graphics.Point(tickx,yhigh))
        tick.setOutline(color)
        tick.draw(win)
        tickx+=xdist
    while ticky<yhigh:
        tick=graphics.Line(\
            graphics.Point(xlow,ticky),\
            graphics.Point(xhigh,ticky))
        tick.setOutline(color)
        tick.draw(win)
        ticky+=ydist
    
## TEST
import math
xlist=[2*math.pi*n/100 for n in range(100)]
ylist=[math.sin(x) for x in xlist]
win=graphingwin(-0.7,2*math.pi,-2,2,xres=800,equal=True)
xaxis(win,ticks=math.pi/6,y=0)
xaxis(win,ticks=1,y=-1)
yaxis(win,x=0,ticks=0.2)
grid(win,xdist=math.pi/3)
plotcoordlists(win,xlist,ylist,color='green')

#win2=graphingwin(0,math.pi,-1,1,xres=800,equal=True)
#plotcoordlists(win2,xlist,ylist,color='green')

win.getMouse() # pause for click in window
win.close()
