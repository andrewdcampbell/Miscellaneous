def count_decodings(s, d):
	"""
	Returns the number of ways a bit string s can be interpreted
	given codes in the dictionary d. For example, consider the code 
	that maps 'A' to '1', 'B' to '01' and 'C' to '101'. A bit string 
	'101' can be interpreted in two ways: as 'C' or as 'AB'.

	Run-time: O(nml) where n is the length of the bit string s, m is 
	the number of symbols, and l is an upper bound on the length of the 
	bit strings representing symbols.
	"""
	n = len(s)
	L = [0 for _ in range(n + 1)]
	for i in range(n-1, -1, -1):
		for c in d.values():
			if i + len(c) == n and s[i:i+len(c)] == c:
				L[i] += 1
			elif s[i:i+len(c)] == c:
				L[i] += L[i + len(c)]
	return L[0]

d = {'A': '1', 'B': '01', 'C': '101'}
s = '101'
assert(count_decodings(s, d) == 2) # expect 2

d = {'A': '0', 'B': '10', 'C': '001', 'D': '010', 'E': '001'}
s = '001010'
assert(count_decodings(s, d) == 6) # expect 6