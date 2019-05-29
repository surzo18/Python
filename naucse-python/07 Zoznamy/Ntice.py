#Chovají skoro stejně jako seznamy, jen nejdou měnit. Nemají tedy metody jako append a pop a nedá se jim přiřazovat do prvků. Dají se ale použít v cyklu for a dají se z nich číst jednotlivé prvky.

osoby = 'máma', 'teta', 'babička' # touple / NTICE
for osoba in osoby:
    print(osoba)
print('První je {}'.format(osoby[0]))

seznam_dvojic = []
for i in range(10):
    # `append` bere jen jeden argument; dáme mu jednu dvojici
    seznam_dvojic.append((i, i**2))#Ntice uzavreta v zatvorkach
print(seznam_dvojic)

x, o = 'xL'
jedna, dva, tri = [1, 2, 3]

print(x)
print(o)
print(dva)

#Funkce Vracejici Ntici
osoby = 'máma', 'teta', 'babička', 'vrah'
vlastnosti = 'hodná', 'milá', 'laskavá', 'zákeřný'
for osoba, vlastnost in zip(osoby, vlastnosti): #ZIP FUNKCE
    print('{} je {}'.format(osoba, vlastnost))

#Další funkce, která vrací dvojice, je enumerate.
#Jako argument bere seznam (či jinou věc použitelnou ve for) a 
# vždy spáruje index (pořadí v seznamu) s příslušným prvkem.
#  Jako první tedy dá (0, první prvek seznamu), potom (1, druhý prvek seznamu),
#  (2, třetí prvek seznamu) a tak dále.

prvocisla = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
for i, prvocislo in enumerate(prvocisla):
    print('Prvočíslo č.{} je {}'.format(i, prvocislo))

prazdna_ntice = ()
jednoprvkova_ntice = ('a', ) #vsimnut si ciarku

