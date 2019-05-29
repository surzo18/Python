ja = {'jméno': 'Anna', 'město': 'Brno', 'čísla': [3, 7]}
print(ja['jméno'])

ja['čísla'] = [3, 7, 42]
print(ja['čísla'] )

ja['jazyk'] = 'Python'
print(ja)

del ja['čísla']

cisla = {
    'Maruška': '153 85283',
    'Terka': '237 26505',
    'Renata': '385 11223',
    'Michal': '491 88047',
}

barvy = {
    'hruška': 'zelená',
    'jablko': 'červená',
    'meloun': 'zelená',
    'švestka': 'modrá',
    'ředkvička': 'červená',
    'zelí': 'zelená',
    'mrkev': 'červená',
}

popisy_funkci = {'len': 'délka', 'str': 'řetězec', 'dict': 'slovník'}
for klic in popisy_funkci:
    print(klic)

for hodnota in popisy_funkci.values():
    print(hodnota)

for klic, hodnota in popisy_funkci.items():
    print('{}: {}'.format(klic, hodnota))

popisy_funkci = dict(len='délka', str='řetězec', dict='slovník')
print(popisy_funkci['len'])