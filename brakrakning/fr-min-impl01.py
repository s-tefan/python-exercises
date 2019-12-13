# Modulen fr
#
# Diverse funktioner som handskas med bråk, representerade som
# talpar (n,d), där n och d är heltal
# Försök inte hitta färdiga paket som implementerar, utan använd
# helst bara inbyggda grundfunktioner och -operationer

def fraction(n,d):
    # givet två argument, täljare (numerator) n och nämnare (denominator) d
    # returnera ett talpar som representerar bråket.
    # Ex: fraction(5,3) ----> (5,3)
    return (n,d)

def fractionString(q):
    # returnerar en strängrepresentation av bråket som
    # representeras av talparet q=(n,d)
    # förslagsvis som "(n/d)"
    pass # ersätt med kod
    return("({}/{})".format(q[0],q[1]))
    
def fix(q):
    # Denna funktion ska , då man bestämt sig för en kanonisk representation
    # av ett rationellt tal som ett bråk returnera denna kanoniska representation.
    # Till exempel bör den kanoniska representationen inte ha gemensamma delare
    # i täljaren och nämnare och funktionen bör då returnera ett ekvivalent bråk
    # som är förkortat på lämpligt sätt.
    # Finns det andra villkor som en kanonisk representation bör ha
    # för att vara entydig?
    # Andra funktioner bör där det behövs använda denna funktion för att returnera sitt resultat.
    return q # Som utgångspunkt returnerar funktionen samma bråk som den fick som arument

def numerator(q):
    # returnerar täljaren till q som ett heltal, <class 'int'>
    pass # ersätt med kod
    return q[0]

def denominator(q):
    # returnerar nämnaren till q som ett heltal, <class 'int'>
    pass # ersätt med kod
    return q[1]

def toFloat(q):
    # returnerar ett flyttal, <class 'float'>, som approximerar bråket
    pass # ersätt med kod
    

def integralPart(q):
    # returnera heltalsdelen av bråket q
    # designfråga: hur ska det funka för negativa tal?
    pass # ersätt med kod

def fractionalPart(q):
    # returnera bråkdelen, dvs q minus heltalsdelen, som ett bråk
    pass # ersätt med kod

def prod(a,b):
    # returnerar produkten av bråken a och b som ett bråk (talpar)
    return fix(fraction(numerator(a)*numerator(b),denominator(a)*denominator(b)))


        
def recipr(q):
    # returnerar, givet bråket q,  1/q som ett bråk (talpar)
    pass # ersätt med kod

def quotient(a,b):
    # returnerar kvoten av bråken a och b som ett bråk (talpar)
    pass # ersätt med kod

def sum(a,b):
    # returnerar summan av bråken a och b som ett bråk (talpar)
    pass # ersätt med kod
    
def minus(q):
    # returnerar -q som bråk
    pass # ersätt med kod

def diff(a,b):
    # returnerar a-b
    pass # ersätt med kod

# Konstruera gärna andra funktioner som du skulle vilja ha.


# Det är fritt fram, och rekommenderas, att deiniera upp hjälpfunktioner
# används av "användarfunktionerna", till exempel en funktion som
# bestämmer största gemensamma delare till två heltal.


# Testprogram, man kan välja vilka test man ska köra
def test(testval):
    for k in testval:
        print("#{}# ".format(k))

        if k==1:
            #1 Skapa och skriv ut ett bråk
            print(fractionString(fraction(5,7)))
        if k==2:
            #2 Dito, men förkortningsbart
            print(fractionString(fraction(42,12)))
        if k==3:
            #3 Heltalsdel och bråkdel
            q=fraction(42,12)
            print(fractionString(integralPart(q)),
                  fractionString(fractionalPart(q))
                  )
        if k==4:
            #4 Produkt
            a=fraction(3,20)
            b=fraction(5,12)
            c=prod(a,b)
            print("{} * {} = {}".format(fractionString(a),fractionString(b),fractionString(c)))
            
        if k==5:
            #5 Summa
            a=fraction(3,20)
            b=fraction(5,12)
            c=sum(a,b)
            print("{} + {} = {}").format(fractionString(a),fractionString(b),fractionString(c))

        if k==6:
            #6 Kvot
            a=fraction(3,20)
            b=fraction(5,12)
            c=quotient(a,b)
            print("{} / {} = {}").format(fractionString(a),fractionString(b),fractionString(c))
            



#if __name__ == "__main__":
    # Om modulen körs som ett program, inte importeras, kör följande
test([1,2,4]) #   Kör test från listan av val av test, justera listan
    # efter vad du vill testa
    
    

