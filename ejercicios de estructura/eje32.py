print("""Suma de matrices""")
a=[[1, 2],
   [3, 4]]

b=[[6, 3],
   [5, 2]]

def sumar_matrices(m1,m2):
    if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):
        m3=[]
        for i in range(len(m1)):
            m3.append([])
            for j in range(len(m1[0])):
                m3[i].append(m1[i][j] +m2[i][j])
        return m3
    else:
        return None
c=sumar_matrices(a,b)

if c==None:
    print("lo siento la suma no se puede resolver")
else:
    for fila in c:
        print("[", end=" ")
        for elemento in fila:
            print(elemento, end=" ")
        print("]")