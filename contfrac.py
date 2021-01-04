class Contfrac:
    def __init__(self, terms = None):
        self.terms = terms # list or other iterable

    def __repr__(self):
        max = 15
        s = "["
        for k, c in enumerate(self.terms):
            if k > max:
                s += " ..."
                break
            else:
                s += str(c) + " "
        return s + "]"


    @staticmethod
    def from_float(x):
        termlist = []
        while x:
            termlist.append(int(x))
            r = x % 1
            x = 1/r if r else 0
        return Contfrac(termlist)

    @staticmethod
    def from_fraction(num, denom):
        termlist = []
        while num and denom:
            q, r = divmod(num, denom)
            termlist.append(q)
            num, denom = denom, r
        return Contfrac(termlist)


    def truncate(self, n):
        try:
            if len(self.terms) < n:  # may raise exception
                n = len(self.terms)
            x = self.terms[n - 1] # may raise exception
            if x == 0:
                x = 1
            for k in self.terms[n-2::-1]:
                x = k + 1/x
            return x
        except:
            for j in self.terms:
                pass

cf = Contfrac.from_float(17/23)
print(cf.truncate(10), cf)
cf = Contfrac.from_fraction(17, 23)
print(cf.truncate(10), cf)
