num = int(input())
nomes = []

for i in range(num):
    nome = input()
    j = 0
    for palavra in nome.split(" "):
        if j == len(nome.split(" ")):
            nomes.append(palavra[i].capitalize())
        else:
            nomes.append(palavra[i].capitalize() + ". ")
        j += 1

for nome in nomes:
    print(nome)


