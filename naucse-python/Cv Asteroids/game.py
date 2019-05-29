import pyglet 
import math
from  ship import Ship

class Game:
    window = pyglet.window.Window()
    ship = Ship()
    obrazok = pyglet.image.load("Spritesheet/sheet.png")
    SPRITE = pyglet.sprite.Sprite(obrazok)

    def __init__(self):
        pyglet.clock.schedule_interval(self.tik, 1/30)
        
        self.window.push_handlers(
        on_draw=self.vykresli,
        ) #Pri zadani textu zavola funkciu zpracujText
    
    
    def tik(self,t):
        self.SPRITE.x += 1
      
    def vykresli(self):
        self.window.clear()
        self.SPRITE.draw()

    
game = Game()   
pyglet.app.run()
