# 30/04/2025

# A palindromic number reads the same both ways.

# The largest palindrom made from the product of two 2-digit numbers is:

# 9009 = 91 * 99

# Find the largest palindrome made from the product of two 3 digits numbers.

def func():

    n1 = 0 # num 1
    n2 = 0 # num 2

    p = 0 # storing largest palindrome

    while n1 or n2 < 999 * 999:
        for i in range(1000):
            
            product = n1 * n2

            # incrementing numbers by 1
            n1 += 1
            n2 += 1


print(func())

# Will continue later.