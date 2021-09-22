for i in  (1,2):
    mqtriz =int(input("ingrese la matriz[i,j]: "))
for j in (1,2):
    matriz= int(input("ingrese la matriz[i,j]: "))

mayor=0
menor=1000
posicion_mayor_i=0
posicion_mayor_j=0
posicion_memor_i=0
posicion_memor_j=0
for i in (1,2):
    for j in (1,2):
        if matriz>mayor:
            mayor =matriz
            posicion_mayor_i=i
            posicion_mayor_j=j

        if matriz < menor:
            menor=matriz
            posicion_menor_i=i
            posicion_menor_j=j
print("El mayor : ", mayor,"la posicion de el es:",posicion_mayor_i,"-",posicion_mayor_j)

print("El menor : ", menor,"la posicion de el es:",posicion_menor_i,"-",posicion_menor_j)