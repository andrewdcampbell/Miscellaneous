import random, turtle

class Sierpinski(object):
	"""A chaos game. A point is randomly chosen inside an equilateral 
	   triangle. A vertex is randomly chosen. The midpoint of the line 
	   between the point and vertex is marked. This is repeated to produce a 
	   triangle fractal.
	"""
	def __init__(self):
		self.wn = turtle.Screen()
		self.wn.bgcolor("black") 
		self.wn.title("Sierpinski Fractal Generator")

		self.t = turtle.Turtle()
		self.t.speed("fastest")
		self.t.hideturtle()
		self.t.penup()

		self.w = self.wn.window_width()
		self.h = self.wn.window_height()
		self.midX = self.w / 2
		self.midY = self.h / 2

	def getPoint(self):
		x = round(random.uniform(10, self.w - 10))
		y = self.getY(x)
		return self.getCoord(x,y)

	def getY(self, x, rand=False):
		upperYbound = 0
		if x < self.midX:
			upperYbound = 2 * x
		else:
			upperYbound = 2 * (self.midX - (x - self.midX))
		y = round(random.uniform(0, upperYbound))
		if rand:
			return upperYbound
		return y

	def getVertex(self):
		vertices = [self.getCoord(x, self.getY(x, True)) for x in [10, self.midX, self.w - 10]]
		return random.choice(vertices)

	def getCoord(self, x, y):
		return x - self.midX, y - self.midY - 10

	def getMidpoint(self, p1, p2):
		x1, y1 = p1
		x2, y2 = p2
		return ((x1 + x2) / 2), ((y1 + y2) / 2)

	def getColor(self):
		colors = ["blue", "red", "white", "yellow"]
		return random.choice(colors)
		
	def draw(self):
		for i in range(100000):
			p = self.getPoint()
			v = self.getVertex()
			mp = self.getMidpoint(p, v)
			x, y = mp
			self.t.setpos(x, y)
			self.t.dot(2, "white")

		
	def main(self):
		self.draw()
		self.wn.exitonclick()


s = Sierpinski()
s.main()