num1 = float(input('1° Número: '))
num2 = float(input('2° Número: '))
num3 = float(input('3° Número: '))
if num1 > num2 and num1 > num3:
    print(f'\033[31mO número {num1} é maior.')
if num2 > num1 and num2 > num3:
    print(f'\033[32mO número {num2} é maior.')
if num3 > num1 and num3 > num2:
    print(f'\033[34mO número {num3} é maior.')