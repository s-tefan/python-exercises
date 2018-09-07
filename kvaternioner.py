import math

class Kvaternion:

    def __init__(self, r=0,i=0,j=0,k=0):
        self.coeffs = [r,i,j,k]  



    def real_part(self):
        return self.coeffs[0]

    def im_part(self):
        return self.coeffs[1:4]

    def re_im(self):
        return self.real_part(),self.im_part()


    def i_part(self):
        return self.coeffs[1]

    def j_part(self):
        return self.coeffs[2]
    
    def k_part(self):
        return self.coeffs[3]



    def fromCoeffs(c):
        q=Kvaternion()
        q.coeffs=c.copy()
        return q

    def withCoeffs(c):
        q=Kvaternion()
        q.coeffs=c
        return q
    
    ## fromCoeffs copies the list while withCoeffs uses the list

    def from_re_im(re,im):
        ## re skalär, im lista av tre skalärer
        c=im
        c.insert(0,re)
        return Kvaternion.fromCoeffs(c)        
        

        
    def __copy__(self):
        return Kvaternion(self.coeffs.copy())

    def __eq__(self,q):
        b=True
        for (x,y) in zip(self.coeffs,q.coeffs):
            b and (x==y)
        return b


    def __add__(self,q):
        try:
            return Kvaternion.fromCoeffs([x+y for (x,y) in zip(self.coeffs,q.coeffs)])
        except:
            return(Kvaternion(r=self.real_part()+q))



    def __sub__(self,q):
        try:
            return Kvaternion.fromCoeffs([x-y for (x,y) in zip(self.coeffs,q.coeffs)])
        except:
            return(Kvaternion(r=self.real_part()-q))

    def __neg__(self):
        q=self
        ## Eftersom vi definierat __copy__ så ger det en kopia, inte bara samma referens.
        q.coeffs=[-a for a in q.coeffs]
        return q

    def scalar_mult(self,k):
        return Kvaternion.fromCoeffs( \
            [x*k for x in self.coeffs] )

    def scalar_div(self,k):
        return Kvaternion.fromCoeffs( \
            [x/k for x in self.coeffs] )


    def __mul__(self,q):
        if isinstance(q,type(self)):
            sc=self.coeffs
            qc=q.coeffs
            m=[0,0,0,0]
            im1=sc[1:4]
            im2=qc[1:4]
            m[0]=sc[0]*qc[0]-sum([im1[i]*im2[i] for i in range(0,3)])
            m[1]=sc[0]*qc[1]+qc[0]*sc[1]+im1[1]*im2[2]-im1[2]*im2[1]
            m[2]=sc[0]*qc[2]+qc[0]*sc[2]+im1[2]*im2[0]-im1[0]*im2[2]
            m[3]=sc[0]*qc[3]+qc[0]*sc[3]+im1[0]*im2[1]-im1[1]*im2[0]
            return Kvaternion.fromCoeffs(m)
        else:
            return Kvaternion.fromCoeffs( \
                [x*q for x in self.coeffs] )

    def conj(self):
        q=self
        for i in range(1,4):
            q.coeffs[i]=-q.coeffs[i]
        return q

    def modulus_sq(self):
        return sum([x**2 for x in self.coeffs[0:4]])

    def modulus(self):
        return math.sqrt(self.modulus_sq())

    def __truediv__(self,q):
        ## Obs, division till höger, dvs a/b=a*b.conj()/b.modulus_sq()
        if isinstance(q,type(self)):    
            return (self*q.conj()).scalar_div(q.modulus_sq())
        else:
            return self.scalar_div(q)
    

    def __repr__(self):
        return repr(self.coeffs[0])+'+'+repr(self.coeffs[1])+'i+' \
                      +repr(self.coeffs[2])+'j+'+repr(self.coeffs[3])+'k'
        
        
        

I=Kvaternion(i=1)
J=Kvaternion(j=1)
K=Kvaternion(k=1)
    

