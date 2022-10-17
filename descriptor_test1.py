class Brunkel:
    def __init__(self, exclamation = "!"):
        self.exclamation = exclamation
    def __get__(self, obj, type=None):
        return self.exclamation

class Bracka:
    brunk = Brunkel("Bracka!")
    def __init__(self, exclamation = None):
        if exclamation:
            self.brunk = Brunkel(exclamation) # Nä, descriptors funkar bara som klassattribut, inte per instans


brack = Bracka()
print(brack.brunk)
putain = Bracka("Putain!")
print(putain.brunk)
print(brack.brunk)
