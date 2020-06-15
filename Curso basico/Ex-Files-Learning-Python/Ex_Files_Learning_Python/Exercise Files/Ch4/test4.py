n=18
if (n%2!=0):
    print ("Weird")
else:
    if (n>=2) and (n<=5):
        print ("Not Weird")
    else:
        if (n<=20) and (n!=1):
            print ("Weird")
        else:
            print ("Not Weird")

i = 4
d = 4.0
s = 'HackerRank '
# Declare second integer, double, and String variables.
i2= 2
d2=input()
s2=input()
# Read and save an integer, double, and String to your variables.
# Print the sum of both integer variables on a new line.
print (i+int(i2))
# Print the sum of the double variables on a new line.
print (d+float(d2))
# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first.
print (str(s) + str(s2))