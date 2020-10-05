class GF:
    def __init__(self, p, poly, gen):
        if poly[-1] != 1:
            raise Exception("Not a monic polynomial")
        self.p = p  # Should check for primality
        self.poly = poly  # Should check for irreducibility
        self.gen = gen  # Should check for primitiveness

    def genpow(self, n):
        if n == 0:
            return [1]
        elif n == 1:
            return self.gen
        elif n % 2 == 0:
            he = self.genpow(n//2)
            return self.prod(he, he)
        else:
            return self.prod(self.genpow(n-1), self.gen)

    def reduce(self, clist):
        # Both changes and returns clist
        if len(clist) < len(self.poly):
            return clist
        else:
            m = clist[-1]
            for k in range(len(self.poly)):
                clist[-1-k] -= m*self.poly[-1-k]
                clist[-1-k] %= self.p
            while clist and clist[-1] == 0:
                clist.pop()
            return self.reduce(clist)

    def sum(self, a, b):
        # TBI sum of two elements
        if len(b) > len(a):
            return self.sum(b, a)
        else:
            s = []
            lena = len(a)
            lenb = len(b)
            for k in range(lena):
                if k < lenb:
                    s.append((a[k]+b[k]) % self.p)
                else:
                    s.append(a[k])
            return self.reduce(s)

    def minus(self, a):
        m = []
        for k in len(a):
            m.append((-a)%self.p)
        return m
            

    def prod(self, a, b):
        # TBI product of two elements
        pass


class GFElement:
    def __init__(self, field, coeffs=None, power=None):
        self.field: GF = field


gf8 = GF(2, [1, 1, 0, 1], [0, 1])
apa = [1]
for k in range(10):
    apa = [0]+apa  # Note: list join, not GF addition
    print(gf8.reduce(apa))
print()
apa = [1]
for k in range(10):
    apa = [0]+apa  # Note: list join, not GF addition
    print(apa, gf8.sum(apa, [0, 1]))
