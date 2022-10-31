#sondre er gay

import (datetime)

liste= []

class Avtale: #a
    def __init__(self, tittel,sted, starttidspunkt=0, varighet=0):
        self.tittel = tittel
        self.sted = sted
        self.starttidspunkt = starttidspunkt
        self.varighet = varighet


    def __str__(self):
        return f"Navn :{self.tittel}, Sted: {self.sted}, Starttidspunkt: {self.starttidspunkt}, Varighet: {self.varighet}, tema {self.tema}"


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
if __name__ == "__main__":

#g) Lag en funksjon som skriver ut ei liste med avtaler til skjermen. Funksjonen skal minimum
#skrive ut indeksen til avtalen i lista og tittel til avtalen. Den kan alternativt skrive ut indeksen
#til avtalen og så hele avtalen som definert i __str__ metoden. Funksjonen skal ha en frivillig
#parameter «overskrift» som skal være en overskrift som funksjonen skriver ut før avtalene i
#lista. Funksjonen skal inkludere indeksen til hver avtale i utskriften.

    def listemedavtaler(liste, overskrift "avtaler"): #g
        for i, value in enumerate(liste):
            print (i, value)
    return liste
    def ListeAvAvtaleValg()
        #print (f"Hva er ønsket handling?")
        #print (f"For ny avtale: 1")
        #print (f"For å se avtale: 2")
        #print (f"For endring av avtale: 3")
        #print (f"For sletting av avtale: 4")
        #valg = (int(input(f"Valg : ")))
       # return valg

#h)Lag en funksjon som lagrer ei liste med avtaler til ei tekstfil. Tenk over hva som vil være et 
#fornuftig format for ei slik tekstfil.

    def list_avtale():
myFile = open('avtale.txt', 'w')
myDict = {'Roll': 4, 'Name': 'Joel', 'Language': 'Golang'}
myFile.write(str(myDict))
myFile.close()
myFile = open('avtale.txt', 'r')
print(myFile.read())

#i)Lag en funksjon som leser inn ei liste med avtaler fra ei tekstfil på samme format som dere 
#definerte for funksjonen som skriver fila med avtaler. 


#j)Lag en funksjon som tar inn ei liste med avtaler og en dato og returnerer ei liste med alle 
#avtalene som foregår på denne datoen. Funksjonen trenger bare å sjekke om datoen 
#stemmer med dato-delen av starttidspunktet til avtalen. 

    def redigereAvtale(): #n
        fila = open("avtaler.txt", "r")
        """for linje in fila:
            variabler = linje.split(;)
        """
