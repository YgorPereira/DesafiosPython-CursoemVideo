# Análise de dados de uma matriz

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_par = soma_3col = maior = 0
for lin in range(0, 3):
    for col in range(0,3):
        matriz[lin][col] = int(input(f'Digite um valor para a coluna {col} da linha {lin}: ')) 
print(30 * '-=')
for lin in range (0,3):
    for col in range(0, 3):
        print(f'[{matriz[lin][col]:^5}]', end='')
        if matriz[lin][col] % 2 == 0:
            soma_par += matriz[lin][col]
    print()
print(f'A soma dos números pares é: {soma_par}')

for lin in range(0,3):
    soma_3col+=matriz[lin][2]
print(f'A soma dos números da 3° coluna é: {soma_3col}')

for c in range(0,3):
    if c == 0 or matriz[1][col] > maior:
        maior = matriz[1][col]
print(f'O maior da segunda linha  é: {maior}')