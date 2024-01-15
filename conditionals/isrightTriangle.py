#!/usr/bin/python3
from math import *

def is_rightangled(a,b,c):
	""" This function takes as inputs 3 sides of a triangle
		Returns True if it is a right angle triangle, False
		Othrewise
	"""
	if abs((a*a) + (b*b) - (c*c)) < 0.000001:
		return True
	else:
		return False

side1 = float(input("Enter the length of side: "))
side2 = float(input("Enter the length of side: "))
side3 = float(input("Enter the length if side: "))

print(is_rightangled(side1,side2,side3))

