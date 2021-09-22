print("""Buscar si se encuentra en el conjunto""")
conjunto=set()

for i in range (1,6):
    print ('',i)
    un_conju = (input ("digite el valor: "))
    conjunto.add(un_conju)
busc= input("digite que desea saber de ese conjunto :")
print(busc in conjunto)
print(conjunto)