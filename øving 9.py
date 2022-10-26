

#d) Lag en klasse for en avtale. En avtale skal minimum ha:
#a. En tittel som sier hva denne avtalen er (streng)
#b. Et sted (streng)
#c. Et starttidspunkt (datetime objekt, se hint nederst)
#d. En varighet i minutter (int)
import (datetime)

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
        return f"Navn :{self.tittel}, Sted: {self.sted}, Starttidspunkt: {self.starttidspunkt}, Varighet: {self.varighet}, tema {self.tema}"
#f) Lag en funksjon som lar brukeren skrive inn en ny avtale. Funksjonen skal bruke input-
#funksjonen til å lese inn egenskapene til avtalen og skal sjekke at det brukeren skriver er
#gyldig, for eksempel at varighet er et tall. Funksjonen skal returnere et avtale-objekt

    def ny_avtale (self): #f
       while True:
            try:
                tittel = input("skriv inn ny tittel:"))

                sted = input("skriv inn ny sted:"))

                starttidspunkt = int(input("skriv inn ny starttidspunkt:"))

                varighet = int(input("skriv inn ny varighet:"))

                tema = input("skriv inn ny tema:"))

            except:
                print("ikke gyldig avtale prøv på nytt")

            else:
                break


        return ny_avtale

#g) Lag en funksjon som skriver ut ei liste med avtaler til skjermen. Funksjonen skal minimum
#skrive ut indeksen til avtalen i lista og tittel til avtalen. Den kan alternativt skrive ut indeksen
#til avtalen og så hele avtalen som definert i __str__ metoden. Funksjonen skal ha en frivillig
#parameter «overskrift» som skal være en overskrift som funksjonen skriver ut før avtalene i
#lista. Funksjonen skal inkludere indeksen til hver avtale i utskriften.

    def listemedavtaler
