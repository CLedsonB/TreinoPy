import os

print('Adicione um número padrão:\nEx: (xx) xxxx-xxxx ')
num = input(' -> ')

num = 'wa.me//+55'+num[1:3]+num[5:10]+num[11:15]

os.system('clear')
print('\n\t',num)