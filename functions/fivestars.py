#!/usr/bin/python3

import turtle

def make_window(colr,ttle):
	"""
	  Set up the window with the given background color and title
	  Return the new window
	"""
	w = turtle.Screen()
	w.bgcolor(colr)
	w.title(ttle)
	return w

def make_turtle(colr,sz):
	"""
	  Set up a turtle with the given color and pensize
	  Return the new turtle
	"""
	t = turtle.Turtle()
	t.color(colr)
	t.pensize(sz)
	return t

def draw_star(t,sz):
	""" Make turtle t draw a star of sz. """
	for i in range(5):
		t.forward(sz)
		t.right(144)


wn = make_window("lightgreen","Tess the artist")
tess = make_turtle("hotpink",2)
size = 100
tess.hideturtle()
tess.penup()
tess.forward(-200)
tess.pendown()

for i in range(5):
	draw_star(tess,size)
	tess.penup()
	tess.forward(350)
	tess.right(144)
	tess.pendown()

wn.mainloop()


