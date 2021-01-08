class Inf():
    def inv(self):
        return 0

    def __mul__(self, a):
        if a:
            return self


INF = Inf()


class Moebius:
    def __init__(self, m):
        self.matrix = m

    def __mul__(self, bm):
        a, b = self.matrix, bm.matrix
        return Moebius(
            [[a[0][0]*b[0][0] + a[0][1]*b[1][0],
            a[0][0]*b[0][1] + a[0][1]*b[1][1]],
            [a[1][0]*b[0][0] + a[1][1]*b[1][0],
            a[1][0]*b[0][1] + a[1][1]*b[1][1]]]
            )

    def apply(self, z, fraction = False):
        a = self.matrix
        if z == INF:
            return (a[0][0], a[1][0]) if fraction else a[0][0] / a[1][0]
        elif a[0][0]*z + a[1][1]:
            return (a[0][0]*z + a[0][1]) , (a[1][0]*z + a[1][1]) if fraction else (a[0][0]*z + a[0][1]) / (a[1][0]*z + a[1][1])
        else:
            return (1, 0) if fraction else INF

    @classmethod
    def identity(cls):
        return Moebius([[1, 0], [0, 1]])

    @classmethod
    def recip(cls):
        return Moebius([[0, 1], [1, 0]])

    @classmethod
    def adder(cls, a):
        return Moebius([[1, a], [0, 1]])

    @classmethod
    def multiplier(cls, a):
        return Moebius([[a, 0], [0, 1]])

    @classmethod
    def cf(cls, a):
        return cls.adder(a)*cls.recip()

    def inverse(self):
        a = self.matrix
        d = a[0][0]*a[1][1] - a[0][1]*a[1][0]
        return Moebius(
            [[a[1][1]/d, -a[1][0]/d], [-a[0][1]/d, a[0][0]/d]]
        )

class Contfrac:
    def __init__(self, terms = None):
        self.terms=terms  # list or other iterable

    def __repr__(self):
        max=15
        s="["
        for k, c in enumerate(self.terms):
            if k > max:
                s += " ..."
                break
            else:
                s += str(c) + " "
        return s + "]"





    def makeiter(self):
        return iter(self.terms)


    @ staticmethod
    def from_float(x):
        termlist=[]
        while x:
            termlist.append(int(x))
            r=x % 1
            x=1/r if r else 0
        return Contfrac(termlist)

    @ staticmethod
    def from_fraction(num, denom):
        termlist=[]
        while denom:
            q, r = divmod(num, denom)
            termlist.append(q)
            num, denom = denom, r
        return Contfrac(termlist)


    def convergent(self, n, fraction = False):
        ap=Moebius.identity()
        for k, a in enumerate(self.makeiter()):
            if k >= n:
                break
            else:
                ap *= Moebius.cf(a)
            #print(ap.apply(INF, fraction = fraction))
        return ap.apply(INF, fraction = fraction)

    def convergent_list(self, n, fraction = False):
        clist = []
        ap=Moebius.identity()
        for k, a in enumerate(self.makeiter()):
            if k >= n:
                break
            else:
                ap *= Moebius.cf(a)
                clist.append(ap.apply(INF, fraction = fraction))
        return clist

    def convergent_gen(self, n = None, fraction = False):
        clist = []
        ap=Moebius.identity()
        for k, a in enumerate(self.makeiter()):
            if n and k >= n:
                break
            else:
                ap *= Moebius.cf(a)
                yield ap.apply(INF, fraction = fraction)


cf=Contfrac.from_float(17/23)
print(cf.convergent(10), cf.convergent(10, fraction = True), cf)
cf=Contfrac.from_fraction(17, 23)
print(cf.convergent(10), cf.convergent(10, fraction = True), cf)

print(cf.convergent_list(20, fraction = True))

def ones():
    while True:
        yield 1

cf = Contfrac(ones())
n = 5
print(cf.convergent(n), cf.convergent(n, fraction = True), cf)
print(cf.convergent_list(n, fraction = True), cf)


def expcoeffs():
    yield 2
    k = 2
    while True:
        yield 1
        yield k
        k += 2
        yield 1


n = 20
print(Contfrac(expcoeffs()).convergent_list(n, fraction = True))
print(Contfrac(expcoeffs()).convergent_list(n, fraction = False))
n = 30
for k in Contfrac(expcoeffs()).convergent_list(n, fraction = False):
    print(k)
