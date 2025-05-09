# 29/04/2025

# If we list all the natural numbers below 10 that are multiples
# of 3 or 5, we get (3, 5, 6, 9).

# The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

def func(x):

    count = 0 # iteration counter

    result = 0 # sum of multiples

    for n in range(x): # iterating through x numbers 
        if n % 3 == 0: # if number is multiple of 3
            result += n # adding number
        elif n % 5 == 0:
            result += n
        else:
            pass
        count += 1

    return result

print(func(1000)) # Prints correct result: 233168

# 1027434th person to have solved this problem.