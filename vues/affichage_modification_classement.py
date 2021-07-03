def nom_disponible(num, nom):
    """
    Fonction affichant le nom d'un joueur et son indice.
    """
    return "{} :{}".format(num, nom)

def input_choix_joueur():
    """
    Fonction input.
    """
    return "\n---------------------------\n\
        \nEntrez l'indice du joueur pour modifier son classement : "

def input_choix_classement(nom):
    """
    Fonction input affichant le nom du joueur.
    """
    return "\nEntrez le classement du joueur {} : ".format(nom)

def retour(num):
    """
    Fonction affichant l'option retour avec son indice.
    """
    return "{} : Retour".format(num)
