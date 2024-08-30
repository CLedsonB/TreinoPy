a = int(input())
b = int(input())
c = int(input())

if abs(b - c) < a < b + c and abs(a - c) < b < a + c and abs(a - b) < c < a + b:
    print("Forma triangulo")
else:
    print("Nao forma triangulo")