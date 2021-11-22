# Funkar inte
class MyBinaryTree:
    rootcontent=None
    left=None
    right=None

    def __init__(self,content,left=None,right=None):
        self.rootcontent=content
        self.left=left
        self.right=right        
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
    def __str__(self):
        if self.is_leaf():
            print('Decision!')
            return str(self.rootcontent)
        else:
            print('Divisiooon!')
            s=str(self.rootcontent)
            if self.left!=None:
                s+=' L:'+str(self.left)
                print('Ayes have it!')
            if self.right!=None:
                s+=' R:'+str(self.right)
                print('Noes have it!')
            return s

class MyHuffmanTree(MyBinaryTree):
            
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
            b+dict[c]
        return b
    def decode(self,bs):
        t=self
        s=''
        for b in bs:
            if t.is_leaf():
                s+=t.rootcontent
            elif b=='0':
                t=self.left
            elif b=='1':
                t=self.right
            else:
                raise Exception('Not a bit')
        return s

    @classmethod
    def huffmantree(cls,s=''):
        if s:
            sdict={}
            for c in s:
                if c in sdict:
                sdict[c]+=1
                else:
                    sdict[c]=1
            slist=[(x,sdict[x]) for x in sdict]
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


s='sffjahfhjgfjsdjgfjshasfkl'
print(s)
ht=MyHuffmanTree.huffmantree(s)
print(ht)
bs=ht.encode(s)
print(bs)
r=ht.decode(bs)
print(r)








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
