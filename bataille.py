import cardgame

main_deck = cardgame.make_shuffled_deck()

player_a_deck = cardgame.Deck()
player_a_memo = cardgame.Deck()

player_b_deck = cardgame.Deck()
player_b_memo = cardgame.Deck()

# Distribution des cartes aux deux joueurs.
turn = 0
while main_deck.nb > 0:
	drawed_card = main_deck.draw_above()
	if turn == 0:
		player_a_deck.add_card_above(drawed_card)
	else:
		player_b_deck.add_card_above(drawed_card)

	turn = (turn + 1) % 2

# Affichage des mains de joueurs après distribution
# print("\n Player A :")
# player_a_deck.show_deck_symbols()
# print("\n Player B :")
# player_b_deck.show_deck_symbols()
# print("\n Main Deck :")
# main_deck.show_deck_symbols()

print("Les cartes ont été distribuées.\nAppuyez sur une touche pour commencer le jeu : ", end='')
input()

# Commencement de la partie
while (player_a_deck.nb > 0 or player_a_memo.nb > 0) and (player_b_deck.nb > 0 or player_b_memo.nb > 0):
	print("\n\n---\nJouer :", end='')
	input()
	card_a = player_a_deck.draw_above()
	card_b = player_b_deck.draw_above()
	print(f"{card_a.display_symbol()}\t|\t{card_b.display_symbol()}")

	# Vérification de la victoire ou non d'un joueur
	# On doit faire "-2 % 13" pour placer l'As en position la plus forte (ca valeur de base dans cardgame.py est de 1)
	if (card_a.value - 2) % 13 > (card_b.value - 2) % 13 :
		print("\t>")
	elif (card_a.value - 2) % 13 < (card_b.value - 2) % 13 :
		print("\t<")
	elif (card_a.value - 2) % 13 == (card_b.value - 2) % 13 :
		print("\t=")
