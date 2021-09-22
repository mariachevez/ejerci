import os
print("""Division mostrando el cociente""")
a = int(input("digite el primer numero: "))
b = int(input("digite el segundo  valor: "))
cociente=0
while a >= b:
    a = a - b
    cociente = cociente + 1
    break
print (" cociente es: ", cociente)
print (" residuo es: ", a)

os.system("pause")