import os
print("""realizar suam y producto de 30 numeros""")
sumatoria = 0
producto = 1
for i in range(1, 31):
    print(i)
    sumatoria = sumatoria+i
    producto = producto*i
print ("resultado de la suma: ", sumatoria)
print ("resultado del producto: ", producto)
os.system("pause")