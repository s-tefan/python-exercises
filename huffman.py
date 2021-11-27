"""
Defines a class MyHuffmanTree for Huffman Code from a base class MyBinaryTree.
"""

class MyBinaryTree:
    """
    A class for binary trees.
    """
    
    rootcontent=None
    left=None
    right=None

    def __init__(self,content,left=None,right=None):
        self.rootcontent = content
        self.left = left
        self.right = right        
    
    def addchildren(self,content,left,right):
        self.rootcontent=content
        self.left=left
        self.right=right
    
    def leftchild(self):
        return self.left
    
    def rightchild(self):
        return self.right
    
    def is_leaf(self):
        return self.left==None and self.right==None
    
    def x__str__(self):
        verbose = False # Speaker
        if self.is_leaf():
            if verbose: print('Decision!')
            return str(self.rootcontent)
        else:
            if verbose: print('Divisiooon!')
            s=str(self.rootcontent)
            if self.left!=None:
                s+=' L:'+str(self.left)
                if verbose: print('Ayes have it!')
            if self.right!=None:
                s+=' R:'+str(self.right)
                if verbose: print('Noes have it!')
            return s

    def __str__(self):
        return self.rec_str()

    def rec_str(self, d=0):
        verbose = False # Speaker
        if self.is_leaf():
            if verbose: print('Decision!')
            return str(self.rootcontent) + '\n' 
        else:
            if verbose: print('Divisiooon!')
            s = str(self.rootcontent) + '\n'
            if self.left!=None:
                s += ' |'*d + '-L:' + self.left.rec_str(d = d+1)
                if verbose: print('Ayes have it!')
            if self.right!=None:
                s += ' |'*d + '-R:' + self.right.rec_str(d = d+1)
                if verbose: print('Noes have it!')
            return s

class MyHuffmanTree(MyBinaryTree):
    '''
    A subclass of MyBinaryTree for Huffman code.
    '''
            
    def __init__(self, content = ('',0), left=None, right=None):
        super().__init__(content, left = left, right = right)
        
    def binarydict(self,dict,b):
        if self.is_leaf():
            dict[self.rootcontent[0]]=b
        else:
            #print('Divisiooon!')
            s=str(self.rootcontent)
            if self.left!=None:
                self.left.binarydict(dict,b+'0')
                #print('Ayes have it!')
            if self.right!=None:
                self.right.binarydict(dict,b+'1')
                #print('Noes have it!')
    
    def encode(self,s):
        dict={}
        self.binarydict(dict,'')
        b=''
        for c in s:
            b += dict[c]
        return b

    def decode(self,bs):
        t=self
        s=''
        for b in bs:
            if b == '0':
                t = t.left
            elif b == '1':
                t = t.right
            else:
                raise Exception('Not a bit')
            if t.is_leaf():
                s += t.rootcontent[0]
                t = self
        return s

    @classmethod
    def huffmantree(cls,s=''):
        """
        Builds a MyHuffmanTree from a string
        """
        if s:
            # Build frequency table:
            sdict = {}
            for c in s:
                if c in sdict:
                    sdict[c] += 1
                else:
                    sdict[c] = 1
            slist = sdict.items()
            treelist=[cls.huffmanleaf(t) for t in slist]
            while len(treelist)>1:
                treelist=sorted(treelist,key = lambda x: x.rootcontent[1],reverse=True)
                a=treelist.pop()
                b=treelist.pop()
                ac=a.rootcontent
                bc=b.rootcontent
                treelist.append(MyHuffmanTree((ac[0]+bc[0],ac[1]+bc[1]),left=a,right=b))
            t=treelist.pop()
        else:
            t=MyHuffmanTree()
        return t

    @classmethod
    def huffmanleaf(cls, content):
        tree=cls()
        tree.rootcontent=content
        tree.left=None
        tree.right=None
        return tree


s = 'sffjahfhjgfjsdjgfjshasfkl'
print('Encoding:', s)
ht = MyHuffmanTree.huffmantree(s)
print(ht.__str__())
bs = ht.encode(s)
print('Encoded:', bs)
r = ht.decode(bs)
print('Decoded:', r)







'''
sdict={}
for c in s:
    if c in sdict:
        sdict[c]+=1
    else:
        sdict[c]=1
slist=[(x,sdict[x]) for x in sdict]
sslist = sorted(slist,key = lambda x: x[1],reverse=True)
#sslist=sorted(sdict,key=lambda x: sdict[x])
        
print(sslist)

treelist=[MyHuffmanTree(t) for t in sslist]

while len(treelist)>1:
    treelist=sorted(treelist,key = lambda x: x.rootcontent[1],reverse=True)
    a=treelist.pop()
    b=treelist.pop()
    ac=a.rootcontent
    bc=b.rootcontent
    treelist.append(MyHuffmanTree((ac[0]+bc[0],ac[1]+bc[1]),left=a,right=b))

t=treelist[0]
print(t)
dict={}
t.binarydict(dict,'')
print(dict)
'''