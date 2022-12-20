print("\t***Calculadora para juros simples***")

valor = float(input("\n\tValor inicial(R$): "))
multa = float(input("\tMulta por atraso(%): "))
juros = float(input("\tJuros por dia de atraso(%): "))
dias = int(input("\tDias de atraso(d): "))

#Multa por atraso + multa por dia de atraso * dias de atraso
jurosTotal = (valor/100) * multa + (valor/100) * juros * dias

valorTotal = valor + jurosTotal

print('\n  Valor inicial: %.2f R$' %(valor))
print("  Juros de: %.2f R$" %(jurosTotal))
print("  Valor atual: %.2f R$" %(valorTotal))