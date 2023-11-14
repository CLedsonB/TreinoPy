#importação de bibliotecas
import os
import random as r
import time as t

#definição de funções
def mode1(palavra):
    x = 0
    for i in palavra:
        os.system('clear')
        x += 1
        print('\n\n\t',palavra[0:x])
        t.sleep(0.2)
        
def mode2(palavra):
    for i in palavra:
        os.system('clear')
        print('\n\n\t',i)
        t.sleep(0.4)
    os.system('clear')
    print('\n\n\t',palavra)
    
def mode3(palavra):
    const = ' '
    for i in range(len(palavra)):
        print('\t',const,const*i,palavra[i])
        t.sleep(0.2)

def mode4(palavra):
    print('\n\n')
    const = ' '
    for i in range(len(palavra)):
        if i % 2 == 1:
            print('\t',const*2,palavra[i])
        else:
            print('\t',const,palavra[i])
            
def mode5(palavra):
        part1 = palavra[::2]
        part2 = palavra[1::2]
        transfor1, transfor2 = '\t','\t '
        for i in part1:
            transfor1 += i+' '
        for i in part2:
            transfor2 += i+' '
        print(transfor1,'\n',transfor2)
        
    
def principal():
    #exibição animada do titulo
    titulo = 'LOOP LETRAS'
    rand = r.randint(1,4)
    os.system('clear')
    
    if rand == 1:
        mode1(titulo)
    elif rand == 2:
        mode2(titulo)
    elif rand == 3:
        mode3(titulo)
    else:
        mode4(titulo)
        
    os.system('clear')
    
    #tela inicial
    print('\n\tDigite uma das opções abaixo : ')
    print('\n\n (1) Completar palavra, letra por letra\n (2) Exibir letra por letra da palavra\n (3) Exibir palavra inclinada\n (4) Exibir inclinada de 2 em 2 na vertical\n (5) Exibir inclinada de 2 em 2 na horizontal')
    opc = int(input('\n  Digite aqui : '))

    string = input('\n\n\tInsira uma palavra\n\t-> ')
    os.system('clear')
    
    if opc == 1:
        mode1(string)
    elif opc == 2:
        mode2(string)
    elif opc == 3:
        mode3(string)
    elif opc == 4:
        mode4(string)
    elif opc == 5:
        mode5(string)
    else:
        print('\n\tTá errado')
        exit()

#execução
num = 1
while num != 0:
    principal()
    print('\n\n  (1) Reiniciar\n  (0) Sair')
    num = int(input('\n  Digite aqui : '))












