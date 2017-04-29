"""
Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
"""

word = input('Word to check if palindrome: ')
backwards = word[::-1]

print(backwards)

if word == backwards:
	print('That\'s a palindrome')
else:
	print('That\'s not a palindrome')

