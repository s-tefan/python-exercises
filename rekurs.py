ap = slice(-1)
print([3,4,5,6][ap])

def dotprod(a,b):
    c = len(a)
    if c != len(b):
        raise ValueError("Arrays not of same size")
    if c == 0:
        return 0
    else:
        return a[-1]*b[-1]+dotprod(a[:-1],b[:-1])
    

print(dotprod([1,2,3],[2,-1,1]))

