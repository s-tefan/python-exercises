#import graphics # Kräver John Zelles modul graphics.py
# http://mcsp.wartburg.edu/zelle/python/graphics.py
import time
import random
import numpy
import matplotlib.pyplot as plt
import matplotlib






#xmin, xmax, ymin, ymax = -2,0.5,-1,1
#xmin, xmax, ymin, ymax = -0.8192,-0.818,0.189,0.19
#xmin, xmax, ymin, ymax = -1.75,-1.7,0,0.02

xc, yc = -0.75, 0.2
cwidth = 0.1

width = 1680
#height = int(width*(ymax-ymin)/(xmax-xmin))
height = 1050
#step = (xmax-xmin)/width

xmin = xc - cwidth/2
ymin = yc - height/width*cwidth/2
step = cwidth/width
delta = step*(1+1j)
xmax = xmin + width*step
ymax = ymin + height*step
cstart = xmin + ymin*1j
cstop = xmax + ymax*1j

nmax = 200


im_arr = numpy.zeros((height,width), dtype=int)
c_arr = numpy.zeros((height,width), dtype=complex)
z_arr = numpy.zeros((height,width), dtype=complex)
n_arr = numpy.zeros((height,width), dtype=int)
n = 0

for row in range(height):
    for column in range(width):
        c_arr[-row,column] = cstart + step*column + step*row*1j 


while n<nmax:
    n+=1
    print(n)
    z_arr = z_arr**2 + c_arr
    mask = abs(z_arr)<2
    #z_arr += mask*numpy.inf
    n_arr += mask


#apcmap = matplotlib.cm.get_cmap('pink', nmax)
apcmap = matplotlib.cm.get_cmap('summer', nmax)
newcolors = apcmap(numpy.linspace(0,1,nmax))
bl = numpy.array([0,0,0,1])
newcolors[0,:] = bl
newcmp = matplotlib.colors.ListedColormap(newcolors)

im_arr = nmax-n_arr
im = plt.imshow(im_arr, cmap=newcmp)
plt.show()



plt.imsave('mandel.png', im_arr, cmap=newcmp) 

'''
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
#from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(numpy.real(c_arr), numpy.imag(c_arr), numpy.real(z_arr), cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

ax.set_zlim(-2, 2)
plt.show()
'''