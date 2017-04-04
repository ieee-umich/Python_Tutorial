# Now that you know the basic mechanics of python, let's talk about some more 
# "pythonic" features of python shall we?


##### Importing Libraries #####################################################
import sys
import os
import re
import math


##### List Comprehension ######################################################
#Let's say you want to make a sublist in a language like C++, like we have
# std::vector<int> numbers = {1,2,3,4,5,4,97 } and but we want to make a sub list of all
# the even numbers:
'''
	vector<int> newList;
	for (unsigned int = 0; i < numbers.size(); i++) {
		if (numbers[i]/2 == 0) {
			newList.push(numbers[i]);
		}	
	}
'''

#Python Land is a little different:
numbers = [1,2,3,4,5,4,97]
newList = [for number in numbers if number/2 == 0]


#####  ##############################################



##### Python's Wonderful Strings ##############################################




##### Python's "Main Fuction" #################################################

if __name__ == "__main__":
	print("main")