import binascii


msg = "SchnuSchnu"
msg_hex = int(binascii.b2a_hex(msg.encode()).decode())
p = int(17)
q = int(29)
e = int(3)
n = p*q
phi = (p-1)*(q-1)

def findInverse (a, p):
    for i in range (0, p):
        if (a * i % p ==1):
            return i
    return False

def encrypt (m):
    c = m ** e % n
    print("Encrypted Message: ", c)
    return c

d = findInverse(e, phi) # d = e^-1 mod (phi)

def decrypt(c):
    dmsg = c ** d % n
    print("Decrypted Message: ", dmsg)
    return dmsg

print ("Original Message:", msg)
c = encrypt(msg)
decrypt(c)