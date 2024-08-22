r = float(input())
d = float(input())

lucro = r - d
margem = (lucro / r) * 100
roi = (lucro / d) * 100

print(f'Lucro Liquido: {lucro:,.2f}')
print(f'Margem de Lucro: {margem:,.2f}%')
print(f'ROI:{ roi:,.2f}%')