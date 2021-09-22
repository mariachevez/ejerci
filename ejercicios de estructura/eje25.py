print("""Almacenar 20 numeros en una lista y mostrar el mayor""")
lista=[]
for i in range (1, 21):
    print ('Numero',i)
    
    un_numero = int(input ("digite un valor para numero: "))
    lista.append(un_numero)
print(lista)
a=max(lista)
print("el indice del numero mayor esta en el indice:",lista.index(a))