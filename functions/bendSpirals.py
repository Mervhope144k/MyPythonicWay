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

def draw_spiral(t,sz):
	""" Make turtle t draw a square of sz. """
	t.right(89)
	t.forward(sz)


wn = make_window("lightgreen","Tess the artist")
tess = make_turtle("blue",2)
size = 5

for i in range(99):
	draw_spiral(tess,size)
	size = size + 3
tess.right(90)

wn.mainloop()


