import passlib.hash

salt="PkWj6gM4"

strings=["changeme","123456","password"]

for string in strings:
    print (f"APR1 {string}: "+passlib.hash.apr_md5_crypt.hash(string, salt=salt))