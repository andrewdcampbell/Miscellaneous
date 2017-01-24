import random, turtle

class SierpinskiTriangle(object):
	"""A chaos game: An initial point is randomly chosen inside an equilateral 
	   triangle. One of the vertices is then randomly chosen. The midpoint of 
	   the line between the point and vertex is drawn. This is repeated to 
	   produce a triangle fractal.
	"""
	def __init__(self):
		self.wn = turtle.Screen()
		self.wn.bgcolor("black") 
		self.wn.title("Sierpinski Fractal Generator")
		self.wn.tracer(0)

		self.t = turtle.Turtle()
		self.t.speed(0)
		self.t.hideturtle()
		self.t.penup()

		self.w = self.wn.window_width() / 1.4
		self.h = self.wn.window_height() / 1.4
		self.midX = self.w / 2
		self.midY = self.h / 2
		self.vertices = [self._getCoord(x, self._getY(x, True)) for x in [10, self.midX, self.w - 10]]

	def getInitialPoint(self):
		x = round(random.uniform(10, self.w - 10))
		y = self._getY(x)
		return self._getCoord(x,y)

	def _getY(self, x, rand=False):
		upperYbound = 0
		if x < self.midX:
			upperYbound = 2 * x
		else:
			upperYbound = 2 * (self.midX - (x - self.midX))
		y = round(random.uniform(0, upperYbound))
		if rand:
			return upperYbound
		return y

	def getRandomVertex(self, lastVertex):
		return random.choice(self.vertices)

	def _getCoord(self, x, y):
		return x - self.midX, y - self.midY - 10

	def getMidpoint(self, p1, p2):
		x1, y1 = p1
		x2, y2 = p2
		return ((x1 + x2) / 2), ((y1 + y2) / 2)

	def getColor(self):
		colors = ["blue", "orange"]
		return random.choice(colors)
		
	def draw(self, iterations):
		prevPoint = self.getInitialPoint()
		count = 0
		updateCount = 0
		lastVertex = None
		while count < iterations:
			v = self.getRandomVertex(lastVertex)
			lastVertex = v
			mp = self.getMidpoint(prevPoint, v)
			x, y = mp
			prevPoint = mp
			self.t.setpos(x, y)
			self.t.dot(0, self.getColor())
			count += 1
			updateCount += 1
			if updateCount == 200:
				self.wn.update()
				updateCount = 0

		
	def main(self, iterations):
		self.draw(iterations)
		self.wn.exitonclick()

class SierpinskiSquare(SierpinskiTriangle):
	"""docstring for SierpinskiSquare"""
	def __init__(self):
		super(SierpinskiSquare, self).__init__()
		ll = (10, self._getY(10, True))
		ul = (10, self._getY(self.midX, True))
		lr = (self.w - 10, self._getY(10, True))
		ur = (self.w - 10, self._getY(self.midX, True))
		self.vertices = [self._getCoord(p[0], p[1]) for p in [ll, ul, lr, ur]]

	def getRandomVertex(self, lastVertex):
		v = random.choice(self.vertices)
		while v == lastVertex:
			v = random.choice(self.vertices)
		return v


# s = SierpinskiTriangle()
s = SierpinskiSquare()
s.main(1000000)