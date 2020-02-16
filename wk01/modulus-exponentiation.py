# B.1
#print ((8**13)%271)
#print ((12**23)%973)

# B.2
M = int(input("Enter message: "))
e = int(input("Enter exponent: "))
p = int(input("Enter prime "))
guess = int(input("Enter guess "))

#M = 8
#e = 5
#p = 269
#guess = 219

def isPrime2(num):
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


def isPrime3(num):
    if (num==1):
        return False
    elif (num==2):
        return True
    else:
        for x in range(2,num):
            if(num % x==0):
                return False
        return True 

# Driver Program 
if (isPrime2(p)): 
    if (guess==((M**e)%p)):
            print ("The guessed remainder",guess,"was correct.")
    else:
            print ("The guessed remainder",guess,"was not correct.")
     


