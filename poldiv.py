
'''
Polynomials represented as lists of coefficients.
'''
def cropped(c, eps = 0):
    while(abs(c[-1]) <= 0):
        c.pop()
    return c

def polsum(a,b):
    c=[]
    if len(b) > len(a):
        longest, shortest = b, a
    else:
        longest, shortest = a, b
    m = len(shortest)
    for k, elem in enumerate(longest):
        if k < m:
            c.append(elem+shortest[k])
        else:
            c.append(elem)
    return cropped(c)


def polscalarmul(k,l):
    c = []
    for k in l:
        c.append(k*l)

def polprod(a,b):
    c=[]
    for n in range(len(a)+len(b)-1):
        c.append(sum(a[k]*b[n-k] for k in range(n+1) if k<len(a) and n-k<len(b)))
    return(cropped(c))

def polshifted(a, k):
    return [0]*k + a

def poldiv(a,b):
    if len(a) < len(b):
        return 0, a
    elif len(a) == len(b):
        c = a/b
        return c, polsum(a,polscalarmul(c,b))
    else:
        d = len(a) - len(b)
        # INTE KLART

print(polsum([3,4,5],[4,5,6,7]))
print(polsum([4,5,6,7],[3,4,5]))
print(polscalarmul(4,[2,3,4]))
print(polprod([2,3,4],[1,2,3,4]))
