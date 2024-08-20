a,b,c,d,e = input().split(" ")


ninjas = int(a)+int(b)+int(c)+int(d)
e = int(e)

if ninjas <= e:
    print(e - ninjas)
