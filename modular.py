# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 10:07:55 2019

@author: kale
"""

def binlistlsbf(a):
    #returns a list of binary digits, LSB first
    bl=[]
    while a>0:
        r=a%2
        q=a//2
        bl.append(r)
        a=q
    return bl


def modexp(a,e,n):
    bl=binlistlsbf(e)
    sqs=[a]
    prod=1
    for b in bl:
        oldsq=sqs[-1]
        newsq=(oldsq**2)%n
        sqs.append(newsq)
        if b: prod*=oldsq
        prod=prod%n
    return prod
    
def euklides(a,b,verbose=True):
#    m=max(a,b)
#    d=min(a,b)
    m,d=a,b
    quotientlist=[]
    remainderlist=[]
    while d>0:
        r=m%d
        if r<=0: break
        q=m//d
        quotientlist.append(q)
        remainderlist.append(r)
        if verbose: print('{m} = {q}*{d} + {r}'.format(m=m,q=q,d=d,r=r))
        m,d=d,r
    return quotientlist,remainderlist



def rsaexempel():
    p=31
    q=47
    n=p*q
    phi=(p-1)*(q-1)
    e=7

#ql,rl=euklides(e,phi)



def diosolve(qlist, verbose=False):
    nn=len(qlist)
    v=[]
    for k in range(nn):
        v.append([-1,qlist[k],1])
    if verbose: print('v = ',v)
    u=v[-1]
    for k in range(1,nn):
        c=u[1]
        if verbose: print('u = {u}, v[{k}] = {vk}, c={c}'.format(u=u,k=nn-k-1,vk=v[nn-k-1],c=c))
        u=[0]+u
        for j in range(3):
            if verbose: print(j)
            u[j]-= c*v[nn-k-1][j]
        if verbose: print('u = ',u)    
    return u

def diosolvewrap(a,b, verbose=True):
    #m,d=max(a,b),min(a,b)
    m,d=a,b
    ql,rl=euklides(m,d)
    if m%d:
        ul=diosolve(ql)
        x=-ul[0]
        y=-ul[1]
        r=rl[-1]
    else:
        x=0
        y=1
        r=d
    if verbose: print('{x}*{m}+{y}*{d}={r}'.format(x=x,y=y,m=m,d=d,r=r))
    return x,y,r
    
    
    
