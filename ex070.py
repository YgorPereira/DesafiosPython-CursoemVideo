# Registrando o produto e gerando informações
print(f'''
{15 * '-'}
REGISTRANDO PRODUTO
{15 * '-'}''')
soma_total = soma_mil = cont = 0
nome_barato = ''
preco_barato = 0
while True:
    nome = str(input('Nome do produto: ')).strip()
    if nome == '':
        print('Não deixe o nome em branco!')
        nome = str(input('Nome do produto: ')).strip()
    preco = float(input('Preço do produto: R$'))
    if preco <= 0:
        print('Digite um valor maior que 0!')
        preco = float(input('Preço do produto: R$'))
    soma_total += preco
    if preco > 1000:
        soma_mil = soma_mil + 1
    cont += 1
    if cont == 1:
        nome_barato = nome
        preco_barato = preco
    else:
        if preco < preco_barato:
            nome_barato = nome
            preco_barato = preco
    stop = str(input('Você quer continuar? [S/N]: ')).strip().upper()
    if stop not in 'SN' or stop == '':
        print('Valor inválido.')
        stop = str(input('Você quer continuar? [S/N]: ')).strip().upper()
    if stop == 'N':
        print(15 * '-=')
        break

print(f'''Você registou {cont} produtos, deles:
A soma total do valor deles é de R${soma_total:.2f};
{soma_mil} custaram mais que R$1000;
e o mais barato foi {nome_barato}.''')