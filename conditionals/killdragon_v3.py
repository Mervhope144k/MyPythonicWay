#!/usr/bin/python3
 
#--------------------------------------
# file: killdragon.py
# swaping the then and else part of the
# conditional. Best alternative
#--------------------------------------

sword_charge = float(input("Level of charge of the sword: "))
shield_energy = int(input("Energy level of the shield: "))

if (sword_charge >= 0.9) and (shield_energy >= 100):
	 print("The dragon crumples in a heap. you rescuee the gorgeous princess!")
else:
	 print("Your attack has no effect, the dragon fries you to a crisp!")
