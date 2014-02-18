"""
Bobi Pu, bobi.pu@usc.edu
"""
import math
import random


def swap_bit(a,b):
	a = a ^ b
	b = a ^ b
	a = a ^ b
	return a, b

def countFactorialTrailingZeros_V1(num):
	"""
	Count how many 10 = how many 2 * 5 = how many 5 (2 is always more than 5)
	"""
	def factorOf5(n):
		count = 0
		while n % 5 == 0:
			count += 1
			n /= 5
		return count

	count = 0
	for i in range(2, num + 1):
		count += factorOf5(i)
	return count

def countFactorialTrailingZeros_V2(num):
	count = 0
	i = 5
	while num / i > 0:
		count += (num / i)
		i *= 5

	return count

def compareTwoNumberWithoutComparator(a, b):
	"""
	Return bigger one
	"""
	try:
		x = (a - b) / abs(a - b)
	except:
		return a

	return  ((a - b) + x * (a + b)) / (2 * x)


def numberToEnglishString_useStack(num):
	def commaToUnit(k):
		if k == 1:
			return 'thousand'
		elif k == 2:
			return 'million'
		elif k == 3:
			return 'billion'
		elif k == 4:
			return 'trillion'
		else:
			return 'ERROR'


	def numberCharArrayLessThanThousandToString(a):
		def processTen(a):
			tenPartList = []
			if len(a) > 1:
				if a[-1] == '0':
					tenPartList.append(tenIntList[int(a[1])])
				elif a[0] == '1':
					if a[1] == '0':
						tenPartList.append('ten')
					else:
						tenPartList.append(oneTenIntList[int(a[1])])
				else:
					tenPartList.append(tenIntList[int(a[0])])
					tenPartList.append(singleIntList[int(a[1])])
			else:
				tenPartList.append(singleIntList[int(a[0])])
			return ' '.join(tenPartList)

		singleIntList = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
		oneTenIntList = ['', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'eighteen', 'nineteen']
		tenIntList = ['', 'ten', 'twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
		length = len(a)
		if length > 3:
			return numberToEnglishString_useStack(a)

		zeroCount = 0
		for i in range(length):
			if a[i] == '0':
				zeroCount += 1

		if zeroCount == length:
			return ''

		partList = []
		if length == 3:
			partList.append(singleIntList[int(a[0])])
			partList.append('hunderd')
			partList.append(processTen(a[1:]))
		elif length == 2:
			partList.append(processTen(a))
		elif length == 1:
			partList.append(singleIntList[int(a[0])])

		return ' '.join(partList)

	digitList = []
	unitCount = 0
	inputNumString = str(num)
	for i in range(len(inputNumString) - 1, -1, -1):
		char = inputNumString[i]
		digitList.append(char)
		if (len(inputNumString) - i) % 3 == 0:
			unitCount += 1
			digitList.append(',')

	buffList, outputList = [], []
	while digitList:
		c = digitList.pop()
		if c == ',':
			numString = numberCharArrayLessThanThousandToString(buffList)
			unitString = commaToUnit(unitCount)
			unitCount -= 1
			outputList.append(numString)
			outputList.append(unitString)
			buffList = []
		else:
			buffList.append(c)

	numString = numberCharArrayLessThanThousandToString(buffList)
	outputList.append(numString)

	return ' '.join(outputList)

def numToString(num):

	def numToString_1000(num):
		if num == 0:
			return ''

		stringList = []
		if num >= 100:
			stringList.append(digitList[num / 100])
			stringList.append('hundred')
			num %= 100

		if num >= 20:
			stringList.append(tenList[num / 10])
			num %= 10
			if num >= 1:
				stringList.append(digitList[num])
		elif 20 > num >= 10:
			stringList.append(teenList[num % 10])
		else:
			stringList.append(digitList[num])

		return ' '.join(stringList)

	digitList = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
	teenList = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'eighteen', 'nineteen']
	tenList = ['', 'ten', 'twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
	unitList = ['', 'thousand', 'million', 'billion', 'trillion']
	unitIntList = [1, 10 ** 3, 10 ** 6, 10 ** 9, 10 ** 12]

	if num == 0:
		return digitList[0]
	elif num < 0:
		return 'negative' + numToString(-1 * num)

	stringList = []
	for i in range(len(unitIntList) - 1, -1, -1):
		if num / unitIntList[i] > 0:
			break


	while num > 0:
		if stringList and num < 1000:
			stringList.append('and')
		stringList.append(numToString_1000(num / unitIntList[i]))
		stringList.append(unitList[i])
		num %= unitIntList[i]
		i -= 1

	return ' '.join(stringList)

def maxContiguousSum(a):
	summation = 0
	maxSum = 0
	start, end = 0, 0
	for i, n in enumerate(a):
		summation += n
		if summation > maxSum:
			maxSum = summation
			end = i
		if summation <= 0:
			summation = 0
			start = i + 1

	return start, end, maxSum

def generateRand(start, end, isInt=True):
	seed = random.random()
	num = start + seed * (end - start)
	return int(num) if isInt else num

def findPairSumToValue(a, v):
	indexDict = {}
	for i, n in enumerate(a):
		if n in indexDict:
			indexDict[n].append(i)
		else:
			indexDict[n] = [i]

	resultList = []
	calculatedDict = {}
	for i, n in enumerate(a):
		remain = v - n
		if remain >= 0 and remain in indexDict and remain not in calculatedDict:
			calculatedDict[remain] = True
			calculatedDict[i] = True
			for index in indexDict[remain]:
				resultList.append((i, index))

	return resultList

def addTwoNum_withoutArithmetic(a, b):
	if b == 0:
		return a
	summation = a ^ b
	carray = (a & b) << 1
	return addTwoNum_withoutArithmetic(summation, carray)

def equallyShuffleArray(a):
	length = len(a)
	for i in range(length - 1):
		swapIndex = generateRand(i + 1, length)
		temp = a[i]
		a[i] = a[swapIndex]
		a[swapIndex] = temp

	return a

def take_set_m_from_n_array(a, m):
	if m > len(a):
		return None
	setDict = {}
	while len(setDict) < m:
		randIndex = generateRand(0, len(a))
		setDict[a[randIndex]] = True
		a.pop(randIndex)

	return setDict

def count_digit_n_in_num(num, d):
	count = 0
	while num > 0:
		digit = num % 10
		if digit == d:
			count += 1
	return count

def count_2_in_range(num):
	def count_2_in_range_at_digit(num, d):
		powerOf10 = math.pow(10, d)
		nextPowerOf10 = powerOf10 * 10
		right = num % powerOf10

		roundDown = num - num % nextPowerOf10
		roundUp = roundDown + nextPowerOf10

		digit = (num / powerOf10) % 10
		if digit < 2:
			return roundDown / 10
		elif digit == 2:
			return roundDown / 10 + right + 1
		else:
			return roundUp / 10

	count = 0
	for i in range(len(str(num))):
		count += count_2_in_range_at_digit(num, i)

	return count

if __name__ == '__main__':
	pass
	# a = 1
	# b = a << 3
	# print(bin(b))
	# print(compareTwoNumberWithoutComparator(3, 3))
	# print(numberToEnglishString_useStack(12345777))
	# print(numToString(123400115))
	# print(maxContiguousSum([1,2,-1,-2, 3, 4, 5]))
	# print(generateRand(10, 20))
	# print(findPairSumToValue(range(10), 3))
	# print(addTwoNum_withoutArithmetic(5, 1))
	# print(equallyShuffleArray(range(10)))
	print(take_set_m_from_n_array([1,2,3,4,5,5,6,6],3))