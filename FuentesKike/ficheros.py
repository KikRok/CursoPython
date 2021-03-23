def main():
    f = open('lines.txt') #abre el fichero. Devielve un objeto file (f). Como argumentos adicionales, se informa el modo de apertura.
                            # por defecto se abre como lectura: f = open('lines.txt','r').
                            # escritura: f = open('lines.txt','w'). Si existe, machaca, si no, lo crea
                            # append: f = open('lines.txt','a'). Si existe añade, si no, lo crea
                            # casos especiales: f = open('lines.txt','r+b'). indica que es binary
                            #                   f = open('lines.txt','r+T'). indica que es TEXTO. Default
    for line in f: #se puede recorrer el obteto linea a linea
        print(line.rstrip()) #imprime el contenido

def copiar_ficheros_texto():
    infile = open('lines.txt', 'rt') #abro en modo lectura y modo texto
    outfile = open ('lines_copy.txt', 'wt') #creación de nuevo fichero. Modo escritura y modo texto

    for line in infile: #loop para leer cada linea del fichero
        print(line.rstrip(), file = outfile) #rstrip es para leer linea a linea. Rompe por cada salto de linea. printa en donde le indicamos en el file
        # outfile.writelines(line) -> hace lo mismo que lo anterior
        print ('.',end='',flush=True) # printa un punto por cada linea del fichero + flush limpia el buffer
    outfile.close()
    print ('\ndone.') 

def copiar_ficheros_binarios():
    infile = open('berlin.jpg', 'rb') #abro en modo lectura y modo binario. Ojo es una imagen!
    outfile = open ('berlin_copy.jpg', 'wb') #creación de nuevo fichero. Modo escritura y modo binario
    while True: # el loop se ira ejecutando siempre, hasta que encuentre un break.
        buf = infile.read(10240) #llenamos el buffer con 10kb. aqui se usa read(). Ojo, esto afecta a la memoria reservada para ejecutar el programa.
        if buf: # si hay algo en buf, se ejecuta
            outfile.write(buf) #excribimos a salida con la opcion write(). Write para binario.
            print ('.',end='',flush=True) # printa un punto por cada 10kb copiados +end ='' para que no haga salto de linea + flush limpia el buffer
        else: break #cuando ya no hay nada en el buffer (lectura del ortiginal). forzamos la salida del bucle.
    outfile.close()
    print ('\ndone.') 

if __name__ == '__main__': 
    #main() #simple lectura
    #copiar_ficheros_texto()
    copiar_ficheros_binarios() #copia de una imagen
    # Prueba Git VDI