import random

number_1 = random.randint(1,20)
number_2 = random.randint (1,20)

print('what is',number_1,'and ',number_2,'?')

result = input()
hello = number_1+number_2
if result == (hello):
	print(' bingo you guesses it right')
else:	
	print('nah the rusult is ',hello)	