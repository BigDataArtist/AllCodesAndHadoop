import random

print(' I Have to flip coin 100 times ,lets see how much times I get heads in 1000 flips')
input()
flips=0
heads=0

while flips <=1000000:
	if random.randint(0,1) == 1:
		heads = heads +1
	flips = flips +1

	if flips == 100:
		print(' these many heads have been there in 100 times',heads)

	if flips==900:
		print(' These many heads are there in 500 in the flips',heads)	

print()

print(' These many heads were there in the 1000000 flips',heads)			