import fileinput
import re

# Opens File, returns file obj.

def removeComments(inFile, outFile):
	
	# This string goes into the re.match function, it matches all lines
	# that start with the '#' Symbol
	commentExp = "^\#.+"

	#Opens a file to read/write from
	inObj = open(inFile, 'r') # The file to read datafrom
	outObj = open(outFile, 'w') #The file to write the data out to

	for line in inObj: #We have access to the infile, so now we loop for it, line by line
		if not re.match(commentExp, line): # if the line doesn't match the commentExp
			print(line) # We print the line (so we can see it)
			outObj.write(line) #And we write it into our outfile

	# Close the files because we're done editing them.
	inObj.close()
	outObj.close()
	return

if __name__ == "__main__":
	inputFile = "../Basics/1b-nutshell.py"
	removeComments(inputFile, "out.txt")
