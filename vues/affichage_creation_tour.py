from time import sleep as sl
from datetime import datetime


def affichage_creation_tour():
    """
    Fonction affichant le questionnaire pour la creation de tour.
    """
    nom = ""
    date_debut = ""
    heure_debut = ""
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
    return nom, date_debut, heure_debut
