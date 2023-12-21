import fonctionsbasiques as fb

def Afficherimagenoiretblanc(listeblocs, largeur, hauteur):
    listedonnees = []
    for i in range(len(listeblocs)):
        (type_bloc, l), contenu = listeblocs[i]
        if type_bloc == 68:
            listedonnees += [contenu]
    d = fb.concatenerlistebytes(listedonnees)
    donnees = bin(int.from_bytes(d, byteorder='big'))[2:].zfill(8 * len(d))
    for i in range(hauteur):
        for j in range(largeur):
            if donnees[i * (largeur) + j] == "0":
                print("X", end='')
            else:
                print(" ", end='')
        print("")  # faire un retour à la ligne une fois la largeur finie
    return


from PIL import Image


def Afficherimageniveauxdegris(listeblocs, largeur, hauteur):
    listedonnees = []
    for i in range(len(listeblocs)):
        (type_bloc, l), contenu = listeblocs[i]
        if type_bloc == 68:
            listedonnees += [contenu]
    donnees = fb.concatenerlistebytes(listedonnees)
    image = Image.new("L", (largeur, hauteur))
    pixelmap = image.load()
    for i in range(hauteur):
        for j in range(largeur):
            pixelmap[i, j] = donnees[i * largeur + j]
    image.show()


def Afficherimage24bits(listeblocs, largeur, hauteur):
    listedonnees = []
    for i in range(len(listeblocs)):
        (type_bloc, l), contenu = listeblocs[i]
        if type_bloc == 68:
            listedonnees += [contenu]
    donnees = fb.concatenerlistebytes(listedonnees)
    image = Image.new("RGB", (largeur, hauteur))
    pixelmap = image.load()
    for i in range(hauteur):
        for j in range(largeur):
            [rouge, vert, bleu] = donnees[(i * largeur + j) * 3:(i * largeur + j) * 3 + 3]
            pixelmap[j, i] = (rouge, vert, bleu)
    image.show()
    image.close()
    return

def afficherpalette(palette):
    for i in range(0, len(palette), 3):
        couleur = palette[i:i + 3]
        print(f"Palette Entry {i // 3 + 1}: {couleur}")
    return

def Afficherimagepalette(listeblocs, largeur, hauteur):
    listedonnees = []
    for i in range(len(listeblocs)):
        (type_bloc, l), contenu = listeblocs[i]
        if type_bloc == 68:
            listedonnees += [contenu]
        elif type_bloc == 80:
            palette = contenu
    afficherpalette(palette)
    donnees = fb.concatenerlistebytes(listedonnees)
    n = len(donnees)
    if n != hauteur*largeur:
        raise Exception("Problèmes de données")
    image = Image.new("P", (largeur, hauteur))
    image.putpalette(palette)
    pixelmap = image.load()
    for i in range(hauteur):
        for j in range(largeur):
            valeurpixel = donnees[i*largeur+j]
            if valeurpixel >= n:
                raise Exception("valeur du pixel hors de la palette")
            pixelmap[j, i] = valeurpixel
    image.show()
    image.close()
    return

