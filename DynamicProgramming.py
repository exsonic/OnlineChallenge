import copy
from math import factorial
import math


def Fibonacci(n):
	cache = [1, 2]
	for i in range(2, n):
		temp = cache[i - 1] + cache[i - 2]
		cache.append(temp)
	print(cache[-1])

def maxPossibleHopNumber(n):
	opt = [0, 1, 2, 4]
	if n <= len(opt):
		return opt[n]
	for i in range(3, n + 1):
		opt.append(max(opt[i - 1] * opt[1], opt[i - 2] * opt[2], opt[i - 3] * opt[3]))

	print(opt[n])

def maxPossiblePathFromOriginalTo_DP(a, b):
	opt = [[0 for _ in range(a + 1)] for _ in range(b + 1)]

	opt[0] = [1] * (a + 1)
	for j in range(b + 1):
		opt[j][0] = 1

	for i in range(1, a + 1):
		for j in range(1, b + 1):
			opt[j][i] = (opt[j - 1][i]) + (opt[j][i - 1])

	print(opt[b][a])

def maxPossiblePathFromOriginalTo_Compute(a, b):
	value = factorial(a + b) / (factorial(a) * factorial(b))
	print(value)

def maxPossiblePathFromOriginalTo_DP_withOffSpot(a, b, offSpotMatrix):
	opt = [[0 for _ in range(a + 1)] for _ in range(b + 1)]

	for i in range(a + 1):
		opt[0][i] = 1 if not offSpotMatrix[0][i] else 0

	for j in range(b + 1):
		opt[j][0] = 1 if not offSpotMatrix[j][0] else 0

	for i in range(1, a + 1):
		for j in range(1, b + 1):
			opt[j][i] = 0 if offSpotMatrix[j][i] else (opt[j - 1][i]) + (opt[j][i - 1])

	print(opt[b][a])

def findMagicIndex(sortedArray):
	if not sortedArray:
		return None

	mid = len(sortedArray) / 2
	if sortedArray[mid] == mid:
		return mid
	elif sortedArray[mid] > mid:
		return findMagicIndex(sortedArray[0:mid])
	else:
		return findMagicIndex(sortedArray[mid + 1:])

def findMagicIndexWithDuplicate(array, start, end):
	if not array or start >= end:
		return None

	mid = (end - start) / 2 + start
	if array[mid] == mid:
		return mid
	elif array[mid] > mid:
		index = max(mid, array[mid]) + 1
		return findMagicIndexWithDuplicate(array, start, index)
	else:
		index = min(mid, array[mid])
		return findMagicIndexWithDuplicate(array, index, end)


def findAllPossibleSubset(s):
	"""
	opt(i) is the all subset of s[:i]
	opt(i) = opt(i - 1) + [subset.append(i) for subset in opt(i - 1)] + [i]
	"""
	subsetList = []
	for i in range(len(s)):
		newAddList = []
		for subset in subsetList:
			temp = list(subset)
			temp.append(i)
			newAddList.append(temp)
		subsetList += newAddList
		subsetList.append([s[i]])
	return subsetList


def getAllStringPermutation(string):
	if not string:
		return []
	p = [string[0]]
	for i in range(1, len(string)):
		newPList = []
		for s in p:
			for j in range(len(s) + 1):
				temp = s[:j] + string[i] + s[j:]
				newPList.append(temp)
		p = newPList
	return p

def getAllParentheseWithDict(n):
	"""
	Brutal force seach, just use dict to avoid duplicate
	"""
	if n == 0:
		return []

	pDict = {'()' : True}
	for i in range(1, n):
		p = '()'
		new_p_dict = {}
		for pString in pDict.iterkeys():
			for j in range(len(pString) + 1):
				temp = pString[:j] + p + pString[j:]
				if temp not in new_p_dict:
					new_p_dict[temp] = True
		pDict = new_p_dict
	return pDict.keys()

