#!/usr/bin/python3 
#--------------------------------------
# file: killdragon_v2.py
# modification using deMorgan's law and
# logical opposite
#--------------------------------------
 
sword_charge = float(input("Level of charge of the sword: "))
shield_energy = int(input("Energy level of the shield: "))

if (sword_charge < 0.9) or (shield_energy < 100):
	print("Your attack has no effect, the dragon fries you to a crisp!")
else:
	print("The dragon crumples in a heap. you rescuee the gorgeous princes")
