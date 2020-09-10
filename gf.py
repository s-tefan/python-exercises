class GF:
    def __init__(self, p, poly, gen):
        self.p = p # Should check for primality
        self.poly = poly # Should check for irreducibility
        self.gen = gen # Should check for primitiveness

    def genpow(self, n):
        if n == 0:
            return [1]
        elif n==1:
            return self.gen
        elif n%2 == 0:
            he = self.genpow(n//2)
            return self.prod(he,he) 
        else:
            return self.prod(self.genpow(n-1),self.gen)

    @classmethod
    def sum(self,a, b):
        % TBI sum of two elements
        pass

    @classmethod
    def prod(self,a,b):
        % TBI product of two elements
        pass
        
        
class GFElement:
    def __init__(self, field, coeffs=None, power=None):
        self.field = field: GF
        

    


