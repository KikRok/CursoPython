#
# Example file for working with filesystem shell methods
#
import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile


def main():
  # make a duplicate of an existing file
  if path.exists("file2.txt"):
    # get the path to the file in the current directory
    source = path.realpath("file2.txt")
    
    # let's make a backup copy by appending "bak" to the name
    destino = source + ".bak"
    
    # copy over the permissions, modification times, and other info
    shutil.copy(source,destino)
    shutil.copystat(source,destino)

    # rename the original file
    #os.rename("file.txt", "file2.txt")
    
    # now put things into a ZIP archive
    root_dir, tail = path.split(source)
    shutil.make_archive("archive","zip",root_dir)


    # more fine-grained control over ZIP files
    with ZipFile("testZip.zip", "w") as newzip:
      newzip.write("file2.txt")
      newzip.write("file2.txt.bak")
      
if __name__ == "__main__":
  main()
