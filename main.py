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
	# print(" 4 - Pierre Feuille Ciseaux")
	# print(" 5 - Batonnets")
	# print(" 6 - Snake")
	# print(" 7 - Démineur")

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
		print("> Appuyez sur entrée pour retourner au menu :", end=" ")
		input()
	elif chx == 2:
		import moreless
		print("> Appuyez sur entrée pour retourner au menu :", end=" ")
		input()
	elif chx == 3:
		import tictactoe
		print("> Appuyez sur entrée pour retourner au menu :", end=" ")
		input()

print("Aurevoir !")