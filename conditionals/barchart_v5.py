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

def make_turtle(colr_draw,sz):
	"""
	  Set up a turtle with the given pensize
	  Return the new turtle
	"""
	t = turtle.Turtle()
	t.color(colr_draw)
	t.pensize(sz)
	return t

def draw_bar(t,height):
	""" Get turtle t to draw one bar, of height."""
	t.begin_fill()
	if height < 0:
		t.write("  " + str(height), align="left")
	t.left(90)
	t.forward(height)
	if height >= 0:
		t.write("  " + str(height), align="left")
	t.right(90)
	t.forward(40)
	t.right(90)
	t.forward(height)
	t.left(90)
	t.penup()
	t.forward(10)
	if height >=200:
		t.color("blue","red")
	elif height >=100 and height <200:
		t.color("blue","yellow")
	else:
		t.color("blue","green")
	t.pendown()
	t.end_fill()

wn = make_window("lightgreen","tess Bar chart")
tess = make_turtle("blue",3)
tess.penup()
tess.forward(-200)
tess.pendown()

xs = [48,117,-200,190,-160,210,200]

for a in xs:
	draw_bar(tess,a)

wn.mainloop()

