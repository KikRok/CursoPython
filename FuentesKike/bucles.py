words = ['one','two','three','four','five']

# while -> Haz esto mientras se cumpla una condicion
n=0
while (n<5): #entra mientras n sea menor que 5
    print (words[n])
    n+=1 # incrementa 1 a n

secret = 'despwd'
pw =''
i=0
while pw != secret:
    pw = input("Enter the password: ")
    if pw=='R': #Si se mete una R, no suma al contador.
        continue #Finaliza esta repetición del bucle desde aqui. No hace lo de detras. También sirve para el bucle for
    else:
        i+=1
    if i > 10:
        print ("Acces non garanted")   
        break     #sale del bucle. También vale para el bucle for
    

if i<=10:    
    print ("Acces garanted")


#for
for numero in words: #i se convierte en un puntero que apunta a cada uno de los elemntos de la lista
    print(numero)
for n in range(10): #se crea un objeto rango con 10 valores, empezando por el 0
    print (n)