z,g = input().split(" ")
d,c = input().split(" ")

if z != g:
    print("Bloqueado")
elif z == g:
    print("Driblado")
    if d != c:
        print("...e o goleiro pega")
    elif d == c:
        print("Gol")
