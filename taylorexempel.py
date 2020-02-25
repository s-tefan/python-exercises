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

def drawline(win,px,py,qx,qy,color='black',width=1):
    linje=graphics.Line(graphics.Point(px,py),graphics.Point(qx,qy))
    linje.setWidth(width)
    linje.setOutline(color)
    linje.draw(win)

def plotpointlist(win,plist,color='black',width=1):
    firstpoint=True
    for p in plist:
        if firstpoint:
            p0=p
            firstpoint=False
        else:
            drawline(win,p0[0],p0[1],p[0],p[1],color=color,width=width)
            p0=p

def plotcoordlists(win,xlist,ylist,**kwargs):
    plist=[]
    for k in range(len(xlist)):
        plist.append((xlist[k],ylist[k]))
    plotpointlist(win,plist,**kwargs)

def xaxis(win,y=0,color='grey',ticks=1,subticks=0.5):
    xlow=win.trans.xbase
    xhigh=xlow+win.trans.xscale*win.width
    linje=graphics.Line(graphics.Point(xlow,y),graphics.Point(xhigh,y))
    linje.setOutline(color)
    linje.draw(win)
    tickx=xlow+subticks-xlow%subticks 
    while subticks>0 and tickx<xhigh:
        tick=graphics.Line(\
            graphics.Point(tickx,y-2*win.trans.yscale),\
            graphics.Point(tickx,y+2*win.trans.yscale))
        tick.setOutline(color)
        tick.draw(win)
        tickx+=subticks
    tickx=xlow+ticks-xlow%ticks 
    while ticks>0 and tickx<xhigh:
        tick=graphics.Line(\
            graphics.Point(tickx,y-4*win.trans.yscale),\
            graphics.Point(tickx,y+4*win.trans.yscale))
        tick.setOutline(color)
        tick.draw(win)
        tickx+=ticks

def yaxis(win,x=0,color='grey',ticks=1,subticks=0.5):
    yhigh=win.trans.ybase
    ylow=yhigh-win.trans.yscale*win.height
    #print(ylow,yhigh)
    linje=graphics.Line(graphics.Point(x,ylow),graphics.Point(x,yhigh))
    linje.setOutline(color)
    #print(linje)
    linje.draw(win)
    ticky=ylow+ticks-ylow%subticks 
    #print(ticky)
    while subticks>0 and ticky<yhigh:
        tick=graphics.Line(\
            graphics.Point(x-2*win.trans.xscale,ticky),\
            graphics.Point(x+2*win.trans.xscale,ticky))
        tick.setOutline(color)
        tick.draw(win)
        #print(ticky)
        ticky+=subticks
    ticky=ylow+ticks-ylow%ticks 
    #print(ticky)
    while ticks>0 and ticky<yhigh:
        tick=graphics.Line(\
            graphics.Point(x-4*win.trans.xscale,ticky),\
            graphics.Point(x+4*win.trans.xscale,ticky))
        tick.setOutline(color)
        tick.draw(win)
        #print(ticky)
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


def sin_coeffs(deg):
    clist = []
    for n in range(deg+1):
        if n%2 == 0:
            clist.append(0)
        elif n == 1:
            clist.append(1)
        else:
            clist.append(-clist[-2]/(n*(n-1)))
    return clist


def sinint_coeffs(deg):
    clist = []
    for n in range(deg+1):
        if n%2 == 0:
            clist.append(0)
        elif n == 1:
            clist.append(1)
        else:
            clist.append(-clist[-2]*(n-2)/(n*n*(n-1)))
    return clist

def geometric_coeffs(deg):
    return [1]*(deg+1)


def derivative(clist):
    dclist = []
    for n in range(1,len(clist)):
        dclist.append(n*clist[n])
    return dclist

def integral(clist):
    iclist = [0]
    for n in range(len(clist)):
        iclist.append(clist[n]/(n+1))
    return iclist

def maclaurin(clist, x):
    if len(clist) == 0:
        return 0
    elif len(clist) == 1: # not really needed
        return clist[0]
    else:
        return clist[0] + x*maclaurin(clist[1:],x)

def main():
    ## TEST
    import math
    
    clist = sin_coeffs(50)
    clist2 = clist[1:] # skip constant term, divide by x
    clist3 = integral(clist2)
    clist_sini = sinint_coeffs(20)
    
    xlist=[2*math.pi*n/100 for n in range(500)]
    ylist3=[maclaurin(clist3, x) for x in xlist]
    ylist4=[maclaurin(clist3, x) for x in xlist]


    win=graphingwin(-0.7,2*math.pi*5,-2,5,xres=800,equal=True)
    xaxis(win,ticks=math.pi/6,y=0)
    xaxis(win,ticks=1,y=-1)
    yaxis(win,x=0,ticks=0.2)
    grid(win,xdist=math.pi/3)
    plotcoordlists(win,xlist,ylist3,color='green')
    plotcoordlists(win,xlist,ylist4,color='blue')

    xlist_geom = [-2+4*k/200 for k in range(200)]
    ylist_geom = [maclaurin(geometric_coeffs(50),x) for x in xlist_geom]
    ylist_geom_i = [(maclaurin(geometric_coeffs(50),x*1j)).real for x in xlist_geom]
    win2=graphingwin(-2,2,-4,4,xres=800,equal=True)
    xaxis(win2,ticks=0.2,y=-1)
    yaxis(win2,x=0,ticks=0.2)
    grid(win2,xdist=1)
    plotcoordlists(win2,xlist_geom,ylist_geom,color='green')
    plotcoordlists(win2,xlist_geom,ylist_geom_i,color='blue')




    win.getMouse() # pause for click in window
    win.close()

main()