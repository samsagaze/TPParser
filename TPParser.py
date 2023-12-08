def PremierPas(file):
    fichier = open(file, "rb").read().hex()
    Largeur = int(fichier[26:34], 16)
    Hauteur = int(fichier[34:42], 16)
    Type_Pixel = int(fichier[42:44], 16)
    if Type_Pixel == 0:
        Type = "noir et blanc"
    elif Type_Pixel == 1:
        Type = "niveaux de gris"
    elif Type_Pixel ==2:
        Type = "palette"
    elif Type_Pixel ==3:
        Type = "couleurs 24 bits"
    else:
        return "Error"
    print("Largeur : ", Largeur)
    print("Hauteur : ", Hauteur)
    print("Type de pixel : ", Type_Pixel, " ", Type)
    return





