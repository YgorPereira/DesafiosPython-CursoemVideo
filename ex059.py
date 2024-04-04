#CALCULADOR EM LOOPING

n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
menu = '''
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa
'''
print(menu)
op = int(input('Digite o número correspondente a ação desejada: '))

while op != 5:
    if op == 1:
        print(f'Soma: {n1} + {n2} = {n1 + n2:.2f}')
    elif op == 2:
        print(f'Multiplicação: {n1} X {n2} = {n1 * n2:.2f}')
    elif op == 3:
        if n1 == n2:
            print('São números iguais')
        if n1 > n2:
            print(f'Maior: {n1}')
        else:
            print(f'Maior: {n2}')
    elif op == 4:
        n1 = float(input('Digite o primeiro valor: '))
        n2 = float(input('Digite o segundo valor: '))
    else:
        print('Opção inválida!')
    print(menu)
    op = int(input('Digite o número correspondente a ação desejada: '))

print('finalizando...')
