from math import sin

x = sin(1)  # (v radiánech)
print(x)

print('1 + 2', end=' ')
print('=', end=' ')
print(1 + 2, end='!')
print()

print(1, "dvě", False)
print(1, end=" ")
print(2, 3, 4, sep=", ")

vstup = input('zadej vstup: ') 
""" Čaká na vstup! """

print(vstup)

from random import randrange, uniform
a = 1
b = 5
randrange(a, b)   # náhodné celé číslo od a do b-1
uniform(a, b)     # náhodné reálné číslo od a do b