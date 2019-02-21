def kvadratrotNRstep(a,x):
    '''Ett steg i approximationen av kvadratroten till a med Newton Raphson.
    x -> x-(x^2-a)/(2x) = (x+2/x)/2.''' 
    return (x+a/x)/2

def kvadratrot2step(a,x):
    '''Ett steg i approximationen av kvadratroten till a med metoden som utnyttjar fixpunkts formeln
    x = 1 + (a-1)/(1+x) = (a+x)/(1+x)'''
    return (a+x)/(1+x)


def test0():
    x1=1
    x2=1
    a=10
    print('Beräkning av kvadroten till {}'.format(a))
    print('{:16} {:16}'.format('N-R','Konjugat'))
    print('{:01.15f} {:01.15f}'.format(x1,x2))
    for n in range(20):
        x1=kvadratrotNRstep(a,x1)
        x2=kvadratrot2step(a,x2)
        print('{:01.15f} {:01.15f}'.format(x1,x2))

def test1(a):
    tol=0.5e-15
    x1=1
    x2=1
    print('{:16} {:16}'.format('N-R','Konjugat'))
    print('{:01.15f} {:01.15f}'.format(x1,x2))
    while abs(x1-a/x1)>tol: # f(x1) ~ (x1-x0)f'(x1)
        x1=kvadratrotNRstep(a,x1)
        x2=kvadratrot2step(a,x2)
        print('{:01.15f} {:01.15f}'.format(x1,x2))

def test2(a,tol=0.5e-12):
    x1=1
    x2=1
    print('{:16} {:16}'.format('N-R','Konjugat'))
    print('{:01.15f} {:01.15f}'.format(x1,x2))
    while abs(x1-a/x1)>tol: # f(x1) ~ (x1-x0)f'(x1)
        x1=kvadratrotNRstep(a,x1)
        print('{:01.15f} {:01.15f}'.format(x1,x2))

    
def NRrek(a,x0,tol=0.5e-12):
    x=x0
    print(x)
    if abs(x-a/x)<2*tol: # f(x) ~ (x-x0)f'(x)
        return x
    else:
        return NRrek(a,kvadratrotNRstep(a,x))
        
def test2(a,tol=0.5e-12):
    print('Beräkning av kvadratroten till {} med rekursiv N-R.'.format(a))
    NRrek(a,1,tol)

def sgdEuklides(a,b):
    if type(b)!=int:
        raise TypeError
    if b==0:
        return a
    if a==0:
        return b
    if b<0:
        a=-a
        b=-b
    while b>0:
        rr=b
        q=a//b
        r=a%b
        a=b
        b=r
    return rr

def forkorta(a,b):
    sgd=sgdEuklides(a,b)
    return a//sgd,b//sgd

def kvadratrotRat(a,p,q):
    p1=p2=p
    q1=q2=q
    #while ...:
    for _ in range(10):
        (p1,q1)=forkorta(p1**2+a*q1**2,2*p1*q1)
        (p2,q2)=forkorta(p2+a*q2,p2+q2)
        print('{}/{} \u2248 {}; {}/{} \u2248 {}'.format(p1,q1,p1/q1,p2,q2,p2/q2))
    

kvadratrotRat(2,1,1)

test1(10)
test2(10000000)
test2(10,0.5e-15)
print('{:0.15f}'.format(NRrek(10,1,.5e-15)))
