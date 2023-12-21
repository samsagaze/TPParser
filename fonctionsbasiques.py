def obtenirfichier(path):
    return open(path, "rb").read()


def concatenerlistebytes(listebyte):
    n = len(listebyte)
    if n==0:
        return []
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
        if typepixel not in [67, 72, 68, 80]:  # 72 : H, 67 : C, 68 : D, P : 80
            raise Exception("Problème : un bloc n'est pas H, C, P ou D")
        longueur = int.from_bytes(fichier[i + 1:i + 5], byteorder='big')
        contenu = fichier[i + 5:i + 5 + longueur]
        listebloc.append(((typepixel, longueur), contenu))
        i = i + 5 + longueur
    if i != n:
        raise Exception("problème d'écarts entre la longueur annoncée et la longueur réelle")
    return listebloc