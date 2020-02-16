def gcd(a, b):
    while (b!=0): 
        print (a,b);
        Remainder = a % b;
        a = b;
        b = Remainder;
    return a

g = gcd(5435,634)
print (g)

g = gcd(5432,634)
print (g)

g = gcd(9,15)
print (g)


