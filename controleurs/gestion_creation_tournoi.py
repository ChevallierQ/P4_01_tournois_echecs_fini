from vues.affichage_creation_tournoi import affichage_creation_tournoi as act
from modeles.tournoi import Tournoi
from vues.outils_vues import OutilsVues


def gestion_creation_tournoi():
    """
    Fonction gerant l'affichage et la creation d'un tournoi.
    """
    data = act()
    tournoi = Tournoi(data[0], data[1], data[2], data[3], data[4], data[5], data[6])
    instance_class = OutilsVues()
    if instance_class.sauvegarde(data[0], data[1], data[2], data[3], data[4], data[5], data[6]) == 1:
        tournoi.serialiser_instance_tournoi()
    return
