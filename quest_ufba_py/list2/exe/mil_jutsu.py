j = int(input())
c = int(input())
n = int(input())
m = int(input())
jutsuN = 0

usoChakra = n * m * 7
c -= usoChakra


for i in range(7):
    c -= (n*m)
    jutsuN +=1

if jutsuN + j >= 1000 and c >= 0:
    print("SUMIDAO!!!")

