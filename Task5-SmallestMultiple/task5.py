import math
def prime_or_not(x):
    for i in range(2,  math.floor(x/2 + 1)):
        if( x%i == 0):
            return False
    return True

def smallestNumberEvenlyDivisible(x):
    multipliers = []
    result = 1
    
    for i in range(2,x+1):
        if prime_or_not(i):
            mul = 1
            while True:
                if(math.pow(i,mul) <= x):
                    mul += 1
                else:
                    result *= math.pow(i,mul-1)
                    multipliers.insert(0,math.pow(i,mul-1))
                    break
    print("multipliers: ", multipliers)
    return int(result)

print(smallestNumberEvenlyDivisible(20))