shini = set()
aliado = set()
diff = []

n = int(input())

for i in range(n):
    shini.add(input())

m = int(input())

for i in range(m):
    aliado.add(input())

diff = shini.difference(aliado)

if len(shini) - len(aliado) == len(diff):
    print("Sociedade das almas salva, Ichigo")
else:
    print("Estamos perdidos, Ichigo")