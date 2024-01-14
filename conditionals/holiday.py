#!/usr/bin/python3

def print_days(start_day,length_stay):
	week_days=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
	if start_day >= 7:
		print("Invalid Entry!, must be from 0 ~ 6")
		return
	else:
		extra_days = length_stay % 7
		if start_day + extra_days <= 6:
			return week_days[start_day + extra_days]
		else:
			return week_days[(start_day + extra_days) % 7]

departure_day = int(input("Enter your departure day: "))
period_of_stay = int(input("Enter how many night you will stay: "))

print("Your day of the week is:", print_days(departure_day,period_of_stay))
