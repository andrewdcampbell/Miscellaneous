import random, turtle

class Tree(object):
	"""Recursive tree fractal art"""
	def __init__(self):
		self.wn = turtle.Screen()
		self.wn.bgcolor("black") 
		self.wn.title("Tree Fractal")
		self.wn.tracer(0)

		self.t = turtle.Turtle()
		self.t.speed(0)
		self.t.hideturtle()
		self.t.penup()

		self.w = self.wn.window_width() / 1.4
		self.h = self.wn.window_height() / 1.4
		self.midX = self.w / 2
		self.midY = self.h / 2

		self.colors = ["white", "red", "blue", "green", "yellow"]
		random.shuffle(self.colors)
		self.colors = self.colors[0:3]

	def draw(self, depth, branches, maxBranchLen, startPoint):
		if depth == 1:
			self.t.dot(2, "blue") 
			return
		xCoords = []
		for i in range(branches):
			self.t.setpos(startPoint)
			self.t.color(self.colors[depth % len(self.colors)])
			self.t.pendown()
			newY = random.uniform(0.3, 1) * maxBranchLen
			if i == branches - 1: # Keep the branches somewhat balanced
				newX = -max(xCoords, key=lambda x: abs(x))
			else:
				newX = (random.random() * maxBranchLen * 2) - maxBranchLen
				xCoords.append(newX)
			newPoint = (startPoint[0] + newX, startPoint[1] + newY)
			self.t.setpos(newPoint)
			self.t.penup()
			self.draw(depth - 1, min(branches, 5), maxBranchLen / 2.5, newPoint)

		self.wn.update()


	def main(self, depth = 6, branches = 7):
		startPoint = (0, -self.midY)
		self.t.setpos(startPoint)
		self.t.color(self.colors[depth % len(self.colors)])
		self.t.pendown()
		newPoint = (0, startPoint[1] + self.midY / 2)
		self.t.setpos(newPoint)
		self.t.penup()
		self.draw(depth, branches, self.midY, newPoint)
		self.wn.exitonclick()

if __name__ == '__main__':
	s = Tree()
	s.main()
