from Crypto.Cipher import AES
import hashlib
import sys
import binascii
import Padding
import base64

ciphertext=input('Enter Base-64 cipher:')
passwords=["hello","ankle","changeme","123456"]

def decrypt(ciphertext,key, mode):
	encobj = AES.new(key,mode)
	return(encobj.decrypt(ciphertext))

ciphertext = base64.b64decode(ciphertext).hex()
ciphertext = bytes.fromhex(ciphertext)
#b'\x8fw\x08\x98\xdd\xb9\xfb8'

for password in passwords:
    key = hashlib.sha256(password.encode()).digest()

    plaintext = decrypt(ciphertext,key,AES.MODE_ECB)

    try:
        plaintext = Padding.removePadding(plaintext.decode(),mode='CMS')
    except:
        print("Error! Wrong Password.")
    else:
        print ("  decrypt: ", plaintext)
        break