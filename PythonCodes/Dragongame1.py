import random
import time

def intro():
	print('this is a place where dragons live')
	print('look acrefully')
	print(' dragon might not be in a good mood')
	print(' he can eat you or gobble you down')
	print()

def chooseCave():
	cave =''
	while cave != 1 and cave !=2:
		print(' enter the cave number')
		cave = input()
	return cave			

def checkCave(chosenCave):
	print('this place is sppoky')
	time.sleep(2)
	print(' be carefull while choosing the cave')
	time.sleep(2)
	print(' a large dragon jumps in front of you')

	print()
	time.sleep(2)

	friendlycave = random.randint(1,2)

	if chosenCave == str(friendlycave):
		print(' You get the treasure')
	else:
		print('dragon will eat you up')

playAgain = 'yes'
 
while playAgain =='yes' or playAgain=='y':
	
	intro()

	caveNumber = chooseCave()

	checkCave(caveNumber)

	print(' do ypu want to play again?(yes or no)')

	playAgain = input()			