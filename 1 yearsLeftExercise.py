"""
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:
	Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
	Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)
"""

print('I will tell you in how many years you will turn 100 years old')

def askQuestions():
	global name 
	name = input('Tell me your name: ')
	global age
	age = int(input('Your age: '))

askQuestions()


def printObservations(name, age)
	print('You said your name is '+ name)
	print('You also said you are '+ str(age) + ' years old')

printObservations()

def calculateYearsLeft(age):
	yearsLeft = 100 - age
	return yearsLeft

yearsLeft = calculateYearsLeft(age)

print(name + ', you will turn 100 years old in '+ str(yearsLeft) + ' years. Sorry')

