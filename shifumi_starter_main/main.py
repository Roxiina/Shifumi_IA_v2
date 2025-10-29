from game import get_computer_choice, determine_winner

def play_round():
    player = input("Choisis pierre, feuille ou ciseaux (ou 'q' pour quitter) : ").lower()
    if player == "q":
        return None, None, None
    computer = get_computer_choice()
    try:
        winner = determine_winner(player, computer)
    except ValueError:
        print("Entrée invalide, recommence !")
        return play_round()
    print(f"Tu as choisi {player}, l'ordinateur a choisi {computer}.")
    if winner == "Égalité":
        print("Égalité !")
    else:
        print(f"{winner} gagne cette manche !")
    return player, computer, winner

def main():
    score = {"Joueur": 0, "Ordinateur": 0, "Égalité": 0}
    while True:
        player, computer, winner = play_round()
        if player is None:
            break
        score[winner] += 1
    print("\n=== Résultat final ===")
    print(f"Joueur : {score['Joueur']}")
    print(f"Ordinateur : {score['Ordinateur']}")
    print(f"Égalités : {score['Égalité']}")
    if score["Joueur"] > score["Ordinateur"]:
        print("🎉 Tu as gagné le match !")
    elif score["Joueur"] < score["Ordinateur"]:
        print("💻 L'ordinateur a gagné le match !")
    else:
        print("🤝 Match nul !")

if __name__ == "__main__":
    main()
