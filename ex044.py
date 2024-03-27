
preco = float(input('Qual o preço do produto? R$'))
met_pag = int(input('''Selecione o método de pagamento:
Para pagar á vista no dinheiro/cheque digite 1;
Para pagar á vista no cartão digite 2;
Para pagar em 2x no cartão digite 3;
Para pagar em 3x ou mais no cartão digite 4: '''))

if met_pag == 1:
    desc = preco * 0.10
    preco = preco - desc
    print(f'''Você recebeu um desconto de R${desc:.2f} por conta do seu método de pagamento.
Total a pagar: R${preco:.2f}.''')

if met_pag == 2:
    desc = preco * 0.05
    preco = preco - desc
    print(f'''Você recebeu um desconto de R${desc:.2f} por conta do seu método de pagamento.
Total a pagar: R${preco:.2f}.''')

if met_pag == 3:
    parce = preco / 2
    print(f'''Total a pagar: R${preco:.2f}.
Sao 2 parcelas de R${parce:.2f} SEM JUROS.''')

if met_pag == 4:
    n_parce = int(input('Em quantas parcelas?'))
    juros = preco * 0.20
    preco = preco + juros
    parce = preco / n_parce
    print(f'''São {n_parce} de R${parce} COM JUROS.
Total a pagar: R${preco:.2f}.''')

else:
    preco = 0
    print('\033[31mOpção de pagamento inválida!')