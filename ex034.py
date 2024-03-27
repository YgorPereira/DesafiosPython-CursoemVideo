sal = float(input('Digite seu salário: '))
if sal > 1250.00:
    aum = sal * 0.10
    sal = sal + aum
    print(f'Seu aumento foi de \033[4;32mR${aum:.2f}\033[m e seu novo salário é de \033[4;32mR$R${sal:.2f} ')
else:
    aum = sal * 0.15
    sal = sal + aum
    print(f'Seu aumento foi de \033[4;32mR${aum:.2f} \033[me seu novo salário é de \033[4;32mR${sal:.2f}')