

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

        hello