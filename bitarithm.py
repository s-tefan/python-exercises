'''Aritmetiska operationer på int som booleska polynom.'''
def sum(a,b):
    return a ^ b
def prod(a,b):
    p = 0
    while a:
        print(bin(a), bin(b), bin(p))
        if a%2:
            p ^= b 
        b <<= 1
        a >>= 1
    return(p)

def deg(a):
    n = -1
    while a:
        a >>= 1
        n += 1
    return n

def divrem(a,b):
    db = deg(b)
    r = a
    q = 0
    while deg(r) >= db:
        d = b
        n = 0
        dr = deg(r)
        print("!")
        while deg(d) < dr:
            d <<= 1
            n += 1
            print(d,r)
        r ^= d
        q ^= 1 << n
        print(bin(q),bin(r))
    return q, r

    
    
    

x = 0b1101
y = 0b101
print(bin(x), bin(y), bin(prod(x,y)), (bin(z) for z in divrem(x,y)))
