print('''Olá! Vejo que você quer um empréstimo para a compra de uma casa.
Preciso de algumas informações suas.''')
val_casa = float(input('Qual o valor da casa? R$'))
val_sal = float(input('Qual o valor do seu salário? R$'))
anos = int(input('Em quantos anos vai pagar? '))
val_prest  = val_casa / (anos * 12)
print(f'''Para pagar uma casa de R${val_casa:.2f} em {anos} anos
 a prestação será de R${val_prest:,2f}''')

if val_prest < val_sal * 0.30:
    print(f'''O emprétimo foi \033[1;32 mAPROVADO!\033[m.
O valor da prestação é de R${val_prest:.2f}.''')

else:
    print('''Infelizmente o empréstimo foi \033[1;31mNEGADO!\033[m''')

print("Obrigado, volte sempre!")