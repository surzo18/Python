VELIKOST_POLE = 20

def over_cislo(cislo):
    if 0 <= cislo < VELIKOST_POLE:
        print("OK")
    else:
        raise ValueError("Číslo {n} neni v poli!".format(n=cislo))

over_cislo(2)

"""
BaseException
 ├── SystemExit                     vyvolána funkcí exit()
 ├── KeyboardInterrupt              vyvolána po stisknutí Ctrl+C
 ╰── Exception
      ├── ArithmeticError
      │    ╰── ZeroDivisionError    dělení nulou
      ├── AssertionError            nepovedený příkaz `assert`
      ├── AttributeError            neexistující atribut, např. 'abc'.len
      ├── ImportError               nepovedený import
      ├── LookupError
      │    ╰── IndexError           neexistující index, např. 'abc'[999]
      ├── NameError                 použití neexistujícího jména proměnné
      │    ╰── UnboundLocalError    použití proměnné, která ještě nebyla nastavená
      ├── SyntaxError               špatná syntaxe – program je nečitelný/nepoužitelný
      │    ╰── IndentationError     špatné odsazení
      │         ╰── TabError        kombinování mezer a tabulátorů
      ├── TypeError                 špatný typ, např. len(9)
      ╰── ValueError                špatná hodnota, např. int('xyz')
      """

def nacti_cislo():
    odpoved = input('Zadej číslo: ')
    try:
        cislo = int(odpoved)
    except ValueError:
        print('To nebylo číslo! Pokračuji s nulou.')
        cislo = 0
    return cislo


nacti_cislo()

"""
try:
    neco_udelej()
except ValueError:
    print('Tohle se provede, pokud nastane ValueError')
except NameError:
    print('Tohle se provede, pokud nastane NameError')
except Exception:
    print('Tohle se provede, pokud nastane jiná chyba')
    # (kromě SystemExit a KeyboardInterrupt, ty chytat nechceme)
except TypeError:
    print('Tohle se neprovede nikdy')
    # ("except Exception" výše ošetřuje i TypeError; sem se Python nedostane)
else:
    print('Tohle se provede, pokud chyba nenastane')
finally:
    print('Tohle se provede vždycky; i pokud v `try` bloku byl např. `return`')
"""

