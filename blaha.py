class Nonsens:
    pass


a=Nonsens()
a.apa=23
a.bepa= lambda : a.apa

print(a.bepa())

