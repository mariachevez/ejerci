for i in (1,2):
    matriz=int(input("ingrese:[i ,j]: "))
for j in (2,2):
    matriz=int(input("ingrese:[i ,j]: "))
mayor=0
posicion_mayor_i=0
posicion_mayor_i=0
for i in range (2):
    for i in range (2):
        if matriz >mayor:
            mayor = matriz
            posicion_mayor_i=i
            posicion_mayor_j=j
print("el mayor: ", mayor,"la posiscion de el es:",posicion_mayor_i,"-",posicion_mayor_j)