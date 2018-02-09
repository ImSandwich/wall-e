import urllib.request
import os
import time
import datetime
def readFile(fileName):
	filePath = os.path.join(os.getcwd(), fileName)
	fStream = open(filePath, 'r')
	fText = fStream.read()
	fStream.exit()
	return fText
	
def writeFile(fileName, fileContent):
	filePath = os.path.join(os.getcwd(), fileName)
	fStream = open(filePath, 'w')
	for line in fileContent.split('\\n'):
		fStream.writelines(line + "\n")
	fStream.close()
	
def readUrl(urlPath):
	urlReader = urllib.request.urlopen(urlPath)
	return urlReader.read()

def cleanText(inputStr):
	indexFirst = -1
	indexLast = -1
	curIndex = 0
	
	for a in list(inputStr):
		if a is "'":
			indexLast = curIndex
			if indexFirst is -1:
				indexFirst = curIndex
		curIndex+=1
	print(indexFirst)
	print(indexLast)
	return inputStr[int(indexFirst) + 1:int(indexLast)]
				
def updateRoutine(url, intervals):
	print('Attempt to read {} @ {}'.format(url,datetime.datetime.now()))
	urlContent = cleanText(str(readUrl(url)))
	print('Content:')
	print(urlContent)
	writeFile('terminal.txt', str(urlContent))
	time.sleep(intervals)
	updateRoutine(url,intervals)
	
if __name__ == "__main__":

	url = input("URL:")
	intervals = 300
	updateRoutine(url,intervals)
	
	

	
