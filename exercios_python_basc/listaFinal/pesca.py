n,t = input().split()
lista = []

n = int(n)
t = int(t)

for i in range(n):
    lista.append(int(input()))

i = 1
while len(lista) >= i:
    t -= lista[i]
    if t <= 0:
        break
    i += 1

print(i)
