verbose = False


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
        return MyMatrix(array)

    def empty_column(j):
        array=[[]]*j
        return MyMatrix(array)


    def set(self,i,j,c):
        self.array[i][j]=c

    def get(self,i,j):
        return self.array[i][j]

    def get_block(self, rslice, cslice):
        rows = self.array[rslice] # make a slice of rows (copy)
        for i in range(len(rows)):
            rows[i] = rows[i][cslice]
        return MyMatrix(rows)

    def size(self):
        m=len(self.array)
        if m == 0:
            return (0,0)
        else:
            n=len(self.array[0])
            return (m,n)

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

    def concat_rowwise_multi(self,*matrices):
        ss=self.size()
        for matrix in matrices:
            sm=matrix.size()
            if sm[0]!=ss[0]:
                raise TypeError("Mismatching number of rows")
            else:
                for r in range(ss[0]):
                    self.array[r]+=matrix.array[r]
        return self

    def concat_colwise_multi(self,*matrices):
        ss=self.size()
        for matrix in matrices:
            sm=matrix.size()
            if sm[1]!=ss[1]:
                raise TypeError("Mismatching number of columns")
            else:
                self.array+=matrix.array
        return self



    def concat_rowwise_inplace(self, matrix):
        ss=self.size()
        sm=matrix.size()
        if sm[0]!=ss[0]:
            raise TypeError("Mismatching number of rows")
        else:
            for r in range(ss[0]):
                self.array[r]+=matrix.array[r]
        return self

    def concat_colwise_inplace(self, matrix):
        ss=self.size()
        sm=matrix.size()
        if sm[1]!=ss[1]:
            raise TypeError("Mismatching number of columns")
        else:
            self.array+=matrix.array
        return self


    @staticmethod
    def concat_rowwise(matrix1, matrix2):
        s1=matrix1.size()
        s2=matrix2.size()
        if s1[0]!=s2[0]:
            raise TypeError("Mismatching number of rows")
        else:
            cmatrix = matrix1.cp()
            for r in range(s1[0]):
                cmatrix.array[r]+=matrix2.array[r]
            return cmatrix

    @staticmethod
    def concat_colwise(matrix1, matrix2):
        s1=matrix1.size()
        s2=matrix2.size()
        if s1[1]!=s2[1]:
            raise TypeError("Mismatching number of columns")
        else:
            cmatrix = matrix1.cp()
            cmatrix.array+=matrix2.array
            return cmatrix
                
        
    def __add__(self,b):
        if not self.size()==b.size():
            raise TypeError
        else:
            m=self.cp()
            for i in range(len(self.array)):
                for j in range(len(self.array[i])):
                    m.array[i][j]+=b.array[i][j]
        return(m)

    def add_zip(self,b):
        if not self.size()==b.size():
            raise TypeError
        else:
            z = zip(self.array, b.array) # pair rows of each matrix
            # now sum these rows
            sum_rows = lambda radpar: list(map(sum,zip(*radpar)))
            sum_array = map(sum_rows ,z)
        return(MyMatrix(list(sum_array)))



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

    def __pow__(self,n):
        ss=self.size()
        sr=ss[0]
        if n<0:
            raise Exception("Negative powers not implemented")
        else:
            p=MyMatrix.eyeMatrix(sr)
            sq=self.cp()
            while n!=0:
                print(n)
                if n%2!=0:
                    print("...1")
                    p*=sq
                else: print("...0")
                n=n//2
                if n: sq*=sq
            return p
                    
            


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



    def swap_rows_inplace(self, i, j):
        # swaps rows i and j of the matrix self
        # first element has index 0
        ri = self.array[i]
        self.array[i] = self.array[j]
        self.array[j] = ri
    
    def add_row_multiple_inplace(self, k, i, j):
        # adds k*row i to row j
        # first element has index 0
        ri = self.array[i]
        rj = self.array[j]
        rnew = list(map(lambda ap: k*ap[0]+ap[1], zip(ri,rj)))
        self.array[j] = rnew

    def pivoting_inplace(self):
        for i in range(1,len(self.array)):
            if abs(self.get(i,0))>abs(self.get(0,0)):
                self.swap_rows_inplace(0,i)

    def gauss_first_inplace(self):
        if len(self.array) <= 1:
            return self.get(0,0)!=0 # return as below if one row
        if not self.array[0]:
            raise IndexError("No columns") # raise error if no columns
        self.pivoting_inplace()
        if self.get(0,0)==0:
            return False # return False if first column is all zero 
        for i in range(1,len(self.array)):
            k = self.get(i,0)/self.get(0,0)
            if k!=0:
                self.add_row_multiple_inplace(-k,0,i)
        return True # return True if first column is pivotal (non-zero)

    def gauss_recursive(self):
        # Inte helt färdig...
        pass
        block = self.cp()
        if verbose: print("Ny vända")
        if verbose: print(block.array)
        
        if block.size()[0] <= 1:
            return block # One row matrix is fully reduced
        if block.size()[1] <= 1:
            return block
        
        zerocolblock=MyMatrix.empty_column(block.size()[0])
        if verbose: print('empty zerocolblock:',zerocolblock.array)
        
        while not block.gauss_first_inplace():
            # run if the first column is not a pivot column,
            # i e it all zero
            #print('No pivot')
            if verbose: print(block.array)
            # Split zero column + rest 'block'
            ###zerocolblock.concat_rowwise_inplace(block.get_block(slice(None), slice(0,1)))
            s = zerocolblock.size()
            zerocolblock = MyMatrix.zeroMatrix(s[0],s[1]+1)
            if verbose: print('zero column added to zerocolblock:', zerocolblock.array)
            block = block.get_block(slice(None), slice(1,None))
            if block.size()[1] == 0:
                if verbose: print('Over and out')
                #break

        if verbose: print('Pivot')
        #print(block.array)

        firstrow = block.get_block(slice(0,1),slice(0,None))
        zerocol = block.get_block(slice(1,None),slice(0,1))
        block = block.get_block(slice(1,None),slice(1,None)) 

        reduced_matrix = \
            MyMatrix.concat_rowwise(
                zerocolblock, 
                MyMatrix.concat_colwise(
                    firstrow, 
                    MyMatrix.concat_rowwise(zerocol, block.gauss_recursive()
                    )
                )
            )


        
        
        if verbose: 
            print("firstrow")
            firstrow.print() 
            
            print("zerocolblock")
            zerocolblock.print()

            print("block")
            block.print() 
            

            print('Rajtan!')
            print(reduced_matrix)
        return(reduced_matrix)

    
        

