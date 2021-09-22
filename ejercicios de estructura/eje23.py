print("""Suma de numeros pares""")
n = int (input ("digite un valor para n: "))
for i in range (1, n + 1):
    un_numero = float (input ("digite un valor para numero: "))
    if i==1 or un_numero<mayor:
        mayor=un_numero
print ("respuesta : ",mayor)