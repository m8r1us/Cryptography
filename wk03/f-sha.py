import passlib.hash;
salt="8sFt66rZ"

strings=["changeme","123456","password"]

for string in strings:
    print (string)
    print ("\tSHA1: "+passlib.hash.sha1_crypt.hash(string, salt=salt))
    print ("\tSHA256: "+passlib.hash.sha256_crypt.hash(string, salt=salt))
    print ("\tSHA512: "+passlib.hash.sha512_crypt.hash(string, salt=salt))