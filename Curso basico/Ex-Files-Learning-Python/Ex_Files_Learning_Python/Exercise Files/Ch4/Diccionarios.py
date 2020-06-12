t = int(input())
diccionario = {}

for i in range (0,t):
    c = input()
    s = c.split()

    diccionario[s[0]] = s[1]

    s.clear()

for i in range (0,t):
    i2 = str(input())
    num = diccionario.get(i2)

    if num == None:
        print ("Not found")
    else:
        print (i2+'='+str(num))

#print (type(s))
#print (type(diccionario))

#print (diccionario)