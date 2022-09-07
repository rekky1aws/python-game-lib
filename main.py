 # IMPORTS
import os

 # FUNCTIONS
def menu ():
	print("\n--------- Menu ---------\n")
	print(" Jeux Solo :")
	print("  1 - Pendu")
	print("  2 - Plus ou Moins")

	print("\n Jeux Multi :")
	print("  3 - Morpion")
	print("  4 - Bataille (Cartes)")
	# print(" 5 - Pierre Feuille Ciseaux")
	# print(" 6 - Batonnets")
	# print(" 7 - Snake")
	# print(" 8 - Démineur")

	print()
	print(" 0 - Quitter\n")
	print("-> ", end="")

 # MAIN

chx = -1
while chx != 0:
	os.system('cls' if os.name == 'nt' else 'clear')
	print("Bienvenue dans la librairie de jeux python.")
	menu()
	chx = int(input())
	print("\n------------------------\n")
	if chx == 1:
		import hangedman

	elif chx == 2:
		import moreless

	elif chx == 3:
		import tictactoe
		
	elif chx == 4:
		import bataille

	print("> Appuyez sur entrée pour retourner au menu :", end=" ")
	input()

print("Aurevoir !")