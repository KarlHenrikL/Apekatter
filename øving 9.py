#sondre er gay

import (datetime)

liste= []

class Avtale: #a
    def __init__(self, tittel,sted, starttidspunkt=0, varighet=0):
        self.tittel = tittel
        self.sted = sted
        self.starttidspunkt = starttidspunkt
        self.varighet = varighet

    def hovedmeny(start):
        while start == 1:
            print("1: Les inn avtaler fra fil")
            print("2: Skriv avtalene til fil")
            print("3: Skriv inn en ny avtale")
            print("4: Skriv ut alle avtalene")
            print("5: Slett en avtale")
            print("6: Rediger en avtale")
            print("0: Avslutt")
            valg = int(input("velg et alternativ: "))
            if valg == 1:
                avtaler_fra_fil()
            elif valg == 2:
                avtaler_til_fil()
            elif valg == 3:
                ny_avtale()
            elif valg == 4:
                skriv_ut_alle_avtaler()
            elif valg == 5:
                slette_avtale()
            elif valg == 6:
                redigere_avtale()
            elif valg == 7:
                exit
            else:
                print("Ugyldig svar, vennligst bruk 1-6")
        return hovedmeny(1)
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


#h)Lag en funksjon som lagrer ei liste med avtaler til ei tekstfil. Tenk over hva som vil være et 
#fornuftig format for ei slik tekstfil.
def _lagAvtale():
    avtaleListe.append(lagAvtale())

def lagAvtale():
    print("Du skriver nå en ny avtale:")
    return Avtale(input("Tittel: "),input("Sted: "),trydate("Dato (yyyy-mm-dd): "), trytime("Tid (hh:mm): "),tryint("Varighet (minutter): "),input('Personer: ').split(','))

#append() insert() variabel.extend(det man vil legge til).
#i)Lag en funksjon som leser inn ei liste med avtaler fra ei tekstfil på samme format som dere 
#definerte for funksjonen som skriver fila med avtaler. 
def velgAvtale():
    if(len(avtaleListe)==0): return -1
    try:
        i= int(input(f"Velg en avtale [0-{len(avtaleListe)-1}]: "))
    except:
        return velgAvtale("Angitt verdi ikke gjenkjent som heltall. Prøv igjen: ")
    if(i<0):
        return 0
    if(i>=len(avtaleListe)):
        return len(avtaleListe)-1
    return i

#j)Lag en funksjon som tar inn ei liste med avtaler og en dato og returnerer ei liste med alle 
#avtalene som foregår på denne datoen. Funksjonen trenger bare å sjekke om datoen 
#stemmer med dato-delen av starttidspunktet til avtalen. 

def _endreAvtale(i=-1): #n
    if i==-1: i=velgAvtale()
    if i==-1: return
    p=[
       f"Tittel: {avtaleListe[i].tittel}",
       f"Sted: {avtaleListe[i].sted}",
       f"Dato: {avtaleListe[i].dato}",
       f"Tid: {avtaleListe[i].tid}",
       f"Varighet: {avtaleListe[i].varighet}min",
       f"Personer: {avtaleListe[i].personerStreng()}",
       "Lagre og gå ut"
       ]
    for j in range(len(p)):
        print(str(j+1)+" "+p[j])
    j=int(input("Endre eller gå ut [1-7]: "))-1
    
    if j==0:
        avtaleListe[i].tittel=input("Ny tittel: ")
    elif j==1:
        avtaleListe[i].sted=input("Nytt sted: ")
    elif j==2:
        avtaleListe[i].date=trydate("Ny dato [yyyy-: ")
    elif j==3:
        avtaleListe[i].date=trydate("Ny tid [hh:mm]: ")
    elif j==4:
        avtaleListe[i].varighet=tryint("Ny varighet: ")
    elif j==5:
        avtaleListe[i].personer=input("Nye personer: ").split(',')
    
    if not j==6: _endreAvtale(i)
