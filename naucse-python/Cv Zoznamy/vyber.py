zoznam=['pepa novák', 'Jiří Sládek', 'Ivo navrátil', 'jan Poledník','Ahoj Svet']

def zleZaznamy(zoznam):

def opraveneZaznamy(zoznam):

def dobreZaznamy(zoznam):
    novyZoznam=[]
    for zaznam in zoznam:
        zaznam = zaznam.split()
        novyZaznam = []
        if len(zaznam) == 2 :
           for slovo in zaznam:
                if slovo[0] == slovo[0].upper():
                   novyZaznam.append(slovo)
                else:
                    novyZaznam = []
                    break
        if(len(novyZaznam)==2):
          vyraz = " ".join(novyZaznam)
          novyZoznam.append(vyraz)
    return novyZoznam

menaVelkeInicialy = dobreZaznamy(zoznam)
print(menaVelkeInicialy)


