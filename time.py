#!/usr/bin/python3

current_time = int(input("current time: "))
print(current_time,"pm")
hours_before_alarm_off = int(input("alarm to go off in: "))
print(hours_before_alarm_off, "hours")
days_passed = hours_before_alarm_off // 24
hours_added = hours_before_alarm_off % 24
time_alarm_off = current_time + hours_added
print("Alarm goes off after ",days_passed,"days at", time_alarm_off,"pm")
