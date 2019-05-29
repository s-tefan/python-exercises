# -*- coding: utf-8 -*-
"""
Created on Mon May 27 16:30:33 2019

@author: kale
"""

from IPython import display
import numpy

#svgheader='<svg version="1.1" height="{height}" width="{width}" xmlns="http://www.w3.org/2000/svg">'.format(height=100,width=100)
svgheader='<svg height="{height}" width="{width}">'.format(height=100,width=100)
svgfooter='</svg>'

def svgpolygon(listoftuples):
    svgpointlist=''
    for coords in listoftuples:
        svgpointlist+=(str(coords[0])+','+str(coords[1])+' ')
    stroke='black'
    fill='red'
    return '<polygon points="{sp}" style="fill:{fill};stroke:{stroke}"/>'.format(sp=svgpointlist,stroke=stroke,fill=fill)


def hommatrixfrompointlist(listoftuples):
    m=[]
    for coords in listoftuples:
        homvek=list(coords)+[1]
        m.append(homvek)
    return numpy.transpose(m)

def pointlistfromhommatrix(matrix):
    pl=[]
    m=numpy.transpose(matrix)
    for row in m:
        pl.append(tuple(row[:-1]))
    return pl

    
def rotmatrix2d(th):
    c,s=numpy.cos(th),numpy.sin(th)
    return [[c,-s,0],[s,c,0],[0,0,1]]

def transmatrix2d(trv):
    return [[1,0,trv[0]],[0,1,trv[1]],[0,0,1]]

def projmatrix2d(th):
    c,s=numpy.cos(th),numpy.sin(th)
    return [[c*c,c*s,0],[c*s,s*s,0],[0,0,1]]

def reflmatrix2d(th):
    c,s=numpy.cos(th),numpy.sin(th)
    return [[c*c-s*s,2*c*s,0],[2*c*s,s*s-c*c,0],[0,0,1]]

    
    


svg=svgheader+svgpolygon([(0,0),(100,100),(100,50)])+svgfooter

print(svg)

## rotera och translatera en figur
m=hommatrixfrompointlist([(0,0),(100,100),(100,50)])
rm=np.dot(transmatrix2d((100,0)),rotmatrix2d(np.pi/2))
p1=pointlistfromhommatrix(m)
p2=pointlistfromhommatrix(np.dot(rm,m))
pols=svgpolygon(p1)+svgpolygon(p2)
svgpols=svgheader+pols+svgfooter

# display verkar inte ge någon bild från script
display.SVG(svg)
apa='<svg height="210" width="500"><polygon points="200,10 250,190 160,210" style="fill:lime;stroke:purple;stroke-width:1" /></svg> '
ap='<svg height="150" version="1.1" width="170" xmlns="http://www.w3.org/2000/svg"><polygon fill="aqua" points="0,0 20,100 25,100 25,0" stroke="black"></polygon><polygon fill="blue" points="21,1 21,10 30,10 30,1" stroke="black"></polygon><polygon fill="fuchsia" points="30,10 30,50 70,50 70,10" stroke="black"></polygon><polygon fill="gray" points="70,50 70,150 170,150 170,50" stroke="black"></polygon></svg>'
display.SVG(ap)        
display.SVG(apa)        

    