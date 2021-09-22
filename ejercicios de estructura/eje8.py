import os
print("""Producto mediante una suma""")
a = int(input("digite el primer numero: "))
b = int(input("digite el segundo numero: "))
producto = int(0)
while b != 0:
    producto = producto + a
    b = b - 1
print(" el resultados de estos dos es : ", producto)

os.system("pause")
