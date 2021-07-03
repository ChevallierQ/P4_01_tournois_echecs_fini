from time import sleep as sl


def affichage_creation_match(joueur):
    """
    Fonction affichant le questionnaire pour la creation de match.
    """
    score_joueur_a = 2
    score_joueur_b = 2
    print("\n---------------------------")
    while score_joueur_a == 2:
        try:
            score = int(input("\nScore du joueur {}\n\n1 - Gagnant 1p\
                \n2 - Perdant 0p\n3 - Match nul 1/2p\n\nVotre choix : ".format(joueur)))
        except ValueError:
            print("\nVous n'avez pas saisi une valeur valide.")
            sl(2)
            continue
        if score == 1:
            score_joueur_a = 1
            score_joueur_b = 0
            break
        if score == 2:
            score_joueur_a = 0
            score_joueur_b = 1
            break
        if score == 3:
            score_joueur_a = 0.5
            score_joueur_b = 0.5
            break
    return score_joueur_a, score_joueur_b
