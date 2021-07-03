from sys import platform
import re


class OutilsControleurs:
    """
    Classe regroupant divers methodes servant dans l'ensemble du programme.
    """

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
