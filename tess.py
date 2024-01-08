#!/usr/bin/python3

import turtle
wn_color = input("favorrite color: ")           #prompt the user for window color
my_color = input("What is tess color?: ")       #prompt the user for tess color
my_width = int(input("Enter tess width: "))     #prompt the user for tess width
wn = turtle.Screen()
wn.bgcolor(wn_color)                            #set the window background color
wn.title("Hello, Tess!")                        #Set the window title


tess = turtle.Turtle()
tess.color(my_color)                            #Tell tess to change her color  
tess.pensize(my_width)                          #Tell tess to set her pen width

tess.forward(50)
tess.left(120)
tess.forward(50)

wn.mainloop()
