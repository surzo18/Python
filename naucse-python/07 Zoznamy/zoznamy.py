cisla = [1, 1, 2, 3, 5, 8, 13]
print(cisla)

for cislo in cisla:
    print(cislo)

print("novy zoznam")
seznam = [1, 'abc', True, None, range(10), len]
print(seznam)

prvocisla = [2, 3, 5, 7, 11, 13, 17]
print(prvocisla)
prvocisla.append(19)
print(prvocisla)

a = [1, 2, 3]   # vytvoření seznamu
b = a           # tady se nový seznam nevytváří

# seznam vytvořený v prvním řádku má teď dvě jména: "a" a "b",
# ale stále pracujeme jenom s jedním seznamem

print(b)
a.append(4)
print(b)

dalsi_prvocisla = [23, 29, 31]
prvocisla.extend(dalsi_prvocisla)#pripoji dalsi zoznam
print(prvocisla)

cisla = [1, 0, 3, 4]
cisla[1] = 2
print(cisla)

print("podzoznam")
cisla = [1, 2, 3, 4]
print("toto",cisla[1:-1])
cisla[1:-1] = [6, 5]
print(cisla)

cisla = [1, 2, 3, 4, 5, 6]
del cisla[-1]
print(cisla)
del cisla[3:5]
print(cisla)
del cisla
#print(cisla)

#pop, která odstraní a vrátí poslední prvek v seznamu – například pokud mám seznam karet v balíčku, jde takhle jednoduše „líznout” kartu,
#remove, která najde v seznamu daný prvek a odstraní ho,
#clear, která vyprázdní celý seznam.
cisla = [1, 2, 3, 'abc', 4, 5, 6, 12]
posledni = cisla.pop()
print(posledni)
print(cisla)

cisla.remove('abc')
print(cisla)

cisla.clear()
print(cisla)

#A taky tu máme metodu sort, která prvky seznamu seřadí.

seznam = [4, 7, 8, 3, 5, 2, 4, 8, 5]
seznam.sort()
print(seznam)

seznam = [4, 7, 8, 3, 5, 2, 4, 8, 5]
seznam.sort(reverse=True)#naopak zoradi
print(seznam)

melodie = ['C', 'E', 'G'] * 2 + ['E', 'E', 'D', 'E', 'F', 'D'] * 2 + ['E', 'D', 'C']
print(melodie)

print(len(melodie))         # Délka seznamu
print(melodie.count('D'))   # Počet 'D' v seznamu
print(melodie.index('D'))   # Číslo prvního 'D'
print('D' in melodie)       # Je 'D' v seznamu?

if seznam:
    print('V seznamu něco je!')
else:
    print('Seznam je prázdný!')

a = [1, 2, 3]
b = list(a) #novy zoznam nezavisly na starom b = a -> ukazuje na rovnaky zoznam v pameti

print(b)
a.append(4)
print(b)

mocniny_dvou = []
for cislo in range(10):
    mocniny_dvou.append(2 ** cislo)
print(mocniny_dvou)

#Balicek Kariet
balicek = []
for barva in '♠', '♥', '♦', '♣':  # (Na Windows použij textová jména)
    for hodnota in list(range(2, 11)) + ['J', 'Q', 'K', 'A']:
        balicek.append(str(hodnota) + barva)
print(balicek)

#-------------------- po slovach (medzera je oddelovac)
slova = 'Tato věta je složitá, rozdělme ji na slova!'.split()
print(slova)

zaznamy = '3A,8B,2E,9D'.split(',')
print(zaznamy)

# Medzera odddeluje jednotlive slova
veta = ' '.join(slova)
print(veta)

import random

balicek = []
for barva in '♠', '♥', '♦', '♣':
    for hodnota in list(range(2, 11)) + ['J', 'Q', 'K', 'A']:
        balicek.append(str(hodnota) + barva)
print(balicek)

random.shuffle(balicek)#shuffle ani sort nic nevracaju
print(balicek) 

import random
mozne_tahy = ['kámen', 'nůžky', 'papír']
tah_pocitace = random.choice(mozne_tahy) #Nahodny vyber

seznam_seznamu = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
prvni_seznam = seznam_seznamu[0]
print(prvni_seznam)

druhy_seznam = seznam_seznamu[1]
prvni_prvek_druheho_seznamu = druhy_seznam[0]
print(prvni_prvek_druheho_seznamu)
#ALEBO!
prvni_prvek_druheho_seznamu = (seznam_seznamu[1])[0]
#alebo
prvni_prvek_druheho_seznamu = seznam_seznamu[1][0]
