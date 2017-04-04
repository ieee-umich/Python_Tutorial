import fileinput
import re

# Opens File, returns file obj.

def removeComments(inFile, outFile):
	
	commentExp = "^\#.+"

	inObj = open(inFile, 'r')
	outObj = open(outFile, 'w')

	for line in inObj:
		if not re.match(commentExp, line):
			print(line)
			outObj.write(line)

	inObj.close()
	outObj.close()
	return





if __name__ == "__main__":
	inputFile = "../Basics/1b-nutshell.py"
	removeComments(inputFile, "out.txt")
