
def hilbertbas(t):
    # Avbildar [0,1] in i [-1/2,1/2]^2
    if t<=0: x = -1/4+3/2*t; y = 1/4
    elif t<=1/3: x = -1/4; y = 1/4 - 3/2*t
    elif t<=2/3: x = -3/4 + 3/2*t; y = -1/4
    elif t<=1: x = 1/4; y = -5/4 + 3/2*t
    else: x = 1/4+3/2*(t-1); y = 1/4
    return (x,y)

def transform(x,y,n):
    if n==0: x1,y1 = -y/2 - 1/4, -x/2 + 1/4
    elif n==1: x1,y1 = x/2 - 1/4, y/2 - 1/4
    elif n==2: x1,y1 = x/2 + 1/4, y/2 - 1/4
    elif n==3: x1,y1 = y/2 + 1/4, x/2 + 1/4
    elif n==-1: x1,y1 = x, y
    return x1,y1

def hilbertett(t):
    if t<=0: x,y = -3/8, 3/8
    elif t<=4/15: x,y = transform(*hilbertbas(5*t),0)
    #elif t<=4/15: x,y = transform(3/4 + (15*t-3)*3/4,3/4,0)
    elif t<=8/15: x,y = transform(*hilbertbas(5*t-4/3),1)
    #elif t<=8/15: x,y = transform(3/4 + (15*t-3)*3/4, 3/4, 1) 
    elif t<=11/15: x,y = transform(*hilbertbas(5*t-8/3),2)
    #elif t<=12/15: x,y = transform(3/4 + (15*t-3)*3/4, 3/4, -1)
    elif t<=15/15: x,y = transform(*hilbertbas(5*t-12/3),3)
    else: x,y = 3/8, 3/8
    return x,y

def hilbertf(t,n):
    # rekursivt ersätter kvadranter med kopior av "sig själv"
    # plus förbindelser mellan
    # denna implementation har förljande egenskaper:
    # + diskretisering av kontinuerlig funktion
    # - "låg hastighet" i förbindelserna högt i hierarkin
    if n<=0: return hilbertbas(t)
    else:
        if t<=0: x,y = -1/2+1/4/2**n, 1/2-1/4/2**n
        elif t<=3/15: x,y = transform(*hilbertf(5*t,n-1),0)
        elif t<=4/15: x,y = -1/2+1/4/2**n, 1/4/2**n - (15*t-3)/2/2**n
        elif t<=7/15: x,y = transform(*hilbertf(5*t-4/3,n-1),1)
        elif t<=8/15: x,y = -1/4/2**n + (15*t-7)/2/2**n, -1/4/2**n
        elif t<=11/15: x,y = transform(*hilbertf(5*t-8/3,n-1),2)
        elif t<=12/15: x,y = 1/2-1/4/2**n, -1/4/2**n + (15*t-11)/2/2**n
        elif t<=1: x,y = transform(*hilbertf(5*t-4,n-1),3)
        else: x,y = 1/2-1/4/2**n, 1/2-1/4/2**n
        return x,y

def hilbertff(t,n):
    # rekursivt ersätter kvadranter med kopior av "sig själv"
    # plus förbindelser mellan
    # nackdel i aktuell implementation:
    # - diskontinuerlig i "förbindelserna"
    # + direkta hopp i förbindelserna högt
    # funkar för plottning
    ### Problem: Tappar punkter
    if n<=0: return hilbertbas(t)
    else:
        #if t<=0: x,y = -1/2+1/4/2**n, 1/2-1/4/2**n
        if t<=1/4: x,y = transform(*hilbertfd(4*t,n-1),0)
        elif t<=1/2: x,y = transform(*hilbertfd(4*t-1,n-1),1)
        elif t<=3/4: x,y = transform(*hilbertfd(4*t-2,n-1),2)
        else: x,y=transform(*hilbertfd(4*t-3,n-1),3)
#        elif t<=1: x,y = transform(*hilbertfd(4*t-3,n-1),3)
#        else: x,y = 1/2-1/4/2**n, 1/2-1/4/2**n
        return x,y

def hilbertfd(l):
    # diskret version
    ll=[]
    for k in range(4):
        for p in l:
            ll.append(transform(*p,k))
    return ll
            

    
def graphics_zelle():
  sc=800
  win=g.GraphWin("Hilbertkurva",sc,sc)
  win.setCoords(-1/2,-1/2,1/2,1/2)
  m=1
  #n=3*5**m
  #n=4*4**m
  n=12
  x0,y0=hilbertf(0,m)
  #x0,y0=hilbertett(0)
  for k in range(n-1):
    t=(k+1)/(n)
    x,y=hilbertf(t,m)
    #x,y=hilbertett(t)
    #print(x,y)
    g.Line(g.Point(x0,y0),g.Point(x,y)).draw(win)
    x0,y0=x,y

def rita_diskret(n):
    sc=1024
    win=g.GraphWin("Hilbertkurva",sc,sc)
    win.setCoords(-1/2,-1/2,1/2,1/2)
    l=[(-1/4,1/4),(-1/4,-1/4),(1/4,-1/4),(1/4,1/4)]
    for k in range(n):
        l=hilbertfd(l)
    p0=l[0]
    for p in l[1:]:
        g.Line(g.Point(*p0),g.Point(*p)).draw(win)
        p0=p


import graphics as g

#graphics_zelle()
rita_diskret(7)



def blaha():
    sc=800
    win=g.GraphWin("Hilbertkurva",sc,sc)
    win.setCoords(-1/2,-1/2,1/2,1/2)
    x0,y0=-3/8,3/8
    for t in [k/100 for k in range(-20,120)]:
        #x,y=hilbertf(t,m)
        x,y=hilbertbas(t)
        print(x,y)
        g.Line(g.Point(x0,y0),g.Point(x,y)).draw(win)
        x0,y0=x,y
        
