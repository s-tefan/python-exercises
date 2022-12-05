inf = float('inf')


class Interval:
    pass

    def blupp(self):
        return type(self)

class Boundarypoint:
    def __init__(self, value, inclusive: bool, start: bool):
        self.value = value
        self.inclusive = inclusive
        self.start = start
    
    def __repr__(self):
        return f'[{self.value}, incl: {self.inclusive}, start: {self.start}'

class IntervalUnion:
    inf = float('inf')
        
    
    def __init__(self):
        self.boundary = []
        
    def _tidy(self):
        self.boundary.sort(key=lambda x: x.value)
        in_interval = False
        for bp in self.boundary.copy():
            if in_interval and bp.start:
                self.boundary.remove(bp)
            elif not in_interval and not bp.start:
                self.boundary.remove(bp)
            in_interval = bp.start

    def __repr__(self):
        s = '.'
        for bp in self.boundary:
            if bp.start:
                if bp.inclusive:
                    s += f'[{bp.value},'
                else:
                    s += f']{bp.value},'
            else:
                if bp.inclusive:
                    s += f'{bp.value}]'
                else:
                    s += f'{bp.value}['
        s += '.'
        return s


    def __contains__(self, a):
        cont = False
        for bp in self.boundary:
            if a == bp.value:
                return bp.inclusive
            elif bp.value > a:
                return cont
            else:
                cont = bp.start
        return False                

    def add(self, a):
        if a not in self:
            self.boundary.append(Boundarypoint(a, inclusive=True, start=True))
            self.boundary.append(Boundarypoint(a, inclusive=True, start=False))
            self._tidy()

    def _add_bp(self, bp):
        self.boundary.append(bp)
        self._tidy

    @staticmethod
    def closed_interval(a,b):
        iu = IntervalUnion()
        iu._add_bp(Boundarypoint(a, inclusive=True, start=True))
        iu._add_bp(Boundarypoint(b, inclusive=True, start=False))
        return iu

    @staticmethod
    def open_interval(a,b):
        iu = IntervalUnion()
        iu._add_bp(Boundarypoint(a, inclusive=False, start=True))
        iu._add_bp(Boundarypoint(b, inclusive=False, start=False))
        return iu



class EmptyInterval(Interval):
    pass

class ClosedInterval(Interval):

    def __init__(self, a, b):
        if a > b:
            raise Exception("Upper bound must not be less than lower bound")
        self.lower = a
        self.upper = b
        
    def intersection(self, c):
        return ClosedInterval(max(self.lower, c.lower), min(self.upper, c.upper))

    def __contains__(self, c):
        return (c >= self.lower) and (c <= self.upper)

    def issubset(self, c):
        return (self.lower >= c.lower) and (self.upper <= c.upper) 

    def issuperset(self, c):
        return (self.lower <= c.lower) and (self.upper >= c.upper) 

    def isdisjoint(self, c):
        return (self.upper < c.lower) or (self.lower > c.upper)

    def copy(self):
        return ClosedInterval(self.lower, self.upper)

    def __eq__(self, c):
        return (self.lower, self.upper) == (c.lower, c.upper)

    def __le__(self, c):
        return (self.lower >= c.lower) and (self.upper <= c.upper)

    def __lt__(self, c):
        return self <= c and self != c

    def __repr__(self) -> str:
        return f'Closed interval [{self.lower, self.upper}]'

    def midpoint(self):
        return (self.lower + self.upper)/2

if __name__ == "__main__":
    a = ClosedInterval(3,7)
    b = ClosedInterval(5,9)
    c = ClosedInterval(4,6)
    r = ClosedInterval(-inf, inf)
    print(a,b,a.intersection(b),c<b,c<a, c>b, c>a, c<r, r <=r, c.blupp())
apa = IntervalUnion.closed_interval(3,4)
apa.add(5)
print(apa)
for bp in apa.boundary:
    print(bp)
for x in (2+n/2 for n in range(8)):
    print(x, x in apa)
