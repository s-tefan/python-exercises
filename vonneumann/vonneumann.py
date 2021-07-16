# vonneumann.py

class NumberByList:

    def __init__(self):
        self.repr = []

    def inc(self):
        self.repr.append(self.repr)

    def dec(self):
        self.repr = self.repr[:-1]

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


apa = NumberByReference()
print(apa)
apa = apa.succ()
print(apa)
apa = apa.succ()
print(apa)

apa