#!/usr/bin/python3

def print_days(x):
	week_days=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
	if x >= 7:
		print("Invalid Entry!, Must be positive from 0 ~ 6")
		return
	else:
		return week_days[x]

day_num = int(input("Enter the day number: "))
print("Your day of the week is:", print_days(day_num))
