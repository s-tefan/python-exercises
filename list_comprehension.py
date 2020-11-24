
alist = list(range(5))
aalist = [ x for x in range(5)]
acartesianlist = [(x,y) for x in range(5) for y in range(3)]
anarray = [[(x,y) for y in range(5)] for x in range(3)]
apa = [ t for row in anarray for t in row]  # flattens anarray

blist = ["bagare", "bengtssons", "bullar"]
clist = ["cyklande", "cirkus"]
bclist = [(b,c) for b in blist for c in clist]
bcarray = [[(b,c) for c in clist] for b in blist]

print(bclist)
print(bcarray)
print([x for r in bcarray for x in r]) # flattens bcarray
# will not work in this order: print([x for x in r for r in bcarray])