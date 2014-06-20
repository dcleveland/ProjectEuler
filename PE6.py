# Project Euler problem 6
# https://projecteuler.net/problem=6

# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.

sq_sum = sum(range(1, 101))**2
sum_sqs = sum([x**2 for x in range(1, 101)])
diff = sq_sum - sum_sqs
print diff