#!/usr/bin/python3

def area_of_circle(r):
	""" Return the area of a circle."""
	pi = 3.141592654
	A = pi * (r ** 2)
	return A

radius = float(input("Enter the radius of your circle: "))
area = area_of_circle(radius)
print("The area of a circle of radius ",radius," is ",area) 
