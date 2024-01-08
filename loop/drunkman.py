#!/usr/bin/python3

import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
drunker = turtle.Turtle()
drunker.pensize(7)

angles = [160, -43, 270, -97, -43, 200, -940, 17, -86]
for angle in angles:
    drunker.left(angle)
    drunker.forward(100)

wn.mainloop()

# More code here ...
