sal = float(input('Seu salário: R$'))
aum = sal * (15 / 100)
print(f'Aumento : R${aum:.2f}')

new_sal = sal + aum
print(f'Novo salário: R${new_sal:.2f}')