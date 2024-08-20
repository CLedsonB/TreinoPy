import string

alfabeto = list(string.ascii_lowercase)

num = int(input())
palavra = input()
crip = ""

for l in palavra:
    num_letra = ord(l)
    if num_letra+num > 122:
        num_letra = (num_letra + num) - 26
    else:
        num_letra += num
    crip += chr(num_letra)

print(crip)