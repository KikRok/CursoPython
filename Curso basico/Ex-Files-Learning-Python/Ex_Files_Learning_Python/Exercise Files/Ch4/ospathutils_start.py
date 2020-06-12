#
# Example file for working with os.path module
#
import os
from os import path
import datetime
from datetime import date, time, timedelta
import time
from datetime import datetime


def main():
  # Print the name of the OS
  print(os.name)

  # Check for item existence and type
  print (path.exists("file.txt"))
  print (path.isfile("file.txt"))
  print (path.isdir("file.txt"))
  
  # Work with file paths
  print (path.realpath("file.txt"))
  print (path.split(path.realpath("file.txt")))
  # Get the modification time
  t = time.ctime(path.getatime("file.txt"))
  print (t)
  print (datetime.fromtimestamp(path.getmtime("file.txt")))
  
  # Calculate how long ago the item was modified
  td = datetime.now() - datetime.fromtimestamp(path.getmtime("file.txt"))
  print (td)



  
if __name__ == "__main__":
  main()
