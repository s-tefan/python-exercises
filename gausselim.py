import mymatrix

class Gausselim(mymatrix.MyMatrix):
    def rowadd(self,i,j,c):
        for k in range(len(self.array[i])):
            self.array[i][k]+=c*self.array[j][k]

    def rowswap(self,i,j):
        a=self.array[i]
        b=self.array[j]
        self.array[i]=b
        self.array[j]=a

    def rowmult(self,i,c):
        for k in range(len(self.array[i])):
            self.array[i][k]*=c
            
