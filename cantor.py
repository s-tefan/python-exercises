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
  sc=1000
  win=graphics.GraphWin("Cantorkurva",sc,sc)
  win.setCoords(0,0,1,1)
  pl=[]
  for p in l:
    pl.append(graphics.Point(p[0],p[1]))
  poly=graphics.Polygon(pl)
  poly.setFill('white')
  poly.draw(win)
  return win


def plotcantor(nmax):
    m=3**nmax
    kr=range(m)
    d=1/m
    xyl=[]
    for k in kr:
        x=k*d
        xyl.append((x,cantor(x,nmax)))
    graphics_zelle(xyl)
        
def cantorlist(n):
    clist=[]
    for k in range(2**n):
        fs='{:0'+str(n)+'b}'
        s=fs.format(k) # binary repr. of k with n bits
        t1=0
        t2=0
        b=0
        flag=False # this flag is False when there are just zeros trailing after the current bit
        for bit in s[::-1]: # traverse s backwords (lsb first)
            if flag:
                if bit=='1':
                    t1=t1+2
                    t2=t2+2
                    b=b+1
            else:
                if bit=='1':
                    t1=1
                    t2=2
                    b=b+1
                    flag=True
            t1=t1/3
            t2=t2/3
            b=b/2
        if k:
            clist.append((t1,b))
        clist.append((t2,b))
    clist.append((1.0,1.0))
    return clist

cl=cantorlist(10)
print(cl)
graphics_zelle(cl+[(1.0,0.0)])
input('---')
