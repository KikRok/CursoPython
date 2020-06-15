class Duck:
    sound = 'Kuak'
    walking = 'camina como un pato...'

    def quack(self):
        print('Quaaack!')
        print(self.sound) #Para usar atributos de la propia clase, hay que indicarlo con el self.att

    def walk(self):
        print('Walks like a duck.')
        print(self.walking)

def main():
    donald = Duck() #se crea un el objeto donald de la clase pato
    donald.quack() #podemos usar los metodos que tiene la clase
    donald.walk()

if __name__ == '__main__': main()