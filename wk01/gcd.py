def gcd(a, b):
    while (b!=0): 
        #print (a,b)
        Remainder = a % b
        a = b
        b = Remainder
    return a

g = gcd(4105,10)
print (g)

g = gcd(4539,6)
print (g)

