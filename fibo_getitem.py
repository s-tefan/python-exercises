class Fibo(object):
    def __init__(self, f0, f1):
        self.first = (f0,f1)

    def __getitem__(self, k):
        if k == 0 or k == 1:
            return self.first[k]
        else:
            return self[k-1] + self[k-2]


ap = Fibo(0,1)
print(ap[7])






