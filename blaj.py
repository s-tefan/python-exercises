def summa(a,b,skrivut=False):
    if skrivut:
        print(f'{a} + {b} = {a+b}')
    return a+b

s=summa(4,5,True)
print(s)
s=summa(4,6)
print(s)

