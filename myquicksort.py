def myquicksort(apa):
    if apa:
        pivot = apa[0]
        tail = apa[1:]
        bepa = []
        cepa = []
        for k in tail:
            if k < pivot:
                bepa.append(k)
            else:
                cepa.append(k)
        return  myquicksort(bepa) + [pivot] + myquicksort(cepa)
    else:
        return []

import random
blaj = [random.random() for k in range(1000)]
blupp = myquicksort(blaj) 
print(blupp[0], blupp[-1])
    
