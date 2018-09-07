class MyMatrix:


    def __init__(self,array):
        self.array=array

    def cp(self):
        cp=[]
        for row in self.array:
            r=[]
            for elem in row:
                r.append(elem)
            cp.append(r)
        return MyMatrix(cp)

    def __eq__(a,b):
        return a.array==b.array

    def print(self):
        for row in self.array:
            print(row)


    @staticmethod
    def zeroMatrix(m,n):
        array=[]
        for k in range(m):
            array.append(n*[0])
        return(MyMatrix(array))

    def set(self,i,j,c):
        self.array[i][j]=c

    def size(self):
        m=len(self.array)
        n=len(self.array[0])
        return [m,n]

    @staticmethod
    def eyeMatrix(n):
        s=MyMatrix.zeroMatrix(n,n)
        for k in range(n):
            s.set(k,k,1)
        return s

    @staticmethod
    def diagMatrix(d):
        n=len(d)
        s=MyMatrix.zeroMatrix(n,n)
        for k in range(n):
            s.set(k,k,d[k])
        return s

        
    def __add__(self,b):
        if not self.size()==b.size():
            raise TypeError
        else:
            m=self.cp()
            for i in range(len(self.array)):
                for j in range(len(self.array[i])):
                    m.array[i][j]+=b.array[i][j]
        return(m)

    def __mul__(a,b):
        az=a.size(); bz=b.size()
        if not az[1]==bz[0]:
            raise TypeError
        else:
            m=MyMatrix.zeroMatrix(az[0],bz[1])
            for i in range(az[0]):
                for j in range(bz[1]):
                    for k in range(az[1]):
                        m.array[i][j]+=a.array[i][k]*b.array[k][j]
        return m

    def transpose(self):
        sz=self.size()
        m=MyMatrix.zeroMatrix(sz[1],sz[0])
        for i in range(sz[0]):
            for j in range(sz[1]):
                m.array[j][i]=self.array[i][j]
        return m

    def minor(self,i,j):
        marray=[]
        if i==0: c=self.array[1:]
        else: c=self.array[:i]+self.array[i+1:]
        for row in c:
            if j==0: r=row[1:]
            else: r = row[:j]+row[j+1:]
            marray.append(r)
        return MyMatrix(marray)


    def det(self):
        z=self.size()
        if z[0]!=z[1]:
            raise TypeError
        else:
            if z[0]==1:
                return self.array[0][0]
            else:
                d=0
                for k in range(z[1]):
                    if k%2==0:
                        d+=self.array[0][k]*self.minor(0,k).det()
                    else:
                        d-=self.array[0][k]*self.minor(0,k).det()
                return d





