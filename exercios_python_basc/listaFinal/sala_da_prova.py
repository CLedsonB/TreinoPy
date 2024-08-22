# import string

# alfabeto = list(string.ascii_uppercase)
# rot1 = alfabeto[:13]
# rot2 = alfabeto[13:]

rot1 = [chr(letra) for letra in range(65,78,1)]
rot2 = [chr(letra) for letra in range(78,91,1)]

letra = input().strip()




if rot1.count(letra) == 1:
    print('Voce fara prova no laboratorio 140')
elif rot2.count(letra) == 1:
    print('Voce fara prova no laboratorio 143')