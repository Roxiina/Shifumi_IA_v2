import random

def get_computer_choice():
    return random.choice(["pierre", "feuille", "ciseaux"])

def determine_winner(player, computer):
    choices = ["pierre", "feuille", "ciseaux"]
    if player not in choices or computer not in choices:
        raise ValueError("Choix invalide")
    if player == computer:
        return "Égalité"
    elif (
        (player == "pierre" and computer == "ciseaux") or
        (player == "feuille" and computer == "pierre") or
        (player == "ciseaux" and computer == "feuille")
    ):
        return "Joueur"
    else:
        return "Ordinateur"
