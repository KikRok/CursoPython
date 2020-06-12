#
# Example file for working with timedelta objects
#

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

# construct a basic timedelta and print it
x = timedelta(days=365, hours=5, minutes=1)
print (x)
# print today's date
now = datetime.now()
print ("Today: ",now)


# print today's date one year from now
MasUno = now + timedelta(days=365)
print ("Año +1año: ", MasUno)

# create a timedelta that uses more than one argument
MasUnoSem = now + timedelta(days=365, weeks=3)
print ("Año +1año y 3 semanas: ", MasUnoSem)

# calculate the date 1 week ago, formatted as a string
MenosUnaSem = now - timedelta(weeks=1)
s=MenosUnaSem.strftime("%A %B %d, %Y")
print ("HAce una semaa: ", s)

### How many days until April Fools' Day?
today = date.today()
afd = date(today.year, 4, 1)

# use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year
if afd < today:
    print ("La fecha ya ha pasado hace %d dias" %((today-afd).days))
    afd = afd.replace(year = today.year+1)



# Now calculate the amount of time until April Fool's Day  
time_to_afd = afd - today
print ("faltan ", time_to_afd.days)

