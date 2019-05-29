class Zviratko:
    def __init__(self, jmeno):
        self.jmeno = jmeno

    def snez(self, jidlo):
        print("{}: {} mi chutná!".format(self.jmeno, jidlo))


class Kotatko(Zviratko):
    def udelej_zvuk(self): #Generalizace
        print("{}: Mňau!".format(self.jmeno))


class Stenatko(Zviratko):
    def udelej_zvuk(self): #Generalizace
        print("{}: Haf!".format(self.jmeno))


zviratka = [Kotatko('Micka'), Stenatko('Azorek')]

for zviratko in zviratka:
    zviratko.udelej_zvuk() #Generalizace
    zviratko.snez('flákota')