def getAllParentheseWithoutDict(n):
	"""
	loop from 0 to end, for each slot try '(' then ')' if output is valid
	"""
	def addParenthese(leftRemain, rightRemain, count):
		if leftRemain < 0 or rightRemain < leftRemain:
			return

		if leftRemain == 0 and rightRemain == 0:
			pList.append(''.join(charArray))
		else:
			# Only two situation that can add paren and keep output valid
			if leftRemain > 0:
				charArray[count] = '('
				addParenthese(leftRemain - 1, rightRemain, count + 1)
			if rightRemain > leftRemain:
				charArray[count] = ')'
				addParenthese(leftRemain, rightRemain - 1, count + 1)

	charArray = [''] * (n * 2)
	pList = []
	addParenthese(n, n, 0)
	return pList


def minNumberOfCoinToGetN(n):

	def getOpt(n):
		if n <= 0:
			return 0
		else:
			return opt[n]

	if n <= 0:
		return 0

	opt = [0, 1]
	for i in range(1, n + 1):
		opt.append(min(getOpt(i - 25), getOpt(i - 10), getOpt(i - 5), getOpt(i - 1)) + 1)
	return opt[n]

def maxCombinationOfCoinsToGetN(n, currentDomination):
	"""
	Denomination are :1, 5, 10, 25

	Decide the largest demoniation "quarter" first, split to subproblem
	makeChange(100) = makeChange(100, used 0 quarters) +
					  makeChange(75, used 1 quarters) +
					  makeChange(50, used 2 quarters) +
					  makeChange(25, used 3 quarters) +
					  makeChange(0, 4 quarters)

	Then, for each subprolem decide the next largest denomintation "dime"
	makeChange(100, used 0 quarters) =  makeChange(100, used 0 quarters, 0 dimes) +
										makeChange(90, used 0 quarters, 1 dimes) +
										makeChange(80, used 0 quarters, 2 dimes) +
										...
										makeChange(0, used 0 quarters, 10 dimes)

	Recurse to 0 cent left.
	"""
	def nextDemoination(n):
		if n == 25:
			return 10
		elif n == 10:
			return 5
		elif n == 5:
			return 1
		else:
			return 1

	if currentDomination == 1:
		return 1

	combination = 0
	nextDenom = nextDemoination(currentDomination)
	for left in range(n, -1, -currentDomination):
		combination += maxCombinationOfCoinsToGetN(left, nextDenom)

	return combination


def n_queen_with_board_update(n, row, board, record):
	"""
	This is the dumb solution!!!!!
	"""
	def updateBoard(board, a, b, value):
		length = len(board)
		for i in range(length):
			board[i][a] = value

		for i in range(length):
			board[b][i] = value

		# pos slope is 1, y = x + (b - a)
		for x in range(length):
			y = x + (b - a)
			if 0 <= y < length:
				board[y][x] = value

		# neg slope is -1, y = -x + (a + b)
		for x in range(length):
			y = -x +  (a + b)
			if 0 <= y < length:
				board[y][x] = value

	takenSpot = False
	newBoard = copy.deepcopy(board)
	for x in range(n):
		if newBoard[row][x]:
			takenSpot = True
			updateBoard(newBoard, x, row, False)
			record[row] = x
			if row == n - 1:
				print(record)
			else:
				n_queen_with_board_update(n, row + 1, newBoard, record)

			newBoard = copy.deepcopy(board)

	if not takenSpot:
		return
		# if you wanna check all the possible arrangement, less than N queen, comment the following code
		###################
		# record[row] = -1
		# if row < n - 1:
		# 	n_queen_with_board_update(n, row + 1, newBoard, count, record)
		# else:
		# 	print(record)

def n_queen_CTCI(n, row, record):
	"""
	From x = 0 to n, each column place a queen.
	For next column, only check self position that are invalidated by previous columns or not
	Index of record is x
	"""
	def checkValid(record, a, b):
		for x in range(a):
			y = record[x]

			if x == a or y == b:
				return False
			x_distance = abs(a - x)
			y_distance = abs(b - y)
			if x_distance == y_distance:
				return False
		return True

	if row == n:
		print(record)
	else:
		for y in range(n):
			if checkValid(record, row, y):
				record[row] = y
				n_queen_CTCI(n, row + 1, record)

