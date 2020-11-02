# vonneumann.py

class NumberByList:

    def __init__(self):
        self.repr = []

    def inc(self):
        self.repr.append(self.repr)


class NumberByFunction:

    # Behöver fixas på

    s = lambda n : Null
    zero = lambda n : n

    def __init__(self, repr=zero):
        self.repr = repr

    def succ(self):
        return NumberByFunction(lambda n : s(repr(n)))

    def count(self):
        pass


apa = NumberByFunction()
print(apa)
apa = apa.succ()
print(apa)
apa = apa.succ()
print(apa)

