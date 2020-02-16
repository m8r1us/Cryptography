from Crypto.Cipher import AES
import hashlib
import sys
import binascii
import Padding

val="hello"
password="hello123"

plaintext=val

def encrypt(plaintext,key, mode):
	encobj = AES.new(key,mode)
	return(encobj.encrypt(plaintext.encode()))

def decrypt(ciphertext,key, mode):
	encobj = AES.new(key,mode)
	return(encobj.decrypt(ciphertext))

key = hashlib.sha256(password.encode()).digest()

plaintext = Padding.appendPadding(plaintext,blocksize=Padding.AES_blocksize,mode='CMS')
output = binascii.hexlify(bytearray(plaintext.encode()))
print ("After padding (CMS): ", binascii.hexlify(bytearray(plaintext.encode())).decode())

ciphertext = encrypt(plaintext,key,AES.MODE_ECB)
print ("Cipher (ECB): ", binascii.hexlify(bytearray(ciphertext)).decode())

plaintext = decrypt(ciphertext,key,AES.MODE_ECB)
plaintext = Padding.removePadding(plaintext.decode(),mode='CMS')
print ("  decrypt: ", plaintext)

plaintext=val

plaintext = Padding.appendPadding(plaintext,blocksize=Padding.AES_blocksize,mode='ZeroLen')
print ("\nAfter padding (ZeroLen): ", binascii.hexlify(bytearray(plaintext.encode())).decode())

ciphertext = encrypt(plaintext,key,AES.MODE_ECB)
print ("Cipher (ECB): ", binascii.hexlify(bytearray(ciphertext)).decode())

plaintext = decrypt(ciphertext,key,AES.MODE_ECB)
plaintext = Padding.removePadding(plaintext.decode(),blocksize=Padding.AES_blocksize,mode='ZeroLen')
print ("  decrypt: ", plaintext)

plaintext=val

plaintext = Padding.appendPadding(plaintext,blocksize=Padding.AES_blocksize,mode='Space')
print ("\nAfter padding (Space): ", binascii.hexlify(bytearray(plaintext.encode())).decode())

ciphertext = encrypt(plaintext,key,AES.MODE_ECB)
print ("Cipher (ECB): ", binascii.hexlify(bytearray(ciphertext)).decode())

plaintext = decrypt(ciphertext,key,AES.MODE_ECB)
plaintext = Padding.removePadding(plaintext.decode(),blocksize=Padding.AES_blocksize,mode='Space')
print ("  decrypt: ", plaintext)


plaintext=val

plaintext = Padding.appendPadding(plaintext,blocksize=Padding.AES_blocksize,mode='Random')
print ("\nAfter padding (Random): ", binascii.hexlify(bytearray(plaintext.encode())).decode())

ciphertext = encrypt(plaintext,key,AES.MODE_ECB)
print ("Cipher (ECB): ", binascii.hexlify(bytearray(ciphertext)).decode())

plaintext = decrypt(ciphertext,key,AES.MODE_ECB)
plaintext = Padding.removePadding(plaintext.decode(),mode='Random')
print ("  decrypt: ", plaintext)


plaintext=val

plaintext = Padding.appendPadding(plaintext,blocksize=Padding.AES_blocksize,mode='Null')
print ("\nAfter padding (Null): ", binascii.hexlify(bytearray(plaintext.encode())).decode())

ciphertext = encrypt(plaintext,key,AES.MODE_ECB)
print ("Cipher (ECB): ", binascii.hexlify(bytearray(ciphertext)).decode())

plaintext = decrypt(ciphertext,key,AES.MODE_ECB)
plaintext = Padding.removePadding(plaintext.decode(),mode='Null')
print ("  decrypt: ", plaintext)