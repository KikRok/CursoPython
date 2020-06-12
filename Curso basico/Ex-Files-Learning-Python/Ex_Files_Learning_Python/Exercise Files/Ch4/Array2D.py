import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []
    s1 = []
    #input
    s1.append("1 1 1 0 0 0")
    s1.append("0 1 0 0 0 0")
    s1.append("1 1 1 0 0 0")
    s1.append("0 0 2 4 4 0")
    s1.append("0 0 0 2 0 0")
    s1.append("0 0 1 2 4 0")
    # expeted output 19

    s2 = []
    s2.append("-1 -1 0 -9 -2 -2")
    s2.append("-2 -1 -6 -8 -2 -5")
    s2.append("-1 -1 -1 -2 -3 -4")
    s2.append("-1 -9 -2 -4 -4 -5")
    s2.append("-7 -3 -3 -2 -9 -9")
    s2.append("-1 -3 -1 -2 -4 -5")
    # expected orutput -6

    s3=[]
    s3.append("-1 1 -1 0 0 0")
    s3.append("0 -1 0 0 0 0")
    s3.append("-1 -1 -1 0 0 0")
    s3.append("0 -9 2 -4 -4 0")
    s3.append("-7 0 0 -2 0 0")
    s3.append("0 0 -1 -2 -4 0")
    # Expected output 0

    for i in range(6):
        arr.append(list(map(int, s3[i].rstrip().split())))

    #print(arr)
    #print (arr[1][1])

    x = 0
    y = 0
    max = 5
    reloj = 0
    rmax = 0
    modificado = 0
    for li in arr:
        for nu in li:
            #print (nu)
            if (y+2 > max) or (x+2 > max):
                break
            else:
                reloj = arr[x][y] + arr[x][y+1] + arr[x][y+2]
                reloj += arr[x+1][y+1]
                reloj += arr [x+2][y] + arr[x+2][y+1] + arr[x+2][y+2]   
            if reloj > rmax or (rmax==0 and modificado == 0):
                rmax = reloj
                modificado = 1
            reloj = 0
            y+=1
        x+=1
        y=0
        #print (li)

    print (rmax)
