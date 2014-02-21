"""
Bobi Pu, bobi.pu@usc.edu
"""
import copy
import sys


def strStr(needle, hayStack):
	"""
	Substring problem, return the first index of subString(needle) in string(hayStack)
	"""
	if not needle:
		return 0
	if not hayStack or len(needle) > len(hayStack):
		return None

	needleLen, hayStackLen = len(needle), len(hayStack)
	for i in range(hayStackLen - needleLen):
		j = i
		k = 0
		for char in needle:
			if char == hayStack[j]:
				j += 1
				k += 1
			else:
				break
		if k == needleLen:
			return i
	return None

def longest_substr_without_repeat(string):
	maxLen, start = 0, 0
	charDict = {}
	for i, char in enumerate(string):
		if char in charDict:
			if len(charDict) > maxLen:
				maxLen = len(charDict)
				start = i - len(charDict)
			charDict = {char : True}
		else:
			charDict[char] = True

	if len(charDict) > maxLen:
		return string[-len(charDict):]
	else:
		return string[start : start + maxLen]

def min_window(s, t):
	"""
	Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).
	"""
	min_begin, minL = 0, sys.maxint
	needToFind, hasFound = {}, {}

	for c in t:
		hasFound[c] = 0
		if c in needToFind:
			needToFind[c] += 1
		else:
			needToFind[c] = 1

	count, start = 0, 0
	for end, c in enumerate(s):
		if c not in needToFind:
			continue
		hasFound[c] += 1

		if hasFound[c] <= needToFind[c]:
			count += 1

		# find a window
		if count == len(t):

			#advance begin index as far as possible until we lost a char
			while s[start] not in needToFind or hasFound[s[start]] > needToFind[s[start]]:
				if s[start] in needToFind and hasFound[s[start]] > needToFind[s[start]]:
					hasFound[s[start]] -= 1
				start += 1

			windowLen = end - start + 1
			if minL > windowLen:
				minL = windowLen
				min_begin = start


	return s[min_begin : min_begin + minL]

def remove_duplicate_in_array(a):
	"""
	Given a array, remove the duplicates in place such that each element appear only once and return the new length.
	"""
	if not a or len(a) == 1:
		return a

	start, end = 0, len(a) - 1
	while start < end:
		i = start + 1
		while i <= end:
			if a[start] == a[i]:
				a[i] = a[end]
				end -= 1
			i += 1
		start += 1
	return a[:end + 1]

def remove_duplicate_in_sorted_array(a):
	"""
	Given a SORTED array, remove the duplicates in place such that each element appear only once and return the new length.
	"""
	if not a or len(a) == 1:
		return a

	index = 0
	for i in range(len(a)):
		if a[index] != a[i]:
			index += 1
			a[index] = a[i]

	return a[:index + 1]

def remove_element(a, n):
	"""
	remove n in array a.
	Two pointer, i for iter, index for write.
	if != n, write index as a[i]
	else move i, index stay
	"""
	index = 0
	for i in range(len(a)):
		if a[i] != n:
			a[index] = a[i]
			index += 1
	return a[:index]



if __name__ == '__main__':
	pass
	# print(strStr('cdef', 'abcdefg'))

	# print(longest_substr_without_repeat('abccdefgga'))

	# print(min_window('ABCDOBECODEBBBANC', 'ABC'))

	# print(remove_duplicate_in_array([8,8,1, 2, 3, 4, 5, 5, 6, 7, 7]))
	# print(remove_duplicate_in_sorted_array([1,2,2,3,3,4,4,5,6]))
	print(remove_element([1,2,3,3,3,4,5,6,0], 3))