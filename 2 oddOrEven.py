"""
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

Extras:
	If the number is a multiple of 4, print out a different message.
	Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
"""

number = int(input('Input a number: '))
otherNumber = int(input('Check if previous number can be divided by: '))

def oddOrEven(numberArg):
	result = ''
	if numberArg % 2 == 0:
		result = 'even'
	else: 
		result = 'odd'
	return result

def extraGiggle(numberArg):
	otherGiggleMessage = "Your first number is also a multiple of 4"
	if numberArg % 4 == 0:
		print(otherGiggleMessage)

def canBeDividedEvenlyBy(numberArg, otherNumberArg):
	canOrCannot = False
	if numberArg % otherNumberArg == 0:
		canOrCannot = True
	return canOrCannot

print('The first number you inserted is an '+ oddOrEven(number) + ' number')

print(str(number) + ' can be divided evenly by '+ str(otherNumber) + ': ' + str(canBeDividedEvenlyBy(number, otherNumber)))

extraGiggle(number)
