print("""CONVERSOR DE DECIMAL A BI-OC-HEX""")
num=int(input("digite el numero a convertir: "))
print("""
1. Binario
2. Octal
3. Hexadecimal
""")
opc=(int(input("elija porfavor : ")))
if opc == 1:
    binario =bin(num) 
    print("el resultado  es:", binario)
elif opc == 2:
    octal =oct(num) 
    print("el resultado  es:", octal)
elif opc == 3:
    hexa=hex(num) 
    print("el resultado  es:", hexa)
else:
    print("------no existe dicha conversion ")