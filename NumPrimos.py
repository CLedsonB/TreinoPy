
primos = []
nMax = 100

for nFixo in range(2, nMax):
	cont = 0
	for nVaria in range(2,nMax):
		if(nFixo > nVaria and nFixo % nVaria == 0):
			cont += 1
	if(cont == 0):
		primos.append(nFixo)
		
print(primos)