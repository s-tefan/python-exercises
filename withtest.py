class grej:
    def __enter__(self):
        print("Startar!")
    def __exit__(self,type,value,traceback):
        print("Slutar!")

with grej() as x:
    print("Gör!")
    pass
