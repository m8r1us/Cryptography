
# Python 3 program to 
# find number of co 
# prime pairs in array 
  
# Recursive function to 
# return gcd of a and b 
def gcd(a, b): 
      
    # Everything divides 0  
    if (a == 0 or b == 0): 
            False
      
    # base case 
    if (a == b): 
        return a 
  
    # a is greater 
    if (a > b): 
        return gcd(a-b, b) 
          
    return gcd(a, b-a) 
      
# function to check  
# for gcd 
def coprime(a, b) : 
    return (gcd(a, b) == 1) 
  
  
# Returns count of  
# co-prime pairs  
# present in array 
def numOfPairs(arr, n) : 
    count = 0
      
    for i in range(0, n-1) : 
        for j in range(i+1, n) : 
      
            if (coprime(arr[i], arr[j])) : 
                count = count + 1
      
    return count 
  
  
# driver code 
arr = [5432,634] 
n = len(arr)  
  
print(numOfPairs(arr, n)) 