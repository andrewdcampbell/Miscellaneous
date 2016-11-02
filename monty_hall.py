import math, random

def montyhall(numTrials, switch):
	"""
	Returns the probability of choosing correct door if using 
	switiching strategy or not (pass it in as argument) after n 
	trials
	"""
	trials = []
	for _ in range(numTrials):
		# door number of car (0, 1, 2)
		car = math.floor(random.random() * 3)
		setup = [False, False, False]
		setup[car] = True

		# guess for door number of car
		guess = math.floor(random.random() * 3)

		if switch:
			unpickedGoat = [i for i in range(3) if i != guess and not setup[i]][0]
			guess = [i for i in range(3) if i != unpickedGoat and i != guess][0]

		trials.append(car == guess)
	return len([s for s in trials if s]) / len(trials)

print("No switch:", montyhall(100000, False))
print("With switch:", montyhall(100000, True))