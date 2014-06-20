# Project Euler problem 2
# https://projecteuler.net/problem=2

# By considering the terms in the Fibonacci sequence whose values do not exceed
# four million, find the sum of the even-valued terms.


a = 1
b = 2

sol = 2

while True:
  x = a + b
  if x % 2 == 0:
    sol += x
  a = b
  b = x
  if b >= 4e6:
    break

print sol