import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    arr.reverse() #invierte la lista
    cadena = ""
    for x in arr:
        cadena += str(x)
        cadena += ' '
    
    print (cadena)

    #arr2 = [] #todo esto se hace con un mylist.reverse()...
    #o = n-1

    #for i in range(0,n):
    #    arr2.append(arr[o])
    #    o = o-1

    #print (arr2)

    #for elemento in arr2: #recorre los elementos del array uno por uno
    #    print (elemento)
