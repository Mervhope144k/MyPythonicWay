#!/usr/bin/python3

import turtle

wn = turtle.Screen()
wn.title("Alex & Tess")
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("hotpink")
tess.pensize(5)

alex = turtle.Turtle()

for i in range(3):
    tess.forward(80)
    tess.left(120)

tess.right(180)
tess.forward(80)

for i in range(4):
    alex.forward(50)
    alex.left(90)

#More code can follow...
