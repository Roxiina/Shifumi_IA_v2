import sys
import os

# Ajouter le dossier parent au path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from game import determine_winner
import pytest

def test_egalite():
    assert determine_winner("pierre", "pierre") == "Égalité"
    assert determine_winner("feuille", "feuille") == "Égalité"
    assert determine_winner("ciseaux", "ciseaux") == "Égalité"

def test_victoires_joueur():
    assert determine_winner("pierre", "ciseaux") == "Joueur"
    assert determine_winner("feuille", "pierre") == "Joueur"
    assert determine_winner("ciseaux", "feuille") == "Joueur"

def test_victoires_ordinateur():
    assert determine_winner("pierre", "feuille") == "Ordinateur"
    assert determine_winner("feuille", "ciseaux") == "Ordinateur"
    assert determine_winner("ciseaux", "pierre") == "Ordinateur"

def test_choix_invalide():
    with pytest.raises(ValueError):
        determine_winner("pierrex", "feuille")
    with pytest.raises(ValueError):
        determine_winner("", "ciseaux")
