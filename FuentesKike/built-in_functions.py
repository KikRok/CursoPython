#Built-in functions, son funciones ya disponibles en puthon de forma intrinseca, para
#hacer cosas que podriamos necesitar.
# ver la documentación en la web de python.


x = '47'
y = int(x)
z = float(x)
w = abs(-y)

d = divmod(y,3) #devuelve una tupla de 15 (3 veces), con un remainder de 2. Hay mucha docu de las built-un functions.

print(f'x is {type(x)}')
print(f'x is {x}')
print(f'y is {type(y)}')
print(f'y is {y}')
print(f'z is {type(z)}')
print(f'z is {z}')
print(f'w is {type(w)}')
print(f'w is {w}')

print(f'd is {type(d)}')
print(f'd is {d}')



s='Hello, World.'
print (repr(s)) #enseña la mejor representación del objeto que se le pasa. Intespreta el objeto y sabe como lo debe presentar

