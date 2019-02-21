
def ytter():
    #global a
    def inner():
        #nonlocal a
        print(a,id(a),'inne i inner')
        a+=1
        print(a,id(a),'inne i inner')
    print(a,id(a),'inne i ytter')
#    a+=1
    print(a,id(a),'inne i ytter')
    #inner()



a=1
print(a,id(a),'ute i rymden')
ytter()
print(a,id(a),'ute i rymden')


def blabla():
    def clacla():
        print('b',b,id(b))
    #b=1
    clacla()
b=23
blabla()

import scopeTestModul
print(scopeTestModul.rapadapp)
