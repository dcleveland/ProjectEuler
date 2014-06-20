# Project Euler Problem 1
# https://projecteuler.net/problem=1

# Find the sum of all the multiples of 3 or 5 below 1000.

sol = 0
for i in range(1, 1000):
  if i % 5 == 0 or i % 3 == 0:
    sol += i

print sol