def highestStack(boxList):
	"""
	Box is (depth, width, hight)
	O(n**3), basically brutal force, no cache used
	"""
	n = len(boxList)
	opt = [[0 for _ in range(n)] for _ in range(n)]
	backPointer = [[-1 for _ in range(n)] for _ in range(n)]

	for i in range(n):
		opt[0][i] = boxList[i][-1]
		backPointer[0][i] = 0

	for i in range(1, n):
		lastLayer = [k for k in range(n) if opt[i - 1][k] > 0]
		for j in range(n):
			maxIndex = -1
			maxHeight = 0
			box = boxList[j]
			for k in lastLayer:
				last_layer_box = boxList[k]
				height = opt[i - 1][k] + box[2]
				if last_layer_box[0] > box[0] and last_layer_box[1] > box[1] and last_layer_box[2] > box[2] and height > maxHeight:
					maxIndex = k
					maxHeight = height

			opt[i][j] = maxHeight if maxIndex != -1 else 0
			backPointer[i][j] = maxIndex

	#trace back
	maxHeight = 0
	maxIndex = 0
	for i in range(n):
		if opt[n - 1][i] > maxHeight:
			maxHeight = opt[n - 1][i]
			maxIndex = i
	maxStack = []
	for i in range(n - 1, -1, -1):
		maxStack.append(boxList[maxIndex])
		maxIndex = backPointer[i][maxIndex]

	print(maxStack)


def highestStack_Recursive(boxList, bottom, stackMap):
	"""
	deepcopy cost
	"""
	def stackHeight(stackList):
		total = 0
		for box in stackList:
			total += box[-1]
		return total


	if bottom is not None and bottom in stackMap:
		return stackMap[bottom][:]

	maxHeight = 0
	maxStack = None

	for i in range(len(boxList)):
		box = boxList[i]
		if bottom is None or (bottom[0] > box[0] and bottom[1] > box[1] and bottom[2] > box[2]):
			newStack = highestStack_Recursive(boxList, box, stackMap)
			newHeight = stackHeight(newStack)
			if newHeight > maxHeight:
				maxStack = newStack
				maxHeight = newHeight

	if maxStack is None:
		maxStack = []
	if bottom is not None:
		maxStack.insert(0, bottom)

	if bottom is not None:
		stackMap[bottom] = maxStack

	return maxStack



if __name__ == '__main__':
	pass
	# Fibonacci(5)
	# maxPossibleHopNumber(10)
	# maxPossiblePathFromOriginalTo_DP(2, 2)
	# maxPossiblePathFromOriginalTo_Compute(2, 2)
	# maxPossiblePathFromOriginalTo_DP_withOffSpot(2, 2, [[False, False, False], [False, True, False], [False, False, False]])
	# a = [-11, -3, -3, -3, 0, 2, 6,9,10, 11]
	# print(findMagicIndexWithDuplicate(a, 0, len(a)))
	# print(findAllPossibleSubset(range(10)))
	# print(len(getAllStringPermutation('abcdefghijk')))
	# print(len(getAllParentheseWithDict(14)))
	# print(getAllParentheseWithoutDict(3))
	# print(minNumberOfCoinToGetN(1))
	# print(maxCombinationOfCoinsToGetN(200, 25))
	# n = 10
	# record = [-1] * n
	# board = [[True for _ in range(n)] for _ in range(n)]
	# n_queen_with_board_update(n, 0, board, record)
	# n_queen_CTCI(n, 0, record)
	# n = 600
	# boxList = [(i, i, i) for i in range(1, n)]
	# stackMap = {}
	# highestStack(boxList)
	# highestStack_Recursive(boxList, None, stackMap)
	# print(stackMap)
