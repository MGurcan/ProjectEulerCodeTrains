'''
https://projecteuler.net/problem=9
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''
import math

def final_funct():
    
    a = 0
    b = 0
    
    while a + b < 1000:
        while a < b:
            c = 1000 - a - b
            result = (1000 * c) + (a * b)
            if result == 500000:
                print("a", a)
                print("b", b)
                print("c", c)
                print("a*b*c: " , a*b*c)
                return
            a += 1
        a = 0    
        b += 1       

final_funct()

print(math.pow(200,2) + math.pow(375,2))
print(math.pow(425,2))