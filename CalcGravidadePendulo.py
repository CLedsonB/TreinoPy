import math

c = [ ]
p = [ ]

n = int(input('\tNumero de ciclos: '))
print('\n')

for i in range(n):
    seg = float(input('\tComprimento (m): '))
    c.append(seg)
    s = float(input('\tPeriodo (s):  '))
    p.append(s)
    print('\n')
    
for i in range(n):
    g = (4*pow(3.14,2)*c[i])/pow(p[i],2)
    print('\t g', i+1, '- - ', round(g,4),' m/s^2')
    print('\n')