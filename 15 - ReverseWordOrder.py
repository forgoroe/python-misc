"""
Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order. For example, say I type the string:

  My name is Michele
Then I would see the string:

  Michele is name My
shown back to me.
"""

userInput = input('Insert a long string of words:')

def reverseWordOrder(inputParam):
	wordsArray = userInput.split()
	result = wordsArray[::-1]
	return " ".join(result)

print(reverseWordOrder(userInput))