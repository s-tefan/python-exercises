def naturals():
    n = 0
    while True:
        yield n
        n +=1


def grej(n):
    print("blurk {}".format(n))
    return n

nat = naturals()
for k in range(4):
    for n in iter(nat):
        print(n)
        if n%5 == 2:
            break
    print("***")
