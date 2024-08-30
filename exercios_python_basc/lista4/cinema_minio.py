c,l = input().split()
mat = []
cont = 0

c = int(c)
l = int(l)

for i in range(c):
    aux = []
    aux.extend(input().split())
    linha = list(map(int,aux))
    mat.append(linha)

for i in range(c):
    for j in range(l):
        if (mat[i][j] == 0) and j+2 <= len(mat[0]):
            print("Fileira: %i" %(i+1))
            print("Assentos: %i e %i" %(j+1, j+2))