a,b = input().split(" ")

if a == "direita" and b == "esquerda":
    print("Achou")
elif a == "direita" and b == "direita":
    print("Tente novamente")
elif a == "esquerda" and b == "esquerda":
    print("Morreu")
elif a == "esquerda" and b == "direita":
    print("Tente novamente")
