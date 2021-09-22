while True:
    numero = int(input("digita el numero : "))
    ffin = input("¿continuar si y solos si? cn=no y cs= si : ")
    if (ffin == "cs"):
     producto = 1
     m = producto * numero
     print("valor de producto : ", m)

    elif (ffin == "f"):
        break

print("-----termino proceso-----")