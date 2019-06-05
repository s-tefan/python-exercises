def newtonv(f,x0,x1):
    x2=x1-f(x1)*(x1-x0)/(f(x1)-f(x0))
    return x2

x0=1
x1=1.2
#f=lambda x : x**2-2

f=lambda x: (x-2)*(x-3)*x

while abs(f(x1))>1e-10:
    x2=newtonv(f,x0,x1)
    x1,x0=x2,x1


print(x0,x1,f(x1))
