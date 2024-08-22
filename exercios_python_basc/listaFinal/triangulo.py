a = int(input())
b = int(input())
c = int(input())

if abs(a - b) < a < b + c and abs(a - c) < b < a + c and abs(a - b) < c < a + b:
    print("Forma Triangulo")
else:
    print("Nao forma triangulo")