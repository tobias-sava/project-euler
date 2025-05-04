# 30/04/2025

# 2520 is the smallest number that can be divided by each of
# the numbers from 1 to 10 without any remainder.

# What is the smallest number that is evenly divisible by
# all of the numbers from 1 to 20?

def gcd(a, b):
    """
    Computing Greatest Common Divisor (GCD) using 
    the Euclidean algorithm. """
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    """
    Computing Least Common Multiple (LCM) using GCD """
    return a * b // gcd(a, b)

def smallest_multiple(limit):
    """
    Function that finds the smallest number divisable by all numbers
    from 1 to 'limit'. """

    result = 1 # init result var

    for i in range(2, limit + 1): # loop through 2 to limit
        result = lcm(result, i) # update result with lcm of current result and i
    return result # after loop, result holds the smallest multiple

print(smallest_multiple(20)) # Output: 232792560

# 523139th person to have solved this problem.