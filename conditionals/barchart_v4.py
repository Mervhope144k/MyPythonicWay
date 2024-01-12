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

def make_turtle(colr_draw,colr_fill,sz):
	"""
	  Set up a turtle with the given color and pensize
	  Return the new turtle
	"""
	t = turtle.Turtle()
	t.color(colr_draw,colr_fill)
	t.pensize(sz)
	return t

def draw_bar(t,height):
	""" Get turtle t to draw one bar, of height."""
	t.begin_fill()
	t.left(90)
	t.forward(height)
	t.write(" " + str(height))
	t.right(90)
	t.forward(40)
	t.right(90)
	t.forward(height)
	t.left(90)
	t.end_fill()
	t.penup()
	t.forward(10)
	t.pendown()


wn = make_window("lightgreen","tess Bar chart")
tess = make_turtle("blue","red",3)
tess.penup()
tess.forward(-200)
tess.right(90)
tess.forward(100)
tess.left(90)
tess.pendown()

xs = [48,117,200,240,160,260,220]

for a in xs:
	draw_bar(tess,a)

wn.mainloop()

