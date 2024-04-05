#lendo, contando e somando até o usuário digitar 999

n = cont = soma = 0
while True:
    n = int(input('Digite um valor [999 para parar]: '))
    if n == 999:
        break
    soma += n
    cont += 1
if cont == 0:
    print('Você não digitou nenehum valor válido.')
else:
    print(f'''
Você digitou {cont} números.
A soma deles é igual a {soma}.''')