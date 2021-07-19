# vonneumann.py

class NumberByList:

    def __init__(self):
        self.repr = []

    def inc(self):
        self.repr.append(self.repr)

    def dec(self):
        self.repr = self.repr[:-1]

    def count(self):
        return len(self.repr)

class NumberByReference:

    # Behöver fixas på

    def __init__(self):
        self.pre = None # makes a zero

    def succ(self):
        self.pre = self
        

    def count(self):
        if self.pre == None:
            return 0
        else:
            return self.pre.count()


#apa = NumberByReference()
apa = NumberByList()
print(apa, apa.count())
#apa = apa.succ()
apa.inc()
print(apa, apa.count())
#apa = apa.succ()
apa.inc()
print(apa, apa.count())
apa.dec()
print(apa, apa.count())
apa.inc()
print(apa, apa.count())
apa.dec()
print(apa, apa.count())
apa.dec()
print(apa, apa.count())
apa.dec()
print(apa, apa.count())
s
