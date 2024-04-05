#MOSTRANDO O FATORIAL DE UM NÚMERO LIDO
num = int(input('Digite um número: '))
print(f'{num}! = ', end='')
count = num
fat = 1
while count > 0: 
    print(f'{count}', end='')
    print(' x ' if count > 1 else ' = ', end='')
    fat *= count
    count-= 1
print(fat)