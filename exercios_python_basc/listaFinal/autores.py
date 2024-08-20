num = int(input())
nomes = ""

for i in range(num):
    nome = input()
    for j in nome.split():
        j = j[0] + ". "
        nomes += j.capitalize()

        
print(nomes)