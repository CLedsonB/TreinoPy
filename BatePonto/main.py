#pegar dados do arquivo bd.py
#transformar horarios em segundos
#obter diferença entre as 2  horas
#somar diferencas encontradas 
#subtrair 6h do total de horas encontrado
#salvar resultado no .txt com hora e data:
from bd import *

def getSeg(arr,aux):
        i = 0
        seg = [0,0]
        while i < 2:
            seg[i] = arr[i] * aux[i]
            i += 1
        totalSeg = seg[0] + seg[1] + arr[2]
        return totalSeg

def getHoras(seg, aux):
    hora = [0,0,0]
    hora[0] = seg // aux[0]
    hora[1] = (seg % aux[0]) // aux[1]
    hora[2] = seg % aux[1]
    return hora

def getTime(seg1, seg2):
    totalTime = seg2 - seg1
    return totalTime

def getSegDia(Time1, Time2, constante):
    SegDia = Time1 + Time2 - constante
    return SegDia

x1 = getSeg(dados[0][0],aux)
y1 = getSeg(dados[0][1],aux)
x2 = getSeg(dados[0][2],aux)
y2 = getSeg(dados[0][3],aux)
z1 = getTime(x1,y1)
z2 = getTime(x2,y2)
a = getSegDia(z1,z2,constante)
h = getHoras(a,aux)

print(x1,y1,x2,y2)
print(z1,z2)
print()
print(a,'segundos  <-> ',h[0],'h ',h[1],'min ',h[2],'s')