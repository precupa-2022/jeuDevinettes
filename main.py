"""
Programme fait par Alexander Precup
Groupe: 402
Description: TP2 - Jeu de devinette
L’ordinateur choisi au hasard un nombre aléatoire entre deux bornes fournies par l'usager.
L’ordinateur demande à l’usager d’entrer un nombre entre les deux bornes de façon à trouver le nombre aléatoire généré.
L'usager peut faire une nouvelle partie ou quitter le jeu.
"""

import random

def gen_chiffre():
   """
   Cette fonction génére un numéro aléatoire selon les bornes fournis par l'usager.
   """
   borne_inf = int(input("Entrez la borne inférieure pour génerer le numéro aléatoire : "))
   borne_sup = int(input("Entrez la borne supérieure pour génerer le numéro aléatoire : "))
   # Générer un numéro aléatoire entre borne_inf et borne_sup
   chiffre_aleatoire = random.randint(borne_inf, borne_sup)
   # Afficher le message que le numéro aléatoire a été généré
   print(f"J'ai choisi un nombre au hasard entre {borne_inf} et {borne_sup}. À vous de le deviner...")
   return chiffre_aleatoire

def jeu_devinette():
    """
    Cette fonction compare l'essai avec le numéro aléatoire
    Si l'usager ne trouve pas le numéro aléatoire, la fonction donne des indices si l'essai est plus grand/petit
    Si l'usager trouve le numéro aléatoire, la fonction affiche le nombre des essais
    """

    # Générer un numéro aléatoire selon les bornes fournis par l'usager
    x = gen_chiffre()
    # Initialisation de la variable nb_essai qui compte le nombre des essais
    nb_essai = 0

    # Initialisation de la variable booléenne boucle_jeu_devinette pour contrôler la durée de la boucle de devinette
    boucle_jeu_devinette = True
    while boucle_jeu_devinette:
        # L'usager fourni le numéro d'essai
        essai = int(input("Entrez votre essai : "))
        # Augumenter la variable nb_essai avec 1 à chaque tour
        nb_essai = nb_essai + 1

        # Comparer le numéro d'essai avec le numéro aléatoire
        if essai < x:
            print(f"Mauvaise choix, le nombre est plus grand que {essai}")
        elif essai > x:
            print(f"Mauvaise choix, le nombre est plus petit que {essai}")
        else:
            # Si l'usager trouve le numéro aléatoire
            # Afficher "Bravo! Bonne réponse" et le nombre des essai(s) pour trouver le numéro aléatoire
            print("Bravo! Bonne réponse")
            print(f"Vous avez réussi en : {nb_essai} essai(s).")
            # Sortir de la boucle de devinette
            boucle_jeu_devinette = False

# Initialisation de la variable booléenne continue_jeu pour continuer le jeu si l'usager le desire
continue_jeu = True
while continue_jeu:
    # Appeler la fonction jeu_devinette pour trouver le numéro aléatoire
    jeu_devinette()
    # L’ordinateur demande à l’usager s’il désire faire une nouvelle partie ou quitter
    quit = input("Voulez vous faire une autre partie (o/n) ? ")

    # Si l'usager desire de quitter, sortir de la boucle continue jeu
    if quit == "n":
        continue_jeu = False

print("Merci et au revoir ...")
