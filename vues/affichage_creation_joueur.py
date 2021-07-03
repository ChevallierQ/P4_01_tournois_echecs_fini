from time import sleep as sl
from controleurs.outils_controleurs import OutilsControleurs


def affichage_creation_joueur():
    """
    Fonction affichant le questionnaire pour la creation de joueur.
    """
    nom = ""
    prenom = ""
    date_de_naissance = ""
    sexe = ""
    classement = 0

    print("\n---------------------------")
    while len(nom) == 0:
        try:
            nom = str(input("\nNom : "))
        except ValueError:
            print("\nVous n'avez pas saisi un nom valide.")
            sl(2)
            continue

    print("\n---------------------------")
    while len(prenom) == 0:
        try:
            prenom = str(input("\nPrenom : "))
        except ValueError:
            print("\nVous n'avez pas saisi un prenom valide.")
            sl(2)
            continue

    print("\n---------------------------")
    while len(date_de_naissance) == 0:
        try:
            date_de_naissance = str(input("\nDate de naissance\nFormat : jj/mm/aaaa : "))
        except ValueError:
            print("\nVous n'avez pas saisi une date valide.")
            sl(2)
            continue
        test_date = OutilsControleurs.test_date(date_de_naissance)
        if test_date == 0:
            print("\nVous avez saisi une valeur trop grande.")
            date_de_naissance = ""
        if test_date == 1:
            print("\nVous avez saisi une valeur trop petite.")
            date_de_naissance = ""
        if test_date == 2:
            break
        if test_date == 3:
            print("\nVous avez saisi un format de date incorrect.")
            date_de_naissance = ""

    print("\n---------------------------")
    sexe_choix = 0
    while sexe_choix != 1 or sexe_choix != 2 or sexe_choix != 3:
        try:
            sexe_choix = int(input("\nSexe\n1 - Femme\n2 - Homme\n3 - Autre\n\nVotre choix : "))
        except ValueError:
            print("\nVous n'avez pas saisi une valeur valide.")
            sl(2)
            continue
        if sexe_choix == 1:
            sexe = "Femme"
            break
        if sexe_choix == 2:
            sexe = "Homme"
            break
        if sexe_choix == 3:
            sexe = "Autre"
            break

    print("\n---------------------------")
    while classement < 1 or classement > 8:
        try:
            classement = int(input("\nClassement : "))
        except ValueError:
            print("\nVous n'avez pas saisi une valeur valide.")
            sl(2)
            continue
    return nom, prenom, date_de_naissance, sexe, classement
