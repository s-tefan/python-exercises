
import mymatrix


m1=mymatrix.MyMatrix.zeroMatrix(3,4)
m2=mymatrix.MyMatrix.eyeMatrix(3)
m3=mymatrix.MyMatrix.diagMatrix([4,5,6])
print(m1.array)
print(m2.array)
print(m3.array)
m4=m3.cp()
m5=m3+m4
print(m3.array,'+',m4.array,'=',m5.array)
m50=m3.add_zip(m4)
print(m50.array)
m6=mymatrix.MyMatrix([[1,2],[3,4]])
m7=mymatrix.MyMatrix([[1,-1],[2,-3]])
print((m6*m7).array)
(m6*m7).print()
(m3.minor(0,1)).print()
print(m3.det())

m8 = mymatrix.MyMatrix([[1,2,3],[4,5,6],[2,5,8]])
m8.add_row_multiple_inplace(-10,0,2)
m8.print()
print()
m8.gauss_first_inplace()
m8.print()
print()
#m8.get_block(slice(1,3),slice(1,3)).print()


m8 = mymatrix.MyMatrix([[1,2,3,4,5,6],[4,5,6,4,2,7],[2,5,8,1,1,1],[1,1,1,1,1,1]])
m8.print()
print()
m8.gauss_recursive().print()
print()
m8 = mymatrix.MyMatrix([[1,2,3,4,5,6],[1,2,3,5,7,3],[2,4,6,10,2,3],[1,1,1,1,1,1],[1,1,1,1,1,1],[1,1,1,1,1,1]])
m8.print()
print()
m8.gauss_recursive().print()

'''
print()
mymatrix.MyMatrix.zeroMatrix(3,0).print()
print(mymatrix.MyMatrix.zeroMatrix(3,0).array)
mymatrix.MyMatrix.zeroMatrix(0,3).print()
print(mymatrix.MyMatrix.zeroMatrix(0,3).array)
'''