print("""numeros primos de una Lista""")
def primo(num):
	cont=0;
	
	for i in range(1,num):
		if(num%i==0):
			
			cont+=1
			if cont>1:
				return False
	return True
 
lista=[5,2,3,4,11,6,7,8,9,10]

for i in lista:
	if primo(i):
		print ("El valor ",i," es primo")
	else:
		print ("El valor ",i," NO es primo")
	