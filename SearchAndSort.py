"""
Bobi Pu, bobi.pu@usc.edu
"""
import copy

def swap(a, i, j):
	temp = a[i]
	a[i] = a[j]
	a[j] = temp

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

def binarySearch_Recursive(n, left, right, data):
	if left == right:
		if n[left] == data:
			return data
		else:
			return None

	mid = (left + right) / 2
	if n[mid] < data:
		lResult = binarySearch_Recursive(n, mid + 1, right, data)
		if lResult is not None:
			return lResult
	else:
		rResult = binarySearch_Recursive(n, left, mid, data)
		if rResult is not None:
			return rResult

	return None

def binarySearch(array, target):
	"""
	Correct non-recursive version.
	Assume array in acsending sorted order.
	return index of target, if target in array. Else return the index that target should insert to.

	This is the framework of Binary search
	Because A[start] <= target < A[end] always holds
	"""
	start = -1
	end = len(array)
	while end - start > 1:
		mid = (end - start) / 2 + start
		if array[mid] >= target:
			end = mid
		else:
			start = mid
	return end

def getSqrt(x):
	start = -1
	end = x + 1

	while end - start > 1:
		mid = (end - start) / 2 + start
		if mid * mid > x:
			end = mid
		else:
			start = mid

	return start


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

def checkWinnerTicTacToe(b):
	size = len(b)
	if size < 3:
		return None

	#check rows
	for i in range(size):
		if b[i][0] is not None:
			for j in range(1, size):
				if b[i][j] != b[i][j - 1]:
					break
			if j == size - 1:
				return b[i][j]

	#check columns
	for i in range(size):
		if b[0][i] is not None:
			for j in range(1, size):
				if b[j][i] != b[j][i - 1]:
					break
			if j == size - 1:
				return b[i][j]


	#check diagonal
	if b[0][0] is not None:
		for i in range(1, size):
			if b[i][i] != b[i - 1][i - 1]:
				break
		if i == size - 1:
			return b[i][i]

	if b[0][size - 1] is not None:
		for i in range(1, size):
			if b[size - 1 - i][i] != b[size - i][i - 1]:
				break
		if i == size - 1:
			return b[0][size - 1]

	return None

def guessHitAndPseudoHit(solution, guess):
	s_dict = {}
	for i, color in enumerate(solution):
		if color not in s_dict:
			s_dict[color] = {i : True}
		else:
			s_dict[color][i] = True

	hit, pseudo_hit = 0, 0
	for i, color in enumerate(guess):
		if color in s_dict:
			if i in s_dict[color]:
				hit += 1
			else:
				pseudo_hit += 1
	return hit, pseudo_hit

def findStartAndEndIndiciesToMakeArraySorted(a):
	"""
	Given an array of integers, write a method to find indices m and n such that if you sorted elements m through n,the entire array would besorted.
	Minimizen - m(that is, find the smallest such sequence).

	Algo:
	For Array:
	1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19

	Split to:
	left: 1, 2, 4, 7, 10, 11
	middle: 7, 12
	right: 6, 7, 16, 18, 19

	TO make:
	min(middle) > end(left)
	max(middle) < start(right)

	So make can make:
	left < mid < right

	All need to do is:
	1)Split
	2)find min and max of middle
	"""
	def findMinMax(a, start, end):
		min_value = a[start]
		max_value = a[end]
		for i in range(start, end + 1):
			if a[i] < min_value:
				min_value = a[i]
			if a[i] > max_value:
				max_value = a[i]
		return min_value, max_value

	length = len(a)
	m_l, m_r = 0, length - 1
	for i in range(length - 1):
		if a[i] > a[i + 1]:
			m_l = i
			break

	if m_l == 0:
		# already sorted
		return

	for i in range(length - 1, m_l, -1):
		if a[i - 1] > a[i]:
			m_r = i - 1
			break

	min_mid, max_mid = findMinMax(a, m_l, m_r)
	l, r = m_l, m_r
	# find the index the more or equal than min_mid in the LEFT
	for i in range(m_l):
		if a[i] >= min_mid:
			l = i
			break

	# find the index the less or equal than max_mid in the RIGHT
	for i in range(length - 1, m_r, -1):
		if a[i] <= max_mid:
			r = i
			break

	return l, r

def selectionRank(a, left, right, rank):
	"""
	Selection Rank is an algorithm to find the "i-th" smallest (or largest) element in an array in linear time.
	If the elements are unique, you can find the ith smallest element in expected 0(n).

	The basic algorithm operates like this:
	1. Pickarandomelementinthearrayanduseitasa"pivot."Partitionelementsaround the pivot, keeping track of the number of elements on the left side of the partition.
	2. Ifthere areexactly i elements ontheleft, then you just return thebiggest element on the left.
	3. If the left side is bigger than i, repeat the algorithm on just the left part of the array.
	4. If the left side is smaller than i, repeat the algorithm on the right, but look for the element with rank i - lef tSize.
	"""
	def partition(a, left, right, pivot):
		while True:
			while left <= right and a[left] <= pivot:
				left += 1
			while left <= right and a[right] > pivot:
				right -= 1
			if left > right:
				return left - 1
			swap(a, left, right)

	pivot = a[left + right / 2]
	leftEnd = partition(a, left, right, pivot)

	leftSize = leftEnd - left + 1
	if leftSize == rank + 1:
		return max(a[left, leftEnd])
	elif rank < leftSize:
		return selectionRank(a, left, leftEnd, rank)
	else:
		return selectionRank(a, leftEnd + 1, right, rank - leftSize)

def n_largest_in_array(a, n):
	"""
	Solution:
	0.just sort.
	1.min - heap, if num is bigger than top-of-min_heap, pop top-of-min_heap, push value. time O(n log(m)), n is length of a, m is size of heap.
	2.selection rank, find the index of rank n, numbers that left of n is n-largest. If unique element, average-time O(n)

	here we use Heap
	"""
	import heapq
	heap = a[:n]
	heapq.heapify(heap)
	for num in a[n:]:
		if num > heap[0]:
			heapq.heappushpop(heap, num)

	return heap

def findCelebrity(peopleList):
	"""
	celebrity knows everyone, everyone knows celebrity. For relationship between others, call knows(a, b), return true or false
	"""
	def knows(a, b):
		if b == 0 or (a != 0 and b != 0 and (a + b) % 2 ==0):
			return True
		else:
			return False

	while len(peopleList) > 1:
		foundCelebrity = True
		for i in range(1, len(peopleList)):
			if knows(peopleList[0], peopleList[i]):
				foundCelebrity = False
				if knows(peopleList[i], peopleList[0]):
					peopleList.pop(0)
					peopleList.pop(0)
				else:
					peopleList.pop(0)
				break
		if foundCelebrity:
			return peopleList[0]
	return None


if __name__ == '__main__':
	n = [-1, 3, 5, 6, 8, 10]
	a = [1, 2, 4, 7, 10 ,7, 12, 6, 7, 16, 18, 19]
	# bublleSort(n)
	# mergeSort(n, 0, len(n))
	# quickSort(n, 0, len(n) - 1)
	# print(n)
	# print(binarySearch_Recursive(n, 0, len(n) - 1, 3))
	# print(binarySearch(n, 5))
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

	# solution = ['R', 'R', 'G', 'B']
	# guess = ['R', 'Y', 'R', 'B']
	# print(guessHitAndPseudoHit(solution, guess))


	# print(findStartAndEndIndiciesToMakeArraySorted(a))
	# print(n_largest_in_array(a, 3))

	print(findCelebrity([1, 2, 3, 0, 4, 5, 6, 7, 8]))