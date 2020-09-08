ap = slice(-1)
print([3,4,5,6][ap])

def dotprod(a,b):
    c = len(a)
    if c != len(b):
        raise ValueError("Arrays not of same size")
    if c == 0:
        return 0
    else:
        return a[-1]*b[-1]+dotprod(a[:-1],b[:-1])
    

print(dotprod([1,2,3],[2,-1,1]))

def matrixtranspose(a):
    # A matrix is is represented as a list of lists
    # A column of rows
    # a[r][c]
    m = len(a)
    n = len(a[0])
    at = [[]]*n
    for row in a:
        i = 0
        for elem in row:
            at[i].append(elem)
            i+=1
    return at

def matrixmult(a,b):
    # A matrix is is represented as a list of lists
    # A column of rows
    # a[r][c]
    bt = matrixtranspose(a)
    c = []
    for arow in a:
        crow = []
        for bcol in bt:
            crow.append(dotprod(arow,bcol))
        c.append(crow)
    return c

def printmatrix(a):
    for row in a:
        prow = ""
        for elem in row:
            prow += str(elem)+"\t"
        print(prow)


a=[[1,2],[3,4]]
b=[[7,-8],[-9,10]]
printmatrix(a)
printmatrix(b)
printmatrix(matrixmult(a,b))
