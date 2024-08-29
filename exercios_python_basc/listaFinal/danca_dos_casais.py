n = int(input())
aux = []
homens = []
mulheres = []

aux.extend(input().split())
homens = list(map(int,aux))

aux = []

aux.extend(input().split())
mulheres = list(map(int,aux))

homens.sort(reverse=True)
mulheres.sort()

for i in range(n):
    print(homens[i], mulheres[i])
