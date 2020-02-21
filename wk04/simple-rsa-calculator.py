CRED = '\033[91m'
CEND = '\033[0m'

p=5
q=7
N=p*q
PHI=(p-1)*(q-1)
e=3
for d in range(1,100):
        if ((e*d % PHI)==1): break

print ("p: ", p)
print ("q: ", q)
print ("d: ", d)
print ("PHI: ", PHI)
print ("n: ", N)
print ("Public Key: ", e,N)
print ("Private Key: ", d,N)
#M=11
print ("--------------------------")
a = []
x = []
for M in range(1,10):
    print ("Message (M): ", M)
    cipher = (M**e) % N
    print ("Cipher (c): ", cipher)
    message = (cipher**d) % N
    print ("Message (m): ", message)
    if M == cipher:
        print (CRED +"EQUAL" + CEND)
    
    a.append(cipher)
    print ("--------------------------")

a.sort()
print (a)
