import math
def cantor(x,nmax=10):
    ip=math.floor(x)
    d=x%1
    y=ip
    n=0
    b=True
    while b:
        n+=1
        if n>nmax: b=False
        m=int(3*d)
        d=(3*d)%1
        if m==1 or (m==2 and d==0):
            a=1
            b=False
        elif m==0:
            a=0
        else:
            a=1
        y+=2**(-n)*a
    return y

def graphics_zelle(l):
  import graphics
  sc=600
  win=graphics.GraphWin("Cantorkurva",sc,sc)
  win.setCoords(0,0,1,1)
  pl=[]
  for p in l:
    pl.append(graphics.Point(p[0],p[1]))
  poly=graphics.Polygon(pl)
  poly.draw(win)


def plotcantor(nmax):
    m=3**nmax
    kr=range(m)
    d=1/m
    xyl=[]
    for k in kr:
        x=k*d
        xyl.append((x,cantor(x,nmax)))
    graphics_zelle(xyl)
        
