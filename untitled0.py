# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 16:28:52 2019

@author: kale
"""

def myfak(n):
    f=1
    for k in range(1,n+1):
        f*=k
    return f

print(myfak(25))
        