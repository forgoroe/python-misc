"""
Write a password generator in Python. 
Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. 
The passwords should be random, generating a new password every time the user asks for a new password. 
Include your run-time code in a main method.
"""

import random, string

print('Choose length of password:')

try:
	length = int(input())
except:
	length = None

def generatePassword(strength=6, chars=string.ascii_letters + string.digits):
	return ''.join(random.choice(chars) for _ in range(strength-1)) # +random.choice(string.punctuation)

if length is None:
	print(generatePassword())
else:
	print(generatePassword(length))

