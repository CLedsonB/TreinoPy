n = int(input())
clones = 2
control = False
i = 1

while i <= n:
     if n == clones:
         control = True
         break
     clones *= 2
     i += 1

if control == True:
    print("Dattebayo")
else:
    print("Tururuuu")