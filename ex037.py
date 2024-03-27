print('''Olá! Seja bem-vindo ao programa de conversão de números!
Nossa função é converter o número que desejar para binário octal ou hexadecimal''')
num = int(input('Qual número deseja converter? '))
conv = int(input('''Para converter para binário, digite 1;
Para converter para octal, digite 2;
Para converter para hexadecimal digite 3: '''))

if conv == 1:
    print(f'O número {num} convertido em binário é {bin(num)}.')
elif conv == 2:
    print(f'O número {num} em octal é {oct(num)}.')
elif conv == 3:
    print(f'O numéro {num} convertido em hexadecimal é {hex(num)}')