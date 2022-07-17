import random

nb_to_find = random.randint(0, 1000) + 500
player_nb = -1
tries = 0

print("Bienvenue dans le jeu du Plus ou Moins.\n")
print("Un nombre entier entre 500 et 1500 a été généré, à vous de le trouver.")

while player_nb != nb_to_find :
    print("\nSaisissez un nombre : ", end="")
    player_nb = int(input())
    tries += 1
    print("->", end=" ")
    if player_nb == nb_to_find :
        print(f"Bravo le nombre à trouver était bien {nb_to_find}. Vous avez réussi en {tries} essais.")
    elif player_nb < nb_to_find :
        print("C'est plus")
    else :
        print("C'est moins")
print(nb_to_find)