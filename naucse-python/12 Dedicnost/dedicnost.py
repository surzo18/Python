class Zviratko:
    def __init__(self, jmeno):
        self.jmeno = jmeno

    def snez(self, jidlo):
        print("{}: {} mi chutná!".format(self.jmeno, jidlo))


class Kotatko(Zviratko): #class Kotatko(Zviratko): Zdedenie Zvieratka
    def zamnoukej(self):
        print("{}: Mňau!".format(self.jmeno))

    def snez(self, jidlo):
        print("{}: {} mi vůbec nechutná!".format(self.jmeno, jidlo))
        super().snez(jidlo) # zavola aj funkciu z nadtriedy zviera 
        #Pozor na to, že takhle volané metodě musíš dát všechny argumenty,
        #  které potřebuje (kromě self, který se jako obvykle doplní automaticky).
        #  Toho se dá i využít – můžeš použít i jiné argumenty než dostala původní funkce:


class Stenatko(Zviratko):
    def zastekej(self):
        print("{}: Haf!".format(self.jmeno))

micka = Kotatko('Micka')
azorek = Stenatko('Azorek')
micka.zamnoukej()
azorek.zastekej()
micka.snez('myš')
azorek.snez('kost')

class Hadatko(Zviratko):
    def __init__(self, jmeno):
        jmeno = jmeno.replace('s', 'sss')
        jmeno = jmeno.replace('S', 'Sss')
        super().__init__(jmeno)


standa = Hadatko('Stanislav')
standa.snez('myš')