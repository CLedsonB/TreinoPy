
#adicao de dados
def criar(dados):
    contador = 0
    dado = 1
    print("\n\tInsira 0 para encerrar\n\n")
    while dado != 0:
        print("\t(",contador,") - Insira um dado: ")
        dado = float(input("\t->> "))
        dados[contador] = dado
        contador += 1
    del dados[contador-1]
    return dados

#ordenar dados
def ordenar(dados):
    valor = [ ]
    posicao = [ ]
    #separar dicionario em vetores
    for k, v in dados.items( ):
        posicao.append( k )
        valor.append( v )
    dados = { }
    valor.sort( )
    for i in posicao:
        dados[ i ] = valor[ i ]
    return dados, posicao, valor

#exibir dados
def exibir(dados):
    try:
        print("\n\n\t| Posicao | Valor | ")
        for k, v in dados.items( ):
            print("\t| %7.d | %.2f | " %(k, v))
    except:
         print("Não há dados para mostrar")
         
#trocar dados
def trocar(dados):
    exibir(dados)
    print("\tDigite um posição: ")
    p = int(input("\t->> "))
    print("\n\tDigite um novo valor")
    n = float(input("\t->>"))
    dados[ p ] = n
    print("\n\tDado n°",p," alterado com sucesso\n")
    return dados

#remocao de dados
def remover(dados ):
    exibir(dados)
    print("\tDigite um posição: ")
    p = int(input("\t->> "))
    del dados[p]
    print("\n\tDado n°",p," removido com sucesso\n")
    return dados

#analise de dados
##frequencia
def frequencia(dados):
    contagem = dict()
    for v in dados.values():
        if v not in contagem:
            contagem[v] = 1
        else:
            contagem[v] += 1
    return contagem

##frequencia relativa
##amplitude
##media
def media(dados):
    som = 0; media = 0
    for i in dados:
        som += i
    media = som/len(dados)
    return media
    
##moda
##mediana
def mediana(posicao,valor):
    if len(posicao) % 2 == 0:
        pos1 = len(posicao) / 2
        pos2 = pos1 + 1
    else:
       print("")
       #dividir por 2 e arredondar para cima
    mediana = (valor[pos1]+valor[pos2])/2
    return mediana
    
##desvios
##desvio medio aritmetico
##variancia
##desvio padrao
##coeficiente de variacao
