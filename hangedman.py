 # Imports
from cmath import pi
import csv
import random
import unicodedata as ud
import os

  # Constantes
MAX_FAILS = 10

 # Variables Globales
words = []

 # Fonctions
def get_random_word (wordArray):
    return wordArray[random.randint(0, len(wordArray))]

def game (word):
    all_found = False
    fails = 0
    letters = []

    while (not(all_found) and fails < MAX_FAILS + 1):
         # Nettoyage de l'écran
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Bienvenue dans le Jeu du pendu.\n")
        print("Pour jouer c'est simple : un mot a été généré aléatoirement, votre but est de trouver les lettres qui le composent.")
        print("Note : Les mots peuvent être des verbes conjugués.")
        print("\n ##########\n")

        # Affichage de la "grille" de lettres
        print("Mot :")
        for l in word:
            print(" ", end="")
            if l in letters:
                print(l.upper(), end="")
            else:
                print("_", end="")
        print("\n")

         # Affichage des tentatives possible
        print("Tentatives :")
        for i in range (MAX_FAILS + 1):
            if i < fails:
                print(" X", end="")
            else:
                print(" O", end="")
        print("\n")

         # Affichage des lettres déjà entrées.
        print("Lettres déjà tentées :")
        for l in letters:
            print(l.upper(), end=" ")
        print("\n")

         # Joueur
        print("Entrez une lettre : ", end="")
        playerInput = input().lower()
        if playerInput not in letters:
            letters.append(playerInput)
            letters.sort()
        
        if playerInput not in word_to_find:
            fails += 1

         # Vérification de victoire
        all_found = True
        for l in word:
            if l not in letters:
                all_found = False

    if fails < MAX_FAILS + 1:
        return True
    else:
        return False

def normalize_string (string):
    string = ud.normalize('NFD', string)\
           .encode('ascii', 'ignore')\
           .decode("utf-8")

    return str(string).lower()

 # Chargement du tableau de mots depuis le fichier words.tsv
with open("words.tsv") as file:
    tsv_file = csv.reader(file, delimiter="\t")
    for line in tsv_file:
        words.append(line[0])
    
word_to_find = normalize_string(get_random_word(words))

victory = game(word_to_find)

print("\n\n")
if(victory):
    print(f"Bravo le mot était bien {word_to_find.upper()}")
else:
    print(f"Dommage, retentez une prochaine fois. Cette fois-ci, le mot était : {word_to_find.upper()}")

print("\n\n")   