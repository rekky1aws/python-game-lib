import random

class Card :
	""" A class to represent playing cards """

	faces = {
		'K': 'King',
		'Q': 'Queen',
		'J': 'Jack',
		'A': 'Ace'
	}

	def __init__ (self, value: str, suit: str) :
		self.value = value
		self.suit = suit

	def display (self) :
		if self.value in ['K', 'Q', 'J', 'A']:
			return f"{self.faces[self.value]} of {self.suit.capitalize()}"
		else :
			return f"{self.value} of {self.suit.capitalize()}"

class Deck :
	""" A class to represent a deck of playing cards 
	cards[0] is first card on the front side => cards[len(cards) - 1] is the first card on the back side
	"""
	def __init__(self, cards: Card = []) :
		self.cards = cards
		self.nb = len(cards)

	def show_deck (self) :
		for c in self.cards :
			print(c.display())

	def add_card_above (self, card: Card) :
		print(self)
		print(card)
		self.cards.append(card)
		self.nb = len(self.cards)
		return self

	def add_card_under (self, card: Card) :
		self.cards.appendleft(card)
		self.nb = len(self.cards)
		return self

	def draw_above (self) :
		result = self.cards.pop()
		self.nb = len(self.cards)
		return result

	def draw_below (self) :
		result = self.cards.pop(0)
		self.nb = len(self.cards)
		return result

	def shuffle (self) :
		cards_result = []
		cards_copy = self.cards
		for i in range(len(self.cards)):
			index = random.randint(0, len(cards_copy) - 1)
			cards_result.append(cards_copy.pop(index))
		self.cards = cards_result
		return self


def generate_deck ():
	deck = Deck()
	values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
	suits = ["hearts", "spades", "diamonds", "clubs"]

	for s in suits :
		for v in values :
			deck.add_card_above(Card(v, s))

	return deck