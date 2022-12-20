#variaveis globais
dados = dict()
opc = 1

from bancoDeFuncoes import * 

while opc != 0:
    print('''
    Análise de dados em Python
    
    1 - Criação de dados
    2 - Exibição de dados
    3 - Alteração de dados
    4 - Remoção de  dados
    5 - Análise estatistica
    
    Digite um dos números apresetados:
''')
    opc = int(input("-> "))

    if opc == 1:
        dados= criar(dados)
    elif opc == 2:
        exibir(dados)
    elif opc == 3:
        dados = trocar(dados)
    elif opc == 4:
        dados = remover(dados)
    elif opc == 5:
      #  analise(dados)
      print(frequencia(dados))
    else:
        print('Caractere incorreto')
    dados, posicao, valor = ordenar(dados)