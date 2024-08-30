cao1 = int(input())
cao2 = int(input())

semana = 7

total_grama = (cao1 + cao2) * semana
total_kilo = round(total_grama/1000)

print(f'{total_kilo}kg')