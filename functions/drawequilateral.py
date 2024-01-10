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

def draw_poly(t,n,sz):
	""" Make turtle t draw a regular polygone of n sides and sz. """
	for i in range(n):
		t.forward(sz)
		t.left(360/n)

def draw_equitriangle(t,sz):
	""" Make turtle draw an equilateral triangle by calling draw_poly(). """
	n = 3
	draw_poly(t,n,sz)

length = int(input("Enter the Length of each side: "))
wn = make_window("lightgreen","Tess the artist")
tess = make_turtle("hotpink",4)

draw_equitriangle(tess,length)

wn.mainloop()
