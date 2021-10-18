#from numba import jit


#@jit(nopython=True)
def fibo(n,a,b):
    # A tail recursive fibonacci algorithm
    if n == 0:
        return a
    elif n == 1:
        return b
    elif n > 1:
        return fibo(n-1, b, a+b)
    else:
        raise Exception("Error!")

#@jit(nopython=True)
def fibo10(n,a,b):
    # A tail recursive fibonacci algorithm
    # Python 3.10 structural pattern matching
    match n:
        case 0:
            return a
        case 1:
            return b
        case n if n > 1:
            return fibo(n-1, b, a+b)
        case _:
            raise Exception("Error!")

def binom(n,k):
    if k == 0:
        return 1
    elif k == n:
        return 1
    elif 0 < k and k < n:
        return n * binom(n-1, k-1) // k

print(fibo(10,0,1))
print(fibo10(10,0,1))
# 0,1,1,2,3,5,8,13,21,34,55
print(binom(7,3))
