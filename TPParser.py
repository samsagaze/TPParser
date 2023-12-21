def obtenirfichier(path):


def decouperbloc(fichier):
    listebloc = []
    n = len(fichier)
    i = 16
    while i < n:
        typepixel = fichier[i:i + 2]
        print(typepixel)
        if typepixel not in ["43", "48", "44"]:
            raise Exception("Problème : un bloc n'est pas H, C ou D")
        longueur = int(fichier[i + 2:i + 10], 16)
        contenu = fichier[i + 10:i + 10 + 2 * longueur]
        if typepixel == 44:
            if longueur != len(contenu) // 4:
                raise Exception(
                    "problème d'écarts entre la longueur annoncée et la longueur réelle sur un bloc de données")
        listebloc.append((typepixel, contenu))
        i = i + 10 + 2 * longueur
    if i != n:
        raise Exception("problème d'écarts entre la longueur annoncée et la longueur réelle")
    return listebloc


def Commentaires(listeblocs):
    commentaireshex = ""
    for (typebloc, contenu) in listeblocs:
        if typebloc == 43:  # 43 correspond à C en ASCII
            commentaireshex += contenu + " "
    return bytes.fromhex(commentaireshex).decode("ASCII")


def PremierPas(path):  # file sous forme C:/...
    fichier = open(path, "rb").read().hex()
    largeur = int(fichier[26:34], 16)
    hauteur = int(fichier[34:42], 16)
    type_pixel = int(fichier[42:44], 16)
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
        if type_bloc == 44:
            donnees += contenu
    tailledonneesbit = len(donnees) * 4
    return tailledonneesbit == largeur * hauteur


def Afficherimagenoiretblanc(fichier):
    largeur = int(fichier[26:34], 16)
    hauteur = int(fichier[34:42], 16)
    type_pixel = int(fichier[42:44], 16)
    listeblocs = decouperbloc(fichier)
    if type_pixel != 0:
        raise Exception("Image pas en noir et blanc")
    donnees = ''
    print(listeblocs)
    for (type_bloc, contenu) in listeblocs:
        if type_bloc == 44:
            donnees += bin(int(contenu, 16))
    for i in range(hauteur):
        for j in range(largeur):
            if donnees[i * (hauteur-1) + j] == 0:
                print("X", end='')
        print("")  # faire un retour à la ligne une fois la largeur finie
    return


def isdonnesconformesniveauxdegris(largeur, hauteur,
                                   listedeblocs):  # On veut que Hauteur * Largeur * nombre octets par pixel = taille
    # fichier donnees
    donnees = ''
    for (type_bloc, contenu) in listedeblocs:
        if type_bloc == 44:
            donnees += contenu
    tailledonneesbit = len(donnees) * 4
    return tailledonneesbit == largeur * hauteur * 8

def isdonnesconformes24bits(largeur, hauteur,
                                   listedeblocs):  # On veut que Hauteur * Largeur * nombre octets par pixel = taille
    # fichier donnees
    donnees = ''
    for (type_bloc, contenu) in listedeblocs:
        if type_bloc == 44:
            donnees += contenu
    tailledonneesbit = len(donnees) * 4
    return tailledonneesbit == largeur * hauteur * 24

#def Afficherimageniveauxdegris(fichier):
