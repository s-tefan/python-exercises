def deco(func):
    def wrapper(*args, **kwargs): # Skapa ett omslag till funktionen i argumentet
        print("Hej!")
        return func(*args, **kwargs) # args och kwargs är argumenten som skickas med
        print("Hej då!")
    return wrapper # Returnera omslagsfunktionen

def afunk():
    print("Läget?")

deco(afunk)() # Applicera dekoratorn deco direkt på afunk

@deco # Applicera dekoratorn deco genom syntaktiskt socker
def bilen():
    print("Och bilen går bra?")

@deco
def politelysay(something):
    print(something)
    return "Hen sa: "+something

bilen()
print(politelysay("Men för fan!"))