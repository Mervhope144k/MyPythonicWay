#!/usr/bin/python3

def week_days(x):
	""" Function that receives an integer input from 0~6
	    Returns day name(string)
	"""
	if x < 0 or x > 6:
		print("Invalid number!")
	else:
		if x == 0:
			print("Sunday")
		elif x == 1:
			print("Monday")
		elif x == 2:
			print("Tuesday")
		elif x == 3:
			print("Wednesday")
		elif x == 4:
			print("Thursday")
		elif x == 5:
			print("Friday")
		elif x == 6:
			print("Saturday")

x = int(input("Enter the day number: "))
week_days(x)
