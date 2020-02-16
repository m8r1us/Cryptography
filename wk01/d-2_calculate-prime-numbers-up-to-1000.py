import sys

def search_for_primes_to(n):
    # Division (floor) of the input number
    size = n//2
    # Create a list of 1 based on the size
    sieve = [1]*size
    # Set a limit of square input number (?)
    limit = int(n**0.5)
    # Loop through the limit
    for i in range(1,limit):
        # If List item is >0
        if sieve[i]:
            # multiplay range i by 2 + 1
            val = 2*i+1
            # tmp value size -1 division by val
            tmp = ((size-1) - i)//val 
            # Set value in the list by jumping ::val
            sieve[i+val::val] = [0]*tmp
    # Loop through the list and based if the result is >0 multiplay (i*2+1) the value and add to the return list
    return [2] + [i*2+1 for i, v in enumerate(sieve) if v and i>0]
 
test=30

print (search_for_primes_to(test))