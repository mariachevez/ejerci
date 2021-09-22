import os
print("""suma de n numeros pares""")

suma = 0
n = int (input ("digite el valor de n: "))
for i in range (1, n +1):
    
    un_numero = int (input ("digite el valor de un numero: "))
    if un_numero%2==0:
        suma=suma+un_numero
    print ()
print ("Valor de suma: ", suma)
os.system ("pause")