#simulando um caixa eletronico 
print(F'''{15* '-='}
SIMULADOR DE CAIXA ELETRÔNICO
{15* '-='}''')
valor = int(input('Qual o valor a ser sacado: R$'))
notas_50 = notas_20 = notas_10 = notas_1 = 0
while True:
    if valor <= 0:
        print('Digite um valor maior que zero')
        valor = int(input('Qual o valor a ser sacado: R$'))
    notas_50 = int(valor / 50)
    resto = valor % 50
    if resto != 0:
        notas_20 = int(resto / 20)
        resto %= 20
        if resto != 0:
            notas_10 = int(resto / 10)
            resto %= 10
            if resto != 0:
                notas_1 = int(resto / 1)
                resto %= 1
    if resto == 0: 
        print(15*'-=')
        break

print(f'''Você receberá:
Notas de R$50: {notas_50};
Notas de R$20: {notas_20};
Notas de R$10: {notas_10};
Notas de R$1: {notas_1}.''')