# Registrando o produto e gerando informações
print(f'''
{15 * '-'}
REGISTRANDO PRODUTO
{15 * '-'}''')
soma_total = soma_mil = cont = preco_barato = 0
nome_barato = ''
while True:
    nome = ' '
    while nome == ' ' or nome == '':
        nome = str(input('Nome do produto: ')).strip()
    preco = 0
    while preco <= 0:
        preco = float(input('Preço do produto: R$'))
    soma_total += preco
    if preco > 1000:
        soma_mil = soma_mil + 1
    cont += 1
    if cont == 1 or preco < preco_barato:
        nome_barato = nome
        preco_barato = preco
    stop = ' '
    while stop not in 'SN':
        stop = str(input('Você quer continuar? [S/N]: ')).strip().upper()[0]
    if stop == 'N':
        print(15 * '-=')
        break

print(f'''Você registou {cont} produtos, deles:
A soma total do valor deles é de R${soma_total:.2f};
{soma_mil} custaram mais que R$1000;
e o mais barato foi {nome_barato} que custou R${preco_barato:.2f}.''')