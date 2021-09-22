print("""Ordenar matriz""")

A=[[1,0,0],[7,3,0],[20,7,77]]
vec=[0,0,0,0,0,0,0,0,0]
c=int(0)

for i in range(0,3):
    for j in range(0,3):
        vec[c]= A[i][j]
        c=c+1
band = False
while(band ==False):
    band = True
    for i in range(0,8):
        if (vec[i] > vec[i+1]):
            aux = vec[i]
            vec[i]= vec[i+1]
            vec[i+1]= aux
            band =False
C=0
for i in range(0,3):
    for j in range(0,3):
        A[i][j] = vec[c]
        c= c +1
for i in range(0,3):
    for j in range(0,3):
        print(str(A[i][j]) + "\t")