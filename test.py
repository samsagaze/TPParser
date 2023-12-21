chemin = "C:/Users/samsa/Desktop/minipng-samples/bw/ok/A.mp"
import TPParser as tppar
#donnees = tppar.Afficherimagenoiretblanc(tppar.obtenirfichier("C:/Users/samsa/Desktop/minipng-samples/bw/ok/unordered_A.mp"))
#from PIL import Image as i
#image = i.new("L", (10, 10))
#image.show()
#print(tppar.Header(tppar.decouperbloc(tppar.obtenirfichier("C:/Users/samsa/Desktop/minipng-samples/bw/ok/unordered_A.mp"))))
#tppar.Afficherimage24bits((tppar.obtenirfichier(("C:/Users/samsa/Desktop/minipng-samples/other/ok/french-flag.mp"))))
tppar.Informations("C:/Users/samsa/Desktop/minipng-samples/bw/nok/wrong-magic.mp")
tppar.Afficherimage("C:/Users/samsa/Desktop/minipng-samples/bw/nok/wrong-magic.mp")
