p,g,t = input().split(" ")

p = int(p)
g = int(g)
t = int(t)

if p*1 + g*10 > t:
    print("NENHUM")
elif p*1 + g*10 < t:
    print("INSUFICIENTE")
elif p*1 + g*10 == t:
    num = t - g*10
    print(f'PREENCHIDO COM {num} PRESENTES')