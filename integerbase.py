def int_to_base(n, base):
    if not isinstance(n, int):
        raise ValueError()
    if base < 0:
        n = - n
        base = - base
    digits = []
    if n > 0:
        while n != 0:
            digit = n % base
            n = n // base
            digits.append(digit)
    elif n < 0:
        while n != 0:
            digit = n % (-base)
            n = - ((-n) // base)
            digits.append(digit)
    return digits


for k in {2345, -2345}:
    print(int_to_base(k,10))
    

for k in {2345, -2345}:
    print(int_to_base(k,-10))
    