#
# Example file for working with classes
#
class myClass():
  def method1(self):
    print("myClass method1")
  def method2(self, someString):
    print ("MyClass method2 "+someString)


class anotherClass(myClass):
  def method1(self):
    myClass.method1(self)
    print("another method1")
  def method2(self, someString):
    print ("another method2 "+someString)



def main():
  c = myClass()
  c.method1()
  c.method2("string")

  c2 = anotherClass()
  c2.method1()
  c2.method2

  
if __name__ == "__main__":
  main()