def can_make(x, args):
	if x < 0:
		return False
	elif x == 0:
		return True
	for i in range(len(args)):
		if can_make(x - args[i], args):
			return True
	return False

def p(*args):
	"""
	Prints an array of integers (less than 100) that can not be produced 
	by an integer linear combination of the args. For example, p(3, 5) 
	returns [1, 2, 4, 7] and p(6, 9, 20) returns [1, 2, 3, 4, 5, 7, 8, 
	10, 11, 13, 14, 16, 17, 19, 22, 23, 25, 28, 31, 34, 37, 43]. 
	Surprisingly fast!
	"""
	print([i for i in range(1, 100) if not can_make(i, args)])

