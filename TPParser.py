def obtenirfichier(path):
    return open(path, "rb").read()


def concatenerlistebytes(listebyte):
    n = len(listebyte)
    if n == 1:
        return listebyte[0]
    else:
        res = listebyte[0]
        for i in range(n - 1):
            res = bytes(res + listebyte[i + 1])
    return res


def decouperbloc(fichier):
    listebloc = []
    n = len(fichier)
    i = 8
    while i < n:
        typepixel = fichier[i]
        if typepixel not in [67, 72, 68]:  # 72 : H, 67 : C, 68 : D
            raise Exception("Problème : un bloc n'est pas H, C ou D")
        longueur = int.from_bytes(fichier[i + 1:i + 5], byteorder='big')
        contenu = fichier[i + 5:i + 5 + longueur]
        listebloc.append((typepixel, contenu))
        i = i + 5 + longueur
    if i != n:
        raise Exception("problème d'écarts entre la longueur annoncée et la longueur réelle")
    return listebloc


def Commentaires(listeblocs):
    listecommentaire = []
    for (typebloc, contenu) in listeblocs:
        if typebloc == 67:  # 43 correspond à C en ASCII
            listecommentaire += [contenu]
    return concatenerlistebytes(listecommentaire).decode("ASCII")


def PremierPas(fichier):  # file sous forme C:/...
    largeur = int.from_bytes(fichier[13:17], byteorder='big')
    hauteur = int.from_bytes(fichier[17:21], byteorder='big')
    type_pixel = int.from_bytes(fichier[21:22], byteorder='big')
    listeblocs = decouperbloc(fichier)
    if type_pixel == 0:
        typepixelstring = "noir et blanc"
        boolconforme = isdonnesconformesnoiretblanc(largeur, hauteur, listeblocs)
    elif type_pixel == 1:
        typepixelstring = "niveaux de gris"
        boolconforme = isdonnesconformesniveauxdegris(largeur, hauteur, listeblocs)
    elif type_pixel == 2:
        typepixelstring = "palette"
        boolconforme = False
    elif type_pixel == 3:
        typepixelstring = "couleurs 24 bits"
        boolconforme = isdonnesconformes24bits(largeur, hauteur, listeblocs)
    else:
        raise Exception("mauvais type de pixels")
    print("Largeur : ", largeur)
    print("Hauteur : ", hauteur)
    print("Type de pixel : ", type_pixel, " ", typepixelstring)
    print("Commentaires :")
    print(Commentaires(listeblocs))
    print("les donnees sont conformes : ", boolconforme)
    return


def isdonnesconformesnoiretblanc(largeur, hauteur,
                                 listedeblocs):  # On veut que Hauteur * Largeur * nombre octets par pixel = taille
    # fichier donnees
    donnees = ''
    for (type_bloc, contenu) in listedeblocs:
        if type_bloc == 68:
            donnees += contenu
    tailledonneesbit = len(donnees) * 8
    return tailledonneesbit == largeur * hauteur


def Afficherimagenoiretblanc(fichier):
    largeur = int.from_bytes(fichier[13:17], byteorder='big')
    hauteur = int.from_bytes(fichier[17:21], byteorder='big')
    type_pixel = int.from_bytes(fichier[21:22], byteorder='big')
    listeblocs = decouperbloc(fichier)
    if type_pixel != 0:
        raise Exception("Image pas en noir et blanc")
    listedonnees = []
    for i in range(len(listeblocs)):
        type_bloc, contenu = listeblocs[i]
        if type_bloc == 68:
            listedonnees += [contenu]
    d = concatenerlistebytes(listedonnees)
    donnees = bin(int.from_bytes(d, byteorder='big'))[2:].zfill(8 * len(d))
    for i in range(hauteur):
        for j in range(largeur):
            if donnees[i * (largeur) + j] == "0":
                print("X", end='')
            else:
                print(" ", end='')
        print("")  # faire un retour à la ligne une fois la largeur finie
    return


def isdonnesconformesniveauxdegris(largeur, hauteur,
                                   listedeblocs):  # On veut que Hauteur * Largeur * nombre octets par pixel = taille
    # fichier donnees
    listedonnees = []
    for (type_bloc, contenu) in listedeblocs:
        if type_bloc == 68:
            listedonnees += [contenu]
    donnees = concatenerlistebytes(listedonnees)
    tailledonneesbit = len(donnees) * 8
    return tailledonneesbit == largeur * hauteur * 8


def isdonnesconformes24bits(largeur, hauteur,
                            listedeblocs):  # On veut que Hauteur * Largeur * nombre octets par pixel = taille
    # fichier donnees
    listedonnees = []
    for (type_bloc, contenu) in listedeblocs:
        if type_bloc == 68:
            listedonnees += [contenu]
    donnees = concatenerlistebytes(listedonnees)
    tailledonneesbit = len(donnees) * 8
    return tailledonneesbit == largeur * hauteur * 24

###def topgm(fichierentree, fichiersortie):
