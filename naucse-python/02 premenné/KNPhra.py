import random
pole=['kámen','nůžky','papír']


while(True):
    tah_pocitace = random.choice(pole)
    tah_cloveka = input('kámen, nůžky, nebo papír? ')

    if tah_cloveka == 'kámen':
        if tah_pocitace == 'kámen':
            print('Plichta.')
        elif tah_pocitace == 'nůžky':
            print('Vyhrála jsi!')
        elif tah_pocitace == 'papír':
            print('Počítač vyhrál.')
        break
    elif tah_cloveka == 'nůžky':
        if tah_pocitace == 'kámen':
            print('Počítač vyhrál.')
        elif tah_pocitace == 'nůžky':
            print('Plichta.')
        elif tah_pocitace == 'papír':
            print('Vyhrála jsi!')
        break
    elif tah_cloveka == 'papír':
        if tah_pocitace == 'kámen':
            print('Vyhrála jsi!')
        elif tah_pocitace == 'nůžky':
            print('Počítač vyhrál.')
        elif tah_pocitace == 'papír':
            print('Plichta.')
        break
    else:
        print('Nerozumím.')

