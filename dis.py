from operator import mul
class Tree:
	def __init__(self, entry, branches=()):
		self.entry = entry
		for branch in branches:
			assert isinstance(branch, Tree)
		self.branches = list(branches)
	def is_leaf(self):
		return not self.branches
	def __repr__(self):
		if self.branches:
			 branches_str = ', ' + repr(self.branches)
		else:
			 branches_str = ''
		return 'Tree({0}{1})'.format(self.entry, branches_str)

def combine_tree(t1, t2, combiner):
	if t1.is_leaf() and t2.is_leaf():
		return Tree(combiner(t1.entry, t2.entry))
	else:
		branches = [combine_tree(t1b, t2b, combiner) for t1b, t2b in zip(t1.branches, t2.branches)]
		return Tree(combiner(t1.entry, t2.entry), branches)

def count_entries(t):
	if t.is_leaf():
		return 1, t.entry
	else:
		return 1 + sum([count_entries(b) for b in t.branches])

def sum_tree(t):
	if t.is_leaf():
		return t.entry
	else:
		return t.entry + sum([sum_tree(b) for b in t.branches])

def average(t):
	return sum_tree(t) / count_entries(t)

def alt_tree_map(t, map_fn):
	layer = 0
	def tree_map(t, map_fn):
		nonlocal layer
		if layer % 2 == 0:
			t.entry = map_fn(t.entry)
		layer += 1
		for b in t.branches:
			tree_map(b, map_fn)
	return tree_map(t, map_fn)

def link_to_list(link):
	if rest(link) == empty:
		return [first(link)]
	else:
		return [first(link)] + link_to_list(rest(link))

def map_link(linky, f):
	if rest(linky) == empty:
		return link(f(first(linky)))
	else:
		return link(f(first(linky)), map_link(rest(linky), f))

class Naturals():
	def __init__(self):
		self.current = 0
	def __next__(self):
		result = self.current
		self.current += 1
		return result
	def __iter__(self):
		return self


class IteratorCombiner(object):
	def __init__(self, iterator1, iterator2, combiner):
		self.iterator1 = iterator1
		self.iterator2 = iterator2
		self.combiner = combiner
	def __next__(self):
		return self.combiner(next(self.iterator1), next(self.iterator2))
	def __iter__(self):
		return self

class FibIterator(object):
	def __init__(self):
		self.prev = 0
		self.curr = 1
	def __next__(self):
		self.prev, self.curr = self.curr, self.prev + self.curr
		return self.curr
	def __iter__(self):
		return self

class Unique(object):
	def __init__(self, iterable):
		self.iterator = iter(iterable)
		self.elements = []
	def __next__(self):
		result = next(self.iterator)
		if result in self.elements:
			return self.__next__()
		self.elements.append(result)
		return result

	def __iter__(self):
		return self



def count_stairs(n):
    if n < 2:
        return 0
    if n == 2 or n == 3:
        return 1
    with2 = count_stairs(n-2)
    with3 = count_stairs(n-3)
    return with3 + with2