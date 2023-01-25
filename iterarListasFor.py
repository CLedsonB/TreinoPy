
par = [x for x in range(10) if x % 2 == 0]
impar = [x for x in range(10) if x % 2 != 0]
index = 0

for each in range(5):
    print('\t| %2d | %2d | ' %(par[index], impar[index]))
    index += 1