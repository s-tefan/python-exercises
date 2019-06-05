# -*- coding: utf-8 -*-
"""
Created on Wed May 29 16:24:59 2019

@author: kale
"""

from math import sqrt,cos,sin,pi


def tredela(tupellist):
    tredelatuple = lambda t : tuple(map(lambda x:x/3,t))
    return list(map(tredelatuple,tupellist))

def rotera(tupellist,th):
    roteratuple = lambda t: (cos(th)*t[0]-sin(th)*t[1],sin(th)*t[0]+cos(th)*t[1])
    return list(map(roteratuple,tupellist))

def translatera(tupellist,v):
    transtuple = lambda t: (t[0]+v[0],t[1]+v[1])
    return list(map(transtuple,tupellist))


def koch(n):
    a=sqrt(3)/6
    if n<=0:
        return [(1/3,0),(1/2,a),(2/3,0),(1,0)]
    else:
        return [] # Fyll i här
    
t=translatera(rotera(koch(0),pi/3),(1,0))
for pnt in t:
    print(pnt)
            
