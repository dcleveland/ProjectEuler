# Project Euler problem 7
# https://projecteuler.net/problem=7

# What is the 10001st prime number?
import math # cheating!

def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

y = 2
primes = 1

while primes < 10001:
  y = y + 1
  if is_prime(y):
    primes += 1

print y