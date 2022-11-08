def deg(a):
    '''graden av ett booleskt polynom representerat binärt som en int, 0b1~1, 0b10~x, 0b100~x**2, etc'''
    n = -1
    while a:
        n += 1
        a >>= 1
    return n


def divres(a,b):
    r = a
    q = 0
    while deg(r) >= deg(b):
        d = b
        n = 0
        while deg(d)<deg(r):
            d <<= 1
            n += 1
        if n < 0:
            continue
        r ^= d
        q ^= (1 << n)
        print(bin(q), bin(r))
    return q, r

print(tuple(bin(z) for z in divres(0b1011001010, 0b1101)))





'''
for k in range(10):
    if k%2:
        continue
    print(k)
'''

'''
import graphicsxkale
win=graphicsxkale.GraphWin('', 300, 200)
'''
