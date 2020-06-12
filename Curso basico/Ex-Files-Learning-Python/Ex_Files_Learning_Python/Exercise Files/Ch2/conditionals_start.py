#
# Example file for working with conditional statements
#

def main():
  x, y = 100, 1000
  
  # conditional flow uses if, elif, else  
  if (x < y):
    st="x is less than y"
  elif (x==y):
    st="y is equal x"
  else:
    st="y is less than x"

  print (st)

  # conditional statements let you use "a if C else b"
  st = "x is less than y" if (x<y) else "x is more or equal to Y"
  print (st)

if __name__ == "__main__":
  main()
