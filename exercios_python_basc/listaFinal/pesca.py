n,t = input().split()

n = int(n)
t = int(t)

for i in range(n):
    h = int(input())
    t -= h
    if t <= 0:
        print(i)
        break
