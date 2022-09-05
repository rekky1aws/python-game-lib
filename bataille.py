import cardgame

main_deck = cardgame.make_shuffled_deck()

player_a_deck = cardgame.Deck()
player_b_deck = cardgame.Deck()

turn = 0
while main_deck.nb > 0:
	drawed_card = main_deck.draw_above()
	if turn == 0:
		player_a_deck.add_card_above(drawed_card)
	else:
		player_b_deck.add_card_above(drawed_card)

	turn = (turn + 1) % 2

print("\n Player A :")
player_a_deck.show_deck_symbols()
print("\n Player B :")
player_b_deck.show_deck_symbols()
print("\n Main Deck :")
main_deck.show_deck_symbols()