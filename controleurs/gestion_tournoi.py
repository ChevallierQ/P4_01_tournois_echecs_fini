from modeles.paires import Paires
from vues.affichage_tournois import *
from modeles.match import Match
from modeles.tours import Tours
from modeles.tournoi import Tournoi
from vues.outils_vues import OutilsVues
from controleurs.modification_classement import ModificationClassement
from vues.affichage_creation_tour import affichage_creation_tour
from vues.affichage_creation_match import affichage_creation_match


class GestionTournoi:
    """
    Classe gerant le déroulement d'un tournoi.
    type d'arguments : int, list, int
    """

    def __init__(self, nb_tours, joueurs, num_tournoi, nom_tournoi):
        self.nb_tours = nb_tours
        self.joueurs = joueurs
        self.num_tournoi = num_tournoi
        self.nom_tournoi = nom_tournoi

    def gestion_tournoi(self):
        """
        Methode gerant le déroulement d'un tournoi.
        """
        tours = []
        scores = {}
        score_final = {}
        x = 1
        while x <= self.nb_tours:
            print(debut_tours(x))
            if x == 1:
                paires = Paires(self.joueurs)
                paires_genere = paires.generation_paires_tour_1()
                data = affichage_creation_tour()
                tour = Tours(data[0], data[1], data[2])
            if x > 1:
                paires = Paires(self.joueurs, scores, x)
                paires_genere = paires.generation_paires()
                data = affichage_creation_tour()
                tour = Tours(data[0], data[1], data[2])
            nom_joueurs_match = []
            y = 1
            for arg in paires_genere:
                print(paires_generes(y, arg[0], paires_genere[arg][0]))
                nom_joueurs_match.append(arg[0])
                nom_joueurs_match.append(paires_genere[arg][0])
                y += 1
            input(affichage_input())
            a = 0
            z = 1
            resultat_tour = []
            while z <= y - 1:
                data = affichage_creation_match(nom_joueurs_match[a])
                match = Match(nom_joueurs_match[a], nom_joueurs_match[a+1], data[0], data[1])
                match_score = match.get_tulpe()
                print(score_match(z, match_score))
                resultat_tour.append("Match {}".format(z))
                resultat_tour.append(match_score)
                if x == 1:
                    for joueur, score in match_score:
                        score_final[joueur] = score
                    scores["Match {}".format(z)] = match_score
                elif x > 1:
                    joueur_a_b = []
                    for joueur, score in match_score:
                        sc = score_final[joueur]
                        score_final[joueur] = sc + score
                        joueur_a_b.append(joueur)
                    match_score = Match.get_tulpe_2(joueur_a_b[0], score_final[joueur_a_b[0]],
                                                    joueur_a_b[1], score_final[joueur_a_b[1]])
                    scores["Match {}".format(z)] = match_score
                z += 1
                a += 2
            tours.append(tour.get_data_tour(resultat_tour))
            x += 1
        input(affichage_input())
        instance_save = OutilsVues()
        score_final = sorted(score_final.items(), key=lambda t: t[1], reverse=True)
        if instance_save.sauvegarde(score_final) == 1:
            Tournoi.ajout_data_tours(self.nom_tournoi, tours)
            modif_classement = ModificationClassement(score_final)
            modif_classement.modification_classement_tounoi()
            return
