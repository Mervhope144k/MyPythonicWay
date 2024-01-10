#!/usr/bin/python3

def sum_to(n):
	""" Return sum of integers up to num."""
	num = 0
	for i in range(n + 1):
		num = num + i
	return num

number = int(input("Enter your number: "))
print("The total sum up to ",number," is ",sum_to(number))


