print("""suma de 30 numeros pero solo los pares""")
suma = 0

for i in range (1,31):
    print ("Numero" ,i)
    un_numero = int (input ("digite porfavor el valor de un numero: "))
    if un_numero%2==0:
        suma=suma+un_numero
    print ()
print ("Valor de suma: ", suma)