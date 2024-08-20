num1 = input("Insira o numero 1 : ")
num2 = input("Insira o numero 2 : ")

num1, num2 = int(num1), int(num2)

calc1 = num1 + num2
calc2 = num1 - num2
calc3 = num1 * num2
calc4 = num1 ** num2

print("(+)",calc1,"(-)",calc2,"(*)",calc3,"(**)",calc4)
print(f'(+) {calc1} (-) {calc2} (*) {calc3} (**) {calc4}')
