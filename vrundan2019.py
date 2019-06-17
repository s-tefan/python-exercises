# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 10:34:59 2019

@author: kale
"""

import datetime as dt

class Lopp:
    dist=[0,47,83,104,133,171,204,225,242,257,274,297]
    namn=['Motala',
    'Ödeshög',
    'Ölmstad',
    'Jönköping',
    'Fagerhult',
    'Hjo',
    'Karlsborg',
    'Boviken',
    'Aspa',
    'Hammarsundet',
    'Medevi',
    'Motala'
    ]
    paus=len(dist)*[dt.timedelta()]
    
class Deltagare:
    namn=str()
    nummer=int()
    medelhastighetsprognos=23
    starttid=dt.datetime.today()
    lopp=Lopp()
    paus=lopp.paus.copy()

    def prognostid(self,i):
        dist=self.lopp.dist[i]
        cykeltid=dt.timedelta(hours=dist/self.medelhastighetsprognos)
        paustid=dt.timedelta()
        for k in range(i):
            paustid+=self.paus[k]
        tid=cykeltid+paustid
        return self.starttid+tid,self.starttid+tid+self.paus[i] 

    def skriv_prognostider(self):
        lopp=self.lopp
        for i in range(len(lopp.dist)):
            intid,uttid=self.prognostid(i)
            print('{:<12} {:%H:%M} {:%H:%M}'.format(lopp.namn[i],intid,uttid))
 
    def lista_prognostider(self):           
        lopp=self.lopp
        lista=[]
        for i in range(len(lopp.dist)):
            intid,uttid=self.prognostid(i)
            lista.append((lopp.dist[i],(intid,uttid)))
        return lista
    
    def dist_nu():
        pass
    
    


class Delsträcka:
    @staticmethod
    def nummer(lopp,i):
        a=Delsträcka
        a.distans=lopp.dist[i-1:i+1]
        a.orter=lopp.namn[i-1:i+1]
        return a
        

vr2019=Lopp
s=Deltagare()
s.namn='Sofie'
s.nummer=2029
s.starttid=dt.datetime(2019,6,14,20,20)
s.medelhastighetsprognos=23
s.paus[1]=dt.timedelta(minutes=10)
s.paus[2]=dt.timedelta(minutes=10)
s.paus[3]=dt.timedelta(minutes=20)
s.paus[4]=dt.timedelta(minutes=10)
s.paus[5]=dt.timedelta(minutes=20)
s.paus[6]=dt.timedelta(minutes=10)
s.paus[7]=dt.timedelta(minutes=10)
s.paus[9]=dt.timedelta(minutes=10)
s.paus[10]=dt.timedelta(minutes=10)

##from numpy import *
##import matplotlib.pyplot as plt
##import matplotlib.image as mpimg
##
##ll=s.lista_prognostider()
##x,y=[],[]
##for z in ll:
##    y.append(z[0])
##    y.append(z[0])
##    x.append((z[1][0]-s.starttid)/dt.timedelta(hours=1))
##    x.append((z[1][1]-s.starttid)/dt.timedelta(hours=1))
##fig,ax=plt.subplots()
##ax.plot(x,y)
##ax.grid()
##plt.show()
