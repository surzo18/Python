array=[['0','0','0'],
       ['0','0','0'],
       ['0','0','0']]
quit = False
znak = 'X'

def Vykresli():
    for cislo in array:
        print(cislo)

def tahHraca(znak):
    try:
        riadok = int(input("Zadaj Riadok? ->")) - 1
        stlpec = int(input("Zadaj Stlpec? " ))  - 1
    except ValueError:
        print("Nezadal si cisla")
    
    if kontrolaRozsahuCisla(riadok) == True:
        if kontrolaRozsahuCisla(stlpec) == True:
            if(not jeTamUzZnak(riadok,stlpec)):
                array[riadok][stlpec] = znak
                return
            else:
                print("Uz tam je zadaný znak, zadaj Znova")
                tahHraca(znak)
        else:
            print("Nezadal si stlpec v platnom rozsahu, zadaj Znova")
            tahHraca(znak)

    else:
        print("Nezadal si riadok v platnom rozsahu, zadaj Znova")
        tahHraca(znak)


def jeTamUzZnak(riadok,stlpec):
    global array
    if(array[riadok][stlpec] != '0'):
        return True
    return False

def kontrolaRozsahuCisla(cislo):
    global array
    if cislo <= len(array) - 1 and cislo >= 0:
        return True
    else:    
        return False

def zmenZnak():
    global znak
    if znak == 'X':
        znak = 'O'
    else:
        znak = 'X'

def vyhral():
    global array
    global quit
    global znak
    if(array[0][0] == array[0][1] == array[0][2]) and array[0][0] != '0':
        print("vyhral znak, 1 riadok")
        quit = True
    if(array[1][0] == array[1][1] == array[1][2]) and array[1][0] != '0':
        print("vyhral znak, 2 riadok")
        quit = True
    if(array[2][0] == array[2][1] == array[2][2]) and array[2][0] != '0':
        print("vyhral znak, 3 riadok")
        quit = True
    if(array[0][0] == array[1][1] == array[2][2]) and array[0][0] != '0':
        print("vyhral znak, Diagonala Zlava")
        quit = True
    if(array[0][2] == array[1][1] == array[2][0]) and array[0][2] != '0':
        print("vyhral znak, Diagonala Zprava")
        quit = True
    if(array[0][0] == array[1][0] == array[2][0]) and array[0][0] != '0':
        print("vyhral znak, 1 Stlpec")
        quit = True
    if(array[0][1] == array[1][1] == array[2][1]) and array[0][1] != '0':
        print("vyhral znak, 2 Stlpec")
        quit = True
    if(array[0][2] == array[1][2] == array[2][2]) and array[0][2] != '0':
        print("vyhral znak, 3 Stlpec")
        quit = True
    return
    
def Update():
    tahHraca(znak)
    vyhral() 
    zmenZnak()

while(True):
    Vykresli()
    Update()
    
    if quit == True:
        Vykresli()
        print("Hra Skončila!, hráč !", znak, "! prehral")
        break