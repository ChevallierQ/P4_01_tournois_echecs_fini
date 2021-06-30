from time import sleep as sl
from os import system as sys
from vues.outils_vues import OutilsVues
from controleurs.outils_controleurs import OutilsControleurs
from modeles.tournoi import Tournoi
from controleurs.gestion_tournoi import GestionTournoi


def menu_tournoi():
    """
    Fonction affichant et gerant le menu des tournois.
    """
    valeur_quitter = 0
    while valeur_quitter != 1:
        sys(OutilsControleurs.which_os())
        print("\nMenu gestion des tournois: ")
        print("\n1 - Liste des tournois\n2 - Reprise d'un tournoi\n3 - Retour\n4 - Quitter")
        try:
            choix_menu_tournoi = int(input("\nVotre choix: "))
        except ValueError:
            print("\nVous n'avez pas saisi un chiffre.")
            sl(2)
            continue
        if choix_menu_tournoi == 1:
            print("\n---------------------------\n")
            liste_tounois = Tournoi.tournois_liste()
            if liste_tounois == 0:
                print("Il n'y a aucun tournois d'enregistrer, veuillez ajouter un tournoi via le menu.")
                input("\nAppuyer sur entrer pour continuer")
                return
            for arg in liste_tounois:
                print(arg)
            input("\nAppuyer sur entrer pour continuer")
        if choix_menu_tournoi == 2:
            print("\n---------------------------\n")
            x = 0
            liste_tounois = Tournoi.tournois_liste()
            if liste_tounois == 0:
                print("Il n'y a aucun tournois d'enregistrer, veuillez ajouter un tournoi via le menu.")
                input("\nAppuyer sur entrer pour continuer")
                return
            a = 1
            for arg in liste_tounois:
                if x % 9 == 0:
                    print("Tounoi n°{} :".format(a))
                    a += 1
                print(arg)
                x += 1
            choix_tournoi_reprise = 0
            while choix_tournoi_reprise == 0:
                try:
                    choix_tournoi_reprise = int(input("\nSelectionnez un tournoi : "))
                except ValueError:
                    print("\nVous n'avez pas saisi un chiffre.")
                if choix_tournoi_reprise > a - 1 or choix_tournoi_reprise == 0:
                    choix_tournoi_reprise = 0
            data_tournoi_reprise = Tournoi.get_data_tournoi(choix_tournoi_reprise)
            joueurs_tournoi_reprise = Tournoi.get_joueurs_tournoi_reprise(data_tournoi_reprise)
            nb_tours_tournoi_reprise = Tournoi.get_nb_tours_tournoi_reprise(data_tournoi_reprise)
            nom = Tournoi.get_nom_tournoi(data_tournoi_reprise)
            gestion_tournoi = GestionTournoi(nb_tours_tournoi_reprise, joueurs_tournoi_reprise,
                                             choix_tournoi_reprise, nom)
            gestion_tournoi.gestion_tournoi()
            return
        if choix_menu_tournoi == 3:
            return
        if choix_menu_tournoi == 4:
            instance_class = OutilsVues()
            instance_class.quitter()
