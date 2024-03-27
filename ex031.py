km = float(input('Qual a distância da viagem? '))
if km <= 200:
    print(f'\033[34mA viagem é de \033[4;32m{km:.2f} km\033[0;34m e o valor da passagem é de\033[4;32mR${km * 0.50:.2f}')
else:
    print(f'\033[34mA viagem é de \033[4;32m{km:.2f}km\033[0;34m e o valor da passagem é de \033[4;32mR${km * 0.45:.2f}')