numberone = input("number1: ")
factor = input("function: ")
numbertwo = input("number2: ")

numberone = int(numberone)
numbertwo = int(numbertwo)

if (factor == '+'):
	print(numberone + numbertwo)
elif (factor == '-'):
	print(numberone - numbertwo)
elif (factor == '*'):
	print(numberone * numbertwo)
elif (factor == '/'):
	print(numberone / numbertwo)
