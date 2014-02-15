
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
	r.addLeft(2)
	r.left.addLeft(1)
	r.left.addRight(0)
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



if __name__ == '__main__':
	t = getTree()
	t1 = getTree()
	# print(findCommonAnccestorWithParent(t.left.right, t.left.left).data)
	# print(findCommonAnccestorWithoutParent(t, t1, t.left.left)[0].data)