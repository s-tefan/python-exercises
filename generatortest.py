def skapagenerator(first,then):
    k=first
    while True:
        k=k+then
        yield k

mingenerator=skapagenerator('c','d')
for apa in mingenerator:
    print(apa)
    if len(apa)>7: break

