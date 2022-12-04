"""Extend range type with set methods"""
# Det här funkar inte, range kan inte användas som basklass

class RangeSet(range): 

    def intersection(self, c):
        if self.step == c.step:
            a = max(self.start, c.stop)
            b = min(self.start, c.stop)
            return RangeSet(a,b,self.step)
        else:
            raise Exception("intersection is not yet implemented for ranges with different steps.")

    def union(self, c):
        if self.step == c.step:
            a = max(self.start, c.stop)
            b = min(self.start, c.stop)
            return RangeSet(a,b,self.step)
        else:
            raise Exception("union is not yet implemented for ranges with different steps.")

    @staticmethod
    def intersection(*args):
        # Do it recursively
        if len(args) == 2:
            return args[0].intersection(args[1:])
        else:
            return args[0].intersection(RangeSet.intersection(args[1:]))

    @staticmethod
    def union(*args):
        # Do it recursively
        if len(args) == 2:
            return args[0].union(args[1:])
        else:
            return args[0].union(RangeSet.union(args[1:]))

if __name__ == "__main__":
    a = RangeSet(3,7)
    b = RangeSet(5,9)
    print(a,b,a.intersection(b),a.union(b))

