''' 
https://projecteuler.net/problem=6
The sum of the squares of the first ten natural numbers is,
The square of the sum of the first ten natural numbers is,
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''
import math

def final_funct(x):
    sum_of_squares = 0
    squares_of_sum = int(math.pow((x * (x+1) / 2),2))
    
    for i in range (1,x+1):
        sum_of_squares += int(math.pow(i,2))
        
    return squares_of_sum - sum_of_squares

print(final_funct(20))