p=11
q=3
N=p*q
PHI=(p-1)*(q-1)
e=3
for d in range(1,100):
        if ((e*d % PHI)==1): break
print ("Public Key: ", e,N)
print ("Private Key: ", d,N)
M=6
cipher = M**e % N
print ("Cipher (c): ", cipher)
message = cipher**d % N
print ("Message (m): ", message)