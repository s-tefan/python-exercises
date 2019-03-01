from time import time

def eratosthenes1(n):
    nl=list(range(2,n+1))
    pl=[]
    while nl:
        p=nl.pop(0)
        pl.append(p)
        psq=p**2
        for k in range(len(nl)):
            if nl[k]>=psq:
                if nl[k]%p==0:
                    nl[k]=0
        nl=[x for x in nl if x!=0]
    return pl

def eratosthenes2(n):
    nl=list(range(2,n+1))
    pl=[]
    while nl:
        p=nl.pop(0)
        pl.append(p)
        pp=p*p
        k=0
        while k < len(nl):
            try:
                while nl[k]<pp:
                    k+=1
                if nl[k]==pp:
                    nl[k]=0
                pp+=p
            except IndexError:
                pass
        nl=[x for x in nl if x!=0]
    return pl

class Prime_iterator:
    def __init__(self):
        self.plist=[2]

    def __iter__(self):
        return self

    def next(self):
        n0=n=self.plist[-1]
        n0sq=n0**2
        ndivisiblebyprime=True
        while ndivisiblebyprime:
            n+=1
            ndivisiblebyprime=False
            for p in self.plist:
                if n%p==0:
                    ndivisiblebyprime=True
                    break
        self.plist.append(n)
        return n

pi=Prime_iterator()
t00=t000=time()
for k in range(10000):
    pi.next()
    t01=time()
#    print(pi.next(),t01-t00)
    t00=t01
plast=pi.next()
print(plast)
t01=time()
print(t01-t000)

n=plast
t0=time()
plist1=eratosthenes1(n)
print(len(plist1),plist1)
t1=time()
print(t1-t0)
plist2=eratosthenes2(n)
print(len(plist2),plist2)
t2=time()
print(t2-t1)
