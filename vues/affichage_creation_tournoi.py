from time import sleep as sl
from modeles.joueur import Joueur
from controleurs.outils_controleurs import OutilsControleurs


def affichage_creation_tournoi():
    """
    Fonction affichant le questionnaire pour la creation de tournoi.
    """
    nom = ""
    lieu = ""
    date = ""
    nb_tours = 4
    joueurs = []
    temps = ""
    note = ""

    print("\n---------------------------")
    while len(nom) == 0:
        try:
            nom = str(input("\nNom : "))
        except ValueError:
            print("\nVous n'avez pas saisi un nom valide.")
            sl(2)
            continue

    print("\n---------------------------")
    while len(lieu) == 0:
        try:
            lieu = str(input("\nLieu : "))
        except ValueError:
            print("\nVous n'avez pas saisi un lieu valide.")
            sl(2)
            continue

    print("\n---------------------------")
    while len(date) == 0:
        try:
            date = str(input("\nDate\nFormat : jj/mm/aaaa : "))
        except ValueError:
            print("\nVous n'avez pas saisi une date valide.")
            sl(2)
            continue
        test_date = OutilsControleurs.test_date(date)
        if test_date == 0:
            print("\nVous avez saisi une valeur trop grande.")
            date = ""
        if test_date == 1:
            print("\nVous avez saisi une valeur trop petite.")
            date = ""
        if test_date == 2:
            break
        if test_date == 3:
            print("\nVous avez saisi un format de date incorrect.")
            date = ""

    print("\n---------------------------")
    nb_tours_modif = ""
    while nb_tours_modif != 2 or nb_tours_modif != 1:
        try:
            print("\nNombre de tours\nPar default le nombre est de 4\nVoulez-vous modifier cette valeur ?")
            nb_tours_modif = int(input("\n1 - Oui\n2 - Non\n\nVotre choix: "))
        except ValueError:
            print("\nVous n'avez pas saisi un nombre valide.")
            sl(2)
            continue
        if nb_tours_modif == 1:
            while nb_tours == 4:
                try:
                    nb_tours = int(input("\nNombre de tours : "))
                except ValueError:
                    print("\nVous n'avez pas saisi un nombre valide.")
                    sl(2)
                    continue
                if nb_tours == 4:
                    break
            break
        if nb_tours_modif == 2:
            break

    print("\n---------------------------\n\nListe des joueurs :\n")
    liste_joueurs_tournois = Joueur.joueurs_tournoi()
    if liste_joueurs_tournois == 0:
        print("Il n'y a pas ou pas suffisament de joueurs pour organiser un tounois.")
        print("Veuillez ajouter des joueurs via le menu.")
        input("\nAppuyer sur entrer pour continuer")
        return

    for arg in liste_joueurs_tournois:
        print(arg)
    x = 8
    while x != 0:
        try:
            joueur = int(input("Saisir encore {} indice de joueurs : ".format(x)))
        except ValueError:
            print("\nVous n'avez pas saisi un indice valide.")
            sl(2)
            continue
        if joueur > 0 and joueur <= len(liste_joueurs_tournois):
            if joueur not in joueurs:
                joueurs.append(joueur)
            else:
                print("Vous avez deja saisi ce joueur.")
                x += 1
        else:
            x += 1
        x -= 1

    y = 1
    nom_joueurs = []
    for arg in liste_joueurs_tournois:
        arg = arg[:-15]
        nom_joueurs.append(str(arg).replace("Indice joueur : {}\n   ".format(y), "").replace("\n   ", ""))
        y += 1
    joueurs = Joueur.get_joueurs_tournoi(joueurs, nom_joueurs)

    print("\n---------------------------")
    temps_choix = 0
    while temps_choix != 1 or temps_choix != 2 or temps_choix != 3:
        try:
            temps_choix = int(input("\nContrôle de temps\n1 - Bullet\
                  \n2 - Blitz\n3 - Coup rapide\n\nVotre choix : "))
        except ValueError:
            print("\nVous n'avez pas saisi une valeur valide.")
            sl(2)
            continue
        if temps_choix == 1:
            temps = "Bullet"
            break
        if temps_choix == 2:
            temps = "Blitz"
            break
        if temps_choix == 3:
            temps = "Coup rapide"
            break

    print("\n---------------------------")
    while len(note) == 0:
        try:
            note = str(input("\nDescription : "))
        except ValueError:
            print("\nVous n'avez pas saisi une valeur valide.")
            sl(2)
            continue
        if len(note) == 0:
            break
    return nom, lieu, date, nb_tours, joueurs, temps, note
