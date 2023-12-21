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
                                 listeblocs, debut):  # On veut que Hauteur * Largeur * nombre octets par pixel = taille
    # fichier donnees
    listedonnees = []
    for i in range(len(listeblocs)):
        (type_bloc, l), contenu = listeblocs[i]
        if type_bloc == 68:
            listedonnees += [contenu]
        bonnelongueur = l == len(contenu)
        if not bonnelongueur:
            return False
    donnees = fb.concatenerlistebytes(listedonnees)
    tailledonneesbit = len(donnees) * 8
    return tailledonneesbit == largeur * hauteur and debut == b'Mini-PNG'


def isdonnesconformesniveauxdegris(largeur, hauteur,
                                   listeblocs, debut):  # On veut que Hauteur * Largeur * nombre octets par pixel = taille
    listedonnees = []
    for i in range(len(listeblocs)):
        (type_bloc, l), contenu = listeblocs[i]
        if type_bloc == 68:
            listedonnees += [contenu]
        bonnelongueur = l == len(contenu)
        if not bonnelongueur:
            return False
    donnees = fb.concatenerlistebytes(listedonnees)
    tailledonneesbit = len(donnees) * 8
    return tailledonneesbit == largeur * hauteur * 8 and debut == b'Mini-PNG'


def isdonnesconformes24bits(largeur, hauteur,
                            listeblocs, debut):  # On veut que Hauteur * Largeur * nombre octets par pixel = taille
    # fichier donnees
    listedonnees = []
    for i in range(len(listeblocs)):
        (type_bloc, l), contenu = listeblocs[i]
        if type_bloc == 68:
            listedonnees += [contenu]
        bonnelongueur = l == len(contenu)
        if not bonnelongueur:
            return  False
    donnees = fb.concatenerlistebytes(listedonnees)
    tailledonneesbit = len(donnees) * 8
    return tailledonneesbit == largeur * hauteur * 24 and debut == b'Mini-PNG'


def isdonnesconformespalette(largeur, hauteur,
                             listeblocs, debut):  # On veut que Hauteur * Largeur * nombre octets par pixel = taille
    listedonnees = []
    for i in range(len(listeblocs)):
        (type_bloc, l), contenu = listeblocs[i]
        if type_bloc == 68:
            listedonnees += [contenu]
        bonnelongueur = l == len(contenu)
        if not bonnelongueur:
            return False
        if type_bloc == 80:
            taillepalette3 = l
            palette = contenu
    if taillepalette3%3 != 0:
        return False
    taillepalette = taillepalette3//3
    donnees = fb.concatenerlistebytes(listedonnees)
    for d in donnees:
        if d>=taillepalette:
            return False
    tailledonneesbit = len(donnees) * 8
    return tailledonneesbit == largeur * hauteur * 8 and debut == b'Mini-PNG'
