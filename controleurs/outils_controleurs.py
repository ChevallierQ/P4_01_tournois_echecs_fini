from tinydb import TinyDB
from sys import platform
import re


class OutilsControleurs:
    """
    Classe regroupant divers methodes servant dans l'ensemble du programme.
    """

    def serialiser_instance_joueur(nom, prenom, date_de_naissance, sexe, classement):
        """
        Methode servant à serialiser une instance de joueur.
        type d'arguments : str
        """
        serialized_player = {
            'nom': nom,
            'prenom': prenom,
            'date de naissance': date_de_naissance,
            'sexe': sexe,
            'classement': classement
        }

        db = TinyDB('data/joueurs.json')
        table_joueurs = db.table('Joueur')
        table_joueurs.insert(serialized_player)

    def serialiser_instance_tournoi(nom, lieu, date, nb_tours, joueurs, temps, note):
        """
        Methode servant à serialiser une instance de tournois.
        type d'arguments : str
        """
        tours = ""
        serialized_tournoi = {
            'nom': nom,
            'lieu': lieu,
            'date': date,
            'nombre de tours': nb_tours,
            'joueurs': joueurs,
            'temps': temps,
            'note': note,
            'tours': tours
        }

        db = TinyDB('data/tournoi.json')
        table_tournoi = db.table('Tournoi')
        table_tournoi.insert(serialized_tournoi)

    def test_date(date):
        """
        Methode servant à controler le format d'une date.
        type d'arguments : str
        return : 0, 1, 3 si erreur, et 2 si valeur correct
        rtype : int
        """
        if len(date) > 10:
            return 0
        if len(date) < 10:
            return 1
        test_date = re.match(r'[0-3][0-9]/[0-1][0-9]/[0-9][0-9][0-9][0-9]', date)
        if test_date:
            return 2
        else:
            return 3

    def which_os():
        """
        Methode qui test l'os de l'ordinateur puis retourne la bonne syntaxe.
        return : syntaxe correcte pour effacer la console
        rtype : str
        """
        if platform == "linux" or platform == "linux2":
            return '"cls"'
        elif platform == "darwin":
            return '"clear"'
        elif platform == "win32":
            return '"cls"'

    def test_heure(heure):
        """
        Methode servant à controler le format d'une heure.
        type d'arguments : str
        return : 0, 1, 3 si erreur, et 2 si valeur correct
        rtype : int
        """
        if len(heure) > 5:
            return 0
        if len(heure) < 5:
            return 1
        test_heure = re.match(r'[0-2][0-9]:[0-5][0-9]', heure)
        if test_heure:
            return 2
        else:
            return 3
