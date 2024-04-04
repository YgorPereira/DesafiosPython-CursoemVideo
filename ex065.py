stop = 1
count = 0
soma = 0
maior = 0
menor = 0
menu = '''
Você deseja continuar?
[1] Sim
[2] Não'''

while stop != 2:
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
    print(menu)
    stop = int(input('''resposta:'''))

print(f'- Você digitou {count} números')
print(f'O menor deles é {menor}')
print(f'O maior deles é {maior}')
print(f'- A soma entre eles é {soma}')
print(f'- A média entre eles é {med}')
