"""
Illustrating namespaces for instance and class attributes.
Python first searches the namespace for the instance of the object,
if not found then the namespace for its class.
"""


class Apa:
    ap = 23 # sets a class attribute

    def __init__(self):
        self.bep = 42 # sets an instance attribute 'bep'
    def set(self, x):
        self.ap = x # sets the instance attribute 'ap'
    def cls_set(self, x):
        type(self).ap = x # sets the class attribute 'Apa.ap'
    
apa = Apa()
print(apa.ap, apa.bep, type(apa).ap) # As 'apa.ap' is not set as an instance attribute, the class attribute value 'Apa.ap' is used
apa.set(97) # Sets the instance attribute 'apa.ap' 
print(apa.ap, apa.bep, type(apa).ap) # Now 'apa.ap' is a distinct attribute
apa.cls_set(93) # Sets the class attribute 'Apa.ap'
print(apa.ap, apa.bep, type(apa).ap)
