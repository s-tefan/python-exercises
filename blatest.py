import random

def blurp(m):
    n=m
    while True:
        print("Rajdida: {}".format(n))
        apa = yield n
        print("Igen: n = {}, apa = {}".format(n, apa))
        yield n
        n += 1








'''
for k in blurp(4):
    print(k)
    if k > 6: break

gen = blurp(23)
gen.send(None)
for k in range(4):
    gen.send(k)
    print(next(gen))
    print()

'''   

        
