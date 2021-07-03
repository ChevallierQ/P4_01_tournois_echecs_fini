import json
from tinydb import TinyDB


class Joueur:
    """
    Classe servant a créer une instance de joueur, et regroupant divers methodes pour la recuperation de data.
    type d'arguments : arguments nommés, str, int
    """

    def __init__(self, nom="", prenom="", date_de_naissance="", sexe="", classement=0):
        self.nom = nom
        self.prenom = prenom
        self.date_de_naissance = date_de_naissance
        self.sexe = sexe
        self.classement = classement

    def serialiser_instance_joueur(self):
        """
        Methode servant à serialiser une instance de joueur.
        type d'arguments : str
        """
        serialized_player = {
            'nom': self.nom,
            'prenom': self.prenom,
            'date de naissance': self.date_de_naissance,
            'sexe': self.sexe,
            'classement': self.classement
        }
        db = TinyDB('data/joueurs.json')
        table_joueurs = db.table('Joueur')
        table_joueurs.insert(serialized_player)

    def joueurs_alpha():
        """
        Methode servant a trier les joueurs par ordre alphabetique.
        return : tulpe nom prenom des joueurs
        rtype : tulpe
        """
        with open('data/joueurs.json', 'r') as joueurs_data:
            data_dict = json.load(joueurs_data)
            nom_list = []
            nom = ''
            prenom = ''
            for joueur in data_dict.values():
                for num_joueur in joueur.values():
                    for cle, valeur in num_joueur.items():
                        if cle == 'nom':
                            nom = valeur
                        if cle == 'prenom':
                            prenom = valeur
                    nom_prenom = nom + ' ' + prenom + '\n'
                    nom_list.append(nom_prenom)
                    nom_list.sort()
            if len(nom_list) < 2:
                return 0
            if len(nom_list) >= 2:
                del nom_list[0]
                return nom_list

    def joueurs_classement():
        """
        Methode servant a trier les joueurs par ordre de classement.
        return : tulpe classement nom prenom des joueurs
        rtype : tulpe
        """
        with open('data/joueurs.json', 'r') as joueurs_data:
            data_dict = json.load(joueurs_data)
            classement_nom_list = []
            nom = ''
            prenom = ''
            classement = ''
            for joueur in data_dict.values():
                for num_joueur in joueur.values():
                    for cle, valeur in num_joueur.items():
                        if cle == 'nom':
                            nom = valeur
                        if cle == 'prenom':
                            prenom = valeur
                        if cle == 'classement':
                            classement = 'Classement : ' + str(valeur)
                    nom_prenom_classement = classement + '\n    ' + nom + ' ' + prenom + '\n'
                    classement_nom_list.append(nom_prenom_classement)
                    classement_nom_list.sort()
            if len(classement_nom_list) < 2:
                return 0
            if len(classement_nom_list) >= 2:
                del classement_nom_list[0]
                return classement_nom_list

    def joueurs_tournoi():
        """
        Methode servant a regroupant les joueurs.
        return : tulpe indice nom prenom classement des joueurs
        rtype : tulpe
        """
        with open('data/joueurs.json', 'r') as joueurs_data:
            data_dict = json.load(joueurs_data)
            classement_nom_list = []
            indice_joueur = 0
            nom = ''
            prenom = ''
            classement = ''
            for joueur in data_dict.values():
                for num_joueur in joueur.values():
                    for cle, valeur in num_joueur.items():
                        if cle == 'nom':
                            nom = valeur
                        if cle == 'prenom':
                            prenom = valeur
                        if cle == 'classement':
                            classement = 'Classement : ' + str(valeur)
                    indice_nom_prenom_classement = 'Indice joueur : ' + str(indice_joueur) + '\n   ' + nom + \
                        ' ' + prenom + '\n   ' + classement + '\n'
                    classement_nom_list.append(indice_nom_prenom_classement)
                    indice_joueur += 1
            if len(classement_nom_list) < 9:
                return 0
            if len(classement_nom_list) >= 9:
                del classement_nom_list[0]
                return classement_nom_list

    def get_joueurs_tournoi(liste_indice_selection, liste_nom_joueurs):
        """
        Methode servant récuperer des joueurs selectionnés par leur indice.
        type d'arguments : int, tulpe
        return : tulpe nom prenom des joueurs
        rtype : tulpe
        """
        liste_nom_joueurs_selection = []
        liste_nom_joueurs_new = []
        for arg in liste_nom_joueurs:
            arg = str(arg).replace("\n", "")
            liste_nom_joueurs_new.append(arg)
        for indice in liste_indice_selection:
            liste_nom_joueurs_selection.append(liste_nom_joueurs_new[indice-1])
        return liste_nom_joueurs_selection

    def get_classement_joueur(joueur_selecion):
        """
        Methode servant a récuperer le classement d'un joueur.
        type d'argument : str
        return : classement
        rtype : int
        """
        with open('data/joueurs.json', 'r') as joueurs_data:
            data_dict = json.load(joueurs_data)
            for joueurs in data_dict.values():
                for num_joueurs in joueurs.values():
                    for cle, valeur in num_joueurs.items():
                        if cle == "nom":
                            nom = valeur
                        if cle == "prenom":
                            prenom = valeur
                    nom_prenom = nom + " " + prenom
                    if nom_prenom == joueur_selecion:
                        for cle, valeur in num_joueurs.items():
                            if cle == "classement":
                                joueur_selecion = valeur
                                return joueur_selecion
