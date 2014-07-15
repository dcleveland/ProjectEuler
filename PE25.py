"""Project Euler problem 25
https://projecteuler.net/problem=25

The Fibonacci sequence is defined by the recurrence relation:


Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the first term in the Fibonacci sequence to contain 1000 digits?
"""

import sys
import time

if __name__ == "__main__":
  start = time.time()
  series = [1, 1, 2]
  while True:
    if len(str(series[-1])) == 1000:
      secs = time.time() - start
      print ("The first term in the Fibonacci sequence to contain one thousand "
             "digits is %s. Found in %s seconds." % (str(len(series)), secs))
      break
    series.append(sum(series[-2:]))

  # The first term in the Fibonacci sequence to contain one thousand digits is
  # 4782. Found in 0.0352318286896 seconds
