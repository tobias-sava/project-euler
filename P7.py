# 04/05/2025

# By listing the first six prime numbers: 2, 3, 5, 7, 11, 13, we can see that the 6th prime is 13.

# What is the 10001st prime number?

# Note to self:

# - Init count and n vars
# - Use while loop (while count < 10001):
# - Check if n is prime
# - If prime increment count and n
# - If not prime increment n

import math


def func(maxprime):

    count = 0 # keeping track of primes found

    n = 0 # number being checked if prime until desired count is reached

    d = 2 # divisor

    while count != maxprime:
        
        # base cases
        if n < 2:
            n += 1
        
        if n == 2:
            count += 1
            n += 1
        
        if n % 2 == 0:
            n += 1
        
            # trial divison
            while d <= math.sqrt(n):
                
                if n % d == 0:
                    n += 1
                    break
                else:
                    d += 1
                
            count += 1
            n += 1

        return n
    
print(func(10001))
        
