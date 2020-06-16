#Tipos de variables

st="kike" #string
print(type(st))

st.capitalize() #ejemplo de funcion sobre objetos string
print(st)


b = True #boleano
print(type(b))

l = ['kike',5] #lista
print(type(l))

#para strings de mas de una linea
ml = '''
paco
paquito
'''

print('ml: {}'.format(ml))
print(type(ml))


#Numericos

x = 7 #numerico
print('x is {}'.format(x))
print(type(x))

f = 1.2
print(type(f))

cl = 7/3 #devuelde un float, xq el resultado es un float
print(type(cl))


from decimal import *
a = Decimal ('0.10')
b = Decimal ('0.30')
re = a+a+a-b
print('re: {}'.format(re))
print(type(re))

#boleano
b2 = 7>5
print('b2: {}'.format(b2))
print(type(b2))
#None , 0, o string vacio, equivalen a Falso

#listas
x2 = [1,2,3,4,5,6]
for i in x2:
    print ('i: {}'.format(i))

x3 = list(range(10))
print(type(x3))
for i in x3:
    print ('i: {}'.format(i))
x3[2] = 42 #cambio el valor de la posición 2 de la lista
print()
for i in x3:
    print ('i: {}'.format(i))

#Diccionario
t1 = {'uno':1,'dos':2,'tres':3} 
for k,v in t1.items():
    print ('k: {}, v: {}'.format(k,v))
t1['tres'] = 33 #cambio la asignación del valor de la clave 'tres'
for k,v in t1.items():
    print ('k: {}, v: {}'.format(k,v))

if isinstance(t1,tuple):
    print ('t1 es un tuple')