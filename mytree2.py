# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 15:05:57 2019

@author: kale
"""

class Mytree:
    def __init__(self,children=None,data=None,symbol=''):
        # Hade inte funkat med exv children=[] som arg eftersom muterbara objekt bara skapas en gång
        self.children = children if children else []
        self.data= data if data else {}
        self.symbol=symbol
    def __iter__(self):
        return iter(self.children)
    def append(self,child):
        self.children.append(child)
    def setdata(self,key,value):
        self.data[key]=value
    def printdepthfirst(self):
        print(self.data)
        for c in self:
            c.printdepthfirst()
    def traverseDF(self,order='pre'):
        if order=='pre':
            out=[self.data]
            for c in self:
                out.append(c.traverseDF(order='pre'))
        elif order=='post':
            out=[]
            for c in self:
                out.append(c.traverseDF(order='post'))
            out.append(self.data)
        else:
            raise(Exception('Unknown order'))
        return out
    def postfix(self):
        p=self.symbol+'('
        for k in self:
            p+=k.postfix()
        p+=')'
        return p
#    def fromreversepolish(expr,binaries,unaries):
#        stack=[]
#        for c in expr:
#            if c in binaries:
#                t2=Mytree(data=stack.pop())
#                t1=Mytree(data=stack.pop())
#                node=Mytree(children=[t1,t2],data=c)
#            elif c in unaries:
#                t=Mytree(data=stack.pop())
#                node=Mytree(children=[t])
                
        
root=Mytree(data={'text':'Jag är rot!'},symbol='a')
root.append(Mytree(data={'text':'ungjävel1'},symbol='b'))
root.append(Mytree(data={'text':'ungjävel2'},symbol='c'))
root.children[0].append(Mytree(data={'text':'ungungjävel1.1'},children=[],symbol='d'))
print(root.traverseDF(order='pre'))
print(root.traverseDF(order='post'))
print(root.postfix())