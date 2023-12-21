import fonctionsbasiques as fb
import PremierPas as pp
import AfficherImage as ai

def Informations(path):                  # file sous forme C:/...
    fichier = fb.obtenirfichier(path)
    listeblocs = fb.decouperbloc(fichier)
    header = pp.Header(listeblocs)
    largeur = int.from_bytes(header[0:4], byteorder='big')
    hauteur = int.from_bytes(header[4:8], byteorder='big')
    type_pixel = int.from_bytes(header[8:9], byteorder='big')
    if type_pixel == 0:
        typepixelstring = "noir et blanc"
        boolconforme = pp.isdonnesconformesnoiretblanc(largeur, hauteur, listeblocs)
    elif type_pixel == 1:
        typepixelstring = "niveaux de gris"
        boolconforme = pp.isdonnesconformesniveauxdegris(largeur, hauteur, listeblocs)
    elif type_pixel == 2:
        typepixelstring = "palette"
        boolconforme = False
    elif type_pixel == 3:
        typepixelstring = "couleurs 24 bits"
        boolconforme = pp.isdonnesconformes24bits(largeur, hauteur, listeblocs)
    else:
        raise Exception("mauvais type de pixels")
    print("Largeur : ", largeur)
    print("Hauteur : ", hauteur)
    print("Type de pixel : ", type_pixel, " ", typepixelstring)
    print("Commentaires :")
    print(pp.Commentaires(listeblocs))
    print("les donnees sont conformes : ", boolconforme)
    return

def Afficherimage(path):
    fichier = fb.obtenirfichier(path)
    listeblocs = fb.decouperbloc(fichier)
    header = pp.Header(listeblocs)
    largeur = int.from_bytes(header[0:4], byteorder='big')
    hauteur = int.from_bytes(header[4:8], byteorder='big')
    type_pixel = int.from_bytes(header[8:9], byteorder='big')
    if type_pixel == 0:
        if not pp.isdonnesconformesnoiretblanc(largeur, hauteur, listeblocs):
            raise Exception("Données non conformes")
        ai.Afficherimagenoiretblanc(listeblocs, largeur, hauteur)
    elif type_pixel == 1:
        if not pp.isdonnesconformesniveauxdegris(largeur, hauteur, listeblocs):
            raise Exception("Données non conformes")
        ai.Afficherimageniveauxdegris(listeblocs, largeur, hauteur)
    elif type_pixel == 2:
        if not pp.isdonnesconformespalette(largeur, hauteur, listeblocs):
            raise Exception("Données non conformes")
        ai.Afficherimagepalette(listeblocs, largeur, hauteur)
    elif type_pixel == 3:
        if not pp.isdonnesconformes24bits(largeur, hauteur, listeblocs):
            raise Exception("Données non conformes")
        ai.Afficherimage24bits(listeblocs, largeur, hauteur)
    else:
        raise Exception("mauvais type de pixels")
    return


