# Lista composta e análise de dados

num = [[], []]

for c in range(1,8):
    n = int(input(f'Digite o {c}° valor:'))
    if n % 2 == 0:
        num[0].append(n)
    else:
        num[1].append(n)

print(30 * '-=')
print(f'Os números pares são: {num[0]}')
print(f'Os números impares são: {num[1]}')