print ('Hello World!'.upper()) #pasa a mayusculas
print ('Hello World!'.swapcase()) #Invierte mayusculas y minusculas
print ('Hello World!'.capitalize()) #Pone la primera en mayusculas
print ('Hello World!'.title()) #Pone la primera LETRA DE CADA PALABRA en mayusculas

print ('Multiplico en un string: {}'.format(42 * 7)) #Para concatenar string con algo

print ("""
        String muy larga
        de varias lineas
        Que quiero que se muestren como pongo aqui...
                PimPam""") #Triple """ para printar como queremos


s = 'Kike {}'
print(s.format(69))


s2 = 'KiKe'
s3 = s2.upper() #Cuando se aplican metodos, crea objetos nuevos con diferentes id
print (id(s2))
print (id(s3))

print (s2 + ' ' + s3) #concatenar strings

s4 = 'Kike' ' Roser' #Asi lo concatena solo
print (s4)

x = 42
print ('Número es {}'.format(x))
y = 73
print ('Los números son {} y {}'.format(x, y))
print ('Los números son {ind1} y {ind2}'.format(ind1=x, ind2=y)) #Lo mismo asignando una clave al formato
print ('Los números son {0} y {1}. Vuelvo a la ocurrencia 0: {0}'.format(x, y)) #Tambien se puede pasar como los indices
print ('Los números son {0:<5} y {1:>05}'.format(x, y)) #formateo del campo, añadiendo espacios para complertar hasta 5 valores. Con el :>05 rellena xon 0 a la izquierda hasta llegar a 5 valores.
print ('Los números son {0:} y {1:+05}'.format(x, y)) #formateo del campo con signo
print ('El numero en hezadecimal: {:x}'.format(x)) #:x muestra en hexadecimal. :o en octal. :b en binario

#A partir de la version 3.6 de Python el format también se puede hacer asi:
print (f'The number is {x:b}')


#Slits y Joins
s5 = 'Esto es un string muy laargo con palabras separadas'
print (s5)
print (s5.split()) #separa por espacios en una lista
print (type(s5.split())) 

print (s5.split('i')) #separa por el caracter  i (es el separador) en una lista

l = s5.split()
print (l)
s6 = ':'.join(l) #junta todos los elementos de la lista (l), usando ':' como concatenador
print (s6)