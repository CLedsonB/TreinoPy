s1,a,b,c,d = input().split(" ")
s2,e,f,g,h = input().split(" ")

totalS1 = int(a)+int(b)+int(c)+int(d)
totalS2 = int(e)+int(f)+int(g)+int(h)

if totalS1 > totalS2:
    print(s1,totalS1)
else:
    print(s2,totalS2)