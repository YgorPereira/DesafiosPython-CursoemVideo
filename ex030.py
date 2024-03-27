num = int(input('Digite um número inteiro: '))
if num % 2 == 0:
    print('\033[35mEsse número é PAR.')
else:
    print('\033[1;36mEsse número é ÍMPAR.')