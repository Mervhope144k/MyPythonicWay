#!/usr/bin/python3

def exam_grade(mark):
	""" This function takes a student mark
		Returns the grade accordingly
	"""
	Grade = ["First","Upper Second","Second","Third","F1 Supp","F2","F3"]

	if mark <40:
		return Grade[6]
	elif mark >=40 and mark <45:
		return Grade[5]
	elif mark >=45 and mark <50:
		return Grade[4]
	elif mark >=50 and mark <60:
		return Grade[3]
	elif mark >=60 and mark <70:
		return Grade[2]
	elif mark >=70 and mark <75:
		return Grade[1]
	else:
		return Grade[0]

xs = [83,75,74.9,70,69.9,65,60,59.9,55,50,49.9,45,44.9,40,39.9,2,0]
for mark in xs:
	print("Your mark is ",mark, "and your Grade is ",exam_grade(mark))
