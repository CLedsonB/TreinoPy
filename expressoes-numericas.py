# gerar lista com expressões numericas

# pedir valor mais alto, valor mais baixo
#pedir operacões usadas
# pedir tamanho da espressao
# pedir quantidade de expressoes pra gerar

# gerar lista sem resposta e lista com respostas

from random import *
import os

print('  Insira valores inteiros para definir\n  suas expressões numéricas.. \n')

vmax = int(input('\tMaior valor : '))
vmin = int(input('\tMenor valor : '))
op = input('\tOperação : ')
tam = int(input('\tTamanho : '))
quant= int(input('\tQuantidade :'))

resultado = [y for y in range(quant)]

for i in range(quant):
    
    valores = [x for x in range(tam)]
    
    # gera lista de valores aleatorios
    for j in range(tam):
        valores[j] = randint(vmin,vmax+1)
        
   # define primeiro valor da expressao     
    num = str(valores[0])
   
     # gerar expressao numerica completa
    id = 1
    while id <= len(valores)-1:
        num += op+str(valores[id])
        id += 1
        
  # gera lista de expressoes
    resultado[i] = num

# imprimir lista de expressoes numericas
os.system('clear')

print('\t-----LISTA DE EXERCÍCIOS-----')
for k in range(len(resultado)):
    print('\n\t(',k+1,') ',resultado[k],'= ?' )

print('\n\n\t-----LISTA DE RESPOSTAS-----')
for k in range(len(resultado)):
    print('\n\t(',k+1,') ',resultado[k],'=',eval(resultado[k]) )
