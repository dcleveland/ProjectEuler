# Project Eurler problem 9
# https://projecteuler.net/problem=9
max = 20

for a in range(0, 500):
  for b in range(0, 500):
    for c in range(0, 500):
      n += 1
      sys.stdout.write("\rTrial %s of 125000000" % n)
      sys.stdout.flush()
      if a**2 + b**2 == c**2 and a + b + c == 1000:
        print "Found: a=%s, b=%s, c=%s. Product = %s" (a, b, c, a*b*c)