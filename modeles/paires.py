from modeles.joueur import Joueur


class Paires:
    """
    Classe servant a générer des paires.
    type d'arguments : tulpe, argument nommé
    """

    def __init__(self, joueurs, score={}, nb_tour=0):
        self.joueurs = joueurs
        self.score = score
        self.nb_tour = nb_tour

    def generation_paires_tour_1(self):
        """
        Methode générant des paires de joueurs selon leur classement.
        return : dictionnaire des paires
        rtype : dict
        """
        classement_joueurs_reprise = []
        for joueur in self.joueurs:
            classement_joueurs_reprise.append(Joueur.get_classement_joueur(joueur))
        dict_classement_joueurs = {}
        x = 0
        while x <= len(self.joueurs) - 1:
            dict_classement_joueurs[self.joueurs[x]] = classement_joueurs_reprise[x]
            x += 1
        dict_classement_joueurs = sorted(dict_classement_joueurs.items(), key=lambda t: t[1])
        dict_classement_joueurs_1 = dict_classement_joueurs[:4]
        dict_classement_joueurs_2 = dict_classement_joueurs[4:]
        dict_paires_genere = {}
        x = 0
        while x <= len(dict_classement_joueurs_1) - 1:
            dict_paires_genere[dict_classement_joueurs_1[x]] = dict_classement_joueurs_2[x]
            x += 1
        return dict_paires_genere

    def generation_paires(self):
        """
        Methode générant des paires de joueurs selon leur score ou leur classement.
        return : dictionnaire des paires
        rtype : dict
        """
        dict_joueurs_score = {}
        for match, joueurs in self.score.items():
            for joueur, score in joueurs:
                dict_joueurs_score[joueur] = str(score)
        dict_joueurs_score = sorted(dict_joueurs_score.items(), key=lambda t: t[1], reverse=True)
        dict_paires_genere = {}
        x = 0
        while x <= len(dict_joueurs_score) - 1:
            dict_paires_genere[dict_joueurs_score[x]] = dict_joueurs_score[x + 1]
            x += 2
        dict_arg_1 = {}
        dict_arg_2 = {}
        tulpe_paires_nom = []
        for arg in dict_paires_genere:
            dict_arg_1[arg[0]] = arg[1]
            dict_arg_2[dict_paires_genere[arg][0]] = dict_paires_genere[arg][1]
            tulpe_paires_nom.append(arg[0])
            tulpe_paires_nom.append(dict_paires_genere[arg][0])
        x = 0
        while x <= len(tulpe_paires_nom) - 1:
            if dict_arg_1[tulpe_paires_nom[x]] == dict_arg_2[tulpe_paires_nom[x+1]]:
                if self.nb_tour > 2:
                    tulpe_paires_joueur_classement = []
                    dict_classement_joueur = {}
                    x = 0
                    while x <= len(tulpe_paires_nom) - 1:
                        tulpe_paires_joueur_classement.append(Joueur.get_classement_joueur(tulpe_paires_nom[x]))
                        dict_classement_joueur[tulpe_paires_nom[x]] = tulpe_paires_joueur_classement[x]
                        x += 1
                else:
                    tulpe_paires_joueur_classement = []
                    dict_classement_joueur = {}
                    x = 0
                    while x <= len(tulpe_paires_nom) - 1:
                        tulpe_paires_joueur_classement.append(Joueur.get_classement_joueur(tulpe_paires_nom[x]))
                        dict_classement_joueur[tulpe_paires_nom[x]] = tulpe_paires_joueur_classement[x]
                        x += 1
                if self.nb_tour > 2:
                    dict_classement_joueur = sorted(dict_classement_joueur.items(), key=lambda t: t[1] % self.nb_tour)
                else:
                    dict_classement_joueur = sorted(dict_classement_joueur.items(), key=lambda t: t[1])
                dict_paires_genere.clear()
                x = 0
                while x <= len(dict_classement_joueur) - 1:
                    dict_paires_genere[dict_classement_joueur[x]] = dict_classement_joueur[x+1]
                    x += 2
            x += 2
        return dict_paires_genere
