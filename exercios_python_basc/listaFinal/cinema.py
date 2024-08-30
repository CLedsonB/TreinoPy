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
    if type(lista[i]['categoria']) == type(busca) and lista[i]['categoria'] == busca:
        print(lista[i]['ano'])
        print(lista[i]['nome'])
        print(lista[i]['data'] + "\n")
    elif type(lista[i]['ano']) == type(busca) and lista[i]['ano'] == int(busca):
        print(lista[i]['nome'])
        print(lista[i]['categoria'])
        print(lista[i]['data'] + "\n")
    else:
        print("Sem filmes nessa consulta")
        break