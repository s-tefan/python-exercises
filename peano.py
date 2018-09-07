def peano1(t):
  x = (t//(1/3)-1)/3
  y = ((9*t)//1%3-1)/3
  if t>=1/3 and t<2/3:
    y=-y
  return [x,y]

def peanosign(t):
  s=[1,1]
  if t>=1/3 and t<2/3:
    s[1]=-1
  if int(9*t//1%3-1)==0:
    s[0]=-1
  return s

def peano(t,n):
  if n>0:
    p=peano1(t)
    q=peano(9*t%1,n-1)
    s=peanosign(t)
    p[0]+=s[0]*q[0]/3
    p[1]+=s[1]*q[1]/3
    return p
  else:
    return peano1(t)

def peanogen(n,k):
    l=[]
    for i in range(n):
        t=1/(2*n)+i/n
        l+=[peano(t,k)]
    return l


def gnuplotexport(f,l):
    for p in l:
        f.write(str(p[0])+' '+str(p[1])+'\n')

def graphics_zelle(l):
  import graphics
  sc=800
  win=graphics.GraphWin("Peanokurva",sc,sc)
  win.setCoords(-sc/2,-sc/2,sc/2,sc/2)
  pl=[]
  for p in l:
    pl.append(graphics.Point(sc*p[0],sc*p[1]))
  poly=graphics.Polygon(pl)
  poly.draw(win)
    
d=5
l=peanogen(9**d*5,d-1)
#f=open('peanofil','w')
#gnuplotexport(f,l)
#f.close()'
print(len(l))
graphics_zelle(l)

