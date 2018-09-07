class Polynomial:

    def __init__(self, coeffs):
        self.coeffs = coeffs  # Bör vara List
        self.trim()

    def copy(self):
        return Polynomial(self.coeffs.copy())

    def not_trimmed(self):
        n = len(self.coeffs)
        return(n > 0 and self.coeffs[-1] == 0)

    def trim(self):
        while self.not_trimmed():
            self.coeffs.pop(len(self.coeffs)-1)

    def deg(self):
        self.trim()
        return len(self.coeffs)

    def to_string(self,var='x'):
        n = len(self.coeffs)
        s=''
        for k in range(n):
            s+='{0} {2}^{1}'.format(self.coeffs[k], k, var)
            if k < n-1:
                s+=' + '
        return s

    def print(self,var='x'):
        print(self.to_string(var))

    def __add__(self,term):
        sc=self.coeffs.copy()
        tc=term.coeffs.copy()
        sn=len(sc)
        tn=len(tc)
        if sn>tn:
            tc+=(sn-tn)*[0] # padding tc with zeros
        elif tn>sn:
            sc+=(tn-sn)*[0] # padding sc with zeros
        for k in range(max(sn,tn)):
            sc[k]+=tc[k]
        return Polynomial(sc)

    def __neg__(self):
        s=Polynomial(self.coeffs)
        for k in range(s.deg()):
            s.coeffs[k]=-s.coeffs[k]
        return s

    def __sub__(self,term):
        return self+(-term)

    @staticmethod
    def listfaltning(a, b):
        m = len(a)
        n = len(b)
        c = []
        for k in range(m+n-1):
            d = 0
            for j in range(max(0, k-n+1), min(k+1, m)):
                d += a[j]*b[k-j]
            c.append(d)
        return c

    def __mul__(self,p):
        return Polynomial(Polynomial.listfaltning(self.coeffs,p.coeffs))


    def product_var(self, polm):
        # p=f.product(g) skapar ett nytt polynom p=fg
        ns = len(self.coeffs)
        nm = len(polm.coeffs)
        n = ns+nm
        c = []
        for k in range(n):
            c.append(0)
            for i in range(max(0, k-nm+1), min(ns, k+1)):
                c[k] += self.coeffs[i]*polm.coeffs[k-i]
        return Polynomial(c)

    def xmult(self, n=1):
        return Polynomial(n*[0]+self.coeffs)



    def xdiv(self, n):
        c=self.coeffs.copy()
        for k in range(n):
            c.pop(0)
        return c

    def scalar_mult(self, c):
        if c == 0:
            return Polynomial([])
        else:
            p=Polynomial(self.coeffs)
            for k in range(len(p.coeffs)):
                p.coeffs[k] *= c
            return p

    def leading_coeff(self):
        return self.coeffs[self.deg()-1]

    def remstep(self,q):
        n=self.deg()
        m=q.deg()
        sl=self.leading_coeff()
        ql=q.leading_coeff()
        c=sl/ql
        return self-q.scalar_mult(c).xmult(n-m)

    def divrem(self,q):
        r=self.copy()
        dc=[0]*(self.deg()-q.deg()+1)
        while q.deg()<r.deg():
            k=r.deg()-q.deg()
            c=r.leading_coeff()/q.leading_coeff()
            dc[k]=c
            r=r.remstep(q)
        return [Polynomial(dc),r]
