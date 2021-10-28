import random

def mysort(apa):
    print(apa)
    if len(apa) > 1:
        return mysplice(mysort(apa[::2]), mysort(apa[1::2]))
    else:
        return apa

def mysplice(apa, bepa):
    cepa = apa[0:0]
    aind, bind = 0, 0
    alen, blen = len(apa), len(bepa)
    while True:
        if aind >= alen:
            return cepa + bepa
        elif bind >= blen:
            return cepa + apa
        else:
            if apa[aind] < bepa[bind]:
                cepa += apa[aind:aind+1]
                aind += 1
            else:
                cepa += bepa[bind:bind+1]
                bind += 1



rl = [random.random() for k in range(10)]
print(rl)
for k in mysort(rl):
    print(k)
    