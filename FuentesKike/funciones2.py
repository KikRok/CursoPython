def main():
    kitten() #llama a kitten
    print (kit2(5)) #llama a kit2 pasando un valor

def kitten(): #Esta función no devuelve nada. Solo hace cosas
    print ('Miau')  #Devolveria un none
def kit2(n): #Esta funcion recibe una variable, y tambien devuelve algo.
    x=[]
    for i in range(n):
        x.append(i)
    return x

#funcion con valres default
def pedo (a='pff', b='pppp', c='brrrrf'): #Si definimos valores default no hace falta pasar todos
                                          # pero se debe poner defaults empezando por la derecha.
    print (a,b,c)    

#funcion con una lista de argumentos variable (tupla)
def valores_var(*argumentos): #crea una clase tuple
    print (type(argumentos))
    if len(argumentos):
        for s in argumentos:
            print (s)
    else: print ("sin argumentos")
#funcion con una lista de argumentos variable (diccionario)
def valores_var2(**kwargs): #crea una clase diccionario. 2* para diccionarios
    print (type(kwargs))
    if len(kwargs):
        for s in kwargs:
            print (s, kwargs[s]) #clave , valor
    else: print ("sin argumentos")


if __name__ == '__main__': main() #invoca el main

pedo('pff','pppp') # Si la llamamos pasando solo 2 argumentos, peta.
# pero si en la propia funcion se inicializan los valores cuando se crea, entonces no peta
print()

#La misma funcion con diferentes argumentos
valores_var('pff','pppp')
print()
valores_var('pff','pppp','pff2','pppp2','pff3','pppp3')

#funcion que recibe diccionario con argumentos variables
valores_var2(pedo1='pff',pedo2='pppp')
print()