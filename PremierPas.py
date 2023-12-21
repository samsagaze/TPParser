import fonctionsbasiques as fb


def Commentaires(listeblocs):
    listecommentaire = []
    for ((typebloc, l), contenu) in listeblocs:
        if typebloc == 67:  # 43 correspond à C en ASCII
            listecommentaire += [contenu]
        if len(listecommentaire) == 0:
            return ""
    return fb.concatenerlistebytes(listecommentaire).decode("ASCII")


def Header(listeblocs):
    for ((type_bloc, l), contenu) in listeblocs:
        if type_bloc == 72:
            if len(contenu) != 9:
                raise Exception("Header non conforme")
            return contenu
    raise Exception("Pas de header")


# Données conformes

def isdonnesconformesnoiretblanc(largeur, hauteur,
                                 listeblocs):  # On veut que Hauteur * Largeur * nombre octets par pixel = taille
    # fichier donnees
    listedonnees = []
    bool = True
    for i in range(len(listeblocs)):
        (type_bloc, l), contenu = listeblocs[i]
        if type_bloc == 68:
            listedonnees += [contenu]
        bonnelongueur = l == len(contenu)
        if not bonnelongueur:
            bool = False
    donnees = fb.concatenerlistebytes(listedonnees)
    tailledonneesbit = len(donnees) * 8
    return tailledonneesbit == largeur * hauteur and bool


def isdonnesconformesniveauxdegris(largeur, hauteur,
                                   listeblocs):  # On veut que Hauteur * Largeur * nombre octets par pixel = taille
    listedonnees = []
    bool = True
    for i in range(len(listeblocs)):
        (type_bloc, l), contenu = listeblocs[i]
        if type_bloc == 68:
            listedonnees += [contenu]
        bonnelongueur = l == len(contenu)
        if not bonnelongueur:
            bool = False
    donnees = fb.concatenerlistebytes(listedonnees)
    tailledonneesbit = len(donnees) * 8
    return tailledonneesbit == largeur * hauteur * 8 and bool


def isdonnesconformes24bits(largeur, hauteur,
                            listeblocs):  # On veut que Hauteur * Largeur * nombre octets par pixel = taille
    # fichier donnees
    listedonnees = []
    bool = True
    for i in range(len(listeblocs)):
        (type_bloc, l), contenu = listeblocs[i]
        if type_bloc == 68:
            listedonnees += [contenu]
        bonnelongueur = l == len(contenu)
        if not bonnelongueur:
            bool = False
    donnees = fb.concatenerlistebytes(listedonnees)
    tailledonneesbit = len(donnees) * 8
    return tailledonneesbit == largeur * hauteur * 24 and bool


def isdonnesconformespalette(largeur, hauteur,
                             listeblocs):  # On veut que Hauteur * Largeur * nombre octets par pixel = taille
    listedonnees = []
    bool = True
    for i in range(len(listeblocs)):
        (type_bloc, l), contenu = listeblocs[i]
        if type_bloc == 68:
            listedonnees += [contenu]
        bonnelongueur = l == len(contenu)
        if not bonnelongueur:
            bool = False
    donnees = fb.concatenerlistebytes(listedonnees)
    tailledonneesbit = len(donnees) * 8
    return tailledonneesbit == largeur * hauteur * 8 and bool
