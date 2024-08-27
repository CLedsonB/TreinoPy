num = int(input())
hab = [0]*num
id = [0]*num
aux = []
ids = ""
cont = 0

aux.extend(input().split())
hab = list(map(int,aux))

aux = []
aux.extend(input().split())
id = list(map(int,aux))

y = int(input())

for i in range(num):
    if y == hab[i]:
        ids += str(id[i]) + " "
        cont += 1

if cont == 0:
    print("Nenhum")
else:
    print(ids)
