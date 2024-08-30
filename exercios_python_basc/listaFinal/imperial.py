x = []
y = []
porc = []
aux = []

n = int(input())

aux.extend(input().split())
x = list(map(int,aux))

aux = []

aux.extend(input().split())
y = list(map(int,aux))

for i in range(n):
    if y[i] == 0 or x[i] == 0:
        ax = 0
    else:
        ax = (y[i]/x[i]) * 100

    porc.append(int(ax))

print(*porc)