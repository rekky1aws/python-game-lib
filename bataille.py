import cardgame

main_deck = cardgame.make_shuffled_deck()
print("\tMain Deck")
main_deck.show_deck_symbols()
print(main_deck.nb)

player_a_deck = cardgame.Deck()
player_b_deck = cardgame.Deck()
turn = 0
while main_deck.nb > 0 :
	rslt = main_deck.draw_above()
	print(rslt.display_symbol())
	# if turn == 0 :
	# 	player_a_deck.add_card_above(rslt)
	# else :
	# 	player_b_deck.add_card_above(rslt)
	# turn = turn + 1 % 2
print("\n\n\tJoueur A")
player_a_deck.show_deck_symbols()
print(player_a_deck.nb)

print("\n\n\tJoueur B")
player_b_deck.show_deck_symbols()

print(player_b_deck.nb)