#!/usr/bin/python3.12

def print_square_root(x):
	""" compute the square root of a positive integer. """
	if x <= 0:
		print("Positive numbers only, please.")
		return

	result = x ** 0.5
	print("The square root of ",x," is ", result)


integer = int(input("Enter an integer number: "))

print_square_root(integer)
