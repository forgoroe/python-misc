"""
Write a function that takes an ordered list of numbers 
(a list where the elements are in order from smallest to largest) and another number. 
The function decides whether or not the given number is inside the list and returns 
(then prints) an appropriate boolean.

Extras:

Use binary search.
"""
import random, math

randomList = random.sample(range(100),10)
myList = [0,1,2,3,4,5,6,7,8,9]

"""
Parameters:
-----------
arg1: list
	must be a sorted list.
arg2: int 
	the number to find within the given list.
"""
def binarySearch(listParam, number):
	middleIndex = math.floor((len(listParam))/2)
	middleElement = listParam[middleIndex]
	print('Current list', listParam)
	print('Current middle element', middleElement)

	if len(listParam) > 1:
		if number > listParam[middleIndex]:
			print('The number to search "{0}" is to the right of the middle element'.format(number))
			newList = listParam[middleIndex:]
			binarySearch(newList, number)
		
		if number < listParam[middleIndex]:
			print('number is to the left of the middle element')
			newList = listParam[:middleIndex]
			binarySearch(newList, number)

		if number == listParam[middleIndex]:
			print('Element found:', listParam[middleIndex])
	else:
		print('Couldn\'t find the element {0}'.format(number))
	
	 

myList.sort()
randomList.sort()
binarySearch(randomList, 55)