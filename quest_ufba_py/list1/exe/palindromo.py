s = input()
s = s.lower()

s_reverso = s[::-1]

if s == s_reverso:
    print("Sim")
else:
    print("Nao")