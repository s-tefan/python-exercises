import operator

## Not att all implemented yet ...
class GameOfLife:
    def __init__(self, living):
        self.livingset = set(living)
        self.make_celldict()

    def make_celldict(self):
        self.celldict = {}
        for c in self.livingset:
            self.celldict[c] = {
                    'alive': True,
                    'neighbours': 0
            }
        for c in self.livingset:
            for k in (-1,0,1):
                for m in (-1,0,1):
                    if (k,m) != (0,0):
                        d = tuple(map(operator.add, c, (k,m)))
                        if d in self.celldict:
                            self.celldict[d]['neighbours'] += 1
                        else:
                            self.celldict[d] = {
                                'alive': False,
                                'neighbours': 1
                            }
    
    def generate(self):
        self.livingset = set({})
        for c in self.celldict:
            cc = self.celldict[c] 
            if cc['alive']:
                if cc['neighbours'] in {2,3}:
                    self.livingset.add(c)
            else:
                if cc['neighbours'] == 3:
                    self.livingset.add(c)
        self.make_celldict()

def printit(livingset):
    for r in range(-5,5):
        s = ''
        for k in range(-5,5):
            if (k,r) in livingset:
                s += 'o'
            else:
                s += ' '
        print(s)
    print()

gol = GameOfLife(((0,0),(1,0),(2,0),(0,1),(1,2)))
printit(gol.livingset)
#print(gol.celldict)
for k in range(1,30):
    gol.generate()
    printit(gol.livingset)
    input()
#    print(gol.celldict)
