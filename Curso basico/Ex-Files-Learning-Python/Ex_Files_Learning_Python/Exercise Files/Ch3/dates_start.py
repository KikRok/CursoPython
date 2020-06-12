#
# Example file for working with date information
#
from datetime import date
from datetime import time
from datetime import datetime

def main():
  ## DATE OBJECTS
  # Get today's date from the simple today() method from the date class
  today = date.today()
  print ("Today: ", today)

  # print out the date's individual components
  print ("DAte componentes: ", today.year, today.month, today.day)
  
  # retrieve today's weekday (0=Monday, 6=Sunday)
  print ("today is week day number: " , today.weekday())
  days=["Mon","Tue","Wed","Thu","Fri","Sat","San"]
  print ("Which is a:", days[today.weekday()])

  ## DATETIME OBJECTS
  # Get today's date from the datetime class
  today = datetime.now()
  print (today)

  # Get the current time
  t = datetime.time(datetime.now())
  print (t)

  
if __name__ == "__main__":
  main();
  