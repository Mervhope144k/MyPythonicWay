#!/usr/bin/python3
import turtle

"""This program creates two instances and manipulate their attributes"""
wn = turtle.Screen()            #Set up the window and its attributes
wn.bgcolor("lightgreen")
wn.title("Tess & Alex")

tess = turtle.Turtle()          #Create tess and set some attributes
tess.color("hotpink")
tess.pensize(5)

alex = turtle.Turtle()          #Create alex

tess.forward(80)                #Make tess draw an equilateral triangle
tess.left(120)
tess.forward(80)
tess.left(120)
tess.forward(80)
tess.left(120)                  #complete the triangle

tess.right(180)                  #turn tess around
tess.forward(80)                #Move tess away from origin

alex.forward(50)                #Make alex draw a square
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)

wn.mainloop()
