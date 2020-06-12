t = int(input())
cadenas = []
for i in range (0,t):
    c = input()
    cadenas.append(c)  

for i in range (0,t):
    pares = []
    impares = []
    print (cadenas[i])
    s = list(cadenas[i])
    y=0

    for x in s: #x tiene directamene los valores de cada elemento de s
        if (y%2==0):
            pares.append(x)
        else:
            impares.append(x)
        y = y+1
    
    print (pares , ' ' , impares)
    str1=""
    str2=""
    print (str1.join(pares), " ", str2.join(impares))