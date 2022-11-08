def binarystring(x):
    if not(isinstance(x,int)):
        raise TypeError('Argument is not an integer')
    b=''
    s=''
    if x==0:
        return '0'
    elif x<0:
        s='-'
        x=-x
    while x>0:
        r=x%2
        x=x//2
        b=str(r)+b
    return s+b

for n in range(16):
    print(binarystring(n))

    
def binary_division(a,b):
    if a<0:
        if b<0:
            s=''
            b=-b
        else:
            s='-'
        a=-a
    else:
        if b<0:
            s='-'
            b=-b
        else:
            s=''
    c=a//b
    d=a%b
    cs=binarystring(c)
    ds='.'
    r=d
    rlist=[r]
    repeat=False
    while r>0 and not(repeat):
        r=2*r
        if r<b:
            dig=0
        else:
            dig=1
            r=r-b
        print(dig,r)
        ds+=str(dig)
        repeat = r in rlist
        if repeat:
            i=rlist.index(r)
            ds=ds[:-1-i]+'_'+ds[-1-i:]
            return s+cs+ds
        else:
            rlist.insert(0,r)
    return s+cs+ds

print(binary_division(115,48))

        
    