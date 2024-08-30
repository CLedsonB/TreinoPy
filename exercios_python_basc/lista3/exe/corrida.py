n = int(input())
premio = []
cont = 0

for i in range(n):
    premio.append(int(input()))

for i in range(n):
    if premio[i] % 3 == 0:
        premio[i] += 50
        cont += premio[i]
    else:
        premio[i] /= 2
        cont += premio[i]

print(cont)
    