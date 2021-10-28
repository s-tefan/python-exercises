# python 3.10

def apa():
    while True:
        x = input()
        match x.split():
            case [apa, '+', bepa]:
                print(eval(apa)+eval(bepa))
            
def bepa():
    for x in ["apa > bepa", "apa", "apa > bepa cepa", "apa bepa > cepa depa"]:
        match x.split():
            case [ap, '>', bep]:
                print("{0} implies {1}".format(ap, bep))
            case [ap, '>', *bep]:
                print("{0} implies {1}".format(ap, bep))
            case [*ap, '>', bep]:
                print("{0} implies {1}".format(ap, bep))


bepa()
