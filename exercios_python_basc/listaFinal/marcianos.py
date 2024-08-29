s,n = input().split()
lista = []
aux = []
nota = []
id = []

n = int(n)
s = int(s)

for i in range(n):
    d1,d2 = input().split()
    nota.append(int(d1))
    id.append(int(d2))

c = int(input())
aux.extend(input().split())
lista = list(map(int,aux))

for i in range(len(lista)):
    if nota.index(lista[i]) < 2:
        print(f'{id[nota.index(lista[i])]} Sim')
    else:
        print(f'{id[nota.index(lista[i])]} Nao')