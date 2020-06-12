import calendar

cal = calendar.TextCalendar(calendar.MONDAY)

myCal = cal.formatmonth(2019,6,0,0)
print(myCal)

from datetime import timedelta
from datetime import date

print (timedelta.max)
print (timedelta.min)
print (timedelta.resolution)

def main():
    today = date.today
    print (today)
