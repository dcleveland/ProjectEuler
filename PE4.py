# Project Euler problem 3
# https://projecteuler.net/problem=3

# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palendrome(n):
  if str(n) == str(n)[::-1]:
    return True
  else:
    return False

max_palindrome = 0

for i in range(100, 1000):
  for j in range(100, 1000):
    if is_palendrome(i*j) and i*j > max_palindrome:
      max_palindrome = i*j
      a = i
      b = j

print "%s x %s = %s" % (a, b, max_palindrome)