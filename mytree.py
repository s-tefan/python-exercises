class MyTree:
    value=None
    branches=[]

    def __init__(self,value=None,branches=[]):
        self.value=value
        self.branches=branches #App, app, kommer inte att funka!

    def setValue(self,val):
        self.value=val
 
    def setBranches(self,branches):
        self.branches=branches

    def appendBranch(self,branch):
        self.branches.append(branch)

    def isLeaf(self):
        return not self.branches

    def traverseDF(self,post=False):
        if post:
            output=[] 
        else:
            output=[self.value]
        if self.branches:
            for branch in self.branches:
                output+=branch.traverseDF()
        if post:
            output.append(self.value)
        return output

    def traverseBF(self):
        output=[]
        levelbranches=[self]
        while levelbranches:
            nextlevelbranches=[]
            for branch in levelbranches:
                output.append(branch.value)
                nextlevelbranches+=branch.branches
            levelbranches=nextlevelbranches
        return output
 


# Testkod
t1=MyTree('a',[MyTree('b'),MyTree('c',[MyTree('d'),MyTree('e')])])
print(t1.traverseDF())
print(t1.traverseDF(post=True))
t1.appendBranch(MyTree('f'))
print('DF, prefix: ',t1.traverseDF())
print('DF, infix: ',t1.traverseDF(post=True))
print('BF: ',t1.traverseBF())

apa=MyTree()
print(apa.isLeaf())
apa.appendBranch(MyTree())
print(apa.isLeaf())
print(apa.branches)
#print(apa.traverseBF())
