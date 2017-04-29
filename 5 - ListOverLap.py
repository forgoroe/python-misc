"""
ake two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

Extras:
	Randomly generate two lists to test this
	Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)
"""

import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

my_random = [random.sample(range(100),10), random.sample(range(100),10)]

for sample in my_random:
	sample.sort()

def commonElementsBetween(firstList, secondList):
	commonList = []
	for element in firstList:
		if element in secondList:
			if element not in commonList:
				commonList.append(element)
	return commonList

print('first list: ' + str(my_random[0]), '\nsecond list: ' + str(my_random[1]))
print('elements in common: ' + str(commonElementsBetween(my_random[0],my_random[1])))