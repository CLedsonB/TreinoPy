

n = int(input('\tNumero de ciclos? '))
print(' ')

for i in range(n):
    print('\n\n')
    v = float(input('\tValor inicial? '))
    t = float(input('\tPorcentagem de juros? '))
    
    r = v*(t/100)
    
    print('Valor final: %.2f Rendimento: %.2f ' %(r+v, r))