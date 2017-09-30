class RelativeAgeSolver(object):
    """ 
    The setup is as follows: you're at a party with n people and 
    everyone is talking about their (relative) ages. For example, 
    you might overhear that person x is older than person y by d 
    years (note that d can be negative if y is older than x). 
    Sometimes you are asked how much older person x is than person 
    y. If you can determine the answer from the conversations you 
    have overheard so far, then give the answer. Otherwise, say
    you don't have enough information.

    This solver class can be used to solve this problem. For 
    example:

    >>> s = RelativeAgeSolver(5) # party with 5 people
    # you overhear person 1 is older than person 3 by 3 years
    >>> s.overhear(1, 3, 3) 
    # you overhear person 4 is older than person 2 by 5 years
    >>> s.overhear(4, 2, 5) 
    # you overhear person 3 is younger than person 2 by 4 years
    >>> s.overhear(2, 3, -4)

    >>> s.infer(4, 3) # person 4 is older than person 3 by 1 year
    1 
    >>> s.infer(1, 4) # person 1 is older than person 4 by 5 years
    5
    >>> s.infer(2, 1) # person 2 is younger than person 1 by 7 years
    -7
    >>> s.inder(0, 1) # we don't know anything about person 0
    'Not enough information'

    The overheard conversations are assumed to give consistent
    information.

    Idea behind imlementation: We model the problem as a graph 
    connectivity problem where the nodes are the n people and the 
    edges are the age relationships between people. To achieve an 
    efficient running time, we modify the disjoint set data structure 
    to also maintain the edge weights (relative ages) from nodes to 
    parents. Then we can infer the age difference between two nodes 
    indirectly by comparing how they differ from their parent node 
    (which we get by summing edge weights on the path to the parent).

    Time complexity:
        overhear: O(log n)
        infer: O(log n)
    Space complexity:
        O(n)

    TODO: Implement path compression to make overhear and infer
    O(log* n).
    """

    def __init__(self, n):
        self._parents        = list(range(n))
        self._ranks          = [0] * n
        self._parent_weights = [0] * n

    def overhear(self, x, y, d=0):
        """ This means x is older than y by d years """
        p_x, p_x_weights = self._get_parents(x)
        p_y, p_y_weights = self._get_parents(y)
        weight_diff = d - p_x_weights + p_y_weights
        if p_x == p_y:
            return
        if self._ranks[p_x] > self._ranks[p_y]:
            self._parents[p_y] = p_x
            self._parent_weights[p_y] = -weight_diff
        else:
            self._parents[p_x] = p_y
            self._parent_weights[p_x] = weight_diff
        if self._ranks[p_x] == self._ranks[p_y]:
            self._ranks[p_y] += 1

    def _get_parents(self, x):
        total_weights = 0
        while self._parents[x] != x:
            total_weights += self._parent_weights[x]
            x = self._parents[x]
        return x, total_weights

    def infer(self, x, y):
        """ Return how much older x is than y """
        p_x, p_x_weights = self._get_parents(x)
        p_y, p_y_weights = self._get_parents(y)
        if p_x != p_y:
            return "Not enough information"
        return p_x_weights - p_y_weights

# TESTS

# Test correctness of internal disjoint set data structure
s = RelativeAgeSolver(15)
s.overhear(0, 1)
s.overhear(2, 3)
s.overhear(4, 5)
s.overhear(6, 7)
s.overhear(8, 9)
s.overhear(10, 11)
s.overhear(12, 13)
s.overhear(0, 2)
s.overhear(10, 12)
s.overhear(7, 8)
s.overhear(4, 6)
s.overhear(5, 11)
expected_parents = [1, 3, 3, 3, 5, 9, 7, 9, 9, 13, 11, 13, 13, 13, 14]
assert(s._parents == expected_parents)

# Test correctness of relative ages
INVALID = "Not enough information"
s = RelativeAgeSolver(9)
s.overhear(1, 2, 3)
s.overhear(6, 7, 4)
s.overhear(3, 8, -1)
s.overhear(5, 7, 9)
assert( s.infer(1, 2) == 3 )
assert( s.infer(2, 1) == -3 )
assert( s.infer(4, 3) == INVALID )
assert( s.infer(5, 6) == 5 )
s.overhear(4, 2, -7)
s.overhear(8, 5, 10)
assert( s.infer(3, 5) == 9 )
assert( s.infer(5, 3) == -9 )
assert( s.infer(7, 3) == -18 )
assert( s.infer(8, 6) == 15 )
assert( s.infer(1, 4) == 10 )
assert( s.infer(4, 3) == INVALID )
s.overhear(4, 5, -4)
assert( s.infer(1, 8) == -4 )
assert( s.infer(3, 6) == 14 )
assert( s.infer(0, 7) == INVALID )
assert( s.infer(2, 7) == 12 )

