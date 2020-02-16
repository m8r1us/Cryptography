import passlib.hash;
string="Napier"
print ("->", string)
print ("LM Hash:"+passlib.hash.lmhash.hash(string))
print ("NT Hash:"+passlib.hash.nthash.hash(string))

string="Foxtrot"
print ("->", string)
print ("LM Hash:"+passlib.hash.lmhash.hash(string))
print ("NT Hash:"+passlib.hash.nthash.hash(string))