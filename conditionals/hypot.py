#!/usr/bin/python3

def find_hypot(x,y):
	""" This function takes as input the two sides
		of a right angle triangle.
		Returns the hypothenuse
	"""
	return(((x*x)+(y*y))**0.5)

side1 = float(input("Enter the length of adjacent side: "))
side2 = float(input("Enter the length of opposite side: "))

hypothenuse = find_hypot(side1,side2)
print("Hypothenuse value is:",hypothenuse)
