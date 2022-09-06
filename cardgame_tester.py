import cardgame

# Initialisations
player_a_deck = cardgame.make_empty_deck()
player_a_memo = cardgame.make_empty_deck()

player_b_deck = cardgame.make_empty_deck()
player_b_memo = cardgame.make_empty_deck()

main_deck = cardgame.make_shuffled_deck()

# Distribution des cartes aux joueurs
turn = 0
while main_deck.nb > 0:
	drawed_card = main_deck.draw_above()

	if turn == 0:
		player_a_deck.add_card_above(drawed_card)

	else:
		player_b_deck.add_card_above(drawed_card)

	turn = (turn + 1) % 2

# Affichage de la carte piochée
print("\tDrawed Card :")
print(drawed_card.display_symbol())

# Affichage du deck et du memo du joueur A
print(f"\tA ({player_a_deck.nb}) :")
player_a_deck.show_deck_symbols()
print(f"\tA Memo ({player_a_memo.nb}) :")
player_a_memo.show_deck_symbols()

# Affichage du deck et du memo du joueur B
print(f"\tB ({player_b_deck.nb}) :")
player_b_deck.show_deck_symbols()
print(f"\tB Memo ({player_b_memo.nb}) :")
player_b_memo.show_deck_symbols()
# Affichage du deck principal
print(f"\tMain ({main_deck.nb}) :")
main_deck.show_deck_symbols()