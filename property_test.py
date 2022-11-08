class Burk:
    
    @property
    def etikett(self):
        print(f"Etiketten är {self._etikett}")
        return self._etikett
    
    @etikett.setter
    def etikett(self, etikett):
        print(f"Sätter etikett till {etikett}")
        self._etikett = etikett
    
    @etikett.deleter
    def etikett(self):
        print(f"Tar bort {self._etikett}")
        del self._etikett


b = Burk()
b.etikett = "Bullens"
print(b.etikett)
del b.etikett
print(b.etikett) # Här blir det AttributeError, som det ska
