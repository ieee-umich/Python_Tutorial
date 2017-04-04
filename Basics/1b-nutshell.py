### The Nutshell guide
### This is the guide for if you know some basic programming or some language 
### already


##### Python General Things ###################################################

'''
Python Comments are done via the '#' sign or with triple quotes (double or single)
It's generally advised to use the # sign because you you can sometimes use triple 
for strings occasionally
'''

"""
Python doesn't use semi-colons to separate lines, it merely uses consistent
spacing, so much like you can have something like this:
"""

# Where I've used tabs (four spaces) to separate each line

if True:
	print("hi")
	print("bye")
	for i in range(10):
		print("Hi again")

# I can also have this: 
# if True:
#  print("hi")
#  print("bye")
#   for i in range(10):
#    print("Hi again")
# Where i decided to separate lines by one space
# It won't run here though, because we need to use one space for the whole document
# for that to work and I've been using 4 for everything else
# Generally use four spaces though, it's standard



### Variables #################################################################
variable_have_no_type_when_declared = "Indeed"
integers = 0
decimal_numbers_are_floats = 5.0
booleans = True
booleans = "You can reuse variables freely/assign them freely between any types"


### Basic Data Structures #####################################################

# Lists:
# Python's array structure is called the list, it operates more similarly to
# the C++ vector class in that it has a lot of features built on top
# They're also not constrained to being a single type

list1 = [] # make an empty list
list2 = [1,2,3,4]
list3 = ["one", 2, 3.0]

# Dictionaries:
# Python's Hash-Table Structure is called a dictionary, it lets you map a key
# to any value, much like the the Lists, these are not type constrained

dictionary1 = {} 
dictionary1["hi"] = "bye" #We map "hi" to "bye"
dictionary1[1] = 2

dictionary2 = {"key":"value", 1:2, "one":"two"} # we can also create dicts.
# manually just by specifying each key/value pair like so.

### Control Statements ########################################################

# In Python: the statements are if, else and elif (else if)
if True:
	print("True")
else:
	print("False")

value = True
if value:
	print("Hi")
elif not value:
	print("Hello")
else:
	print ("Bye")

### The For Loop ##############################################################

# Python's for loop is a each loop, that it to say it goes through each thing
# once before stopping:
for item in list2:
	print(i)
# This will print everything 

# but what if we don't want to iterate through an existing list?	
# range generates a list of integers between the specified range, so with this
# we have the "for i" structure more commonly seen in other languages


array = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
for i in range(1,10):
	# This will print the array by accessing each entry
	print(array[i])

# You can name the "i" or "item" whatever you want, it's just a name for you to access
# your current item during iteration:

for falcon in array:
	print(falcon)


### Functions #################################################################
def functionName(input1, input2):
	print(input1)
	# Do all your function mumbo-jumbo here
	# All of it
	return #You can return nothing or something!

def functions_can_return_multiple_things(input1, input2):
	return input1, input2


# A side note for those wondering: primitives (basic data types) in python
# are all pass by value, and generally, python doesn't support pass by 
# reference in the traditional sense.



### The Main Function ##################### Wait python has a main function? ##

if __name___ == "__main__":
	#You do your code here!

# This main is actually quite important ibecause it lets you import the current
# file in other places w/o having all the code run. 


# And that's all the basics of python, so start using your newfound python-fu and
# get coding!


### Appendix ##################################################################
### Style #####################################################################
# If you didn't notice, python is the kind of language that's very "loose" so
# so to speak, so it's important to keep that in mind and stay organized and
# consistent with your code style

# The defacto 
