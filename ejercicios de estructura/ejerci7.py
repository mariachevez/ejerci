import os

print("""se debe sumar hasta que de resultado nos de un valor negativo""")
suma = 0
while True:
    numero = int(input("digite el numero: "))
    if numero < 0:
        print("-------Fin del proceso-------")
        break
    elif numero > 0:
        suma = suma + numero
        print("respuesta: ", suma)
os.system("pause")