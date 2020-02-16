from Crypto.Cipher import DES
import hashlib
import sys
import binascii
import Padding

val="hello"
password="hello123"

if (len(sys.argv)>1):
    val=sys.argv[1]

if (len(sys.argv)>2):
    password=sys.argv[2]

plaintext=val

def encrypt(plaintext,key, mode):
	encobj = DES.new(key,mode)
	return(encobj.encrypt(plaintext.encode()))

def decrypt(ciphertext,key, mode):
	encobj = DES.new(key,mode)
	return(encobj.decrypt(ciphertext))

print ("\nDES")
key = hashlib.sha256(password.encode()).digest()[:8]

plaintext = Padding.appendPadding(plaintext,blocksize=Padding.DES_blocksize,mode='CMS')
output = binascii.hexlify(bytearray(plaintext.encode()))
print ("After padding (CMS): ", binascii.hexlify(bytearray(plaintext.encode())).decode())


ciphertext = encrypt(plaintext,key,DES.MODE_ECB)
print ("Cipher (ECB): ", binascii.hexlify(bytearray(ciphertext)).decode())
print (type(ciphertext))

plaintext = decrypt(ciphertext,key,DES.MODE_ECB)
plaintext = Padding.removePadding(plaintext.decode(),mode='CMS')
print ("  decrypt: ", plaintext)