'''
def is_leap_year(year):
	if (year%400)==0:
		print(" yes yes")
		return True


	elif (year%100)==0:
		print(" this is not")
		return False
	    
	elif (year %4)==0:  
		print("This executes")
	 	return True
	
	else:
		print("This executes if nothing matches")
		return False

year =2009

leap_year = is_leap_year(year)	  

if leap_year:
	print(" Yes its the leap Year")
else:
	print(" its not a leap year")	
'''

import random

def random_dice():
	dice_1 = random.randrange(1,7,2)
	dice_2 = random.randrange(1,7,3)	

	return dice_1+dice_2 or dice_1,dice_2

print " sum of the dice ,rolled once:",random_dice()
print " sum of the dice ,rolled once:",random_dice()
print " sum of the dice ,rolled once:",random_dice()