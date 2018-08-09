#!/usr/bin/python

from Crypto.PublicKey import RSA
from Crypto.Util import number

def genRSAkey(p,q):
    n = p*q                        # modulus; goes in public key
    e = 65537L                     # public key exponent, standard value
    phi = (p-1)*(q-1)
    d = number.inverse(e,phi)    # private key exponent
    #return RSA.construct((n,e,d,p,q,None))
    return RSA.construct((n,e,d,p,q))

n1 = long(open('rsa_n1.txt').read())
n2 = long(open('rsa_n2.txt').read())
msg = [line.strip().decode('hex') for line in open('rsa_conversation.txt')]

# Your solution here!

print(number.GCD(n1, n2))
