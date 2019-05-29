from turtle import forward, left, right, exitonclick
from turtle import shape,penup, pendown


shape("turtle") 
"""nastavi šípku ako želvu"""
for squares in range(8):
    for square in range(4):
        forward(50)
        left(90)
    left(45)

for i in range(10):
    penup()
    forward(10)
    pendown()
    forward(10)

exitonclick()