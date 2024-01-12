#!/usr/bin/python3

#--------------------------------------
# file: killdragon.py
# conditional using not logical operator
#--------------------------------------

sword_charge = float(input("Level of charge of the sword: "))
shield_energy = int(input("Energy level of the shield: "))

if not((sword_charge >= 0.9) and (shield_energy >= 100)):
	print("Your attack has no effect, the dragon fries you to a crisp!")
else:
	print("The dragon crumples in a heap. you rescuee the gorgeous princess!")
