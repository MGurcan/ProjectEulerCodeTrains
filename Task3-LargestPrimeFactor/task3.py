import math
def prime_or_not(x):
    for i in range(2,  math.floor(x/2 + 1)):
        if( x%i == 0):
            return False
    return True

def final_funct(x):
    divisor = 1
    i = math.floor(x/divisor)
    while True:
        if(x % i == 0):
            if(prime_or_not(i)):
                print("Largest Prime Factor for", x, "is: ", i)
                return
        i = math.floor(x / divisor)
        divisor = divisor+1

final_funct(13)
final_funct(27)
final_funct(13195)  
final_funct(600851475143) 
