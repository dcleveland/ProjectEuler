"""# Project Euler problem 20
# https://projecteuler.net/problem=20

n! means n x (n - 1) x ... x 3 x 2 x 1

For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!"""

def Factorial(n):
  product = 1
  for i in range(1, n+1):
    product *= i
  return product

if __name__ == "__main__":
  f = Factorial(100)
  digits = [int(d) for d in str(f)]
  digit_sum = sum(digits)
  print "The sum of the digits in 100! is %s" % digit_sum