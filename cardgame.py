import random

class Card :
	""" A class to represent playing cards """

	faces_full = {
		13: 'King',
		12: 'Queen',
		11: 'Jack',
		1: 'Ace'
	}

	faces = {
		13: 'K',
		12: 'Q',
		11: 'J',
		1: 'A'
	}

	symbols = {
		"clubs": "♣",
		"hearts": "♥",
		"diamonds":"♦",
		"spades": "♠"
	}

	def __init__ (self, value: str, suit: str) :
		self.value = value
		self.suit = suit.lower()

	def display (self) :
		if self.value in [1, 11, 12, 13]:
			return f"{self.faces_full[self.value]} of {self.suit.capitalize()}"
		else :
			return f"{self.value} of {self.suit.capitalize()}"

	def display_symbol (self):
		if self.value in [1, 11, 12, 13]:
			return f"{self.symbols[self.suit]} {self.faces[self.value]}"
		else :
			return f"{self.symbols[self.suit]} {self.value}"


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

	def show_deck_symbols (self):
		for c in self.cards :
			print(c.display_symbol())

	def add_card_above (self, card: Card) :
		self.cards.append(card)
		self.nb = len(self.cards)
		return self

	def add_card_under (self, card: Card) :
		self.cards.appendleft(card)
		self.nb = len(self.cards)
		return self

	def draw_above (self) :
		if self.nb > 0 :
			result = self.cards.pop()
			self.nb = len(self.cards)
			return result
		else :
			return None

	def draw_below (self) :
		if self.nb > 0 :
			result = self.cards.pop(0)
			self.nb = len(self.cards)
			return result
		else :
			return None

	def shuffle (self) :
		cards_result = []
		cards_copy = self.cards
		for i in range(len(self.cards)):
			index = random.randint(0, len(cards_copy) - 1)
			cards_result.append(cards_copy.pop(index))
		self.cards = cards_result
		return self

def make_sorted_deck () :
	deck = Deck()
	values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
	suits = ["hearts", "spades", "diamonds", "clubs"]

	for s in suits :
		for v in values :
			deck.add_card_above(Card(v, s))

	return deck

def make_shuffled_deck () :
	deck = make_sorted_deck()
	deck.shuffle()
	return deck