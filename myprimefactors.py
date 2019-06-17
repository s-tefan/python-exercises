# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 16:35:27 2019

@author: kale
"""

class PrimeFactors:

    primelist = []


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
        for p in self.primelist:
            if self.divisible(n,p):
                self.factors.append(p)
                self.residual//=p
                return self.factorize()
        while True:
            p=self.addprime()
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
    