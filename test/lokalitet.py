apa = 23
bepa = [1,2,3]

def blupp(n):
    print(apa) # Det här går bra, kan referera till namnet utanför
    #apa+=n # Här går det inte, kan bara ändra värde på lokala variabler
    #print(apa)
    bepa[0]=4 # Det här går bra, ändrar inte bepa, utan ett refererat värde
    print(bepa)

blupp(4)
blupp(-2)


