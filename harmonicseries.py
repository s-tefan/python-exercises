from grafritare import *

gw=graphingwin(0,100,-1,2)
xl,yl=[0],[0]
for k in range(1,101):
    xl.append(k)
    yl.append(yl[-1]-(-1)**k/k)
plotcoordlists(gw,xl,yl)
xaxis(gw,ticks=10,subticks=1)
yaxis(gw,ticks=0.5,subticks=0.1)

        
