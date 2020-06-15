def nombreFunc(n=1): #la funcion se define con def nombre (atributos que recibe)
    print (n)           # en este caso, el n=1, es por si llaman a la funcion sin pasar un valor.

nombreFunc(100)

print () #imprime linea en blanco

#Funcion para calcular si un numero dado es primo o no
def esPrimo(n):
    if n<=1:
        return False #Un return para la funcion directamente. Sale de ella
    for x in range(2, n):
        if n%x == 0: # % es un perador que devuelve el resto de la división
            return False
        else:
            return True

n=5
if esPrimo(n): #directamente evalua el retorno de true/false de la funcion
    print('El numero {} es primo'.format(n))
else:
    print('El numero {} no es primo'.format(n))


def listaPrimos():
    for n in range (100): #range indica desde hasta. En este caso solo el hasta, por lo que el desde es 0
        if esPrimo(n): #invoca la fncion anterior
            print (n, end=' ', flush=True) #en end i flush son para mostrar los valores sin salto de linea, separados por espacio    
listaPrimos() #Invoca a la función (en este caso, sin parametros)