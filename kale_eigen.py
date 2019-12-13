def dot(v,w):
    vl=len(v)
    if vl!= len(w):
        raise Exception('The vectors are not of the same dimension.')
    s=0
    for i in range(vl):
        s+=v[i]*w[i]
    return s



def matrix_vector_mult(a,v):
    prod = []
    for row in a:
        prod.append(dot(row,v))
    return prod


a=[[1,2],[3,4]]
print(matrix_vector_mult(a,[1,-2]))



def eigen_it(a,v):
    av=matrix_vector_mult(a,v)
    eigsq=dot(av,av)/dot(v,v)
    if ...