"""# Project Euler problem 19
# https://projecteuler.net/problem=19

You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""



DAYS_OF_WEEK = {
  0: "sunday",
  1: "monday",
  2: "tuesday",
  3: "wednesday",
  4: "thursday",
  5: "friday",
  6: "saturday"
}

months = {
  1: 31,
  2: 28,
  3: 31,
  4: 30,
  5: 31,
  6: 30,
  7: 31,
  8: 31,
  9: 30,
  10: 31,
  11: 30,
  12: 31
}

day_of_week = 1
sundays = 0

for year in range(1901, 2001):
  for month in range(1, 13):
    #if month == 2 and not (year % 4):
    if month == 2 and not year % 4 and (year % 100 or not year % 400):
      m_days = 29
    else:
      m_days = months[month]
    for day in range(1, m_days + 1):
      if day == 1 and day_of_week == 6:
        sundays += 1
      if day_of_week == 6:
        day_of_week = 0
      else:
        day_of_week += 1

print ("The first of the month was a sunday %s times between January 1, 1901 "
       "and December 31, 2000" % sundays)

# The first of the month was a sunday 171 times between January 1, 1901 and
# December 31, 2000