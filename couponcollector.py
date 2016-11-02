import random, math

def numCards(numTrials):
	"""
	Returns the average number of cards you need to buy
	before collecting all 150 cards
	""" 
	results = 0
	for _ in range(numTrials):
		cards = set()
		numBought = 0
		while len(cards) != 150:
			newCard = math.ceil(random.random() * 150)
			cards.add(newCard)
			numBought += 1
		results += numBought
	return results / numTrials

print("Got:", numCards(5000))
print("Expected:", 838.6)

def numCards2(numTrials):
	"""
	Returns the average number of cards you need to buy
	before collecting all 150 cards if you start with 25
	""" 
	results = 0
	for _ in range(numTrials):
		cards = set({i for i in range(1,26)})
		numBought = 0
		while len(cards) != 150:
			newCard = math.ceil(random.random() * 150)
			cards.add(newCard)
			numBought += 1
		results += numBought
	return results / numTrials

print("Got:", numCards2(5000))
print("Expected:", 811.4)