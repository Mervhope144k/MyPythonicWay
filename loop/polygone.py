#!/usr/bin/python3

import turtle

sides = int(input("How many size? : "))
wn = turtle.Screen()
wn.bgcolor("lightgreen")
newton = turtle.Turtle()
newton.pensize(7)
newton.penup()
newton.forward(-150)
newton.left(-90)
newton.pendown()

angle = 360 / sides
for s in range(sides):
    newton.left(angle)
    newton.forward(50)

wn.mainloop()

# More code could come here ...

