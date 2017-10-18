""" 
The following are three equivalent algorithms to return the smallest 
(by lexicographical ordering) subsequence in string S of length exactly k.

For example: in the word “rocket”, the smallest subsequence of length 3 is “cet”.
"""

def iterativeSSK(s, k):
    """ 
    Run-time: O(n) (assuming list slicing and concatenation is constant time).
    """
    n = len(s) - k
    pos = 0
    while n > 0 and pos < len(s) - 1:
        if(s[pos] > s[pos+1]):
            s = s[:pos]+s[pos+1:]
            n = n - 1 
            if pos > 0: 
                pos = pos - 1
        else:
            pos = pos + 1
    if n > 0:
        s = s[:len(s)-n]
    return s

def recursiveSSK(s, k, i=0):
    """ 
    A recursive variant of the iterative version.
    Run-time: O(n) (assuming list slicing and concatenation is constant time).
    """ 
    n = len(s)
    if i == n - 1 or n == k:
        return s[:k]
    if s[i] > s[i + 1]:
        return recursiveSSK(s[:i]+s[i+1:], k, max(i - 1, 0))
    else:
        return recursiveSSK(s, k, i + 1)

def greedySSK(s, k, i=0):
    """
    A greedy approach to the problem. Perhaps most intuitive approach.
    Run-time: O(nk)
    """
    n = len(s)
    if k == 0:
        return ''
    minCharIndex = i
    for j in range(i, n - k + 1):
        if s[j] < s[minCharIndex]:
            minCharIndex = j
    return s[minCharIndex] + greedySSK(s, k - 1, minCharIndex + 1)

S = 'shjagdfhjsdkuyh'

for k in range(1, len(S) + 1):
    r1 = iterativeSSK(S, k)
    r2 = recursiveSSK(S, k)
    r3 =    greedySSK(S, k)
    assert(r1 == r2)
    assert(r2 == r3)
