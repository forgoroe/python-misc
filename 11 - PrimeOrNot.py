"""
Ask the user for a number and determine whether the number is prime or not. 
(For those who have forgotten, a prime number is a number that has no divisors.). 
"""

def primeCheck(numberToTest):
	if numberToTest == 1:
		prime = False
	if numberToTest == 2:
		prime = True
	else:
		myRange = range(2, numberToTest)
		for number in myRange:
			if numberToTest % number == 0:
				prime = False
			else:
				prime = True
	return prime

numberToTest = int(input('Choose a number: '))

result = primeCheck(numberToTest)

print('Prime number: ', result)

