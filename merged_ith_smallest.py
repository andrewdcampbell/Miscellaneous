import math
import sys
import random
import itertools

def get_median(arr):
	med_index = max(math.floor(len(arr) / 2 - 1), 0)
	return arr[med_index]

def deep_len(arrs):
	return sum(len(a) for a in arrs)

def merged_ith_smallest(arrs, i):
    """ Get the ith smallest element of k sorted arrays
    Args:
        arrs: array of k sorted arrays
    Returns:
        The ith smallest element out of all elements in arrs
    """
    assert(i > 0 and i <= deep_len(arrs))
    # remove empty arrays
    arrs = [a for a in arrs if len(a) > 0] 

    # use median of medians as choice of pivot
    medians = [get_median(a) for a in arrs]
    pivot = get_median(medians)

    arrs_l, arrs_p, arrs_r = [], [], []

	# partition each array in arrs based on pivot
    for a in arrs:
    	arrs_l.append([a_i for a_i in a if a_i  < pivot])
    	arrs_p.append([a_i for a_i in a if a_i == pivot])
    	arrs_r.append([a_i for a_i in a if a_i  > pivot])

    if i <= deep_len(arrs_l):
    	return merged_ith_smallest(arrs_l, i)
    elif i <= deep_len(arrs_l) + deep_len(arrs_p):
    	return pivot
    else:
    	return merged_ith_smallest(arrs_r, i - deep_len(arrs_l) - deep_len(arrs_p))

# Tests
def test_merged_ith_smallest(arrs):
	merged = sorted(list(itertools.chain.from_iterable(arrs)))
	for i in range(len(merged)):
		assert(merged[i] == merged_ith_smallest(arrs, i + 1))

# Different array sizes
arrs = [sorted([random.randint(-1000, 1000) for _ in range(random.randint(1, 100))]) for _ in range(15)]

test_merged_ith_smallest(arrs)
