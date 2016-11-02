intarray = [18, 36, 13, 6, 7, 64, 81, 15, 9, 67]
strarray = ["banana", "orange", "apple", "strawberry", "grapes", "mango", "peach", "watermelon"]

def list_to_link(lst):
    if len(lst) == 1:
        return Link(lst[0])
    return Link(lst[0], list_to_link(lst[1:]))

def selectsort(array, index=0):
    """ Sorts an array (a Python list) in place """
    if index == len(array)-1:
        return
    minindex, minvalue = index, array[index]
    for i in range(index+1, len(array)):
        if array[i] < minvalue:
            minindex, minvalue = i, array[i]
    array[index], array[minindex] = minvalue, array[index]
    return selectsort(array, index+1)

def selectsort_link(link):
    """ Sorts a linked list in place """
    if len(link) < 2:
        return
    minvalue, minpointer = link.first, link
    pointer = link
    while pointer.rest is not Link.empty:
        pointer = pointer.rest 
        if pointer.first < minvalue:
            minpointer, minvalue = pointer, pointer.first
    link.first, minpointer.first = minvalue, link.first
    selectsort_link(link.rest)

"""Linked List Implementation"""

class Link:
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __getitem__(self, i):
        if i == 0:
            return self.first
        else:
            return self.rest[i-1]

    def __len__(self):
        return 1 + len(self.rest)

    def __repr__(self):
        if self.rest:
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
        return 'Link({0}{1})'.format(self.first, rest_str)

    def selectsort_link(self):
        """ Sorts a linked list in place """
        if len(self) < 2:
            return
        minvalue, minpointer = self.first, self
        pointer = self
        while pointer.rest is not Link.empty:
            pointer = pointer.rest 
            if pointer.first < minvalue:
                minpointer, minvalue = pointer, pointer.first
        self.first, minpointer.first = minvalue, self.first
        Link.selectsort_link(self.rest)
    
    def reverse(self):
        """ Reverse a linked list, non-destructively """
        reverse = Link.empty
        while self is not Link.empty:
            reverse = Link(self.first, reverse)
            self = self.rest
        return reverse

    def concat(self, other):
        """ Concatenate a linked list with another, in place """
        if self.rest is Link.empty:
            self.rest = other
            return
        Link.concat(self.rest, other)

    def insert(self, item, index):
        """ Inserts an item at the index, in place 
        Does not work for index 0 """
        if index == 1 or index == 0 or self.rest is Link.empty:
            self.rest = Link(item, self.rest)
            return
        Link.insert(self.rest, item, index-1)



