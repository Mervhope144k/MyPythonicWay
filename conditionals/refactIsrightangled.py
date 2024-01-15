#!/usr/bin/python3
from math import *

def is_rightangled(a,b,c):
	""" This function takes as inputs 3 sides of a triangle
		Returns True if it is a right angle triangle, False
		Othrewise
	"""
	if a >= b and a >= c:
		if ((a*a) - (b*b) - (c*c)) < 0.000001:
			return True
		else:
			return False
	elif b >= a and b >= c:
		if ((b*b) - (a*a) - (c*c)) < 0.000001:
			return True
		else:
			return False
	elif c >= a and c >= b:
		if ((c*c) - (a*a) - (b*b)) < 0.000001:
			return True
		else:
			return False

side1 = float(input("Enter the length of side: "))
side2 = float(input("Enter the length of side: "))
side3 = float(input("Enter the length if side: "))

print(is_rightangled(side1,side2,side3))

