import hashlib;
import passlib.hash;
import sys;

salt=b"ZDzPE45C"
strings=["changeme","123456","password"]

for string in strings:
    print (string)
    print ("\tPBKDF2 (SHA1): "+passlib.hash.pbkdf2_sha1.hash(string, salt=salt))
    print ("\tPBKDF2 (SHA256): "+passlib.hash.pbkdf2_sha256.hash(string, salt=salt))