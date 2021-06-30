from vues.affichage_tournois import AffichageTournois
from controleurs.outils_controleurs import OutilsControleurs
from os import system as sys
from tinydb import TinyDB, Query


class ModificationClassement:
    """
    Classe servant a modifier le classement d'un joueur.
    type d'arguments : dict
    """

    def __init__(self, nom_joueurs_classement):
        self.nom_joueurs_classement = nom_joueurs_classement

    def modification_classement_tounoi(self):
        """
        Methode modifiant le classement des joueurs d'un tournoi fini.
        """
        x = len(self.nom_joueurs_classement)
        a = 1
        list_nom = []
        while a <= x:
            reponse = 0
            while reponse == 0 or reponse > x:
                try:
                    sys(OutilsControleurs.which_os())
                    z = 1
                    for arg in self.nom_joueurs_classement:
                        if arg not in list_nom:
                            affichage = AffichageTournois("{} : {}".format(z, arg))
                            affichage.affichage()
                        z += 1
                    affichage = AffichageTournois("\n---------------------------")
                    affichage.affichage()
                    affichage = AffichageTournois("\nEntrez l'indice du joueur pour modifier son classement : ")
                    reponse = int(affichage.affichage_input())
                except ValueError:
                    print("\nVous n'avez pas saisi un nombre valide.")
                    sys(OutilsControleurs.which_os())
                    continue
            nom_joueur = ""
            e = 1
            for nom, classement in self.nom_joueurs_classement:
                if e == reponse:
                    nom_joueur = nom
                e += 1
            e = 1
            for arg in self.nom_joueurs_classement:
                if e == reponse:
                    list_nom.append(arg)
                e += 1
            reponse_2 = 0
            while reponse_2 == 0 or reponse_2 > x:
                try:
                    affichage = AffichageTournois("\nEntrez le classement du joueur {} : ".format(nom_joueur))
                    reponse_2 = int(affichage.affichage_input())
                except ValueError:
                    print("\nVous n'avez pas saisi un nombre valide.")
                    continue
            nom_joueur = nom_joueur.split(" ")
            a += 1
            db_file = 'data/joueurs.json'
            db = TinyDB(db_file)
            db = db.table("Joueur")
            db.all()
            nom_joueur_db = Query()
            db.update({"classement": reponse_2}, nom_joueur_db.nom == nom_joueur[0])

    def modification_classement(self):
        """
        Methode modifiant le classement d'un joueur en dehors d'une fin de tournoi.
        """
        z = len(self.nom_joueurs_classement) + 1
        reponse = 0
        while reponse != z:
            reponse = 0
            while reponse == 0 or reponse > z:
                try:
                    sys(OutilsControleurs.which_os())
                    x = 1
                    for arg in self.nom_joueurs_classement:
                        arg = str(arg).replace("\n", "")
                        affichage = AffichageTournois("{} : {}".format(x, arg))
                        affichage.affichage()
                        x += 1
                    affichage = AffichageTournois("{} : Retour".format(x))
                    affichage.affichage()
                    affichage = AffichageTournois("\n---------------------------")
                    affichage.affichage()
                    affichage = AffichageTournois("\nEntrez l'indice du joueur pour modifier son classement : ")
                    reponse = int(affichage.affichage_input())
                except ValueError:
                    print("\nVous n'avez pas saisi un nombre valide.")
                    sys(OutilsControleurs.which_os())
                    continue
                if reponse == z:
                    return
            nom_joueur = ""
            e = 1
            for nom in self.nom_joueurs_classement:
                if e == reponse:
                    nom = str(nom).replace("\n", "")
                    nom_joueur = nom
                e += 1
            reponse_2 = 0
            while reponse_2 == 0 or reponse_2 > x:
                try:
                    affichage = AffichageTournois("\nEntrez le classement du joueur {} : ".format(nom_joueur))
                    reponse_2 = int(affichage.affichage_input())
                except ValueError:
                    print("\nVous n'avez pas saisi un nombre valide.")
                    continue
            nom_joueur = nom_joueur.split(" ")
            db_file = 'data/joueurs.json'
            db = TinyDB(db_file)
            db = db.table("Joueur")
            db.all()
            nom_joueur_db = Query()
            db.update({"classement": reponse_2}, nom_joueur_db.nom == nom_joueur[0])
