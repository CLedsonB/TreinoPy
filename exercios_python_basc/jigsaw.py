s = input()
quant, oc = input().split(" ")

quant = int(quant)

s = s.replace(" ", "")
contagem = s.count(oc)

print(s)
print()

print(contagem)

if contagem == quant:
    print("SIM!")
else:
    print("NAO!")

