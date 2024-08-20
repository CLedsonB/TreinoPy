num = int(input())
palavra = input()
crip = ""

for l in palavra:
    crip += chr(ord(l)+num)

print(crip)