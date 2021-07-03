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

    def serialiser_instance_tournoi(self):
        """
        Methode servant à serialiser une instance de tournois.
        type d'arguments : str
        """
        tours = ""
        serialized_tournoi = {
            'nom': self.nom,
            'lieu': self.lieu,
            'date': self.date,
            'nombre de tours': self.nb_tours,
            'joueurs': self.joueurs,
            'temps': self.temps,
            'note': self.note,
            'tours': tours
        }

        db = TinyDB('data/tournoi.json')
        table_tournoi = db.table('Tournoi')
        table_tournoi.insert(serialized_tournoi)

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
