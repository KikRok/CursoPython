# clase maestra
class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

#clase que se crea en base a otra. Indicar padre entre ()
class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    #Hay que crear u constructor con todos los atributos. Incluidos los del padre
    def __init__(self, firstName, lastName, idNumber, scores):
        Person.__init__(self, firstName, lastName, idNumber) #invocamos el constructor del padre
        self.scores = scores
    #   Function Name: calculate
    #   Return: A character denoting the grade.
    def calculate(self): #se rcive a ella misma. Puede usar todos los campos
        listScores = []
        listScores = self.scores
        puntuacion = 0

        for score in listScores:
            puntuacion += score

        media = puntuacion / len(listScores)

        return (self.convertirMedia(media))
    
    def convertirMedia(self, media): #clase auxiliar interna
        if media < 40:
            return 'T'
        elif media < 55:
            return 'D'
        elif media <70:
            return 'P'
        elif media < 80:
            return 'A'
        elif media < 90:
            return 'E'
        else:
            return 'O'

if __name__ == '__main__':
    # Los inputs
    line = input().split()
    firstName = line[0]
    lastName = line[1]
    idNum = line[2]
    numScores = int(input()) # not needed for Python
    scores = list( map(int, input().split()) )

    #definiión del objeto Student en s
    s = Student(firstName, lastName, idNum, scores)

    #invocación del metodo de la clase padre
    s.printPerson()

    #Invocación del metodo de la clase hija
    print("Grade:", s.calculate())