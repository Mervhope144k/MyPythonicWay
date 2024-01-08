#!/usr/bin/python3

import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
duck = turtle.Turtle()
duck.pensize(7)

duck.penup()
duck.forward(-100)
duck.pendown()

duck.hideturtle()
for i in range(5):
    duck.forward(200)
    duck.right(144)

wn.mainloop()
