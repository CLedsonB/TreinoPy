n,t = input().split()
cont = 0

n = int(n)
t = int(t)

for i in range(n):
    h = int(input())
    t -= h
    cont += 1

if cont == 0:
    print(0)
else:
    print(i-1)
