def print_grid (grid):
	correspondances = [" ", "O", "X"]
	for i in grid:
		print("+---+---+---+")
		for j in i:
			print(f"| {correspondances[j]} ", end ="")
		print(f"|")
	print("+---+---+---+")

def print_help ():
	print("Pour jouer, saisisez le nombre de la case correspondante :")
	print("+---+---+---+")
	print("| 7 | 8 | 9 |")
	print("+---+---+---+")
	print("| 4 | 5 | 6 |")
	print("+---+---+---+")
	print("| 1 | 2 | 3 |")
	print("+---+---+---+")

def check_victory (grid):
	if grid[1][1] != 0:
		if grid[0][0] == grid[1][1] & grid[2][2] == grid[1][1]:
			return True
		if grid[1][0] == grid[1][1] & grid[1][2] == grid[1][1]:
			return True
		if grid[0][2] == grid[1][1] & grid[2][0] == grid[1][1]:
			return True
		if grid[0][1] == grid[1][1] & grid[2][1] == grid[1][1]:
			return True

	if grid[0][0] != 0:
		if grid[0][1] == grid [0][0] & grid[0][2] == grid[0][0]:
			return True
		if grid[1][0] == grid[0][0] & grid[2][0] == grid[0][0]:
			return True

	if grid[2][2] != 0:
		if grid[0][2] == grid[2][2] & grid[1][2] == grid[2][2]:
			return True
		if grid [2][0] == grid[2][2] & grid[2][1] == grid[2][2]:
			return True
	return False

def check_full (grid):
	for i in grid:
		for j in i:
			if j == 0:
				return False
	return True

print('Morpion')
 # Variables
game_grid = [
	[0, 0, 0],
	[0, 0, 0],
	[0, 0, 0]
]
joueur = 1

print_help()
print()

while not check_victory(game_grid) and not check_full(game_grid):
	print_grid(game_grid)
	print(f" -> Joueur {joueur} : ", end="")
	in_value = input()
	if in_value == '1':
		game_grid[2][0] = joueur
	elif in_value == '2':
		game_grid[2][1] = joueur
	elif in_value == '3':
		game_grid[2][2] = joueur
	elif in_value == '4':
		game_grid[1][0] = joueur
	elif in_value == '5':
		game_grid[1][1] = joueur
	elif in_value == '6':
		game_grid[1][2] = joueur
	elif in_value == '7':
		game_grid[0][0] = joueur
	elif in_value == '8':
		game_grid[0][1] = joueur
	elif in_value == '9':
		game_grid[0][2] = joueur
	else:
		print('Valeur incorrecte, veuillez saisir une valeur qui correspond a ceci :')
		print_help()
		continue

	joueur = (joueur + 2) % 2 + 1


joueur = (joueur + 2) % 2 + 1
print(f"Le joueur {joueur} a gagné")


