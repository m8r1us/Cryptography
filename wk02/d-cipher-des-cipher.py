from Crypto.Cipher import DES
import hashlib
import sys
import binascii
import Padding

ciphertext=input('Enter cipher:')
password=input('Enter password:')

def decrypt(ciphertext,key, mode):
	encobj = DES.new(key,mode)
	return(encobj.decrypt(ciphertext))

key = hashlib.sha256(password.encode()).digest()[:8]

ciphertext = bytes.fromhex(ciphertext)

#b'\x8fw\x08\x98\xdd\xb9\xfb8'

plaintext = decrypt(ciphertext,key,DES.MODE_ECB)
plaintext = Padding.removePadding(plaintext.decode(),mode='CMS')
print ("  decrypt: ", plaintext)