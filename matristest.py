
import mymatrix


m1=mymatrix.MyMatrix.zeroMatrix(3,4)
m2=mymatrix.MyMatrix.eyeMatrix(3)
m3=mymatrix.MyMatrix.diagMatrix([4,5,6])
print(m1.array)
print(m2.array)
print(m3.array)
m4=m3.cp()
m5=m3+m4
print(m5.array)
m6=mymatrix.MyMatrix([[1,2],[3,4]])
m7=mymatrix.MyMatrix([[1,-1],[2,-3]])
print((m6*m7).array)
(m6*m7).print()
(m3.minor(0,1)).print()
print(m3.det())