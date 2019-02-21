import graphics, math

def plottalistor(xlist,ylist,win,color='black'):
    xmin=min(xlist)
    xmax=max(xlist)
    ymin=min(ylist)
    ymax=max(ylist)
    #w=win.getWidth()
    #h=win.getHeight()
    win.setCoords(xmin,ymin,xmax,ymax)
    x0,y0=xlist[0],ylist[0]
    for n in range(1,len(xlist)):
        x1,y1 = xlist[n],ylist[n]
        xs0,ys0 = win.toScreen(x0,y0)
        xs1,ys1 = win.toScreen(x1,y1)
        dx,dy = x1-x0, y1-y0
        dxs,dys = xs1-xs0,ys1-ys0
        steps=max(abs(dxs),abs(dys))
        for k in range(0,steps):
            x,y = x0+dx*k/steps, y0+dy*k/steps
            win.plot(x,y,color)
        x0,y0=x1,y1

ints=100
xl=[j*2*2*math.pi/ints for j in list(range(ints+1))]
yl=[math.sin(x) for x in xl]
print(xl)
print(yl)
win=graphics.GraphWin('x:[{:0.2f},{:0.2f}], y:[{:0.2f},{:0.2f}]'\
                      .format(min(xl),max(xl),min(yl),max(yl)),\
                      600, 400)
plottalistor(xl,yl,win)


