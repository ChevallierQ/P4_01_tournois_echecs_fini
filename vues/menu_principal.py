from time import sleep as sl
from os import system as sys
from vues.outils_vues import OutilsVues
from controleurs.outils_controleurs import OutilsControleurs
from vues.menu_joueur import menu_joueur
from controleurs.gestion_creation_tournoi import gestion_creation_tournoi as gct
from vues.menu_tournoi import menu_tournoi


def menu_principal():
    """
    Fonction affichant et gerant le menu principal.
    """
    valeur_quitter = 0
    while valeur_quitter != 1:
        sys(OutilsControleurs.which_os())
        print("\nMenu principal: ")
        print("\n1 - Creer un nouveau tournoi\n2 - Joueurs\n3 - Gestion des tournois\n4 - Quitter")
        try:
            choix_principal = int(input("\nVotre choix: "))
        except ValueError:
            print("\nVous n'avez pas saisi un chiffre.")
            sl(2)
            continue
        if choix_principal == 1:
            gct()
        if choix_principal == 2:
            menu_joueur()
        if choix_principal == 3:
            menu_tournoi()
        if choix_principal == 4:
            instance_class = OutilsVues()
            instance_class.quitter()
