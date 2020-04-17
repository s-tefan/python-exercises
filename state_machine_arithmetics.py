class binaryadder:
    def __init__(self):
        self.state = False
    
    def toggle(self):
        self.state = not self.state

    def bitadd(self, bita, bitb):
        # self.state: there is a carry 
        if self.state:
            self.state = bita or bitb
            return bool(bita) == bool(bitb)
        else:
            self.state = bita and bitb
            return not(bool(bita) == bool(bitb))
    
    def bitsub(self, bita, bitb):
        # self.state: there is a loan
        if self.state:
            self.state = (not bita) or bitb 
            return (bool(bita) == bool(bitb))
        else:
            self.state = (not bita) and bitb
            return not (bool(bita) == bool(bitb))

    def add(self, inta, intb):
        a, b = inta, intb
        result = 0
        step = 1
        while a or b:
            if self.bitadd(a & 1, b & 1):
                result |= step
            print("a = {}, b = {}, c = {}, result = {}".format(a,b,self.state,result))
            a >>= 1
            b >>= 1
            step <<= 1
        print("a = {}, b = {}, c = {}, result = {}".format(a,b,self.state,result))
        if self.state:
            result |= step
            self.toggle()
        print("a = {}, b = {}, c = {}, result = {}".format(a,b,self.state,result))
        return result

sm = binaryadder()

print( sm.add(23,42))








