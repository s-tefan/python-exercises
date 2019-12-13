a=23
b=42
c=99
def apa():
    a=123
    b=142
    c=199
    def bepa():
        nonlocal b
        global c
        a=323
        b=342
        c=399
        print('bepa:',a,b,c)
    print('apa:',a,b,c)
    bepa()
    print('apa:',a,b,c)

print('global:',a,b,c)
apa()
print('global:',a,b,c)

    
    
