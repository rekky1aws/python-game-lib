class Card :
	""" A class to represent playing cards """

	faces = {
		'K': 'King',
		'Q': 'Queen',
		'J': 'Jack',
		'A': 'Ace'
	}

	def __init__ (self, value, suit) :
		self.value = value
		self.suit = suit

	def display (self) :
		if self.value in ['K', 'Q', 'J', 'A']:
			return f"{self.faces[self.value]} of {self.suit.capitalize()}"
		else :
			return f"{self.value} of {self.suit.capitalize()}"

values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
suits = ["hearts", "spades", "diamonds", "clubs"]
cards = []

for s in suits :
	for v in values :
		cards.append(Card(v, s))

for c in cards :
	print(c.display())

print(len(cards))