a,b,c,d,e = input().split(" ")


naves = int(b)+int(c)+int(d)+int(e)
a = int(a)

if naves <= a:
    print(a - naves)