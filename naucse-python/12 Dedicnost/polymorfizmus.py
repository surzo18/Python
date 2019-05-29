lass Zviratko:
    def __init__(self, jmeno):
        self.jmeno = jmeno

    def snez(self, jidlo):
        print("{}: {} mi chutná!".format(self.jmeno, jidlo))


class Kotatko(Zviratko):
    def zamnoukej(self):
        print("{}: Mňau!".format(self.jmeno))


class Stenatko(Zviratko):
    def zastekej(self):
        print("{}: Haf!".format(self.jmeno))

zviratka = [Kotatko('Micka'), Stenatko('Azorek')] #JE NAM JEDNO AKE ZVIERATKO TO JE

for zviratko in zviratka:
    zviratko.snez('flákota')