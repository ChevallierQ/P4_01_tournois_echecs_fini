from time import sleep as sl
from vues.outils_vues import OutilsVues
from controleurs.outils_controleurs import OutilsControleurs
from modeles.joueur import Joueur
import json
from tinydb import TinyDB, Query


class Tournoi:
    """
    Classe servant a créer une instance de tournoi, et regroupant divers methodes pour la recuperation de data.
    type d'arguments : arguments nommés, str, int, tulpe
    """

    def __init__(self, nom="", lieu="", date="", nb_tours=4, joueurs=[], temps="", note=""):
        self.nom = nom
        self.lieu = lieu
        self.date = date
        self.nb_tours = nb_tours
        self.joueurs = joueurs
        self.temps = temps
        self.note = note

        print("\n---------------------------")
        while len(nom) == 0:
            try:
                nom = str(input("\nNom : "))
            except ValueError:
                print("\nVous n'avez pas saisi un nom valide.")
                sl(2)
                continue

        print("\n---------------------------")
        while len(lieu) == 0:
            try:
                lieu = str(input("\nLieu : "))
            except ValueError:
                print("\nVous n'avez pas saisi un lieu valide.")
                sl(2)
                continue

        print("\n---------------------------")
        while len(date) == 0:
            try:
                date = str(input("\nDate\nFormat : jj/mm/aaaa : "))
            except ValueError:
                print("\nVous n'avez pas saisi une date valide.")
                sl(2)
                continue
            test_date = OutilsControleurs.test_date(date)
            if test_date == 0:
                print("\nVous avez saisi une valeur trop grande.")
                date = ""
            if test_date == 1:
                print("\nVous avez saisi une valeur trop petite.")
                date = ""
            if test_date == 2:
                break
            if test_date == 3:
                print("\nVous avez saisi un format de date incorrect.")
                date = ""

        print("\n---------------------------")
        nb_tours_modif = ""
        while nb_tours_modif != 2 or nb_tours_modif != 1:
            try:
                print("\nNombre de tours\nPar default le nombre est de 4\nVoulez-vous modifier cette valeur ?")
                nb_tours_modif = int(input("\n1 - Oui\n2 - Non\n\nVotre choix: "))
            except ValueError:
                print("\nVous n'avez pas saisi un nombre valide.")
                sl(2)
                continue
            if nb_tours_modif == 1:
                while nb_tours == 4:
                    try:
                        nb_tours = int(input("\nNombre de tours : "))
                    except ValueError:
                        print("\nVous n'avez pas saisi un nombre valide.")
                        sl(2)
                        continue
                    if nb_tours == 4:
                        break
                break
            if nb_tours_modif == 2:
                break

        print("\n---------------------------\n\nListe des joueurs :\n")
        liste_joueurs_tournois = Joueur.joueurs_tournoi()
        if liste_joueurs_tournois == 0:
            print("Il n'y a pas ou pas suffisament de joueurs pour organiser un tounois.")
            print("Veuillez ajouter des joueurs via le menu.")
            input("\nAppuyer sur entrer pour continuer")
            return

        for arg in liste_joueurs_tournois:
            print(arg)
        x = 8
        while x != 0:
            try:
                joueur = int(input("Saisir encore {} indice de joueurs : ".format(x)))
            except ValueError:
                print("\nVous n'avez pas saisi un indice valide.")
                sl(2)
                continue
            if joueur > 0 and joueur <= len(liste_joueurs_tournois):
                if joueur not in joueurs:
                    joueurs.append(joueur)
                else:
                    print("Vous avez deja saisi ce joueur.")
                    x += 1
            else:
                x += 1
            x -= 1

        y = 1
        nom_joueurs = []
        for arg in liste_joueurs_tournois:
            arg = arg[:-15]
            nom_joueurs.append(str(arg).replace("Indice joueur : {}\n   ".format(y), "").replace("\n   ", ""))
            y += 1
        joueurs = Joueur.get_joueurs_tournoi(joueurs, nom_joueurs)

        print("\n---------------------------")
        temps_choix = 0
        while temps_choix != 1 or temps_choix != 2 or temps_choix != 3:
            try:
                temps_choix = int(input("\nContrôle de temps\n1 - Bullet\
                    \n2 - Blitz\n3 - Coup rapide\n\nVotre choix : "))
            except ValueError:
                print("\nVous n'avez pas saisi une valeur valide.")
                sl(2)
                continue
            if temps_choix == 1:
                temps = "Bullet"
                break
            if temps_choix == 2:
                temps = "Blitz"
                break
            if temps_choix == 3:
                temps = "Coup rapide"
                break

        print("\n---------------------------")
        while len(note) == 0:
            try:
                note = str(input("\nDescription : "))
            except ValueError:
                print("\nVous n'avez pas saisi une valeur valide.")
                sl(2)
                continue
            if len(note) == 0:
                break

        instance_class = OutilsVues()
        if instance_class.sauvegarde(nom, lieu, date, nb_tours, joueurs, temps, note) == 1:
            OutilsControleurs.serialiser_instance_tournoi(nom, lieu, date,
                                                          nb_tours, joueurs, temps, note)

    def tournois_liste():
        """
        Methode retournant la liste des tournois.
        return : tulpe datas tournoi
        rtype : tulpe
        """
        with open('data/tournoi.json', 'r') as tournois_data:
            data_dict = json.load(tournois_data)
            tournoi_list = []
            nom = []
            lieu = []
            date = []
            nombre_tours = []
            joueurs = []
            temps = []
            note = []
            tours = []
            data = []
            for tournoi in data_dict.values():
                for num_tournoi in tournoi.values():
                    data = []
                    for cle, valeur in num_tournoi.items():
                        if cle == 'nom':
                            nom = cle, valeur
                        if cle == 'lieu':
                            lieu = cle, valeur
                        if cle == 'date':
                            date = cle, valeur
                        if cle == 'nombre de tours':
                            nombre_tours = cle, valeur
                        if cle == 'joueurs':
                            joueurs = cle, valeur
                        if cle == 'temps':
                            temps = cle, valeur
                        if cle == 'note':
                            note = cle, valeur
                        if cle == 'tours':
                            tours = cle, valeur
                    data = nom, lieu, date, nombre_tours, joueurs, temps, tours, note
                    x = 1
                    while x <= len(data):
                        tournoi_list.append("{} : {}".format(data[x-1][0], data[x-1][1]))
                        x += 1
                    tournoi_list.append("\n")
            if len(tournoi_list) <= 9:
                return 0
            if len(tournoi_list) > 9:
                del tournoi_list[0:9]
                return tournoi_list

    def get_data_tournoi(indice_tournoi_selction):
        """
        Methode retournant les datas d'un tournoi via son indice.
        type d'argument : int
        return : tulpe datas tournoi
        rtype : tulpe
        """
        with open('data/tournoi.json', 'r') as get_data:
            data_dict = json.load(get_data)
            for tournoi in data_dict.values():
                for num_tournoi in tournoi.items():
                    num_tournoi_str = str(num_tournoi[0:1])
                    if num_tournoi_str[2] == str(indice_tournoi_selction):
                        return num_tournoi
                    else:
                        continue

    def get_joueurs_tournoi_reprise(data_tournoi_reprise):
        """
        Methode retournant les joueurs d'un tournoi.
        type d'argument : dict
        return : nom prenom joueur
        rtype : str
        """
        for arg in data_tournoi_reprise:
            dict_data = arg
        for cle, valeur in dict_data.items():
            if cle == "joueurs":
                return valeur

    def get_nb_tours_tournoi_reprise(data_tournoi_reprise):
        """
        Methode retournant le nombre de tours d'un tournoi.
        type d'argument : dict
        return : nombre de tours
        rtype : int
        """
        for arg in data_tournoi_reprise:
            dict_data = arg
        for cle, valeur in dict_data.items():
            if cle == "nombre de tours":
                return valeur

    def get_nom_tournoi(data_tournoi):
        """
        Methode retournant le nom d'un tournoi.
        type d'argument : dict
        return : nom
        rtype : str
        """
        for arg in data_tournoi:
            data = arg
        for cle, valeur in data.items():
            if cle == "nom":
                return valeur

    def ajout_data_tours(nom_tournoi, data_tours):
        """
        Methode sauvegardant les resultats d'un tournoi.
        type d'argument : str, list
        """
        db_file = 'data/tournoi.json'
        db = TinyDB(db_file)
        db = db.table("Tournoi")
        db.all()
        nom_tournois = Query()
        db.update({"tours": data_tours}, nom_tournois.nom == nom_tournoi)
