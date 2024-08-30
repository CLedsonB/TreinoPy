quarto = { 'Casal': 2, 'Triplo': 3, 'Quadruplo': 4, 'Familia': 5}
lista = []
tipoQuarto = None
cont = 0

n = int(input())

while tipoQuarto != "FIM":
    tipoQuarto = input()
    lista.append(tipoQuarto)

for i in range(len(lista)-1):
    if quarto[lista[i]] == 'Casal':
        cont += quarto['Casal']
    elif quarto[lista[i]] == 'Triplo':
        cont += quarto['Triplo']
    elif quarto[lista[i]] == 'Quadruplo':
        cont += quarto['Quadruplo']
    elif quarto[lista[i]] == 'Familia':
        cont += quarto['Familia']

if cont <= n:
    print("Pode reservar! Esses quartos cabem todos.")
else:
    print("Procure outra pousada")
    