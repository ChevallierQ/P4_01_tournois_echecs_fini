from datetime import datetime


class Tours:
    """
    Classe servant a créer une instance de tour, et regroupant divers methodes pour la recuperation de data.
    type d'arguments : arguments nommé
    """

    def __init__(self, nom, date_debut, heure_debut, date_fin="", heure_fin=""):
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
