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

p = int(input())

for i in range(c):
    for j in range(l):
        if mat[i][j] == p:
            cont += 1

print(f'Ash pegou {cont} pokemon')
