import math
import sys


class SuffixTreeNode(object):

	children = None
	value = None
	indexList = None

	def __init__(self):
		self.children = {}
		self.value = None
		self.indexList = []

	def insertString(self, string, index):
		self.indexList.append(index)

		if string:
			self.value = string[0]
			if self.value in self.children:
				child = self.children[self.value]
			else:
				child = SuffixTreeNode()
				self.children[self.value] = child
			remainder = string[1:]
			child.insertString(remainder, index)

	def search(self, string):
		if not string:
			return self.indexList
		else:
			first = string[0]
			if first in self.children:
				remainder = string[1:]
				return self.children[first].search(remainder)
		return None

class SuffixTree(object):
	root = None

	def __init__(self, string):
		self.root = SuffixTreeNode()
		for i in range(len(string)):
			suffix = string[i:]
			self.root.insertString(suffix, i)

class Node(object):
	left, right, parent, data = None, None, None, None

	def __init__(self, data):
		self.data = data

	def addLeft(self, data):
		l = Node(data)
		l.parent = self
		self.left = l

	def addRight(self, data):
		r = Node(data)
		r.parent = self
		self.right = r

def getTree():
	r = Node(3)
	r.addLeft(1)
	r.left.addLeft(0)
	r.left.addRight(2)
	r.addRight(5)
	r.right.addLeft(4)
	r.right.addRight(6)

	return r

def findCommonAnccestorWithParent(a, b):
	aParent = {}

	while a is not None:
		aParent[a] = True
		a = a.parent

	while b is not None:
		if b in aParent:
			return b
		else:
			b = b.parent
	return None

def findCommonAnccestorWithoutParent(root, a, b):
	"""
	retrun:
	root if root is CA
	a if a in subtree and b not
	b if b in subtree and a not
	None if a and b both not in subtree

	The algo above assume a and b both in tree.
	If one of node not in tree. When b not in tree, algo return a, it will think b is the child of a.

	To fix this add 2nd return value, specify returned is the anccesstor or not.
	"""
	if root is None or a is None or b is None:
		return None, False

	if root is a and root is b:
		return root, True

	l, lx = findCommonAnccestorWithoutParent(root.left, a, b)
	if lx:
		return l, True

	r, rx = findCommonAnccestorWithoutParent(root.right, a, b)
	if rx:
		return r, True

	if l is not None and r is not None:
		return root, True
	elif root is a or root is b:
		return root, (l is not None) or (r is not None)
	elif l is None and r is None:
		return None, False
	else:
		return r if l is None else r, False

def isBST(root):
	if root is None:
		return True

	if root.left is not None and root.right is not None:
		if root.left.data <= root.right.data:
			return isBST(root.left) and isBST(root.right)
		else:
			return False
	else:
		return isBST(root.left) and isBST(root.right)

def BST_to_double_linkedList(root, last_visit):
	"""
	In order travserse, left to prev, right to next. Ascending order.
	"""
	if root is None:
		return last_visit

	last_visit = BST_to_double_linkedList(root.left, last_visit)
	if last_visit is not None:
		last_visit.right = root
	root.left = last_visit
	last_visit = root
	last_visit = BST_to_double_linkedList(root.right, last_visit)
	return last_visit

def searchWordListInLongString(string, wordList):
	"""
	If use brutal force, time cost will be:O(m*n)
	We use suffix tree here, time cost reduce to:O(n + m), but space increase
	"""
	st = SuffixTree(string)
	resutlList = []
	for word in wordList:
		res = st.root.search(word)
		resutlList.append(res)
	return resutlList

def serializeBinaryTree(root):
	"""
	User pre-order tranverse
	"""
	if not root:
		print('#')
	else:
		print(root.data)
		serializeBinaryTree(root.left)
		serializeBinaryTree(root.right)

def deserializeBinaryTree(parent, isLeft, dataList, index):
	"""
	Has problem in Python, can't pass reference, we have to pass parent
	"""
	if index >= len(dataList):
		return None, index + 1
	if dataList[index] != '#':
		node = Node(dataList[index])
		if isLeft and parent is not None:
			parent.left = node
		elif not isLeft and parent is not None:
			parent.right = node
		_, index = deserializeBinaryTree(node, True, dataList, index + 1)
		_, index = deserializeBinaryTree(node, False, dataList, index)
		return node, index
	else:
		return None, index + 1

def serializeBST(root):
	"""
	User pre-order tranverse, this is the only way that parent come firt than child
	"""
	if root:
		print(root.data)
		serializeBinaryTree(root.left)
		serializeBinaryTree(root.right)


def deserializeBST(min_v, max_v, parent, isLeft, dataList, index):
	"""
	Set min, max value to reconstruct
	"""
	if index >= len(dataList):
		return None, index + 1

	value = dataList[index]
	if max_v > value > min_v:
		node = Node(value)
		if parent is not None:
			if isLeft:
				parent.left = node
			else:
				parent.right = node
		_, index = deserializeBST(min_v, value, node, True, dataList, index + 1)
		_, index = deserializeBST(value, max_v, node, False, dataList, index)
		return node, index
	else:
		return None, index



if __name__ == '__main__':
	t = getTree()
	t1 = getTree()
	# print(findCommonAnccestorWithParent(t.left.right, t.left.left).data)
	# print(findCommonAnccestorWithoutParent(t, t1, t.left.left)[0].data)
	# BST_to_double_linkedList(t, None)
	# while t.left is not None:
	# 	t = t.left
	# while t is not None:
	# 	print(t.data)
	# 	t = t.right

	# print(searchWordListInLongString('I am a jerk, how a about you?', ['jerk',' me']))
	# print(serializeBinaryTree(t))
	# root, n = deserializeBinaryTree(None, True, [1,3, '#', '#', 2, '#', '#'], 0)
	# print(root)

	root, _ = deserializeBST(-sys.maxint, sys.maxint, None, True, [5, 1, 0, 2, 7, 6, 8], 0)
	print(root)