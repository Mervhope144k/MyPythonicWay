#!/usr/bin/python3

import turtle

def make_window(colr,ttle):
	"""
	  Set up a window with the given background color and title.
	  Return the new window
	"""
	w = turtle.Screen()
	w.bgcolor(colr)
	w.title(ttle)
	return w

def make_turtle(colr,sz):
	"""
	  Set up a turtle with the given color and pensize.
	  Return the new turtle
	"""
	t = turtle.Turtle()
	t.color(colr)
	t.pensize(sz)
	return t

wn = make_window("lightgreen","Tess and Alex dancing")
tess = make_turtle("hotpink",3)
tess.left(90)
tess.forward(100)
alex = make_turtle("black",3)
alex.right(180)
alex.backward(-100)
dave = make_turtle("yellow",3)
dave.right(45)
dave.forward(100)


wn.mainloop()
