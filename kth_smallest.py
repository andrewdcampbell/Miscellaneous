# TODO: The function can be made more efficient by converting it into
# an iterative function. Leaving as recursive for now because I think
# it is easier to understand.

import math
import sys
import random

def kth_smallest(a1, a2, k):
    """ Get the kth smallest element in the union of a1 and a2 in O(log k) time
    Args:
        a1: Sorted array of length n
        a2: Sorted array of length m
    Returns:
        The kth smallest element in the union (multiset) of a1 and a2
    """	
    assert(k >= 1 and k <= len(a1) + len(a2))

    a1 = a1[:k]
    a2 = a2[:k]
    if len(a1) < k:
    	a1.extend([sys.maxsize] * ( k - len(a1)))
    if len(a2) < k:
    	a2.extend([sys.maxsize] * ( k - len(a2)))

    if k == 1:
    	return min(a1[0], a2[0])

    a1_mid = math.floor(k / 2)
    a2_mid = math.ceil(k / 2)

    if a1[a1_mid - 1] == a2[a2_mid - 1]:
    	return a1[a1_mid - 1]
    elif a1[a1_mid - 1] > a2[a2_mid - 1]:
    	return kth_smallest(a1[:a1_mid], a2[a2_mid:], a1_mid)
    else:
    	return kth_smallest(a1[a1_mid:], a2[:a2_mid], a2_mid)

# Tests
def test_kth_smallest(a1, a2):
	union = sorted(a1 + a2)
	for i in range(len(union)):
		assert(union[i] == kth_smallest(a1, a2, i + 1))

# Same array size
a1 = sorted([random.randint(-1000, 1000) for _ in range(1000)])
a2 = sorted([random.randint(-1000, 1000) for _ in range(1000)])

test_kth_smallest(a1, a2)

# Different array sizes
a1 = sorted([random.randint(-1000, 1000) for _ in range(random.randint(1, 100))])
a2 = sorted([random.randint(-1000, 1000) for _ in range(random.randint(1, 100))])

test_kth_smallest(a1, a2)
	