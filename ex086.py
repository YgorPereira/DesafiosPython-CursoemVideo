# Matriz em python

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for lin in range(0, 3):
    for col in range(0,3):
        matriz[lin][col] = int(input(f'Digite um valor para a coluna {col} da linha {lin}: ')) 
print(30 * '-=')
for lin in range (0,3):
    for col in range(0, 3):
        print(f'[{matriz[lin][col]:^5}]', end='')
    print()