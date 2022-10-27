'''Erathostenes sieve for primes, with bitarray'''
import bitarray
q = 100
n = q**2
primes = []
checks = bitarray.bitarray(n)
checks[:] = True
checks[0:2] = False
prime = 1 # Inte primtal, men startvärde
while prime < q:
    prime = checks.index(True, prime+1) # Nästa primtal
    checks[2*prime::prime] = False # Bocka bort alla efter prime delbara med prime
    primes.append(prime)
    print(f'- {prime}')
primes = []
p = 2
while True:
    try:
        primes.append(p)
        p = checks.index(True, p+1)
    except:
        break # bryt när listan är slut
#print(*primes, sep = ", ")
print(len(primes))

