from cmath import exp,pi,phase
from math import sqrt
sh=sqrt(1/2)
def fft(samp,k):
    nn=len(samp)
    if nn==0:
        return 0
    elif nn==1:
        return samp[0]
    else:
        s=[]
        twiddle=exp(-2*pi*1j*k/nn)
        e=fft(samp[0::2],k)
        o=fft(samp[1::2],k)
        return e+twiddle*o

def fft2(samp):
    nn=len(samp)
    if nn==0:
        return 0
    elif nn==1:
        return samp[0]
    else:
        f=[]
        for k in range(nn):
            s=[]
            twiddle=exp(-2*pi*1j*k/nn)
            e=fft(samp[0::2],k)
            o=fft(samp[1::2],k)
            f.append(e+twiddle*o)
        return f

def ditfft2(x):      #  DFT of (x0, xs, x2s, ..., x(N-1)s):
    N=len(x)
    if N == 1:
        return [x[0]]       #  trivial size-1 DFT base case
    else:
        fx=ditfft2(x[0::2])+ditfft2(x[1::2])
        for k in range(N//2):   # combine DFTs of two halves into full DFT
            t = fx[k]
            twiddle=exp(-2*pi*1j*k/N)
            fx[k] = t + twiddle *fx[k+N//2]
            fx[k+N//2] = t - twiddle*fx[k+N//2]
        return fx

def grej0():
    for k in range(8):
        print(fft([0,sh,1,sh,0,-sh,-1,-sh],k))

    print(ditfft2([0,sh,1,sh,0,-sh,-1,-sh]))   
                        
        
    for k in range(8):
        print(fft([0,1,0,-1,0,1,0,-1],k))

    print(ditfft2([0,1,0,-1,0,1,0,-1]))


def grej1():
    import time
    tstart = time.time()
    print(ditfft2([1+2*(x%2) for x in range(256)]))
    tend = time.time()
    print(tend - tstart)
    tstart = time.time()

    tstart = time.time()
    print(fft2([1+2*(x%2) for x in range(256)]))
    tend = time.time()
    print(tend - tstart)
    tstart = time.time()

    ## f=[]
    ##for k in range(256):
    ##    f.append(    fft([1+2*(x%2) for x in range(256)],k))
    ##print(f)
    ##tend = time.time()
    ##print(tend - tstart)

def grej2(n):
    x=[2*(k//(n/2))-1 for k in range(n)]
    f=ditfft2(x)
    return x,f

def main():
    import grafritare
    n=256
    nn=range(n)
    x,f=grej2(n)
    print('brupp',x,f)
    gw=grafritare.graphingwin(0,n,-pi,pi)
    grafritare.grid(gw)
    grafritare.plotcoordlists(gw,nn,x,color='green',width=5)
    grafritare.plotcoordlists(gw,nn,[abs(a)/n for a in f],color='blue')
    grafritare.plotcoordlists(gw,nn,[phase(a) for a in f],color='red')
    

if __name__ == "__main__":
    # execute only if run as a script
    main()
