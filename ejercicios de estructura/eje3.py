import os
print("""veamos el numero mayor """)
a = float(input("digite el primer numero: "))
b = float(input("digite el segundo nombre: "))
if a > b:
    mayor = a
else:
    mayor = b
print("el mayor seria : ", mayor)
os.system("pause")