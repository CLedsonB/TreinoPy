i = 1
a = ' '
while a != 0:
    a = float(input('\tValor [%d] ->> ' %(i)))
    result = (a*10)/0.493
    
    print('\n\t%.2f -->> %.2f ' %(a, result))
    i += 1
  
print('FIM')