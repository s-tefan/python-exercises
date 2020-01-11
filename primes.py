
def primes():
    primelist = []
    n=2
    while True:
        isPrime = True
        for p in primelist:
            if n%p == 0: 
                isPrime = False
                break
            if p**2 > n:
                break
        if isPrime:
            primelist.append(n)
            yield n
        n += 1



for k in primes():
    print(k)
    if k>10000000: break


