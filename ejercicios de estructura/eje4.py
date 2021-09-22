import os
print("""revisemos cual es el mayor de los tres """)
a = float(input("digite el primer numero: "))
b = float(input("digite el segundo  numero: "))
c = float(input("digite el tercer numero: "))
mayor = a
if mayor < b:
    mayor = b
if mayor < c:
    mayor = c
print("el mayor seria: ", mayor)
os.system("pause")