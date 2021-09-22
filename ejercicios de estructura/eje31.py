print("""Almacenar 20 numeros y ponerlos en orden""")
lista=[]
for i in range (1, 21):
    print ('Numero',i)
    un_numero = int(input ("digite un valor de un numero: "))
    lista.append(un_numero)
    
orden=lista.sort()
print(lista)