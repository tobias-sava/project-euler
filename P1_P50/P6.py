# 02/05/2025

# The sum of squares of the first ten natural numbers is,

# 1 ** 2 + 2 ** 2 + ... + 10 ** 2 = 385

# The square of the sum of the first ten natural numbers is,

# (1 + 2 + ... + 10) ** 2 = 55 ** 2 = 3025

# Hence the difference between the sum of the squares of the first ten
# natural numbers and the square of the sum is 3025 - 385 = 2640

# Find the difference between the sum of the square of the first one
# hundred natural numbers and the square of the sum.

def func(x):

    sum_of_squares = sum(n ** 2 for n in range(x + 1))

    square_of_sum = sum(range(x + 1)) ** 2

    return square_of_sum - sum_of_squares

print(func(100)) # prints 25164150

# 526912th person to have solved this problem.