def dk(f, degree, seed, n):
    p = []
    p0 = 1
    for j in range(degree):
        p.append(p0)
        p0 *= seed
    for k in range(n):
        q = []
        for j in range(degree):
            x = f(p[j])
            for i in range(degree):
                if i != j:
                    x /= (p[j] - p[i])
            q.append(p[j] - x)
        p = q.copy()
        print(q)
    return p

f = lambda x: (x+1)*(x+1)*(x+3)*(x-4)
dk(f, 4, 1+1j, 10)

         
