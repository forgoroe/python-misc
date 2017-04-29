"""
Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

Extras:

Write two different functions to do this - one using a loop and constructing a list, and another using sets.
Go back and do Exercise 5 using sets, and write the solution for that in a different function.
"""

listOfDuplicates = [1,1,1,2,2,2,5,5,5,9,10]

def removeDuplicates(listParam):
	myList = list(set(listParam))
	myList.sort()
	return myList

def secondaryRemoveDuplicate(listParam):
	newList = []
	for element in listParam:
		if element not in newList:
			newList.append(element)
	newList.sort()
	return newList		

print(removeDuplicates(listOfDuplicates))
print(secondaryRemoveDuplicate(listOfDuplicates))