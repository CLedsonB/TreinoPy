num = int(input())
nomes = []
completo = ""

for i in range(num):
    nome = input()
    quant = []
    quant.extend(nome.split())
    for i in range(len(quant)):
        if  i == len(quant)-1:
            completo += quant[i].capitalize() + "\n"
        else:
            completo += quant[i][0].capitalize() + ". "

print(completo)
