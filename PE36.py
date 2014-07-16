"""Project Euler problem 36
https://projecteuler.net/problem=36

The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in
base 10 and base 2.

(Please note that the palindromic number, in either base, may not include
leading zeros.)
"""

def IsPalindrome(n):
  if str(n)[0] == "0":
    return False
  elif str(n) == str(n)[::-1]:
    return True
  else:
    return False

if __name__ == "__main__":
  pal_sum = 0
  for i in range(1, 1000001):
    if all(IsPalindrome(x) for x in [i, bin(i).replace("0b", "")]):
      pal_sum += i
  print ("The sum of all numbers that are palindromic in both base 2 and base "
         "10 is %s." % pal_sum)

  # The sum of all numbers that are palindromic in both base 2 and base 10 is
  # 872187.