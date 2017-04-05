import os
import subprocess
import glob

# Disclaimer: If you want to do a full, more robust amount of testing, 
# I would recommend using the unittest library
import unittest # <- Yeah this one
# But it requires a little more than what we're just going over in this
# tutorial (e.g. classes), but with a little bit reading, it's not
# too hard.

def runTests(folderPath):
	outputList = []

	files = glob.glob(os.path.join(folderPath, "*.cpp"))
	flags = ["g++", "-O3", "-pedantic", "-Werror",  "-o", "testout"] 

	for file in files:
		try:
			compileCommand = flags + [file]
			subprocess.check_call(compileCommand)
			executeCommand = ["./testout"]

			output = subprocess.check_output(executeCommand)
			# print(output)
			outputList.append(str(output.strip(), 'utf-8'))

		except subprocess.CalledProcessError:
			print(file + " failed")
			outputList.append("|"+file+"|" + " Failed")
	return outputList

def getSolutions(filepath):
	inObj = open(filepath, 'r')
	solutionList = inObj.read().split('\n')
	# print(solutionList)
	return solutionList

def compareLists(testcaseList, solutionList):
	if len(testcaseList) != len(solutionList):
		print("list lengths are not consistent")
		return
	else:
		numPassed = 0
		numCases = len(testcaseList)

		for i in range(numCases):
			if testcaseList[i] == solutionList[i]:
				numPassed+=1
			else:
				print("failed case:" + str(i))
		print("Passed: " + str(numPassed) +'/'+ str(numCases) + " cases.")
		return numPassed

def main():
	outputList = runTests("../cppSample/testcases")
	solutionList = getSolutions("../cppSample/answers/answers.txt")
	compareLists(outputList, solutionList)

	return


if __name__ == "__main__":
	main()