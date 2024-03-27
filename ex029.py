vel = float(input('Qual a velocidade do carro? '))
if vel > 80:
    print('\033[1;31mVocê foi multado')
    multa = (vel - 80) * 7
    print(f'\033[0;33mO valor da multa é de \033[4;31mR${multa:.2f}')
else:
    print()