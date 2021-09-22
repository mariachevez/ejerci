import os
print("""conozcamos la  tabla de multiplicacion """)
numero = int(input("porfavor ingresar el numero de la tabla que desea saber : "))
for i in range(1, 11):
    resultado = i * numero
    print(numero, "x", i, "=", resultado)
os.system("pause")