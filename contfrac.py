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
    def from_number(x, n):
        termlist = []
        for k in range(n):
            termlist.append(int(x))
            if x % 1 == 0:
                break
            else:
                x = 1/(x % 1)
        return Contfrac(termlist)


    def truncate(self, n):
        try:
            if len(terms) < n:  # may raise exception
                n = len(terms)
            x = self.terms[n - 1] # may raise exception
            if x == 0:
                x = 1
            for k in self.terms[n-2::-1]:
                x = k + 1/x
            return x
        except:
            for j in self.terms:
                pass

cf = Contfrac.from_number(3/4, 10)
print(cf.truncate(10), cf)
