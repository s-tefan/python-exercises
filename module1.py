import poly

print('?')
p1=poly.Polynomial([1,2])
p2=poly.Polynomial([3,4])
p3=p1.product_var(p2)
p3.print()
(p1*p2).print()
print(p1+p2)
(p1+p2).print()
dr=poly.Polynomial([5,5,0,3,0,2]).divrem(poly.Polynomial([1,0,2]))
dr[0].print()
dr[1].print()
print('!')