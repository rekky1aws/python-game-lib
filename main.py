 # FUNCTIONS
def menu ():
	print("\n----- Menu -----\n")
	print(" 1 - Morpion")
	print(" 2 - Pendu")
	# print(" 3 - Juste Prix")
	# print(" 4 - Pierre Feuille Ciseaux")
	# print(" 5 - Batonnets")
	# print(" 6 - Snake")
	# print(" 7 - Démineur")

	print()
	print(" 0 - Quitter\n")
	print("-> ", end="")

 # MAIN
print("Bienvenue dans la librairie de jeux python.")
chx = -1
while chx != 0:
	menu()
	chx = int(input())
	print("----------------\n")
	if chx == 1:
		import tictactoe
	elif chx == 2:
		import hangedman

print("Aurevoir !")