class Heap:
    @classmethod 
    def comp(cls, a, b):
        return a > b # for max-heap
        # return a < b # for min-heap

    def __init__(self):
        self.h = [None]

    def push(self, obj):
        n = len(self.h)
        self.h.append(obj)
        while n>1 and Heap.comp(self.h[n], self.h[n >> 1]): 
            self.swap(n, n>>1)
            n >>= 1
    
    def swap(self,n,m):
        temp = self.h[n]
        self.h[n] = self.h[m]
        self.h[m] = temp
    ''' ta itu med sen
    def pop(self, n):
        hlen = len(self.h)
        if hlen <= 1:
            raise Exception("Heap is empty")
        elif n+1 < hlen >> 1:
            if Heap.comp(self.h[n << 1], self.h[(n << 1) | 1]):
                self.h[n] = self.pop(n << 1)
            else:
                self.h[n] = self.pop((n << 1) | 1)
        elif n << 1 == hlen:
            self.h[n] = self.pop(n << 1)
        else:
            self.h[]         
            m = n << 1
            if m == hlen:
'''

class Heap2:
    @staticmethod
    def comp(a,b):
        return a > b # or any order
    @staticmethod
    def heapify(li):
        for k, a in enumerate(li):
            while k > 0:
                parind = ((k+1) >> 1) -1
                b = li[parind]
                if Heap2.comp(a,b):
                    li[parind] = a
                    li[k] = b
                    k = parind
                else:
                    break
    @classmethod
    def pop(cls, heap):
        a = heap.pop(0)
        cls.heapify(heap)
        return a

    @classmethod
    def heapsort(cls, li):
        '''funkar inte riktigt'''
        cls.heapify(li)
        for k in range(len(li)):
            lili = li[k:]
            li[k] = cls.pop(lili)
            li[k+1:] = lili


apa = range(10)
hipster = Heap()
for k in apa:
    hipster.push(k)
print(hipster.h)

hip2 = list(range(1000))
Heap2.heapsort(hip2)
print(hip2[0],hip2[-1])