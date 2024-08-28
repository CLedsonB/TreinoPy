s,i,j,k,l,m = input().split()
situacao = ""

i = int(i)
j = int(j)
k = int(k)
l = int(l)
m = int(m)

if j == k == l== m == 1 and i >= 12:
    print(f'{s}, condicoes ok! Boa sorte na busca pelo tesouro!')
else:
    if i < 12:
        situacao += "Nao possui idade minima; "
    if j != 1:
        situacao += "Nao possui bussola; "
    if k != 1:
        situacao += "Nao possui mapa do tesouro; "
    if l != 1:
        situacao += "Nao possui po magico; "
    if m != 1:
        situacao += "Nao possui espada magica; "

    print(situacao[:-1])
    print(f'{s} nao cumpre todas as condicoes!')
