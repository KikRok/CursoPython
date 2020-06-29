class Duck:
    sound = 'Kuak' #es un data de la clase, no del objeto. Puede ser mutable y afecta a todos los objetos de la clase.
    walking = 'camina como un pato...' #variable de clase

    def quack(self):
        print('Quaaack!')
        print(self.sound) #Para usar atributos de la propia clase, hay que indicarlo con el self.att

    def walk(self):
        print('Walks like a duck.')
        print(self.walking) #self, hace referencia al objeto

class Animal:
    def __init__(self,type,name,sound): #constructor / inicializador. self es para que apunte al propio objeto
        self._type = type #variable de objeto
        self._name = name
        self._sound = sound
    def type(self): #esto es como un get.
        return self._type
    def name(self):
        return self._name
    def sound(self):
        return self._sound

class Animal2:
    def __init__(self,**kwargs):
        self._type = kwargs['type'] if 'type' in kwargs else 'Animal'
        self._name = kwargs['name'] if 'name' in kwargs else 'NoName'
        self._sound = kwargs['sound'] if 'sound' in kwargs else 'NoSound'

    def type(self, t = None):
        if t: self._type = t
        try: return self._type
        except AttributeError: return None

    def name(self, n = None):
        if n: self._name = n
        try: return self._name
        except AttributeError: return None

    def sound(self, s = None):
        if s: self._sound = s
        try: return self._sound
        except AttributeError: return None

class Perro(Animal2): #hereda de la clase animal 2
    def __init__(self,**kwargs):
        self._type = 'Perro'
        if 'type' in kwargs: del kwargs['type'] #Si llega el tipo informado, borramos y se asigna perro
        super().__init__(**kwargs) #super llama a la clase padre, pasando los mismos parametros que ha recibido

    def __str__(self): #define la representacion del objeto en modo cadena
        return ('Perro: Tipo:{} Nombre: {} Sonido:{}'.format(self.type(),self.name(),self.sound()))

    def morder(self):
        print('Nyaaaam')


class Coche:
    def __init__(self,**kwargs):
        self._color = kwargs['Color'] if 'Color' in kwargs else 'NoColor' #Inicializa si no lo mandan. SE pueden poner otras condiciones.
        self._puertas = kwargs['Puertas'] if 'Puertas' in kwargs else 'NoDoors'
        self._cv = kwargs['CV'] if 'CV' in kwargs else 'NoPotence'

    #geters
    def color(self):
        return self._color
    def puertas(self):
        return self._puertas
    def cv(self):
        return self._cv

class Casa:
    def __init__(self,**kwargs):
        self._metros = kwargs['metros'] if 'metros' in kwargs else 0 
        self._puertas = kwargs['puertas'] if 'puertas' in kwargs else 0
        self._piscina = kwargs['piscina'] if 'piscina' in kwargs else False
        self._gas = kwargs['gas'] if 'gas' in kwargs else False
        self._internet = kwargs['internet'] if 'internet' in kwargs else False

    #geters/seters
    def metros (self,m=None):
        if m: self._metros = m #Si m no es None, es decir, se manda algo, le asigna este valor (seter)
        return self._metros #Si no llega nada, no entra en el if, y es simplemente un geter
    def puertas (self,p=None):
        if p: self._puertas = p
        return self._puertas
    def piscina (self,p=None):
        if p: self._piscina = p
        return self._piscina
    def gas (self,g=None):
        if g: self._gas = g
        return self._gas
    def internet (self,i=None):
        if i: self._internet = i
        return self._internet

    def __str__(self): #define la representacion del objeto en modo cadena
        return ('Caracteristicas de la casa: Metros:{} Puertas: {} Piscina:{} Gas:{} Internet:{}'.format(self.metros(),self.puertas(),self.piscina(),self.gas(),self.internet()))

def print_animal(o):
    if not isinstance(o, Animal):
        raise TypeError ('Se requiere un objeto de la clase Animal')
    print (o.type()) 
    print (o.name())
    print (o.sound())

def printCar(o):
    print ('Caracteristicas del coche: {} {} {}'.format(o.color(), o.puertas(), o.cv()))

def printCasa(o):
    print ('Caracteristicas de la casa: Metros:{} Puertas: {} Piscina:{} Gas:{} Internet:{}'.format(o.metros(),o.puertas(),o.piscina(),o.gas(),o.internet()))

def main():
    donald = Duck() #se crea un el objeto donald de la clase pato
    donald.quack() #podemos usar los metodos que tiene la clase
    print (donald.sound) #también se pu ede usar directamente el atributo
    donald.walk()

    a = Animal('Gato','Bruna','Miau')
    print_animal(a)

    c = Coche(Color='Negro',Puertas=5, CV=95)
    printCar(c)

    c2 = Coche()
    printCar(c2)

    miCasa = Casa(metros=1800,puertas=3,piscina=True,gas=False,internet=True)
    printCasa(miCasa)
    miCasa.gas(True) #Le hace el set a gas
    printCasa(miCasa)
    print(miCasa) #Invoca la función __str__

    Duna = Perro(name='Duna',sound='Bup')
    print (Duna)
    Duna.morder()

if __name__ == '__main__': main()