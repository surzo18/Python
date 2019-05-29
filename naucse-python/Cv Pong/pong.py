#CONSTANTY V HRE
SIRKA = 900
VYSKA = 600

VELKOST_LOPTY = 20
HRUBKA_PALKY = 10
DLZKA_PALKY = 100
RYCHLOST = 200 #PIXEL ZA SEKUNDU  # pixel Za sekundu

DLZKA_STREDOVEJ_CIARY = 20
VELKOST_FONTU = 42
ODSADENIE_TEXTU = 30

#Premenne
pozicia_palok = [VYSKA // 2, VYSKA // 2]
pozicia_lopty = [0,0]
rychlost_lopty = [0,0]
stisknute_klavesy = set()
skore = [0,0]

#IMPORTY
import pyglet
from pyglet import gl
from pyglet.window import key
import random

#FUNKCIE
def stisk_klavesy(symbol, modifikatory):
    if symbol == key.W:
        stisknute_klavesy.add(('nahoru', 0))
    if symbol == key.S:
        stisknute_klavesy.add(('dolu', 0))
    if symbol == key.UP:
        stisknute_klavesy.add(('nahoru', 1))
    if symbol == key.DOWN:
        stisknute_klavesy.add(('dolu', 1))


def pusteni_klavesy(symbol, modifikatory):
    if symbol == key.W:
        stisknute_klavesy.discard(('nahoru', 0))
    if symbol == key.S:
        stisknute_klavesy.discard(('dolu', 0))
    if symbol == key.UP:
        stisknute_klavesy.discard(('nahoru', 1))
    if symbol == key.DOWN:
        stisknute_klavesy.discard(('dolu', 1))

def nakresliObdlznik(x1,y1,x2,y2):
    gl.glBegin(gl.GL_TRIANGLE_FAN) # zacni kreslit spojene trojuholniky
    gl.glVertex2f(int(x1), int(y1))  # vrchol A
    gl.glVertex2f(int(x1), int(y2))  # vrchol B
    gl.glVertex2f(int(x2), int(y2))  # vrchol C, nakresli trojuhelnik ABC
    gl.glVertex2f(int(x2), int(y1))  # vrchol D, nakresli trojuhelnik BCD
    # dalsi souradnice E by nakreslila trojuhelnik CDE, atd.
    gl.glEnd()  # ukonci kresleni trojuhelniku

def vykresliLoptu():
     nakresliObdlznik( # LOPTA
        pozicia_lopty[0] - VELKOST_LOPTY // 2,
        pozicia_lopty[1] - VELKOST_LOPTY // 2,
        pozicia_lopty[0] + VELKOST_LOPTY // 2,
        pozicia_lopty[1] + VELKOST_LOPTY // 2
    )

def nakresli_text(text, x, y, pozice_x):
    """Nakresli dany text na danou pozici

    Argument ``pozice_x`` muze byt "left" nebo "right", udava na kterou stranu
    bude text zarovnany
    """
    napis = pyglet.text.Label(
        text,
        font_size=VELKOST_FONTU,
        x=x, y=y, anchor_x=pozice_x
    )
    napis.draw()

def vykresliPalky():
    for x,y in [(0,pozicia_palok[0]),(SIRKA, pozicia_palok[1])]:
        nakresliObdlznik( # OBE PALKY
            x - HRUBKA_PALKY,
            y - DLZKA_PALKY // 2,
            x + HRUBKA_PALKY,
            y + DLZKA_PALKY // 2
        )

def vykresliCiaru():
        nakresliObdlznik(
            SIRKA // 2 - 1,
            0,
            SIRKA // 2 + 1,
            VYSKA
        )

def vykresli():
    """Vykresli stav hry"""
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)  # smaz obsah okna (vybarvi na cerno)
    gl.glColor3f(1, 1, 1)  # nastav barvu kresleni na bilou
    vykresliLoptu()
    vykresliPalky()
    vykresliCiaru()
    #vykresliPocitadlo()
    nakresli_text(
        str(skore[0]),
        x=ODSADENIE_TEXTU,
        y=VYSKA - ODSADENIE_TEXTU - VELKOST_FONTU,
        pozice_x='left',
    )

    nakresli_text(
        str(skore[1]),
        x=SIRKA - ODSADENIE_TEXTU,
        y=VYSKA - ODSADENIE_TEXTU - VELKOST_FONTU,
        pozice_x='right',
    )


def obnov_stav(dt):
    for cislo_palky in (0, 1):
        # pohyb podle klaves (viz funkce `stisk_klavesy`)
        if ('nahoru', cislo_palky) in stisknute_klavesy:
            pozicia_palok[cislo_palky] += RYCHLOST * dt
        if ('dolu', cislo_palky) in stisknute_klavesy:
            pozicia_palok[cislo_palky] -= RYCHLOST * dt

        # dolni zarazka - kdyz je palka prilis dole, nastavime ji na minimum
        if pozicia_palok[cislo_palky] < DLZKA_PALKY / 2:
            pozicia_palok[cislo_palky] = DLZKA_PALKY / 2
        # horni zarazka - kdyz je palka prilis nahore, nastavime ji na maximum
        if pozicia_palok[cislo_palky] > VYSKA - DLZKA_PALKY / 2:
            pozicia_palok[cislo_palky] = VYSKA - DLZKA_PALKY / 2

    pozicia_lopty[0] += rychlost_lopty[0] * dt
    pozicia_lopty[1] += rychlost_lopty[1] * dt

     # Odraz micku od sten
    if pozicia_lopty[1] < VELKOST_LOPTY // 2:
        rychlost_lopty[1] = abs(rychlost_lopty[1])
    if pozicia_lopty[1] > VYSKA - VELKOST_LOPTY // 2:
        rychlost_lopty[1] = -abs(rychlost_lopty[1])
    
    palka_min = pozicia_lopty[1] - VELKOST_LOPTY / 2 - DLZKA_PALKY / 2
    palka_max = pozicia_lopty[1] + VELKOST_LOPTY / 2 + DLZKA_PALKY / 2
    
      # odrazeni vlevo
    if pozicia_lopty[0] < HRUBKA_PALKY + VELKOST_LOPTY / 2:
        if palka_min < pozicia_palok[0] < palka_max:
            # palka je na spravnem miste, odrazime micek
            rychlost_lopty[0] = abs(rychlost_lopty[0])
        else:
            # palka je jinde nez ma byt, hrac prohral
            skore[1] += 1
            reset()

    # odrazeni vpravo
    if pozicia_lopty[0] > SIRKA - (HRUBKA_PALKY + VELKOST_LOPTY / 2):
        if palka_min < pozicia_palok[1] < palka_max:
            rychlost_lopty[0] = -abs(rychlost_lopty[0])
        else:
            skore[0] += 1
            reset()

def reset():
    pozicia_lopty[0] = SIRKA // 2
    pozicia_lopty[1] = VYSKA // 2

    # x-ova rychlost - bud vpravo, nebo vlevo
    if random.randint(0, 1):
        rychlost_lopty[0] = RYCHLOST
    else:
        rychlost_lopty[0] = -RYCHLOST
    # y-ova rychlost - uplne nahodna
    rychlost_lopty[1] = random.uniform(-1, 1) * RYCHLOST

#HRA
reset()
window = pyglet.window.Window(width = SIRKA, height = VYSKA)
window.push_handlers(
    on_draw = vykresli,
    on_key_press=stisk_klavesy,
    on_key_release=pusteni_klavesy,
)
pyglet.clock.schedule(obnov_stav)
pyglet.app.run() #Vsetko je nastavene a hra môže začať