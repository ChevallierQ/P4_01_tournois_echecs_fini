from vues.affichage_creation_joueur import affichage_creation_joueur as acj
from modeles.joueur import Joueur
from vues.outils_vues import OutilsVues


def gestion_creation_joueur():
    """
    Fonction gerant l'affichage et la creation d'un joueur.
    """
    data = acj()
    joueur = Joueur(data[0], data[1], data[2], data[3], data[4])
    instance_class = OutilsVues()
    if instance_class.sauvegarde(data[0], data[1], data[2], data[3], data[4]) == 1:
        joueur.serialiser_instance_joueur()
    return
