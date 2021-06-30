from time import sleep as sl
from os import system as sys
from controleurs.flake8_report_generator import report
from controleurs.outils_controleurs import OutilsControleurs


class OutilsVues:
    """
    Classe regroupant divers methodes servant dans l'ensemble du programme.
    type d'arguments : argument nommé str
    """

    def __init__(self, reponse=""):
        self.reponse = reponse

    def quitter(self):
        """
        Methode permettant de quitter le programme.
        return : 0 si retour en arriere
        rtype : int
        """
        while self.reponse != 2 or self.reponse != 1:
            sys(OutilsControleurs.which_os())
            try:
                self.reponse = int(input("\nEtes-vous sûr de vouloir quitter le programme ?\
                    \n\n1 - Oui\n2 - Non\n\nVotre choix: "))
            except ValueError:
                print("\nVous n'avez pas saisi un chiffre.")
                sl(2)
                continue
            if self.reponse == 1:
                report()
                sys(OutilsControleurs.which_os())
                quit()
            if self.reponse == 2:
                return 0

    def sauvegarde(self, *args):
        """
        Methode permettant de savoir si l'utilisateur veux sauvegarder.
        type d'arguments : str
        return : 1 pour oui, 0 pour non
        rtype : int
        """
        while self.reponse != 2 or self.reponse != 1:
            sys(OutilsControleurs.which_os())
            for n in args:
                print(n)
            print("\n---------------------------")
            try:
                self.reponse = int(input("\nVoulez-vous vraiment sauvegarder ?\n\n1 - Oui\n2 - Non\n\nVotre choix: "))
            except ValueError:
                print("\nVous n'avez pas saisi un chiffre.")
                sl(2)
                continue
            if self.reponse == 1:
                return 1
            if self.reponse == 2:
                return 0
