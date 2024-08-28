n = int(input())
cont = 0
amigo = {}

for i in range(n):
    nome,peso = input().split()
    amigo[nome] = int(peso)

c = int(input())

for v in amigo.values():
    if v > c:
        cont += 1

if cont > 0:
    print("Vamos virar almoço de aranhas gigantes!")
    for k,v in amigo.items():
        if v > c:
            print(k)
else:
    print("Vamos todos encontrar a montanha!")