"""
Make a two-player Rock-Paper-Scissors game. 
(Hint: Ask for player plays (using input), 
compare them, print out a message of congratulations to the winner, 
and ask if the players want to start a new game)

"""

PlayerOneInput = ''
PlayerOneInput = ''
game = ''

def isValidInput(inputOne, inputTwo):
	validInputs = ['rock', 'paper', 'scissors', 'quit']
	if inputOne.lower() not in validInputs or inputTwo.lower() not in validInputs:
		return False
	else:
		return True

while (game != 'quit' or PlayerOneInput != 'quit' or PlayerTwoInput != 'quit'):
	PlayerOneInput = input('P1: rock, paper, scissors or quit? ')	
	PlayerTwoInput = input('P2: rock, paper, scissors or quit? ')

	if not isValidInput(PlayerOneInput, PlayerTwoInput):
		print('\nSomeone entered invalid input and ruined the game for everyone.\nThis is why we can\'t have nice things')
		break

	if PlayerOneInput == 'quit' or PlayerTwoInput == 'quit':
		print('\nSomeone gave up. Losers...')
		break
	else:
		if PlayerOneInput == PlayerTwoInput:
			print('DRAW!')
		else:
			if PlayerOneInput == 'rock' and PlayerTwoInput == 'scissors':
				print('PLAYER ONE WINS!')
			if PlayerOneInput == 'scissors' and PlayerTwoInput == 'paper':
				print('PLAYER ONE WINS!')
			if PlayerOneInput == 'paper' and PlayerTwoInput == 'rock':
				print('PLAYER ONE WINS!')
			else:
				print('PLAYER TWO WINS!')





