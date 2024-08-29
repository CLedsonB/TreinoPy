n = int(input())
aux = []
i = []
r = []

for z in range(n):
    n1,n2 = input().split()
    i.append(int(n1))
    r.append(int(n2))

reserva = r
r.sort(reverse=True)


for z in range(n):
    print(i[reserva.index(r[z])], r[z])



#  print(f'{id[nota.index(lista[i])]} Sim')