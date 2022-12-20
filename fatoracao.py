primos = []
fatoresA = []
fatoresB = []
nMax = 200

##______LISTA__DE__PRIMOS______#####

for nFixo in range(2, nMax):
	cont = 0
	for nVaria in range(2,nMax):
		if(nFixo > nVaria and nFixo % nVaria == 0):
			cont += 1
	if(cont == 0):
		primos.append(nFixo)

##____________PROGRAMA_________###

a = int(input("a: "))
b = int(input("b: "))
max = int(input("Maximo de iterações: "))

for primo in primos:
	aux = 0
	
	while aux < max:
		if(a % primo == 0 and a != 0):
			result = a / primo
			fatoresA.append(primo)
			a = result
		aux += 1
		
#REPETIR METODO ACIMA PARA INTEIRO B
for primo in primos:
	aux = 0
	
	while aux < max:
		if(b % primo == 0 and b != 0):
			result = b / primo
			fatoresB.append(primo)
			b = result
		aux += 1

print("fatoração A ->\n",fatoresA)
print("fatoração B ->\n",fatoresB)

setFatoresA = set(fatoresA)
setFatoresB = set(fatoresB)

igualdade = setFatoresA.difference(setFatoresB)

print("igualdade de termos: ",igualdade)

