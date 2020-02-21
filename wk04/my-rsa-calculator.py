# V0.6
# Author: m8r1us
# Link: https://github.com/m8r1us/esecurity
# Comment: 
# This is a simple RSA implementation. It does not want to be neither fast nor safe!
# The aim is to provide a working and easy to read codebase to learn the RSA algorithm.

import binascii
import random
import math

# -----------------
# 0 DEFINTION
# -----------------

e = int(65537) # A very common value for the public exponent is e=65537, because 65537=216+1, which has a nice binary representation (like all Fermat primes): 10000000000000001
length = 29 # length of p and q

# -----------------
# 1 FUNCTIONS
# -----------------

# Check if prime
def isPrime(num):
    # prime numbers are greater than 1
    # Corner cases 
    if num > 1:
        # check for factors
        for i in range(2,num):
            if (num % i) == 0:
                print(num,"is not a prime number")
                print(i,"times",num//i,"is",num)
                return False
        else:
            print(num,"is a prime number")
            return True
 
    # if input number is less than
    # or equal to 1, it is not prime
    else:
        print(num,"is not a prime number")
        return False

# Generate primes
def get_primes(start, stop):
    #Return a list of prime numbers in ``range(start, stop)``.

    if start >= stop:
        return []

    primes = [2]

    for n in range(3, stop + 1, 2):
        for p in primes:
            if n % p == 0:
                break
        else:
            primes.append(n)

    while primes and primes[0] < start:
        del primes[0]

    return primes

# Find relatively prime numbers
# Two numbers are relatively prime if they share no common factors, i.e. there is no integer (except 1) that divides both.
def are_relatively_prime(a, b):  
    #Return ``True`` if ``a`` and ``b`` are two relatively prime numbers.
    for n in range(2, min(a, b) + 1):
        if a % n == b % n == 0:
            return False
    return True

#Extended Euclidean Algorithm (GCD)
def eea(a,b):
    if(a%b==0):
        return(b,0,1)
    else:
        gcd,s,t = eea(b,a%b)
        s = s-((a//b) * t)
        print("%d = %d*(%d) + (%d)*(%d)"%(gcd,a,t,s,b))
        return(gcd,t,s)
 
# Function to find modular inverse
#The following code would also calculate d (slower):
# for d in range(3, phi, 2):
#     if d * e % phi == 1:
#         break
# else:
#     raise AssertionError("cannot find 'd' with p={!r}, q={!r} and e={!r}".format(p, q, e))
def mult_inv(e,r):
    gcd,s,_=eea(e,r)
    if(gcd!=1):
        return None
    else:
        if(s<0):
            print("s=%d. Since %d is less than 0, s = s(modr), i.e., s=%d."%(s,s,s%r))
        elif(s>0):
            print("s=%d."%(s))
        return s%r

# Encryption
# If m_text is the message to be transmitted, it is encrypted as c_text ≡ m_text^e * (mod n) and c_text is send over network.
def encrypt(pub_key,m_text):
    e,n=pub_key
    hex_data = binascii.hexlify(m_text.encode())
    plain_text = int(hex_data, 16)
    print("Your original message as int: \t", plain_text)

    if plain_text > n:
        raise Exception("plain text too large for key (n)")

    c_text = pow(plain_text, e, n) #c_text = (plain_text**e)%n
    
    return c_text

# Decryption
# Upon recieving the encrypted message c_text, it is descrypted as m ≡ c_text^d * (mod n) to retrieve original message m.
def decrypt(priv_key,c_text):
    d,n=priv_key
    decrypted_text = pow(c_text, d, n) #decrypted_text=(int(c_text)**d)%n
    print("decrypted text integer: \t", decrypted_text)
    decrypted_decoded = binascii.unhexlify(hex(decrypted_text)[2:]).decode() # [2:] slicing, to strip the 0x part    

    return decrypted_decoded

# -----------------
# 2 MAIN
# -----------------

print("-------------------------------------------------------")
print("-> 1 STEP (p,q) <-")
print("-> Generate 2 distinct random prime numbers p and q")
print("-------------------------------------------------------\n")
RandomGenerator = input("RandomGenerator for the Primes? (Yes/No): ")

# Define p and q
if RandomGenerator == "Yes":
    if length < 4:
        raise ValueError('cannot generate a key of length less than 4 (got {!r})'.format(length))

    # find a number ``n`` which is the product of two prime numbers (``p`` and ``q``). 
    # ``n`` must have the number of bits specified
    # by ``length``, therefore it must be in ``range(n_min, n_max + 1)``.
    # The argument ``length`` specifies the bit length of the number ``n`` shared between
    # the two keys: the higher, the better.
    n_min = 1 << (length - 1)
    n_max = (1 << length) - 1

    # The key is stronger if ``p`` and ``q`` have similar bit length. We
    # choose two prime numbers in ``range(start, stop)`` so that the
    # difference of bit lengths is at most 2.
    start = 1 << (length // 2 - 1)
    stop = 1 << (length // 2 + 1)
    primes = get_primes(start, stop)

    # Now that we have a list of prime number candidates, randomly select
    # two so that their product is in ``range(n_min, n_max + 1)``.
    while primes:
        p = random.choice(primes)
        primes.remove(p)
        q_candidates = [q for q in primes
                        if n_min <= p * q <= n_max]
        if q_candidates:
            q = random.choice(q_candidates)
            break
    else:
        raise AssertionError("cannot find 'p' and 'q' for a key of length={!r}".format(length))
# ELSE: Prime Wizard
else:
    check_p = False
    check_q = False
    while(((check_p==False)or(check_q==False))):
        p = int(input("Enter a prime number for p (17): "))
        q = int(input("Enter a prime number for q (29): "))
        check_p = isPrime(p)
        check_q = isPrime(q)

# Print p and q
print("The first factor of the modulus (p) is: ",p)
print("The second factor of the modulus (q) is: ",q)

print("\n-------------------------------------------------------")
print("-> 2 STEP (n) <-")
print("-> Compute n = pq. n is used as the modulus for both the public and private keys. Its length is the key length.")
print("-------------------------------------------------------\n")

# Compute n = pq. n is used as the modulus for both the public and private keys. Its length is the key length.
n = p * q
print("n is: ",n)

print("\n-------------------------------------------------------")
print("-> 3 STEP (phi) <-")
print("Compute phi = (p-1)*(q-1) where phi is Euler’s totient function.")
print("-------------------------------------------------------\n")

#Eulers Toitent 'phi'
# Compute φ(n) = φ(p)φ(q) = (p − 1)(q − 1) where φ is Euler’s totient function. (https://en.wikipedia.org/wiki/Euler%27s_totient_function)
phi= (p-1)*(q-1)
print("Eulers Toitent(phi) is: ",phi)

print("\n-------------------------------------------------------")
print("-> 4 STEP (e) <-")
print("Choose an integer e such that 1 < e < phi and gcd(e, phi)")
print("-------------------------------------------------------\n")

# -> e Value Calculation
# Choose an integer e such that 1 < e < phi and gcd(e, phi) = 1; i.e., e and n are coprime. e is released as the public key exponent.
# choose a number ``e`` lower than ``(p - 1) * (q - 1)`` which shares no factors with ``(p - 1) * (q - 1)``.

if phi < e:
    e = int(3) # Take 3 as e otherwise 65537

    # The following method would calculate other e
    '''
    for e in range(3, phi, 2):
        if are_relatively_prime(e, phi):
            break
        else:
            AssertionError("cannot find 'e' with p={!r} and q={!r}".format(p, q))
    '''
print("The value of e is: ",e)

print("\n-------------------------------------------------------")
print("-> 5 STEP (d) <-")
print("Find d such that (d * e - 1) is divisible by phi (inverse modulus)")
print("-------------------------------------------------------\n")

# -> d Value Calculation
# Find ``d`` such that ``(d * e - 1)`` is divisible by ``(p - 1) * (q - 1)``.
# Determine d as d ≡ e−1 (mod φ(n)); i.e., d is the multiplicative inverse of e (modulo φ(n))
# modinv is calculated using Extended Euclidean Algorithm.

d = mult_inv(e,phi)
print("The value of d is: ",d)

print("\n-------------------------------------------------------")
print("-> 6 STEP <-")
print("Build private (d,n) and public (e,n) key")
print("-------------------------------------------------------\n")

# Private and public key
private = (d,n)
public = (e,n)

print("Private Key is: ",private)
print("Public Key is: ",public)

print("\n-------------------------------------------------------")
print("-> SUMMARY <-")
print("-------------------------------------------------------")

print("p is: \t\t",p)
print("q is: \t\t",q)
print("n is: \t\t",n)
print("phi is: \t",phi)
print("e is: \t\t",e)
print("d is: \t\t",d)
print("Private Key is: ",private)
print("Public Key is: \t",public)

print("\n-------------------------------------------------------")
print("-> 7 STEP <-")
print("Message encryption [c ≡ m^e * (mod n)]")
print("Message decryption [m ≡ c^d * (mod n)]")
print("-------------------------------------------------------\n")

#Message
message = input("What would you like encrypted or decrypted? (e.g. red / 82616517): ")
print("Your input is: ",message)
print("-------------------------------------------------------\n")
#Choose Encrypt or Decrypt and Print
choose = input("Type '1' for encryption and '2' for decryption: ")
print("-------------------------------------------------------")
if(choose=='1'):
    print("Your original message (m) is: \t",message)
    c_text=encrypt(public,message)
    print("Your encrypted message (c) is: \t",c_text)
    print("-------------------------------------------------------")
    print("Your encrypted message (c) is: \t",c_text)
    print("Your decrypted message (m) is: \t",decrypt(private,c_text))
    print("-------------------------------------------------------")
elif(choose=='2'):
    print("Your decrypted message (m) is: \t",decrypt(private,int(message)))
    print("-------------------------------------------------------")
else:
    print("You entered the wrong option.")