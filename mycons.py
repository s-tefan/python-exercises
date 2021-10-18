class Cons:
    """
    A class of lisp-like lists
    """

    def __init__(self, CAR, CDR = None):
        self.CAR = CAR
        self.CDR = CDR
        self.EMPTY = False

    @staticmethod
    def new(CAR, CDR):
        return Cons(CAR, CDR)


    def __len__(self):
        if self.CDR:
            return 1 + len(self.CDR)
        else:
            return 1

    def insert(self, obj, n):
        if n < 0:
            n = len(self) + n
        if n == 0:
            self.push(obj)
        else:
            for k in range(n):
                self = self.CDR
                self.push(obj)
            '''
            apa = self
            for k in range(n):
                parent = apa 
                apa = apa.CDR
            parent.CDR = Cons(obj, apa)
            '''

    def __iter__(self):
        return ConsIterator(self)

    def pushed(self, obj):
        return Cons(obj, self)


    def push(self, obj):
        # self = Cons(obj, self)
        # does not work.
        # self is a local variable referencing the object
        # Need to create new CDR
        self.CDR = Cons(self.CAR, self.CDR)
        self.CAR = obj

    def pop(self):
        if self.CDR:
            popped = self.CAR
            self.CAR = self.CDR.CAR
            self.CDR = self.CDR.CDR
            return popped
        else:
            raise Exception("Can't pop a Cons with no CDR")


class ConsIterator:
    def __init__(self, cons):
        self._cons = cons
        self._in_turn = cons
    
    def __next__(self):
        if self._in_turn:
            result = self._in_turn.CAR
            self._in_turn = self._in_turn.CDR
            return result
        else: 
            raise StopIteration
                    

apa = Cons(1, Cons(2, Cons(3, None)))
apa = Cons(0, apa)
print(len(apa))
print(list(apa))
while apa:
    print(apa.CAR)
    apa = apa.CDR

apa = Cons(1, Cons(2, Cons(3, None)))
apa.insert(0, 0)
apa.insert(23, 1)
apa = apa.pushed(42)
apa.push(41)
print(list(apa))

while True:
    print(apa.pop())