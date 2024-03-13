i = 0
valor = 6
max = 6.4


v = [x for x in range(valor)]
c = [x for x in range(valor)]

while i <= valor - 1:
    c[i] = float(input("\tValor: "))
    v[i] = c[i] * 100 / max
    i += 1

for i in range(valor):
    print("valor:", c[i], "porcentagem:", "{:.2f}".format(v[i]))