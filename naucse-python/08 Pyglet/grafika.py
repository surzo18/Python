#Nainstalujeme PYGLET:
# python -m pip install pyglet 
import math
import pyglet 
window = pyglet.window.Window()

def tik(t): #HODINY
    had.x = had.x + t *20
    had.y = 20 + 20 * math.sin(had.x / 5)
    #had.rotation += 5

def zpracujText(text):
    had.x += 150

def vykresli():
    window.clear()
    had.draw()

def zmen(t):
    had.image = obrazek2
    pyglet.clock.schedule_once(zmen_zpatky, 0.2)

def zmen_zpatky(t):
    had.image = obrazok
    pyglet.clock.schedule_once(zmen, 0.2)

def klik(x, y, tlacitko, mod): #Nie je mi jasne naco tu je mod a tlacitko
    had.x = x

obrazok = pyglet.image.load("templates/snake.jpg")
had = pyglet.sprite.Sprite(obrazok) # vytvoří speciální objekt Sprite, který určuje, že tento obrázek 
                                    #chceme „posadit“ na určité místo v černém okýnku. 
                                    #Když neuděláme nic dalšího, bude obrázek čekat v
                                    #levém rohu.

pyglet.clock.schedule_interval(tik, 1/30)#zavolat funkci tik každou třicetinu (1/30) vteřiny. 30FPS
window.push_handlers(
    on_text=zpracujText,
    on_draw=vykresli,
    on_mouse_press=klik
    ) #Pri zadani textu zavola funkciu zpracujText
    
obrazek2 = pyglet.image.load('templates/had2.png')

pyglet.clock.schedule_once(zmen, 1)
pyglet.app.run()

