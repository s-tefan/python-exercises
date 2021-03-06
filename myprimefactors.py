# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 16:35:27 2019

@author: kale
"""

class PrimeFactors:

    primelist = []
    # primelist is a list of all primes up to the last one, incrementally built.
    # xprimelist might be a list of sporadic larger primes that are found while trying to factor.
    # not implemented yet
    #xprimelist = []

    @staticmethod
    def divisible(n,p):
        return n%p==0

    def __init__(self,residual=1,factors=[]):
        self.residual=residual
        self.factors=factors

    def factorize(self):
        n=self.residual
        print(n)
        if n==1:
            return self.factors
        # check divisibility with primes in the saved prime list upp to the sqrt of n
        for p in self.primelist:
            if p**2>n:
                # n is a prime
                self.factors.append(n)
                self.residual=1
                return self.factors
            if self.divisible(n,p):
                self.factors.append(p)
                self.residual//=p
                return self.factorize()
        # if the prime list is not complete up to sqrt(n) add new primes until finished
        while True:
            p=self.addprime()
            if p**2>n:
                # n is a prime
                self.factors.append(n)
                self.residual=1
                return self.factors
            if self.divisible(n,p):
                self.factors.append(p)
                self.residual//=p
                return self.factorize()
        print("Nej, fan!")
        
    @classmethod
    def addprime(cls):
        if len(cls.primelist)==0:
            cls.primelist=[2]
        lastprime=cls.primelist[-1]
        k=lastprime
        while True:
            k+=1
            kisprime=True
            for p in cls.primelist:
                if cls.divisible(k,p):
                    kisprime=False
                    break
            if kisprime:
                cls.primelist.append(k)
                return k
    