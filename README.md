# Apekatter
 # 8

class Land: #a
    def __init__(self, navn, befolkning=0, areal=0):
        self.navn = navn
        self.befolkning = befolkning
        self.areal = areal

    def __str__(self): #b
        return f"Navn :{self.navn}, Befolkning: {self.befolkning}, Areal: {self.areal}"

    def tetthet(self): #c
        tetthet = self.befolkning/self.areal
        return tetthet


def storst_befolkning(land1, land2): #d
    if land1.befolkning > land2.befolkning:
        return land1
    else:
        return land2

def readBefolkning(): #e
    file = open("befolkning_tabell_csv.txt", "r", encoding="utf8")
    landDict = {}
    for line in file:
        navn, befolkning = line.split(";")
        befolkning = int(befolkning)
        land = Land(navn,befolkning)
        landDict[navn] = land
    file.close()
    return landDict

def readAreal(landDict): #f
    file = open("areal_tabell_csv.txt", "r", encoding="utf8")
    for line in file:
        navn, areal = line.split(";")
        areal = int(areal)
        if navn in landDict:
            landDict[navn].areal = areal
        else:
            print(f"Landet {navn} er ikke i dictionary!")
    file.close()
    return landDict


def loopOgPrint(landDict): #g
    for key in landDict:
        land = landDict[key]
        if land.befolkning > 0 and land.areal > 0:
            print(f"{land} Tetthet: {str(land.tetthet())}")
        else:
            print(f"{land.navn} har ikke satt areal!")

def storstTetthet(landDict): #h
    firstrun = True
    for key in landDict:
        land = landDict[key]
        if firstrun:
            storst = land
            firstrun = False
        else:
            if land.befolkning > 0 and land.areal > 0:
                if land.tetthet() > storst.tetthet():
                    storst = land
            else:
                print(f"{land.navn} har ikke satt areal eller befolkning!")
    print(f"{storst.navn} har høyest befolkningstetthet")


if __name__ == "__main__":
    landDict = readBefolkning() #e
    landDict = readAreal((landDict)) #f
    print()
    loopOgPrint(landDict) #g
    print()
    storstTetthet(landDict) #h
