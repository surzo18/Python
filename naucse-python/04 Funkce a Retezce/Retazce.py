spojeny_retezec = 'a' + 'b'
dlouhy_retezec = 'ó' * 100

pate_pismeno = 'čokoláda'[5]

print(pate_pismeno)

print('Čokoláda'[-1])  # → a
print('Čokoláda'[-2])  # → d
print('Čokoláda'[-3])  # → á
print('Čokoláda'[-4])  # → l

"""
   [0] [1] [2] [3] [4] [5] [6] [7]
   [-8][-7][-6][-5][-4][-3][-2][-1]
  ╭───┬───┬───┬───┬───┬───┬───┬───╮
  │ Č │ o │ k │ o │ l │ á │ d │ a │
  ╰───┴───┴───┴───┴───┴───┴───┴───╯
  """

retezec = 'Ahoj'
print(retezec.upper())
print(retezec.lower())
print(retezec)

def zadajUdaje():
    meno=input("Zadaj svoje meno: ")
    priezvisko =input("Zadaj svoje priezvisko: ")
    print(meno,priezvisko,meno[0].upper(),priezvisko[0].upper())

zadajUdaje()


vypis = '{}×{} je {}'.format(3, 4, 3 * 4)

retezec = 'čokoláda'
print(retezec[:4])
print(retezec[2:5])
print(retezec[-4:])
print(vypis)

"""
  ╭───┬───┬───┬───┬───┬───┬───┬───╮
  │ Č │ o │ k │ o │ l │ á │ d │ a │
  ├───┼───┼───┼───┼───┼───┼───┼───┤
  │   │   │   │   │   │   │   │   │
  0   1   2   3   4   5   6   7   8
 -8  -7  -6  -5  -4  -3  -2  -1

  ╰───────────────╯
  'čokoláda'[:4] == 'čoko'

          ╰───────────────╯
        'čokoláda'[2:6] == 'kolá'

                      ╰───────────╯
                      'čokoláda'[-3:] == 'áda'
"""

def zamen(retezec, pozice, znak):
    """Zamění znak na dané pozici

    Vrátí řetězec, který má na dané pozici daný znak;
    jinak je stejný jako vstupní retezec
    """

    return retezec[:pozice] + znak + retezec[pozice + 1:]

zamen('palec', 0, 'v') == 'valec'
zamen('valec', 2, 'j') == 'vajec'