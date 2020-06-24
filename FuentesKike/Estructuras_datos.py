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



if __name__ == '__main__': 
    #main()
    diccionarios()