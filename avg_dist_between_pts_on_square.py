import math
import random

trials = 1000000

class Point(object):
	def __init__(self, xCor, yCor):
		self.xCor = xCor
		self.yCor = yCor

	def distTo(self, other):
		dx = self.xCor - other.xCor
		dy = self.yCor - other.yCor
		return math.sqrt(dx*dx + dy*dy)

total_distance = 0

for _ in range(trials):
	pt1 = Point(random.random(), random.random())
	pt2 = Point(random.random(), random.random())
	total_distance += pt1.distTo(pt2)

print("Average distance:", total_distance / trials)
