from time import sleep as sl
from os import system as sys
from vues.outils_vues import OutilsVues
from controleurs.outils_controleurs import OutilsControleurs
from vues.menu_joueur_liste import menu_joueur_liste
from modeles.joueur import Joueur
from controleurs.gestion_creation_joueur import gestion_creation_joueur as gcj
from controleurs.modification_classement import ModificationClassement


def menu_joueur():
    """
    Fonction affichant et gerant le menu des joueurs.
    """
    valeur_quitter = 0
    while valeur_quitter != 1:
        sys(OutilsControleurs.which_os())
        print("\nMenu joueurs: ")
        print("\n1 - Liste des joueurs\n2 - Ajout d'un joueur\n3 - Modification des classements")
        print("4 - Retour\n5 - Quitter")
        try:
            choix_menu_joueur = int(input("\nVotre choix: "))
        except ValueError:
            print("\nVous n'avez pas saisi un chiffre.")
            sl(2)
            continue
        if choix_menu_joueur == 1:
            menu_joueur_liste()
        if choix_menu_joueur == 2:
            gcj()
        if choix_menu_joueur == 3:
            if Joueur.joueurs_alpha() == 0:
                print("\n---------------------------\n")
                print("Il n'y a aucun joueurs d'enregistrer, veuillez ajouter des joueurs via le menu.")
                input("\nAppuyer sur entrer pour continuer")
            else:
                modif_classement = ModificationClassement(Joueur.joueurs_alpha())
                modif_classement.modification_classement()
        if choix_menu_joueur == 4:
            return
        if choix_menu_joueur == 5:
            instance_class = OutilsVues()
            instance_class.quitter()
