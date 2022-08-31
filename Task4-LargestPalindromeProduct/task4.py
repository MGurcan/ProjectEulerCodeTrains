import math
def isPalindrome(x):
    number = str(x)
    reverse_number = number [::-1]
    length_of_number = len(number)
    return number[0:math.floor(length_of_number/2)] == reverse_number[0:math.floor(length_of_number/2)]
    
def max3digitsPalindrome():
    for i in range(999,100,-1):
        for j in range(999,100,-1):
            if isPalindrome(i*j):
                print(i*j)
                return
            
max3digitsPalindrome()
