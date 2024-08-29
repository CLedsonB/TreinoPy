n = int(input())
lista = []

for i in range(n):
    poster = {}
    ano = int(input())
    nome = input()
    categoria = input()
    data = input()
    poster['ano'] = ano
    poster['nome'] = nome
    poster['categoria'] = categoria
    poster['data'] = data
    lista.append(poster)

busca = input()
print(busca + "\n")

for i in range(n):
    if lista[i]['categoria'] == busca:
        print(lista[i]['ano'])
        print(lista[i]['nome'])
        print(lista[i]['data'])
        print()
    elif lista[i]['ano'] == int(busca):
        print(lista[i]['nome'])
        print(lista[i]['categoria'])
        print(lista[i]['data'])
        print()
    else:
        print("Sem filmes nessa consulta")
        break