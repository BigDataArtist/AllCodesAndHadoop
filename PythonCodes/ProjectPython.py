def greet(friend,money):
	if friend and (money>20):
		print("hi")
		money = money -20
	elif friend:
	    print("hope you are fine")	
	else:	
		print("hellp")
		money=money+10
	return money 

money = 15

money = greet(True,money)
print("i give money because he is true friend",money)
	

money = greet(False,money)
print(" wont give my money ",money)

money = greet(True,money)
print(" Will give the money",money)