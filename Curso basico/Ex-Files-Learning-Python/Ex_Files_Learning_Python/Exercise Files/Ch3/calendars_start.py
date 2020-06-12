#
# Example file for working with Calendars
#

# import the calendar module
import calendar


# create a plain text calendar
c = calendar.TextCalendar(calendar.MONDAY)
st=c.formatmonth(2020, 1, 0, 0)
print (st)

# create an HTML formatted calendar
hc = calendar.HTMLCalendar(calendar.MONDAY)
sc = hc.formatmonth(2020,1)
print (sc)

# loop over the days of a month
# zeroes mean that the day of the week is in an overlapping month
for i in c.itermonthdays(2017, 8):
    print (i)
  
# The Calendar module provides useful utilities for the given locale,
# such as the names of days and months in both full and abbreviated forms
for name in calendar.month_name:
    print (name)
for day in calendar.day_name:
    print (day)

# Calculate days based on a rule: For example, consider
# a team meeting on the first Friday of every month.
# To figure out what days that would be for each month,
# we can use this script:
for m in range(1,13):
    cal = calendar.monthcalendar(2020,m)
    w1=cal[0]
    w2=cal[1]
    if w1[calendar.FRIDAY] != 0:
        meetday = w1[calendar.FRIDAY]
    else:
        meetday = w2[calendar.FRIDAY]
    print ("%10s %2d" % (calendar.month_name[m], meetday))