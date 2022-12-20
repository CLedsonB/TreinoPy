import math as m

def apresentacao():
    print('\t','*'*30,'\n\t','*'*30)
    print('\t **** FAIXA DE VALORES PARA ***\n\t ****** ONDAS SENOIDAS ********')
    print('\t','*'*30,'\n\t','*'*30)
    print()
    valores()
def valores():
    amp = float(input('\tAmplitude da onda : '))
    v = float(input('\tVelocidade Angular (щ) : '))
    ang = float(input('\tAngulo de defasagem (Ф) : '))
    print('''
    \tDigite uma das opções para Base de tempo:
     \t1 = 0.01 segundo
     \t2 = 0.1 segundo
     \t3 = 1 segundo
     \t4 = 10 segundos ''')
    opc = int(input('\t --> '))
    
    if opc == 1:
       fator = 0.01
    elif opc == 2:
       fator = 0.1
    elif opc == 3:
       fator = 1
    elif opc == 4:
       fator = 10
    else:
       print('\n\tValor inesperado!!!')

    calc()       
     
def calc():
    for i in 360:
        tempo= i * fator
        R = amp * ( m.sin ( v * tempo + ang))
        print(' %.2f = %.2f * sen( %.1f * %.2f + %.2f ) ' %(R, amp, v, tempo, ang))

apresentacao()