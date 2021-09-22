import os

mayor = 0
n = int (input ("cuantos quiere ingresar : "))
print("-----------")
for i in range (1, n + 1):
    un_numero = float (input ("valor de un numero: "))
    if i==1 or mayor<un_numero:
        mayor=un_numero

    print ()
print ("valor del mayor: ",mayor)
os.system ("pause")