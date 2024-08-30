pontos = []
aux = []

fase = int(input())
aux.extend(input().split())
pontos = list(map(int,aux))
vida = int(input())

salve = vida
    
for i in pontos:
    if i == 0:
        continue
    elif i == 1:
        vida = salve
    elif i >= 2:
        vida -= i
        if vida < 1:
            vida = 0
            break

if vida > 0:
    print("Yes, you can")
else:
    print("You Died")
    