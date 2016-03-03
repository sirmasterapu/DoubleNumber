
number = 0

converted = False
while not converted:
	userNumber = raw_input("Tel me a number. ")
	
	try:
		userNumber = float(userNumber)
		number = userNumber
		
	except ValueError:
		print("not a number")
	else:
		converted = True


print("Double that is {}".format(number * 2))