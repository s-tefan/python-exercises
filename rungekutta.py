# Runge Kutta


# exempelfunktion
def funk(t,y):
    k=1
    return k*y

def rk4step(f,s0,h):
    t0=s0[0]
    y0=s0[1]
    k1=h*f(t0,y0)
    k2=h*f(t0+h/2,y0+k1/2)
    k3=h*f(t0+h/2,y0+k2/2)
    k4=h*f(t0+h,y0+k3)
    t1=t0+h
    y1=y0+(k1+2*(k2+k3)+k4)/6
    return([t1,y1])

s1=rk4step(funk,[0,1],0.1)

s0=[0,1]
s=[s0]
for n in range(20):
    s.append(rk4step(funk,s[-1],0.1))
    print(s[-1])




    


