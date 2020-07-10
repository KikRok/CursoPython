import sys #importamos la clase sys para poder usar la funcion que devuelve informaación de la excepción

def main():
    try:
        #Dentro del try informamos el código que podria dar una excepción y que queremos controlar
        x=int('foo')

        #Para probar el exept:
        #    x = 0
        #    r2 = 5/0
    except ValueError: #Se crea lo que se debe hacer si se genera una excepción de este tipo
        print ('Catch de un error del tipo ValueError')
        x = 0
    except: #Si no se informa el tipo, las recoge todas
        print ('Error desconocido.')
        print (sys.exc_info()[1]) #Información de la excepción. el argumento 1 es el typo. Se puede usar sin,. y muestra todo
        print (sys.exc_info())
    else:
        print (x) 

    try:
        r = 10 / x
    except ZeroDivisionError:
        print ('No se puede divir por 0')
        x = 1
        r = 10 / x    
    else: #Entra en el else si no se ha dado ninguna excepción
        print ('División OK: ' + r)


    raise TypeError('Prueba de generar excepción!') # La función raise levanta una excepción forzada


if __name__ == '__main__': main()