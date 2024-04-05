resp = 'S'
count = 0
soma = 0
maior = 0
menor = 0
while resp == 'S':
    n = int(input('''
Digite um valor: '''))
    count += 1
    soma += n
    if count == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    med = soma / count
    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()
    while resp not in 'SN':
        print('Resposta inválida, digite novamente...')
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()
if count == 1:
    print(f'''
Você digitou somente 1 número.
O maior, menor, sua soma e sua média é ele mesmo ou seja, {n}''')
else:
    print(f'- Você digitou {count} números')
    print(f'- O menor deles é {menor}')
    print(f'- O maior deles é {maior}')
    print(f'- A soma entre eles é {soma}')
    print(f'- A média entre eles é {med}')
