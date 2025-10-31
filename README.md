# 🎮 Shifumi IA v2

Un jeu de Pierre-Feuille-Ciseaux en Python avec une interface en ligne de commande simple et intuitive.

## 📋 Description

Ce projet implémente le jeu classique de Pierre-Feuille-Ciseaux (Shifumi) où un joueur affronte l'ordinateur. Le jeu suit les règles traditionnelles :
- 🗿 **Pierre** bat **Ciseaux**
- 📄 **Feuille** bat **Pierre** 
- ✂️ **Ciseaux** bat **Feuille**

## 🚀 Fonctionnalités

- ✅ Jeu interactif en ligne de commande
- ✅ Choix aléatoire de l'ordinateur
- ✅ Système de score avec comptage des victoires
- ✅ Gestion des égalités
- ✅ Validation des entrées utilisateur
- ✅ Suite de tests unitaires avec pytest
- ✅ Support pour quitter le jeu à tout moment

## 🛠️ Installation

### Prérequis
- Python 3.7 ou plus récent
- pip (gestionnaire de paquets Python)

### Étapes d'installation

1. **Cloner le repository**
   ```bash
   git clone https://github.com/Roxiina/Shifumi_IA_v2.git
   cd Shifumi_IA_v2
   ```

2. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```

## 🎯 Utilisation

### Lancer le jeu
```bash
python main.py
```

### Comment jouer
1. Le jeu vous demande de choisir entre `pierre`, `feuille` ou `ciseaux`
2. Tapez votre choix et appuyez sur Entrée
3. L'ordinateur fait son choix automatiquement
4. Le résultat de la manche s'affiche
5. Continuez à jouer ou tapez `q` pour quitter
6. À la fin, le score final et le gagnant du match sont affichés

### Exemple de session de jeu
```
Choisis pierre, feuille ou ciseaux (ou 'q' pour quitter) : pierre
Tu as choisi pierre, l'ordinateur a choisi ciseaux.
Joueur gagne cette manche !

Choisis pierre, feuille ou ciseaux (ou 'q' pour quitter) : feuille
Tu as choisi feuille, l'ordinateur a choisi feuille.
Égalité !

Choisis pierre, feuille ou ciseaux (ou 'q' pour quitter) : q

=== Résultat final ===
Joueur : 1
Ordinateur : 0
Égalités : 1
🎉 Tu as gagné le match !
```

## � Tests

Le projet inclut une suite de tests unitaires pour valider la logique du jeu.

### Exécuter les tests
```bash
# Exécuter tous les tests
pytest

# Exécuter avec plus de détails
pytest -v

# Exécuter avec couverture de code
pytest --cov=.
```

### Tests inclus
- ✅ Test des égalités (pierre vs pierre, etc.)
- ✅ Test des victoires du joueur
- ✅ Test des victoires de l'ordinateur
- ✅ Validation des choix invalides

## 📁 Structure du projet

```
Shifumi_IA_v2/
├── main.py              # Point d'entrée principal
├── game.py               # Logique du jeu
├── requirements.txt      # Dépendances Python
├── README.md            # Documentation
├── LICENSE              # Licence du projet
├── __init__.py          # Package Python
├── pytest-mock.py       # Configuration pytest
├── tests/               # Tests unitaires
│   ├── test_game.py     # Tests de la logique du jeu
│   └── __pycache__/     # Cache Python
└── __pycache__/         # Cache Python
```

## 🔧 Développement

### Modules principaux

#### `game.py`
- `get_computer_choice()` : Génère un choix aléatoire pour l'ordinateur
- `determine_winner(player, computer)` : Détermine le gagnant d'une manche

#### `main.py`
- `play_round()` : Gère une manche complète
- `main()` : Boucle principale du jeu avec gestion du score

## 🚀 Améliorations futures

### �🧠 Activités proposées
- [ ] Corriger les bugs du jeu
- [ ] Ajouter des tests pour les cas limites
- [ ] Améliorer les messages utilisateur
- [ ] Étendre le jeu en interface web (Flask/Django)
- [ ] Ajouter des outils de qualité de code (`flake8`, `black`)
- [ ] Intégrer la couverture de code dans le pipeline CI/CD
- [ ] Ajouter un mode multijoueur
- [ ] Implémenter des statistiques avancées
- [ ] Créer une IA plus sophistiquée avec apprentissage

### Idées d'extensions
- 🎨 Interface graphique (Tkinter/PyQt)
- 🌐 Version web avec Flask ou FastAPI
- 📊 Statistiques détaillées et graphiques
- 🤖 IA adaptative qui apprend les patterns du joueur
- 🏆 Système de classement et achievements

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :
1. Fork le projet
2. Créer une branche pour votre fonctionnalité
3. Commiter vos changements
4. Pousser vers la branche
5. Ouvrir une Pull Request

## 📝 Licence

Ce projet est sous licence. Voir le fichier `LICENSE` pour plus de détails.

## 👤 Auteur

**Roxiina** - [GitHub](https://github.com/Roxiina)

---

*Projet réalisé dans le cadre d'un exercice de programmation Python* 🐍
