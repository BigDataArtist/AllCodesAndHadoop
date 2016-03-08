
'''
lines = list()
enterThelines = int(input(" enter athe number of lines you want to enter"))
takeRequest = input(" if enter y then enter more input items for list")
while takeRequest =='y':
	line = input(" enter the lines on bye one")
	lines.append(line)
	takeRequest = input("for more lines")


print ('Your lines were:')
for line in lines:
	print(line)	
'''
'''
import itertools

type_card = ['Dimond', 'Spades', 'Heart', 'Clubs']
rank_card = [str(n) for n in range(1, 11)] + ['J', 'Q', 'K', 'A']

deck_combo = list(itertools.product(type_card, rank_card))

print([(x+y) for x, y in deck_combo])
'''
print('Hello world!')
print('What is your name?')
myName = input()
print('It is good to meet you, ' + myName)
"when using + we have to be carefull and input should be string like above and then replace + with (,) in order to make it independent of its starting "
print(" now enter the money ")
myName = input()
print('Its good to have so much money',myName)