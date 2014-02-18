"""
Bobi Pu
bobi.pu@usc.edu
"""
import copy
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

def splitStringToWord(string, start, wordDict, cacheTable):
	"""
	Cache the false situation
	"""
	if string[start:] in cacheTable:
		return cacheTable[string[start:]]

	if start == len(string):
		return True, [[]]

	hasSplit = False
	wordList = []
	for j in range(start + 1, len(string) + 1):
		word = string[start : j]
		if word in wordDict:
			result, tempWordList = splitStringToWord(string, j, wordDict, cacheTable)

			if result:
				hasSplit = True
				for subWordList in tempWordList:
					subWordList.insert(0, word)
					wordList.append(subWordList)

	cacheTable[string[start:]] = hasSplit, wordList
	return hasSplit, copy.deepcopy(wordList)

def findShortesDistanceBetweenTwoArray(a, b):
	"""
	merge with tag, sort, then compare the neighbor
	"""
	n_dict = {}
	for n in a:
		n_dict[n] = True
	for n in b:
		if n in a:
			return 0
		else:
			n_dict[n] = False

	sortedList = sorted(n_dict.keys())
	min_v = abs(sortedList[0] - sortedList[1])
	for i in range(1, len(n_dict) - 1, 1):
		v = abs(sortedList[i] - sortedList[i + 1])
		if v < min_v and n_dict[sortedList[i]] != n_dict[sortedList[i+1]]:
			min_v = v
	return min_v

def isSubString(s, sub):
	for i in range(len(s) - len(sub)):
		isSub = True
		for j in range(len(sub)):
			if sub[j] != s[i + j]:
				isSub = False
				break
		if isSub:
			break
	return isSub

def LCString(s1, s2):
	"""
	Longest common subString
	Time:O(n^2) Space:O(n^2)
	OPT(i, j): length of longest common substring that ends with s1[i], s2[j].
	OPT(i, j) = opt(i-1, j-1) + 1 if s1[i] == s2[j] else 0
	"""
	opt = [[0 for _ in range(len(s1))] for _ in range(len(s2))]

	for i, char in enumerate(s1):
		opt[0][i] = int(char == s2[0])

	for i, char in enumerate(s2):
		opt[i][0] = int(char == s1[0])


	longest = 0
	s1_start, s2_start = 0, 0
	for i in range(1, len(s1), 1):
		for j in range(1, len(s2), 1):
			opt[j][i] = opt[j - 1][i - 1] + 1 if s1[i] == s2[j] else 0

			if opt[j][i] > longest:
				longest = opt[j][i]
				s1_start = i - longest + 1
				s2_start = j - longest + 1



	return s1[s1_start : s1_start+longest]

def LCSequence(s1, s2):
	"""
	Longest common subString
	Time:O(n^2) Space:O(n^2)
	OPT(i, j): length of longest common substring that ends with s1[i], s2[j].
	OPT(i, j) = opt(i-1, j-1) + 1 if s1[i] == s2[j] else MAX(OPT[i - 1][j], opt[i][j - 1])
	"""
	opt = [[0 for _ in range(len(s1))] for _ in range(len(s2))]

	longest = 0

	longest_sequence = []
	for i, char in enumerate(s1):
		if char == s2[0]:
			opt[0][i] = 1
		else:
			opt[0][i] = opt[0][i - 1] if i != 0 else 0
		if opt[0][i] > longest:
			longest_sequence.append(char)
			longest = opt[0][i]

	for i, char in enumerate(s2[1:]):
		if char == s1[0]:
			opt[i][0] = 1
		else:
			opt[i][0] = opt[i - 1][0] if i != 0 else 0
		if opt[i][0] > longest:
			longest_sequence.append(char)
			longest = opt[i][0]


	for i in range(1, len(s1), 1):
		for j in range(1, len(s2), 1):
			if s1[i] == s2[j]:
				opt[j][i] = opt[j - 1][i - 1] + 1
			else:
				opt[j][i] = max(opt[j - 1][i], opt[j][i - 1])

			if opt[j][i] > longest:
				longest_sequence.append(s1[i])
				longest = opt[j][i]

	print(longest_sequence)

if __name__ == '__main__':
	pass
	# xmlStrign = '<family lastName="McDowell" state="CA">\n<person firstName="Gayle">Some Message</person>\n</family>'
	# print(XML_to_string(xmlStrign))
	# wordDict = dict(zip(['i', 'a', 'the', 'he', 'at', 'doctor'], [0] * 6))
	# print(splitStringToWord('iathedoctor', 0, wordDict, {}))
	# print(findShortesDistanceBetweenTwoArray([1, 2, 3, 5], [4, 10, 20,30]))
	# print(isSubString('abced', 'abc'))
	print(LCString('abcdefghijk', 'efghi'))
	LCSequence('aabbccdd', 'abcde')