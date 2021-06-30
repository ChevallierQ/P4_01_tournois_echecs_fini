from os import system as sys
from sys import platform
from time import sleep as sl


def report():
    """
    Fonction qui test l'os de l'odinateur, génére un rapport falke8-html puis ouvre ce dernier.
    """

    if platform == "linux" or platform == "linux2":
        sys("flake8 --max-line-length=119 --format=html --htmldir=flake8_rapport \
        vues/* controleurs/* modeles/* TournoisSuisse.py")
        sl(2)
        sys("flake8_rapport/index.html")
    elif platform == "darwin":
        sys("flake8 --max-line-length=119 --format=html --htmldir=flake8_rapport \
        vues/* controleurs/* modeles/* TournoisSuisse.py")
        sl(2)
        sys("open flake8_rapport/index.html")
    elif platform == "win32":
        sys("python3 -m flake8 --max-line-length=119 --format=html --htmldir=flake8_rapport \
        vues/* controleurs/* modeles/* TournoisSuisse.py")
        sl(2)
        sys("start flake8_rapport/index.html")
