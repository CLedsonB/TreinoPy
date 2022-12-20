#Equacao do segundo grau
import math
#F3 - Imprimir concavidade


###_____________EQUACOES____________###

def eq2completa(a,b,c):
	
	delta = pow(b,2) - 4*a*c
	print("Delta = ", delta);
	
	if (delta > 0):
		print("A equacão tem 2 soluções reais");
		x1 = -b + delta**0.5 / 2*a
		x2 = -b - delta**0.5 / 2*a
		print("Conjunto solução: {%.2f,%.2f}" %(x1,x2))
		
	elif (delta < 0):
		print("A equação não tem solução real");
		
	else:
		print("A equção tem 1 solução real");
		x = -b / 2*a
		print("Conjunto solução: {%.2f}" %(x))

def eq2semC(a,b):
	
	delta = pow(b,2) - 4*a
	print("Delta = ", delta)
	
	if (delta > 0):
		print("A equacão tem 2 soluções reais");
	elif (delta < 0):
		print("A equação não tem solução real");
		
	else:
		print("A equção tem 1 solução real");
		
	if(a % 2 == 0):
		a /= 2
		b /= 2
		x = -b/a
		
		print("Conjunto solução: {%.2f, 0}" %(x))
		
	else:
		x = -b/a
		print("Conjunto solução: {%.2f, 0}" %(x))

def eq2semB(a,c):
	
	delta = -4*a*c
	print("Delta = ", delta)

	if (delta > 0):
		print("A equacão tem 2 soluções reais");
		x1 = +delta**0.5 / 2*a
		x2 = -delta**0.5 / 2*a
		
		print("Conjunto solução: {%.2f,%.2f}" %(x1,x2))
	elif (delta < 0):
		print("A equação não tem solução real");
		
	else:
		print("A equção tem 1 solução real nula");
		print("Conjunto solução: {0}")


def eq2semBC(a):
	print("Conjunto solução: {0}")


###___________PROGRAMA___________####

print("\t***Calculadora***\n");
print("Equações disponivéis");
print("(1) ax2 + bx + c");
print("(2) ax2 + bx");
print("(3) ax2 + c");
print("(4) ax2");
print("\nFunções disponivéis");



system = input("\nInsira um valor\n->");

print("\n")

####____________FUNCOES__________####

def intervaloY(a,b,c):
	x0 = float(input("Primeiro valor para x: "))
	x1 = float(input("Ultimo valor para x: "))
	x01 = float(input("Aumentar valor de x em quanto: "))
	
	print('\nFuncão proposta: y = {}*x**2 +{}*x +{}\n' .format(a,b,c))
	while x0 <= x1:
		y = a*pow(x0,2)+b*x0+c
		print("\tx: ", round(x0,2), " y: ", round(y,2))
		x0 += x01

intervaloY(2,2,2)

		