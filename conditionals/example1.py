#!/usr/bin/python3

x = int(input("Enter a positive integer number: "))

if x % 2 == 0:
	print(x, " is even. ")
	print("Did yo know that 2 is the only even number that is prime?")
else:
	print(x, " is odd. ")
	print("Did you know that multiplying two odd numbers " + "always give an odd results?")
