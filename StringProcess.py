"""
Bobi Pu
bobi.pu@usc.edu
"""
import re

def XML_to_string(xmlString):

	def extractPartsFromLine(line):
		partList = re.findall(r'<[^>]*>', line)
		if len(partList) == 2:
			message = re.findall(r'>[^<]*<', line)
			if message:
				partList.insert(1, message[0][1:-2])
		return partList

	def processPartList(partList):
		resultList = []
		if len(partList) == 3:
			resultList += processBracket(partList[0])
			resultList.append(partList[1])
			resultList.append('0')
		else:
			resultList = processBracket(partList[0])
		return resultList

	def processBracket(string):
		if string[1] == '/':
			return ['0']

		wordList = string[1: -2].split()
		resultList = []
		for word in wordList:
			if word.find('=') == -1:
				resultList.append(getIndexFromWordDict(wordDict, word))
			else:
				[attribute, value] = word.split('=')
				resultList.append(getIndexFromWordDict(wordDict, attribute))
				resultList.append(value.replace('"', ''))

		return resultList

	def getIndexFromWordDict(wordDict, word):
		if word not in wordDict:
			wordDict[word] = str(len(wordDict) + 1)
		return wordDict[word]

	lineList = xmlString.split('\n')
	wordDict = {}
	resultList = []
	for line in lineList:
		partList = extractPartsFromLine(line)
		resultList += processPartList(partList)

	return ' '.join(resultList)


if __name__ == '__main__':
	pass
	xmlStrign = '<family lastName="McDowell" state="CA">\n<person firstName="Gayle">Some Message</person>\n</family>'
	print(XML_to_string(xmlStrign))