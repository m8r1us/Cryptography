#p = int(input("Enter number to check if it's prime "))

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

# Driver Program 
check = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
for i in check:
    isPrime2(i)


