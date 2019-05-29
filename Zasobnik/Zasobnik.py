//Jednoduchy Zasobnik v Pythone
//  -----
//  | 7 |
//  | 3 |
//  | 2 | -> LIFO 
//  -----
import numpy as np
class Zasobnik:

    def __init__(self,size):
        print("Creating")
        self.index=0
        self.array = np.empty(size)

    def push(self,value):
        print("index je ",self.index)
        print("Pushing value: ",value)
        self.array[self.index] = value
        self.index = self.index + 1
    
    def get(self):
        print("Getting values...")
        self.index = self.index - 1
        return self.array[self.index]

zasobnik = Zasobnik(10)
zasobnik.push(10)
zasobnik.push(2)
zasobnik.push(4)
zasobnik.push(6)
zasobnik.push(100)

print(zasobnik.get())
print(zasobnik.get())
print(zasobnik.get())

print("Koniec programu")
