from time import sleep as sl
from datetime import datetime


class Tours:
    """
    Classe servant a créer une instance de tour, et regroupant divers methodes pour la recuperation de data.
    type d'arguments : arguments nommé
    """

    def __init__(self):
        nom = ""
        date_debut = ""
        heure_debut = ""
        date_fin = ""
        heure_fin = ""
        valide = False
        while not valide:
            print("\n---------------------------")
            while len(nom) == 0:
                try:
                    nom = str(input("\nNom du tour : "))
                except ValueError:
                    print("\nVous n'avez pas saisi un nom valide.")
                    sl(2)
                    continue
            now = datetime.now()
            date_debut = now.strftime("%d/%m/%Y")
            heure_debut = now.strftime("%H:%M")

            print("\n---------------------------")
            validation = 0
            print("\n{}\n{}\n{}".format(nom, date_debut, heure_debut))
            while validation == 0:
                try:
                    validation = int(input("\nVoulez-vous valider ?\
                        \n\n1 - Valider\n2 - Recommencer\n\nVotre choix : "))
                except ValueError:
                    print("\nVous n'avez pas saisi une valeur valide.")
                    sl(2)
                    continue
                if validation == 1:
                    print("\n---------------------------")
                    valide = True
                else:
                    nom = ""
                    date_debut = ""
                    heure_debut = ""

        self.nom = nom
        self.date_debut = date_debut
        self.heure_debut = heure_debut
        self.date_fin = date_fin
        self.heure_fin = heure_fin

    def get_data_tour(self, matches):
        """
        Methode retournant les infos du tour.
        return : liste date et heure de debut/fin du tour et matches
        rtype : list
        """
        now = datetime.now()
        self.date_fin = now.strftime("%d/%m/%Y")
        self.heure_fin = now.strftime("%H:%M")
        data_tour = []
        data_tour = self.nom, self.date_debut, self.heure_debut, self.date_fin, self.heure_fin, matches
        return data_tour
