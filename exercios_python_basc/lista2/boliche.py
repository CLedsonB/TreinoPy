a,b,c = input().split(" ")
grupo = 0

a = int(a)
b = int(b)
c = int(c)

while c >= b:
    c -= b
    grupo += 1

if grupo == a:
    print("N")
else:
    print("S")