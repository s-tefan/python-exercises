def vlq(xx):
    bytelist = []
    outbytelist = []
    for x in xx:
        while x != 0:
            tail = x % 128
            x = x // 128
            bytelist.append(tail)
        while len(bytelist) > 1:
            bb = bytelist.pop()
            outbytelist.append(bb + 0x80)
        bb = bytelist.pop()
        outbytelist.append(bb)
    return outbytelist

def vlq_decode(bytelist):
    outlist = []
    x = 0
    for b in bytelist:
        if b >= 128:
            x = x*128 + (b-128)
        else:
            x = x*128 + b
            outlist.append(x)
            x = 0
    return outlist

def testvlq():
    apa = vlq([300000,400000,500000])
    print(apa)
    print(bytes(apa))
    bepa = vlq_decode(apa)
    print(bepa)


class LZW:
    def __init__(self, std=True):
        self.codepage = {}
        self.code = []
        if std:
            self.nextcode = 256
            for n in range(self.nextcode):
                self.codepage[chr(n)] = n

    def addtocodepage(self, s):
        self.codepage[s] = self.nextcode
        self.nextcode += 1


    def encode(self, input):
        # encodes a string input
        s = ""
        buf = []
        for c in input:
            if s+c in self.codepage:
                s += c
            else:
                if s: # don't code empty string
                    self.code.append(self.codepage[s])
                self.addtocodepage(s+c)
                s = c
        if s :
            self.code.append(self.codepage[s])


    def decode(self,code):
        for c in code:
            pass

    def printcode(self):
        print(self.code)

  

def testlzw():
    mylzw = LZW()
    mylzw.encode('ABABABBAABAAAABBBAABBBBABABABBBBBAB')
    mylzw.printcode()
    print(mylzw.codepage)

testlzw()