"""
Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
Take this opportunity to think about how you can use functions. 
Make sure to ask the user to enter the number of numbers in the sequence to generate.
(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in 
the sequence is the sum of the previous two numbers in the sequence. 
The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
"""

#Iterative solution

def fibonacciThisMany(number):
	counter = 1
	if number == 0:
		fib = []
	elif number == 1:
		fib = [1]
	elif number == 2:
		fib = [1,1]
	elif number > 2:
		fib = [1,1]
		while counter < (number - 1):
			fib.append(fib[counter-1] + fib[counter])
			counter += 1
	return fib

fibonacciLength = input('How many numbers do you want in the sequence? ')

if fibonacciLength.isdigit():
	sequence = fibonacciThisMany(int(fibonacciLength))
	print(sequence)
else:
	print('invalid input')