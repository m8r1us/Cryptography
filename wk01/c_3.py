message = input("Enter message: ")
e = input("Enter exponent: ")
p = input("Enter prime ")
guess = input("Guess the cipher ")

cipher = (int(message) ** int(e)) % int(p)
print ("Cipher:",cipher)

if (int(guess)==cipher):
    print ("The Answer is correct")
else:
    print ("The Answer is not correct")