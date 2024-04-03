# lendo 6 números e somando somente os pares

soma = 0
for count in range(0, 6):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        soma = soma + n
print(f'A soma entre o números pares desse valores é {soma}')