def min(a,b):
	"""
	`int, int --> int`

	Returns minimum between a and b
	"""
	return a if a < b else b

def mean(A):
	"""
	`List[int] --> float`

	Returns arithmetic mean of A
	"""
	if len(A):
		return 1.0*sum(A)/len(A)

def median(A):
	"""
	`List[int] -> float`

	Returns median value of A
	"""
	
	if not len(A):
		return

	A.sort()
	l = len(A)

	if l % 2:
		return A[l / 2]
	else:
		return (A[l/2 - 1] + A[l/2])/2. 

def std_deviation(A):
	"""
	`List[int] --> float`

	Returns standard deviation of A
	"""
	return -1.0

def is_arith_progression(A):
	"""
	`List[int] --> bool`

	Returns whether A follows or not an arithmetic progression
	"""
	return False

def is_geo_progression(A):
	"""
	`List[int] --> bool`

	Returns whether A follows or not an geometric progression
	"""
	return False

def next_arith_progression(n,A):
	"""
	`int, List[int] --> tuple(bool, List[int])`

	Returns whether A follows or not an arithmetic progression and if so, the next n elements
	"""
	return False, [-1.0]

def next_geo_progression(n,A):
	"""
	`int, List[int] --> tuple(bool, List[int])`

	Returns whether A follows or not an arithmetic progression and if so, the next n elements
	"""
	return False, [-1.0]
