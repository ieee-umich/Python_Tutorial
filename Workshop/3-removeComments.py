import fileimport
import re

# Opens File, returns file obj.

def removeComments(inFile, outFile):
	
	commentExp = "^\#.+"

	outFile = 

	with open(...) as f:
	    for line in f:
	        <do something with line>

	return


f = open("target.txt","r+")
d = f.readlines()
f.seek(0)
for i in d:
    if i != "line you want to remove...":
        f.write(i)
f.truncate()
f.close()




if __name__ == "__main__":
	filename = "../Basics/1b-nutshell.py"
	removeComments
