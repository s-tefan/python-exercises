class FibonacciIterator:
    n0=0
    n1=1

    def __iter__(self):
        return self

    def __init__(self,n0,n1):
        self.n0=n0
        self.n1=n1
        

    def __next__(self):
        n=self.n0 # Första värdet sparas, ska returneras
        n2=self.n0+self.n1 # Skapar nästa värde
        self.n0=self.n1 # Uppdaterar
        self.n1=n2
        return n   # Detta värde returneras av funktionen next(...)
                    # och används i en for-loop över iteratorn

    def __str__(self):
        return str(self.n0)+','+str(self.n1)+',...'

    def __val0__(self):
        return self.n0

    def __val1__(self):
        return self.n1
    
    
# exempel på användning
def fibonaccitest(max):
    fib=FibonacciIterator(0,1)
    for n in fib:
        print(n,';',fib)
        if n>max: break

fibonaccitest(100)

        
    
