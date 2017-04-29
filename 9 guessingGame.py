""""
Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. 
(Hint: remember to use the user input lessons from the very first exercise)

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.
"""

import random

randomNumber = random.randint(1,9)
counter = 0
userInput = ''
gameRunning = True

while(gameRunning == True):
	userInput = input('Guess which random number between 1 and 9 got rolled: ')

	if userInput.isalpha():
		if userInput == 'exit':
				print('You quit. Loser.')
				break
		else:
			print('Invalid input. Fail.')
			break

	if int(userInput) == randomNumber:
		print('You got it right')
		gameRunning = False

	elif int(userInput) < randomNumber:
		print('Too low')
	else:
		print('Too high')

	counter+=1

print('You took '+ str(counter) + ' tries to guess')
print('The random number was ' + str(randomNumber))