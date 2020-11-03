# vonneumann.py

class NumberByList:

    def __init__(self):
        self.repr = []

    def inc(self):
        self.repr.append(self.repr)


class NumberByFunction:

    # Behöver fixas på

    s = lambda n : n
    zero = Null


    def __init__(self):
        self.repr = self.zero # makes a zero

    def succ(self):
        return s(self.repr)
        

    def count(self):
        if self.repr == self.zero:
            return 0
        else:
            return self.repr.count


apa = NumberByFunction()
print(apa)
apa = apa.succ()
print(apa)
apa = apa.succ()
print(apa)

