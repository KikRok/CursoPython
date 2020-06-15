print ("Hello World!")
print ("I'm Kike, and this is my first Python program")

print (2+2)
n = 2+2

if n+1 > 4:
    z = 112 # z se define dentro del if pero se puede usar fuera
    print ('2+2+1 es mayor que 4') #Todo el codigo se basa en la indentación
else:
    print ('2+2+1 no es mayor que 4')
    print ('Dentro del else')
print ('Fuera del if-else')

print ('z is {}'.format(z)) # se usa fuera del if la variable definida en dentro del if