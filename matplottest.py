# -*- coding: utf-8 -*-
"""
Created on Fri May 31 14:55:55 2019

@author: kale
"""

from numpy import *
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

x=arange(0,pi,pi/100)
y=sin(x)
fig,ax=plt.subplots()
ax.plot(x,y)
ax.grid()
plt.show()