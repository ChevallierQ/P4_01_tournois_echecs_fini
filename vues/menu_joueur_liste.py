from time import sleep as sl
from os import system as sys
from vues.outils_vues import OutilsVues
from controleurs.outils_controleurs import OutilsControleurs
from modeles.joueur import Joueur


def menu_joueur_liste():
    """
    Fonction affichant et gerant le menu de la liste des joueurs.
    """
    valeur_quitter = 0
    while valeur_quitter != 1:
        sys(OutilsControleurs.which_os())
        print("\nMenu liste des joueurs: ")
        print("\n1 - Par ordre alphabétique\n2 - Par classement\n3 - Retour\n4 - Quitter")
        try:
            choix_menu_liste_joueur = int(input("\nVotre choix: "))
        except ValueError:
            print("\nVous n'avez pas saisi un chiffre.")
            sl(2)
            continue
        if choix_menu_liste_joueur == 1:
            print("\n---------------------------\n")
            liste_joueurs_alpha = Joueur.joueurs_alpha()
            if liste_joueurs_alpha == 0:
                print("Il n'y a aucun joueurs d'enregistrer, veuillez ajouter des joueurs via le menu.")
                input("\nAppuyer sur entrer pour continuer")
                return
            for arg in liste_joueurs_alpha:
                print(arg)
            input("\nAppuyer sur entrer pour continuer")
        if choix_menu_liste_joueur == 2:
            print("\n---------------------------\n")
            liste_joueurs_classement = Joueur.joueurs_classement()
            if liste_joueurs_classement == 0:
                print("Il n'y a aucun joueurs d'enregistrer, veuillez ajouter des joueurs via le menu.")
                input("\nAppuyer sur entrer pour continuer")
                return
            for arg in liste_joueurs_classement:
                print(arg)
            input("\nAppuyer sur entrer pour continuer")
        if choix_menu_liste_joueur == 3:
            return
        if choix_menu_liste_joueur == 4:
            instance_class = OutilsVues()
            instance_class.quitter()
