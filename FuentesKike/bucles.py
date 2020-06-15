# while -> Haz esto mientras se cumpla una condicion
words = ['one','two','three','four','five']

n=0
while (n<5): #entra mientras n sea menor que 5
    print (words[n])
    n+=1 # incrementa 1 a n

#for
for i in words: #i se convierte en un puntero que apunta a cada uno de los elemntos de la lista
    print(i)