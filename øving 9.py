

#d) Lag en klasse for en avtale. En avtale skal minimum ha:
#a. En tittel som sier hva denne avtalen er (streng)
#b. Et sted (streng)
#c. Et starttidspunkt (datetime objekt, se hint nederst)
#d. En varighet i minutter (int)


class Avtale: #a
    def __init__(self, tittel,sted, starttidspunkt=0, varighet=0):
        self.tittel = tittel
        self.sted = sted
        self.starttidspunkt = starttidspunkt
        self.varighet = varighet

#e) Lag en __str__ metode for avtaler som returnerer en streng som kan skrives ut med en print-
#setning slik at du får skrevet ut avtalen med alle egenskapene til avtalen på et leselig format
#for brukeren.


    def __str__(self):
        return f"Navn :{self.tittel}, Sted: {self.sted}, Starttidspunkt: {self.starttidspunkt}, Varighet: {self.varighet}"
#f) Lag en funksjon som lar brukeren skrive inn en ny avtale. Funksjonen skal bruke input-
#funksjonen til å lese inn egenskapene til avtalen og skal sjekke at det brukeren skriver er
#gyldig, for eksempel at varighet er et tall. Funksjonen skal returnere et avtale-objekt

    def ny_avtale (self): #f
        while True:
            try:
                avtale = float(input("skriv inn avtale 1:"))
                break
            except:
                print("ikke gyldig input prøv på nytt")




