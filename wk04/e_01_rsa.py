#https://stuvel.eu/python-rsa-doc/usage.html
import rsa
from base64 import b64decode
import binascii
(bob_pub, bob_priv) = rsa.newkeys(512)
print ("RSA Public Key:\n\n",bob_pub)
print ("\nRSA Private Key:\n\n",bob_priv)
ciphertext = rsa.encrypt(b'Here is my message', bob_pub)
print ("\nRSA Ciphertext B64:\n\n",binascii.b2a_base64(ciphertext).decode())

message = rsa.decrypt(ciphertext, bob_priv)
print("\nRSA Ciphertext Decrypted:\n\n",message.decode('utf8'))
print ("\n")