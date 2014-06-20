# Project Euler problem 5
# https://projecteuler.net/problem=5
# What is the smallest positive number that is evenly divisible by all of the
# numbers from 1 to 20?

# Brute Force:
x = 20
while True:
  # if divisible by 11-20 then also divisible by 1-10.
  if sum([x % i for i in range(11, 21)]) == 0:
    break
  else:
    x += 20

print x