#jogo de par ou impar
from random import randint

print('PAR OU ÍMPAR')
print(12 * '-=')
pc = randint(1, 10)
n = 0
while True:
    n = int(input('Escolha um número: '))
    pi = str(input('Você quer par ou ímpar? [P/I]: ')).strip().upper()
    soma = n + pc
    if pi not in 'PI':
        print('Valor Invalido')
        pi = str(input('Você quer par ou ímpar? [P/I]: ')).strip().upper()
    if pi == 'P' and soma % 2 == 0:
        print(f'Você jogou {n} e o computador {pc}. A soma deu {soma} que é PAR.')
        print('PARABÉNS. VOCÊ VENCEU!')
        print('Vamos jogar novamente...')
        print(12 * '-=')
    if pi == 'I' and soma % 2 != 0:
        print(f'Você jogou {n} e o computador {pc}. A soma deu {soma} que é ÍMPAR.')
        print('PARABÉNS. VOCÊ VENCEU!')
        print('Vamos jogar novamente...')
        print(12 * '-=')
    if pi == 'P' and soma % 2 != 0:
        print(f'Você jogou {n} e o computador {pc}. A soma deu {soma} que é ímpar')
        print('Você perdeu...')
        break
    else:
        print(f'Você jogou {n} e o computador {pc}. A soma deu {soma} que é ímpar')
        print('Você perdeu...')
        break
print('FIM')