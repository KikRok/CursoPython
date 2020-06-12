#
# Read and write files using the built-in Python file methods
#

def main():  
  # Open a file for writing and create it if it doesn't exist
  # f = open("file.txt","w+")

  # Open the file for appending text to the end
  # f = open("file.txt","a")

  # write some lines of data to the file
  #for i in range (10):
  #  f.write("Ejemplo: "+ str(i+10)+"\r\n")
  
  # close the file when done
  #f.close()
  
  # Open the file back up and read the contents
  f = open("file.txt","r")
  #if f.mode == 'r':
  #  contents = f.read()
  #  print (contents) #todo el contenido

  fl = f.readlines()
  for l in fl:
    print (l) #linea a linea

if __name__ == "__main__":
  main()
