# Typ objektu umí zjistit funkce type:
type(0)
type(True)
type("abc")


# with open('soubor.txt') as f:
#    type(f)
# vypise : <class '_io.TextIOWrapper'>

class Macka:
    def __init__(self, jmeno):
        self.jmeno = jmeno

    #Podobných „opodtržítkovaných“ metod je víc,
    #  třeba __str__ se volá, když je potřeba
    #  převést objekt na řetězec:
    def __str__(self):
        return '<Kotatko jmenem {}>'.format(self.jmeno)

    def zamnaukaj(self):
        print("{}: Mňau!".format(self.jmeno))

    
    def snez(self, jidlo):
        print("{}: Mňau mňau! {} mi chutná!".format(self.jmeno, jidlo))

"""
# Vytvoření konkrétního objektu
macka = Macka()

# Volání metody
macka.zamnaukaj()
"""
mourek = Macka(jmeno='Mourek')

micka = Macka(jmeno = "Tata")

mourek.zamnaukaj()
micka.zamnaukaj()
mourek.snez("jablko")

print(mourek.__str__())
#micka.zamnaukaj = 12345
#micka.zamnaukaj() Metoda nepojde prepise sa pravdepodobne v pameti

#---------------------------------------------

def __init__(self):         # Init funkce nemusi brat jako parametr
        self.pocet_zivotu = 9   # pocet zivotu, ten je pokazde 9.

def zamnoukej(self):
        print("Mnau, mnau, mnauuu!")

    def je_ziva(self):
        return self.pocet_zivotu > 0

    def uber_zivot(self):
        if not self.je_ziva():
            print("Nemuzes zabit uz mrtvou kocku!")
        else:
            self.pocet_zivotu -= 1

    def snez(self, jidlo):
        if not self.je_ziva():
            print("Je zbytecne krmit mrtvou kocku!")
            return
        if jidlo == "ryba" and self.pocet_zivotu < 9:
            self.pocet_zivotu += 1
            print("Kocka spapala rybu a obnovil se ji jeden zivot.")
        else:
            print("Kocka se krmi.")