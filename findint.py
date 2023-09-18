# Finding the missing int in a list containing all but one of 0 - 9 (unsorted)
# This is entirely an exercise to make sure I can do what is apparently a common interview question.
import numpy as np

intlist = [4,7,8,9,1,3,0,6,5] # in this example, 2

# Clever math way
missingint1 = 45 - np.sum(intlist)
print("The missing int is: ", missingint1)

# O(n^2) looping over list, probably necessary if these are strings
checklist = [0,1,2,3,4,5,6,7,8,9]
foundmatch = False
missingint2 = -1

for checkint in checklist: #iterating over the check list: is 0 in, is 1 in, ... is 9 in?
	foundmatch = False
	for item in intlist: #match every integer in our given list against the (complete) checklist.
		if(item == checkint):
			foundmatch = True
	if(foundmatch == False):
		missingint2 = checkint

print("The missing int is: ", missingint2)

