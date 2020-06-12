import math
import os
import random
import re
import sys

con = 0

def convertBin(i): #Convierte el numero a binario
    return (bin(i)[2:]) #Devuelve a partir de la posición 2. Las 2 primeras indican la base

def contar1seguidos(n): #Se tiene que quedar con el máximo de 1 seguidos
    l = []
    l = list(n)
    c = 0

    global con #para indicar que use la variable global
    #print ('Con:',con)

    #print (len(l))

    for i in range (0,len(l)-1):
        #print ('l de i=', l[i])
        #print ('l de i+1', l[i+1])
        if ((int(l[i])==1)):
            if (c==0):
                c=1
        if ((int(l[i])==1) and (int(l[i+1])==1)):
            c+=1 #Acumulando 1
        if ((int(l[i])==0)): #cortar el bucle cuando encuentra un 0
            if (con == 0):
                con = c
            else:
                if (c > con):
                    con = c
                    #Si no, se queda con el valor actual de con
            break
    #print (len(l))
    if (con == 0):
        con = c
    else:
        if (c > con):
    #        print ('asigna con como c')
            con = c
    if (len(l)>1):
        if (i >= len(l)):
            if (con == 0):
                con = c
            else:
                if (c > con):
    #                print ('asigna con como c')
                    con = c
            return (con)
        else:
            if (i==0):
                i+=1
            return (contar1seguidos(l[i:]))
    else:
        return (con)

if __name__ == '__main__':
    #Probar con 439
    n = int(input())
    print ('Numero en binario:', convertBin(n))
    b = convertBin(n)
    print ('resultado:', contar1seguidos(b))
    #print (con)

    #Otra forma de hacerlo... Mucho mas simple y eficiente.
    # Utilizando los metdos split y count
    l2 = []
    l2 = list(b)
    print ('Count:', l2.count('1')) #metodo count cuenta cantas veces se repite un valor en una lista
    l3 = b.split('0')
    print (l3)
    c = 0
    for i in l3:
        if ((c==0) or (c<i.count('1'))):
            c=i.count('1')
    print ('c:',c)