print("""Suma de numeros pares""")
suma=0
n = int (input ("digite un valor para n: "))
for i in range (1, n + 1):
    print ('Numero',i)
    un_numero = int (input ('digite un valor para numero: '))
    if un_numero%2==0:
        suma=suma+un_numero
    print ()
print ('resultado de la suma de ambos numeros : ',suma)