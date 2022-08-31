'''
https://projecteuler.net/problem=7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
'''
import math

def prime_or_not(x):
    for i in range(2,  math.floor(x/2 + 1)):
        if( x%i == 0):
            return False
    return True

def final_funct(x):
    counter = 2
    prime_counter = 0
    while True:
        if prime_or_not(counter):
            prime_counter += 1
        if prime_counter == x:
            return counter
        counter += 1
        
print(final_funct(10001))

print(prime_or_not(104743))