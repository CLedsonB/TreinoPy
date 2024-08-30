partida = 3
totalP = 0
totalL = 0

for i in range(partida):
    l,p = input().split(" ")
    l = int(l)
    p = int(p)
    totalP += p
    totalL += l

if totalL > totalP:
    print("Lucas")
elif totalL < totalP:
    print("Pedro")
else:
    print("Empate")