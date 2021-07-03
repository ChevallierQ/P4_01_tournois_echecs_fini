def debut_tours(arg):
    """
    Fonction affichant le numero du tour.
    """
    return "\n\nTour numero {}".format(arg)

def paires_generes(num, j_a, j_b):
    """
    Fonction affichant le numero du match ainsi que les joueurs d'une paire.
    """
    return "\n\nMatch {} :\n{}\n{}".format(num, j_a, j_b)

def affichage_input():
    """
    Fonction input.
    """
    return "\nAppuyer sur entrer pour continuer"

def score_match(num, score):
    """
    Fonction affichant le numero du match ainsi que les scores de ce match.
    """
    return "\nLe score du match {} : {}".format(num, score)
