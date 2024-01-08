#!/usr/bin/python3

import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
clock = turtle.Turtle()
print(type(clock))
clock.shape("turtle")
clock.color("blue")

clock.penup()

clock.stamp()
clock.forward(100)
clock.stamp()
for i in range(11):
    clock.backward(100)
    clock.left(30)
    clock.forward(100)
    clock.stamp()

wn.mainloop()
