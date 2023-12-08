import binascii
def test(file):
    return open(file, 'rb')

path = "C:/Users/samsa/Downloads/minipng-samples/minipng-samples/bw/ok/A.mp"
file=binascii.hexlify(test(path).read())
file0=test(path).read().hex()
#print(test(path).read())
#rint(test(path).read()[0])

def t():
    return "a", "b"
print(t())