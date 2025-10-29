import pytest
from game import determine_winner, get_computer_choice

def test_multi_manches(mocker):
    # On simule l’ordinateur qui choisit toujours "ciseaux"
    mocker.patch("game.get_computer_choice", return_value="ciseaux")

    scores = {"Joueur": 0, "Ordinateur": 0, "Égalité": 0}
    # Simulons plusieurs manches
    for player_choice in ["pierre", "feuille", "ciseaux"]:
        winner = determine_winner(player_choice, get_computer_choice())
        scores[winner] += 1

    assert scores["Joueur"] == 1   # pierre bat ciseaux
    assert scores["Ordinateur"] == 1 # feuille perd contre ciseaux
    assert scores["Égalité"] == 1    # ciseaux vs ciseaux
