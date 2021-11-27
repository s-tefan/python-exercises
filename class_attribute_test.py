"""
Illustrating namespaces for instance and class attributes.
Python first searches the namespace for the instance of the object,
if not found then the namespace for its class.
"""


class Apa:
    ap = 23
    def __init__(self):
        self.bep = 42
    def change(self, x):
        self.ap = x
    def cls_change(self, x):
        type(self).ap = x
    
apa = Apa()
print(apa.ap, apa.bep, type(apa).ap)
apa.change(97)
print(apa.ap, apa.bep, type(apa).ap)
apa.cls_change(93)
print(apa.ap, apa.bep, type(apa).ap)
