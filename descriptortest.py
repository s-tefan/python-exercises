import logging

class Desco:
    def __get___(self, obj, objtype = None):
        print("Got it!")
        return 10

    def __set__(self, obj, value=None):
        print("Här sätts apa till", value)
        obj._apa = value

    def __delete__(self, obj):
        print("Äh")


class Blubb:
    apa = Desco()

blubb = Blubb()

print(blubb.apa)
blubb.apa = 7
print(blubb.apa)
#blubb.apa += 7
print(blubb.apa)


# Vet inte om det här funkar som tänkt...
  

