class AffichageTournois:
    """
    Classe affichant un message sur la console.
    type d'arguments : str
    """

    def __init__(self, arg):
        self.arg = arg

    def affichage(self):
        """
        Methode affichant un message via la fonction print.
        """
        print(self.arg)

    def affichage_input(self):
        """
        Methode affichant un message via la fonction input.
        """
        x = input(self.arg)
        return str(x)
