class MyBinaryTree:
    value=None
    left=None
    right=None

    def __init__(self,value=None,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right


    def setLeft(self,ltree):
        self.left=ltree

    def setRight(self,rtree):
        self.right=rtree

    def setValue(self,val):
        self.value=val

    def traverseDF(self):
        output=[]
        if self.left==None:
            if self.right==None:
                return output+[self.value]
            else:
                return output+[self.value]+self.right.traverseDF()
        else:
            if self.right==None:
                return self.left.traverseDF()+[self.value]
            else:
                return self.left.traverseDF()+[self.value]+self.right.traverseDF()
            
            
