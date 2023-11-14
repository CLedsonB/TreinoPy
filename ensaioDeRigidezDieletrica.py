print('\tValores pra ensaio de rigidez\n')

#definir quantidade de ensaios
quant = int(input('Quantidade de ensaios : '))
valores = [x for x in range(quant) ]
numR = float(input('Relação maxima de desvio padrão e media (%) :  '))

#receber valores de ensaios
print('\n')
for i in range(quant):
    valores[i] = float(input('\t[%d] - Valor : ' %(i+1)))

#calcular a media dos valores de ensaio
m = 0  
for i in valores:
    m += i
    media = m/quant
 
#calcular desvio padrao e porcentagem
temp = 0  
for i in valores:
    temp += (i - media) ** 2
    
s = (1/5 * temp) ** 0.5
pDesvio = s/media * 100

#apresentar resultados
print('\n\tMedia = %f' %(media))
print('\tDesvio = %f' %(s))

print('\tPorcentagem de desvio : %f' %(pDesvio))

if pDesvio < numR :
    print('\n\tResultado : Aprovado')
else:
    print('\n\tResultado : Reprovado')