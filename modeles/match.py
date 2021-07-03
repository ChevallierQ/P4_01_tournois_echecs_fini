class Match:
    """
    Classe servant a créer une instance de match, et regroupant divers methodes pour la recuperation de data.
    type d'arguments : str
    """

    def __init__(self, joueur_a, joueur_b, score_joueur_a, score_joueur_b):
        self.joueur_a = joueur_a
        self.joueur_b = joueur_b
        self.score_joueur_a = score_joueur_a
        self.score_joueur_b = score_joueur_b

    def get_tulpe(self):
        """
        Methode retourant le resultat d'un match.
        return : tulpe nom joueur a, score du jour, joueur b, son score
        rtype : tulpe
        """
        liste_joueur_a = []
        liste_joueur_b = []
        tuple = ()
        liste_joueur_a = self.joueur_a, self.score_joueur_a
        liste_joueur_b = self.joueur_b, self.score_joueur_b
        tuple = liste_joueur_a, liste_joueur_b
        return tuple

    def get_tulpe_2(joueur_a, score_a, joueur_b, score_b):
        """
        Methode retourant le resultat d'un match.
        return : tulpe nom joueur a, score du jour, joueur b, son score
        rtype : tulpe
        """
        liste_joueur_a = []
        liste_joueur_b = []
        tuple = ()
        liste_joueur_a = joueur_a, score_a
        liste_joueur_b = joueur_b, score_b
        tuple = liste_joueur_a, liste_joueur_b
        return tuple
