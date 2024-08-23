num = int(input())
palavras = []
cont = 0

for i in range(num):
    palavras.append(input())

rima = input()

for i in range(num):
    if rima[-3:] == palavras[i][-3:]:
        cont += 1

if cont >= 1:
    print("Sim")
else:
    print("Nao") 