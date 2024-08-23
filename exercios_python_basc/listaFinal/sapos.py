s,n = input().split()
s = int(s)
n = int(n)
pedras = [0]*n

for i in range(s):
    pulo = int(input())
    if pulo <= len(pedras) and pulo > 0:
        for j in range(0,n,pulo):
            pedras[j] = 1

print(*pedras)
