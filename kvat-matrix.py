import mymatrix as m
import kvaternioner
kv_one_matrix=m.MyMatrix.eyeMatrix(4)
im_i_matrix=m.MyMatrix([[0,-1],[1,0]])
kv_i_matrix=m.MyMatrix([[0,-1,0,0],[1,0,0,0],[0,0,0,-1],[0,0,1,0]])
kv_j_matrix=m.MyMatrix([[0,0,-1,0],[0,0,0,1],[0,0,1,0],[0,0,0,-1]])
kv_k_matrix=kv_i_matrix*kv_j_matrix


##
##apa=m.MyMatrix([[2,0],[0,3]])
##(apa**5).print()
