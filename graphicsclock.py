# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 13:07:19 2019

@author: kale
"""

from graphics import *
import time
from datetime import datetime

def pointcnum(z,origin=Point(60,60),radius=50):
    return Point((origin.getX()+radius*z.imag),(origin.getX()-radius*z.real))
    

def drawface(wi):
    w=(-1)**(1/6)
    for k in range(12):
        pt=pointcnum(w**k)
        pt.draw(wi)

def stopwatch():
    w=(-1)**(1/30)
    z=1
    win=GraphWin('',120,120)
    orig=pointcnum(0)
    drawface(win)
    print("Click in the window to close it")
    while not win.checkMouse():
        pt=pointcnum(z)
        secondhand=Line(orig,pt)
        secondhand.draw(win)
        #time.sleep(1)
        update(1)
        #secondhand.undraw()
        z*=w
    win.close()
        
def clock():
    orig=Point(60,60)
    sechandlelength=50
    minhandlelength=50
    hourhandlelength=30
    w=(-1)**(1/30)
    win=GraphWin('',120,140)
    drawface(win)
    print("Click in the window to close the clock")
    while not win.checkMouse():
        nu=datetime.now()
        hourz=w**(5*(nu.hour%12))
        minz=w**(nu.minute)
        secz=w**(nu.second)
        hourpt=pointcnum(hourz,orig,hourhandlelength)
        minpt=pointcnum(minz,orig,minhandlelength)
        secpt=pointcnum(secz,orig,sechandlelength)
        hourline=Line(orig,hourpt)
        minline=Line(orig,minpt)
        secline=Line(orig,secpt)
        dig=Text(Point(60,130),nu.strftime("%H:%M:%S"))
        dig.draw(win)
        hourline.setOutline('black')
        hourline.setWidth(3)
        minline.setOutline('black')
        minline.setWidth(3)
        secline.setOutline('red')
        secline.setWidth(2)
        hourline.draw(win)
        minline.draw(win)
        secline.draw(win)
        #time.sleep(1)
        update(1)
        print(nu)
        hourline.undraw()
        minline.undraw()
        secline.undraw()
        dig.undraw()
    win.close()