def decouperbloc(fichier):
    list=[]
    n=len(fichier)
    i=8
    while i<n:
        type = fichier[i:i+2]
        print(type)
        if type not in [43, 48, 44]:
            raise Exception("Problème : un bloc n'est pas H, C ou D")
        longueur = int(fichier[i+2:i+10], 16)
        contenu = fichier[i+10:i+10+2*longueur]
        if type == 44:
            if longueur != len(contenu)//4:
                raise Exception("problème d'écarts entre la longueur annoncée et la longueur réelle sur un bloc de données")
        list.append((type, contenu))
        i = i+10+2*longueur
    if i!=n:
        raise Exception("problème d'écarts entre la longueur annoncée et la longueur réelle")
    return list

def Commentaires(listeblocs):
    commentaireshex= ""
    for (type, contenu) in listeblocs:
        if type == 43:      #43 correspond à C en ASCII
            commentaireshex += contenu + " "
    return bytes.fromhex(commentaireshex).decode("ASCII")

def PremierPas(path):                 #file sous forme C:/...
    fichier = open(path, "rb").read().hex()
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
        raise Exception("mauvais type de pixels")
    listeblocs = decouperbloc(fichier)
    print("Largeur : ", Largeur)
    print("Hauteur : ", Hauteur)
    print("Type de pixel : ", Type_Pixel, " ", Type)
    print("Commentaires :")
    print(Commentaires(listeblocs))
    return


