#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      merve
#
# Created:     09/01/2024
# Copyright:   (c) merve 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import turtle
__import__("turtle").__traceable__=False

def make_window(colr, ttle):
    """
      Set up the window with the given background color and title.
      Return the new window
    """
    w = turtle.Screen()
    w.bgcolor(colr)
    w.title(ttle)
    return w


def make_turtle(colr, sz):
    """
      Set up a turtle with the given color and pensize.
      Return the new turtle
    """
    t = turtle.Turtle()
    t.color(colr)
    t.pensize(sz)
    return t

wn = make_window("lightgreen","Tess and Alex dancing")
tess = make_turtle("hotpink",5)
alex = make_turtle("black",1)
dave = make_turtle("yellow",2)
