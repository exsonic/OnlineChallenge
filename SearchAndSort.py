"""
Bobi Pu, bobi.pu@usc.edu
"""
import copy
from Tree import getTree


def bublleSort(n):
	"""
	Time: O(n^2)
	Space: O(1)
	"""
	if len(n) <= 1:
		return n

	length = len(n)
	for i in range(length):
		swapped = False
		for j in range(0, length - i - 1):
			if n[j] > n[j + 1]:
				swapped = True
				temp = n[j]
				n[j] = n[j + 1]
				n[j + 1] = temp
		if not swapped:
			break
	return n

def mergeSort(n, start, end):
	"""
	Time: O(nlogn)
	Space: O(n)
	"""
	if len(n) <= 1 or start >= (end - 1):
		return

	mid = (end + start) / 2
	mergeSort(n, start, mid)
	mergeSort(n, mid, end)

	#merge
	l, r = start, mid
	sortedArray = []
	while l < mid and r < end:
		if n[l] < n[r]:
			sortedArray.append(n[l])
			l += 1
		else:
			sortedArray.append(n[r])
			r += 1

	if l == mid:
		# r left
		while r < end:
			sortedArray.append(n[r])
			r += 1
	else:
		while l < mid:
			sortedArray.append(n[l])
			l += 1
	for i in range(start, end):
		n[i] = sortedArray[i - start]

def quickSort(n, start, end):
	"""
	Time: O(n^2) worst case, O(nlogn) average
	Space:O(logn)
	"""
	if end - start <= 0:
		return

	# Split first, left should be less than right
	left = start
	right = end
	pivot = n[(end + start) / 2]
	while left <= right:
		while n[left] < pivot:
			left += 1
		while n[right] > pivot:
			right -= 1

		if left <= right:
			temp = n[left]
			n[left] = n[right]
			n[right] = temp
			left += 1
			right -= 1


	if start < right:
		quickSort(n, start, right)
	if left < end:
		quickSort(n, left, end)

def binarySearch(n, left, right, data):
	if left == right:
		if n[left] == data:
			return data
		else:
			return None

	mid = (left + right) / 2
	if n[mid] < data:
		lResult = binarySearch(n, mid + 1, right, data)
		if lResult is not None:
			return lResult
	else:
		rResult = binarySearch(n, left, mid, data)
		if rResult is not None:
			return rResult

	return None

def DFS(root, data):
	if root is None:
		return None

	if root.data == data:
		return root
	lResult = DFS(root.left, data)
	if lResult is not None:
		return lResult
	rResult = DFS(root.right, data)
	if rResult is not None:
		return rResult
	return None

def BFS(root, data):
	q = [root]
	while len(q) > 0:
		n = q.pop(0)
		if n.data == data:
			return n
		if n.left is not None:
			q.append(n.left)
		if n.right is not None:
			q.append(n.right)

def mergeTwoSortedArrayFromBack(a, b, a_buffer):
	"""
	Both a and b are sorted.
	Assume a has long enough buffer to hold b.
	Merge them from the back.
	"""
	insert_index, a_index, b_index = len(a) + len(b) - 1, len(a) - 1, len(b) - 1
	a += a_buffer
	while a_index >= 0 and b_index >= 0:
		if a[a_index] > b[b_index]:
			a[insert_index] = a[a_index]
			a_index -= 1
		else:
			a[insert_index] = b[b_index]
			b_index -= 1
		insert_index -= 1
	while a_index >= 0:
		a[insert_index] = a[a_index]
		insert_index -= 1
		a_index -= 1
	while b_index >= 0:
		a[insert_index] = b[b_index]
		insert_index -= 1
		b_index -= 1
	return a


def sortListOfWordAndAnagramGroup(wordList):
	def isAnagram(charCountDict, word):
		a = copy.deepcopy(charCountDict)
		for char in word:
			if char not in a:
				return False

			a[char] -= 1
			if a[char] == 0:
				del a[char]

		return False if a else True

	def getCharCountDict(string):
		charCountDict = {}
		for char in string:
			charCountDict[char] = 1 if char not in charCountDict else (charCountDict[char] + 1)
		return charCountDict

	i = 0
	while i < len(wordList):
		charCountDict = getCharCountDict(wordList[i])
		swapIndex = i + 1
		for j in range(i + 1, len(wordList)):
			if isAnagram(charCountDict, wordList[j]):
				temp = wordList[swapIndex]
				wordList[swapIndex] = wordList[j]
				wordList[j] = temp
				swapIndex += 1
		i = swapIndex


def findIndexOfRotatedArray(a, n):
	for i in range(len(a) - 1):
		if a[i] > a[i + 1]:
			b = a[(i + 1) :] + a[: (i + 1)]
			break
	return b.index(n)

