import time as t

# estrela da árvore
print('☆'.center(20))
#center(int) para centralizar a estrela
# construindo a árvore
for i in range(1, 20, 2):
    print(('*'*i).center(20))
    t.sleep(0.5)
# tronco da árvore
for r in range(2):
    print(('||').center(19))
    t.sleep(0.5)
# base da árvore
print('\====/'.center(19))
print()
# mensagem final
print('\n\tFeliz Natal e que a mão invisível\n\tdo mercado, não recaia sobre voces!',end='\n\n')







