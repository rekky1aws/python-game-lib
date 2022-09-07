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
print("Les cartes ont été distribuées.\nAppuyez sur une touche pour commencer le jeu : ", end='')
input()

# Commencement de la partie
while (player_a_deck.nb > 0 or player_a_memo.nb > 0) and (player_b_deck.nb > 0 or player_b_memo.nb > 0):
	print("\n\n---\nJouer :", end='')
	input()

	# Affichage des cartes restantes pour chaque joueur
	print(f"\t\tJ1\t\tJ2\nEn main :   {player_a_deck.nb}\t\t  {player_b_deck.nb}\nEn mémo :   {player_a_memo.nb}\t\t  {player_b_memo.nb}\n")

	# Si un deck est vide, on vérifie si le mémo correspondant a des cartes et on le transfère.
	if player_a_deck.nb == 0:
		player_a_memo.shuffle()
		player_a_deck = player_a_memo
		player_a_memo = cardgame.make_empty_deck()
		print("Le joueur A a repris les cartes qu'il a gagné.")

	if player_b_deck.nb == 0:
		player_b_memo.shuffle()
		player_b_deck = player_b_memo
		player_b_memo = cardgame.make_empty_deck()
		print("Le joueur B a repris les cartes qu'il a gagné.")

	# Pioche des cartes 
	card_a = player_a_deck.draw_above()
	card_b = player_b_deck.draw_above()
	print(f"{card_a.display_symbol()}\t|\t{card_b.display_symbol()}")

	# Vérification de la victoire ou non d'un joueur
	# On doit faire "-2 % 13" pour placer l'As en position la plus forte (ca valeur de base dans cardgame.py est de 1)
	if (card_a.value - 2) % 13 > (card_b.value - 2) % 13 :
		print("\t>")
		# Le joueur A récupère les deux cartes dans son mémo
		player_a_memo.add_card_above(card_a)
		player_a_memo.add_card_above(card_b)
	elif (card_a.value - 2) % 13 < (card_b.value - 2) % 13 :
		print("\t<")
		# Le joueur B récupère les deux cartes dans son mémo
		player_b_memo.add_card_above(card_a)
		player_b_memo.add_card_above(card_b)
	elif (card_a.value - 2) % 13 == (card_b.value - 2) % 13 :
		print("\t=")
		# !Temporaire : Les joueurs récupère chacun leur cartes respectives
		player_a_memo.add_card_above(card_a)
		player_b_memo.add_card_above(card_b)
		# Ici, faire en sorte que les vraies règles s'appliquent à l'avenir