def binarySearchWordListWithEmpty(wordList, left, right, word):
	if left > right or left < 0 or right >= len(wordList):
		return None

	mid = (left + right) / 2
	while mid >= left:
		if wordList[mid] != word and wordList[mid] == "":
			mid += 1
		else:
			break

	if wordList[mid] != word:
		if wordList[mid] > word:
			return binarySearchWordListWithEmpty(wordList, left, mid - 1, word)
		else:
			return binarySearchWordListWithEmpty(wordList, (left + right) / 2 + 1, right, word)
	else:
		return mid


def findElementInSortedMatrix_Elimination(m, data):
	"""
	M*N matrix
	Time:O(Max(M,N))
	Space:O(1)

	Algo: Scan from up right
	"""
	row, column = 0, len(m[0]) - 1
	while row >= 0 and column < len(m[0]):
		if m[row][column] == data:
			return data
		elif m[row][column] < data:
			row += 1
		else:
			column -= 1
	return None

def findElementInSortedMatrix_BinarySearch(m, data, start, end):
	"""
	Psedudo code, not runable
	"""
	def getUpLeftValue(m, start, end, mid):
		if mid[0] - 1 < start[0] or mid[1] - 1 < start[1]:
			return m[mid[0]][mid[1]]
		else:
			return m[mid[0] - 1][mid[1] - 1]

	if start == end:
		return data if m[start[0]][start[1]] == data else None

	mid = ((start[0] + end[0]) / 2, (start[1] + end[1]) / 2)
	midValue = m[mid[0]][mid[1]]
	leftUpValue = getUpLeftValue(m, start, end, mid)
	if midValue == data or leftUpValue == data:
		return data
	elif leftUpValue < data < midValue:
		# should be on right-up or left down
		a = findElementInSortedMatrix_BinarySearch(m, data, (mid[0], start[1]), (end[0], mid[1] - 1))
		b = findElementInSortedMatrix_BinarySearch(m, data, (start[0], mid[1]), (mid[0] - 1, end[1]))
	elif data > midValue:
		# eliminate left-up
		a = findElementInSortedMatrix_BinarySearch(m, data, (mid[1] + 1, start[0]), end)
		b = findElementInSortedMatrix_BinarySearch(m, data, (start[0], mid[1] + 1), (mid[0] + 1, end[1]))
	elif data < leftUpValue:
		# elimnate right dwon
		a = findElementInSortedMatrix_BinarySearch(m, data, start, (mid[0] - 1, end[1]))
		b = findElementInSortedMatrix_BinarySearch(m, data, (mid[0] + 1, start[1]), (end[0], mid[1] - 1))

	if a is None and b is None:
		return None
	else:
		return a if a is None else b

def maxPeopleStack(remainPeopleList, bottom, cacheTable):
	def isCompatible(bottom, person):
		return bottom is None or (bottom[0] > person[0] and bottom[1] > person[1])

	if not remainPeopleList:
		return []

	if bottom in cacheTable:
		return cacheTable[bottom]

	maxStack = []
	for i, person in enumerate(remainPeopleList):
		if isCompatible(bottom, person):
			newRemainPeopleList = remainPeopleList[:i-1] + remainPeopleList[i:]
			newStack = maxPeopleStack(newRemainPeopleList, person, cacheTable)
			if len(newStack) > len(maxStack):
				maxStack = newStack

	maxStack.insert(0, bottom)
	cacheTable[bottom] = maxStack

	return maxStack

if __name__ == '__main__':
	n = [5, 1, 3, 4, 2, 0, -1]
	# bublleSort(n)
	# mergeSort(n, 0, len(n))
	# quickSort(n, 0, len(n) - 1)
	# print(n)
	# print(binarySearch(n, 0, len(n) - 1, 3))
	# root = getTree()
	# print(DFS(root, 6).data)
	# print(BFS(root, 6).data)
	# a, b, a_buffer = range(3), range(4), [-1] * 10
	# a = mergeTwoSortedArrayFromBack(a, b, a_buffer)
	# print(a)

	# wordList = ['abc', 'ccc', 'cba', 'bbb', 'bca', 'zxy', 'ddd', 'yxz']
	# sortListOfWordAndAnagramGroup(wordList)
	# print(wordList)
	# print(findIndexOfRotatedArray([5 ,6,7,1,2,3,4], 3))

	# wordList = ['a', '', '', 'b', 'c', '', '', 'd', '', 'e']
	# print(binarySearchWordListWithEmpty(wordList, 0, len(wordList) - 1,''))

	# m = [[1,2,3,4],[5,6,7,8],[9, 10,11,12]]
	# print(findElementInSortedMatrix_Elimination(m, 11))
	# peopleList = [(65, 100), (70, 150), (56, 90), (75, 190), (60, 95), (68, 110)]
	# print(maxPeopleStack(peopleList, None, {}))