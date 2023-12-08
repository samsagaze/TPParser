import binascii
def test(file):
    return open(file, 'rb')

path = "C:/Users/samsa/Downloads/minipng-samples/minipng-samples/bw/ok/A.mp"
print(binascii.hexlify(test(path).read()))