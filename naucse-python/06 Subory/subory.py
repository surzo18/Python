
subor = open('basnicka.txt', encoding='utf-8')
obsah = subor.read()
print(obsah)
subor.close()

print()
print('Slyšela jsem tuto básničku:')
print()
soubor = open('basnicka.txt', encoding='utf-8')
for radek in soubor:
    print('    ' + radek, end="")
soubor.close()
print()
print('Jak se ti líbí?')

def iniciala():
    """Vrátí první písmeno v daném souboru."""

    soubor = open('basnicka.txt', encoding='utf-8')
    try:
        obsah = soubor.read()
        return obsah[0]
    finally:
        soubor.close()

print(iniciala())

def inicialaWith():
    """Vrátí první písmeno v daném souboru."""

    with open('basnicka.txt', encoding='utf-8') as soubor:
        obsah = soubor.read()
        return obsah[0]

print(inicialaWith())



with open('druha-basnicka.txt', mode='w', encoding='utf-8') as soubor:
    soubor.write('Naše staré hodiny\n')
    soubor.write('Bijí čtyři hodiny\n')



with open('druha-basnicka.txt', mode='w', encoding='utf-8') as soubor:
    print('Naše staré hodiny', file=soubor)
    print('Bijí', 2+2, 'hodiny', file=soubor)