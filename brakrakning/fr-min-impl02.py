# Modulen fr
# mall version 0.2
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
    if denominator(q)>0:
        return q
    else:
        return fraction(-numerator(q),-denominator(q))
    # Som utgångspunkt returnerar funktionen ett likvärdigt bråk med positiv nämnare


def numerator(q):
    # returnerar täljaren till q
    return q[0]

def denominator(q):
    # returnerar nämnaren till q
    return q[1]


def toFloat(q):
    # returnerar ett flyttal som approximerar bråket
    return numerator(q)/denominator(q)
    

def integralPart(q):
    # returnera heltalsdelen av bråket q
    # designfråga: hur ska det funka för negativa tal?
    # designfråga: ska resultatet vara av heltalstyp eller av bråktalstyp?
    # Påverkar hur funktionen kan användas.
    return numerator(q)//denominator(q) # returnerar heltal

def fractionalPart(q):
    # returnera bråkdelen, dvs q minus heltalsdelen, som ett bråk
    n=numerator(q)
    d=denominator(q)
    ip=integralPart(q)
    return fraction(n-ip*d,d)

#### Aritmetiska operationer

def prod(a,b):
    # returnerar produkten av bråken a och b som ett bråk (talpar)
    return fix(fraction(numerator(a)*numerator(b),denominator(a)*denominator(b)))

def recipr(q):
    # returnerar, givet bråket q,  1/q som ett bråk (talpar)
    return fix(fraction(denominator(q),numerator(q)))

def quotient(a,b):
    # returnerar kvoten av bråken a och b som ett bråk (talpar)
    return fix(prod(a,recipr(b)))


def sum(a,b):
    # returnerar summan av bråken a och b som ett bråk (talpar)
    return fix(fraction(numerator(a)*denominator(b)+numerator(b)*denominator(a),
                        denominator(a)*denominator(b)))
    # Kan effektiviseras genom att kolla minsta gemensamma nämnare först.

def minus(q):
    # returnerar -q som bråk
    return fix(-numerator(q),denominator(q))

def diff(a,b):
    # returnerar a-b
    return sum(a,minus(b))

## Jämförelser mellan bråk

def eq(a,b): # 'equals'
    # returnera True om a och b är bråk som representerar samma rationella tall, annars False
    # Implementera så att det fungerar även om bråken inte är förkortade
    # Ex: eq(fraction(-12,11),fraction(24,-22) ska alltså ge värdet True
    return numerator(a)*denominator(b)==numerator(b)*denominator(a)

def lt(a,b): # 'less than'
    # returnera True om a<b för bråk a och b, annars False
    # Observera kommentarerna för eq
    aa=fix(a)
    bb=fix(b)
    # Behöver se till att nämnarna är positiva, annars blir det fel
    return numerator(aa)*denominator(bb)<numerator(bb)*denominator(aa)
    

def gt(a,b): # 'greater than', '
    # returnera True om a>b för bråk a och b, annars False
    # Observera kommentarerna för eq
    aa=fix(a)
    bb=fix(b)
    # Behöver se till att nämnarna är positiva, annars blir det fel
    return numerator(aa)*denominator(bb)>numerator(bb)*denominator(aa)
    


# Konstruera gärna andra funktioner som du skulle vilja ha.


# Det är fritt fram, och rekommenderas, att deiniera upp hjälpfunktioner
# används av "användarfunktionerna", till exempel en funktion som
# bestämmer största gemensamma delare till två heltal.

######################################################
# Testprogram, man kan välja vilka test man ska köra
# test(testlista) kör i tur och ordning testen med nummer i listan testlista
# Testprogrammen bör du inte ändra koden i, men studera dem för att se vad de gör.

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
            heltalsdel=integralPart(q)
            brakdel=fractionalPart(q)
            if type(heltalsdel)==type(q): # Om heltalsdelen är ett bråk, använd fractionstring
                hdstr=fractionstring(q)
            else: # Annars (om det är tex av heltalstyp), använd standardsträngrepresentationsfunktionen str
                hdstr=str(q)
            print(hdstr,
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
            print("{} + {} = {}".format(fractionString(a),
                                         fractionString(b),
                                         fractionString(c)))

        if k==6:
            #6 Kvot
            a=fraction(3,20)
            b=fraction(5,12)
            c=quotient(a,b)
            print("{} / {} = {}".format(fractionString(a),fractionString(b),fractionString(c)))

        if k==7:
            #7 Jämförelser
            a=fraction(-12,11)
            b=fraction(24,-22)
            print("{} == {} is {}".format(fractionString(a),fractionString(b),eq(a,b)))
            print("{} < {} is {}".format(fractionString(a),fractionString(b),lt(a,b)))
            print("{} > {} is {}".format(fractionString(a),fractionString(b),gt(a,b)))
            a=fraction(23,10)
            b=fraction(24,11)
            print("{} == {} is {}".format(fractionString(a),fractionString(b),eq(a,b)))
            print("{} < {} is {}".format(fractionString(a),fractionString(b),lt(a,b)))
            print("{} > {} is {}".format(fractionString(a),fractionString(b),gt(a,b)))
            a=fraction(-23,10)
            b=fraction(-24,11)
            print("{} == {} is {}".format(fractionString(a),fractionString(b),eq(a,b)))
            print("{} < {} is {}".format(fractionString(a),fractionString(b),lt(a,b)))
            print("{} > {} is {}".format(fractionString(a),fractionString(b),gt(a,b)))

            



#if __name__ == "__main__":
    # Om modulen körs som ett program, inte importeras, kör följande
    #   Kör test från listan av val av test, justera listan
    # efter vad du vill testa
test([1,2,3,4,5,6,7]) 

