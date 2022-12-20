import math

def GR(numero):
    rad = (numero/180)*math.pi
    return rad
    
def seno(numero):
    resultado = 0
    resultado = math.sqrt(1 - (coseno(numero))**2)
    return resultado 
    
def coseno(rad):
    numero = GR(rad)
    cont = 0
    resultado = 1
    while(cont < 50):
        cont += 1
        resultado += (((-1)**cont)*(numero**(2 * cont)))/(math.factorial(2 * cont))
        return round(resultado, 6)

print('\n\t1 -  Retangular -> Polar')
print('\n\t2 - Polar -> Retangular')

opc = int(input('\n\t--> '))

if opc == 1:
    a = float(input('\n\tParte Real: '))
    b = float(input('\n\tParte Imaginária: '))
    
    mod = math.sqrt(math.pow(a,2)+math.pow(b,2))
    ang = (math.atan(b/a))
    
    print('\n\tValor : %.2f | %.2f ' %(mod, ang))
    
elif opc == 2:
    mod = float(input('\n\tModulo: '))
    ang = float(input('\n\tAngulo: '))
    
    a = abs(mod)*coseno(ang)
    b = abs(mod)*seno(ang)
     
    print('\n\tValor : %.2f + j%.2f ' %(a, b))

else:
    print('\n\tOpcao Incorreta')