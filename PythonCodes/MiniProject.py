import random

def name_to_number(name):
	if (name =='rock'):
		return '0'
	elif(name =='spock'):
		return'1'
	elif(name =='paper'):
		return'2'
	elif(name=='lizzard'):
		return '3'
	elif(name=='scissors'):
		return '4'
	else:
		return " is is not from the above choice"
Nametonumber = name_to_number('rock')
print Nametonumber

def number_to_name(number):
	if(number==0):
		return'rock'
	elif(number==1):
		return 'spock'
	elif(number==2):
		return 'paper'
	elif(number==3):
		return'lizzard'
	elif(number==4):
		return'scissors'
	else:
		return " not from the above choice"		

#NumberToName =number_to_name(random.randrange(0,4))
#print NumberToName		


def rpsls(name):
	player_number = name_to_number(name)
	comp_number = random.randrange(0, 5)
	difference = (player_number - comp_number) % 5
	print "Player chooses", name
	print "Computer chooses", number_to_name(comp_number)

    #print "Score was:", difference # XXX


	if difference == 0: print " its a tie"
	elif difference <= 2: print "Player wins!"
	else:                 print "Computer wins!"

	print

    
# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")


'''

	print ("players_choice",name)

	player_number = name_to_number(name)


	comp_number = random.randrange(0,5)

	comp_choice = number_to_name(comp_number)

	print("comp_choice" ,comp_choice)

	difference = (player_number - comp_choice) % 5

	if difference == 0:
		print"its a tie"
   	
	elif difference <= 2:

		print"player wins"


	else: print "computer wins"
    		



rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
'''


	

