def main():
    #####   Listas. #####
    #Se definen con [] separados por ,
    game = ['Piedra', 'Papel', 'Tijeras']
    print_list(game)

    i = game.index('Papel') #La función index, devuelve el valor donde se encuentra el elemento indicado.
    print (i)

    game.append('Lagarto') #append: Inserta al final de la lista
    print_list(game)
    i = game.index('Lagarto')
    print (i)

    game.insert(3,'Spock') #insert: Inserta en la posición de indice que le indicas. Mueve el resto
    print_list(game)
    i = game.index('Lagarto')
    print (i)

    game.append('Roser')
    print_list(game)
    game.remove('Roser') #Elimina por valor
    print_list(game)

    game.append('Kike')
    print_list(game)
    eliminado = game.pop() #elimina el ultimo valor de la lista. Lo devuelve.

    eliminado2 = game.pop(3) #También elimina por indice
    print_list(game)
    print(eliminado)
    print(eliminado2)

    game.append('Spock')

    #####  Tuplas #####
    #Se definen con () separados por ,
    #Tupla: Es lo mismo que una lista, pero los elementos son inmutables.
    # Muchas de las funciones valen igual
    gameT = ('Piedra2', 'Papel2', 'Tijeras2')
    print_list(gameT) #Por ejemplo, se puede recorrer igual y imprimir igual
    #pero no se puede hacer append, remove, insert, etc...
def print_list(l):
    for i in l:
        print (i, end=' ', flush=True)
    print ()
    print (', '.join(l)) #join, junta los elementos.
    print (len(l)) #len: numero de elementos de la lista



def diccionarios():
    ##### Diccionarios #####
    # Se definen con {}, indicando clave : valor, y separando por ,
    animales = {'Bou':'Muuuuuu', 'Caball':'Hiiiiiii', 'Anec':'Kuaaaak', 'Gos':'Guauuuuuu',
        'Gall':'Kikiriki'}
    # También se pueden crear indicando dict(gato='miau', perro='guau')
    # Las claves pueden ser numeros, y los valores también
    print_dic(animales)
    print (f'La función items devuelve esto: {animales.items()}')

    print (animales['Gos']) #Devuelve el valor de la clave indicada. Guau
    animales['Gos'] = 'Bup'

    animales['Gallina'] = 'PopopopoPo' #Añade un nuevo valor con su clave
    print_dic(animales)

    esta = 'lion' in animales #in, busca el valor en el diccionario. Devuelve true o false
    print (esta)

    # print (animales['lion']) #Peta xq no existe
    # para ver primero si existe, se puede usar el get
    buscar = animales.get('lion')
    print (buscar)
    if buscar == None: #Si no existe, devuelve None
        print ('No esta. Lo añado')
        animales['lion'] = 'Grrrrrr'
    else:
        print (animales['lion'])
    print_dic(animales)
def print_dic(d):
    for x in d:
        print (f'{x}: {d[x]}') #f de format
        #x: contiene la clave
        #d[x]: d contiene los valores. Muestra segun la clave que le pasas: x

    for k,v in d.items(): #otra forma de recorrerlo. k=key, v=value
        print (k, v)
    
    for v in d.values(): print(v) #imprime solo los valores



def sets():
    ##### Set #####
    # Lista de elementos de una fuente que no permite duplicados
    # Se definen con set(), indicando el valor
    a = set('Kike,Roser,Iona') #guarda un conjunto de valores unicos, ordenados
    print_set(a)
    b = set('Mi nabo saca suco') 
    print_set(sorted(b))

    c = a - b #c contiene los elementos que estan en a, pero no en b
    print_set(c)

    d = a and b #Los que estan en los 2. Se puede usar OR, xor, etc...
    print_set(d)

    f=[201901,201902,201903,201905,201901,201910,201905]
    f2 = set(f) #se puede hacer lo mismo con listas, mientras se pase solo un objeto.
    print_set(f2)
def print_set(s):
    for x in s:
        print (x, end = ' ') #en end indica que despues de cara print, mete un espacio en vez del default, que es un salto de linea
    print()



def list_compehension():
    ##### list (comprhension) #####
    # Lista de listas. Se crean definiendo una lista [ con logica dentro ]
    seq = range(11)
    print (type(seq))
    print_list2(seq)

    seq2 = [x * 2 for x in seq] #creamos una lista, desde la lista anterior, multiplicando por 2 los elementos
                                # se recorre la primera lista en la propia definición                                
    print_list2(seq2)

    seq3 = [y for y in seq if y % 3 != 0] #Crea la lista seq3 recorriendo seq con y, y solo guardando el valor si al dividir entre 3 no da 0
    print_list2(seq3)
def print_list2(l):
    for i in l:
        print (i, end=' ', flush=True)
    print ()

if __name__ == '__main__': 
    #Notas: Todas las estructuras pueden contener elementos de diferente tipo, incluso listas de listas
    # se puede usar la funcion isinstance para evaliar si que hay dentro
    # if isintance (objeto, tipo): haz esto -> if isintance (o, list):

    #main() # listas y tuplas
    #diccionarios()
    sets()
    #list_compehension()