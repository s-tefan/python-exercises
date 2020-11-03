import random
import math
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#fig = plt.figure(figsize=(15,15))
#ax = plt.axes((-2,-2,2,2))

fig, ax = plt.subplots()
ax.set_aspect(1)
ax.set_xlim(-2,2)
ax.set_ylim(-2,2)

x, y = [], []

#om1, om2 = 3, 11
om1, om2 = 2, 4
a, b = 1, 0.2


#index= count()
n = 1000
index = iter(range(n))  
def animate(i):
    k = (next(index))
    t = math.pi*k/n
    c, s = math.cos(om1*t), math.sin(om1*t)
    x.append(c*a*math.cos(om2*t)-s*b*math.sin(om2*t))
    y.append(s*a*math.cos(om2*t)+c*b*math.sin(om2*t))
    #plt.style.use("ggplot")    
    #ax.plot(x,y)

while index: 
    try:
        animate(0)
    except StopIteration:
        break
    pass

plt.style.use("ggplot")    
ax.plot(x,y)


#ani = FuncAnimation(fig, animate, interval=10)
plt.show()
